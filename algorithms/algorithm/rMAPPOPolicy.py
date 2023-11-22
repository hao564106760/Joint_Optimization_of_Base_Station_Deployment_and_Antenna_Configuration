import json
import numpy as np
import torch
from torch import nn
from algorithms.utils.util import init, check
from algorithms.algorithm.r_actor_critic import R_Actor, R_Critic
from utils.util import update_linear_schedule
from algorithms.utils.Unet import UNet
from algorithms.utils.mlp import MLPLayer


class RMAPPOPolicy:
    """
    MAPPO Policy  class. Wraps actor and critic networks to compute actions and value function predictions.
    包装策略和价值函数来输出动作和价值
    :param args: (argparse.Namespace) arguments containing relevant model and policy information.
    :param obs_space: (gym.Space) observation space.
    :param cent_obs_space: (gym.Space) value function input space (centralized input for MAPPO, decentralized for IPPO).
    :param action_space: (gym.Space) action space.
    :param device: (torch.device) specifies the device to run on (cpu/gpu).
    """

    def __init__(self, args, obs_space, cent_obs_space, act_space, device=torch.device("cpu")):
        self.device = device
        self.lr = args.lr
        self.critic_lr = args.critic_lr
        self.opti_eps = args.opti_eps
        self.weight_decay = args.weight_decay
        self.episode_length = args.episode_length
        # TODO
        self.use_pretrain_model = args.use_pretrain_model
        self.agent_num = 224
        self.row = 177
        self.column = 156

        self.obs_space = obs_space
        self.share_obs_space = cent_obs_space
        self.act_space = act_space

        self.actor = R_Actor(args, self.obs_space, self.act_space, self.device)
        self.critic = R_Critic(args, self.share_obs_space, self.device)
        self.Unet = UNet(6, 64).to(device)
        self.present = MLPLayer(72+1, 500,
                                args.layer_N, args.use_orthogonal, args.use_ReLU)
        # TODO
        if self.use_pretrain_model == True:
            self.actor.load_state_dict(
                torch.load("/data7/liuhaoqiang/results_4/MyEnv/MyEnv/mappo/check/run1/models/actor.pt"))
            self.critic.load_state_dict(
                torch.load("/data7/liuhaoqiang/results_4/MyEnv/MyEnv/mappo/check/run1/models/critic.pt"))
            self.Unet.load_state_dict(
                torch.load("/data7/liuhaoqiang/results_4/MyEnv/MyEnv/mappo/check/run1/models/Unet.pt"))
            print('导入模型成功')

        self.tpdv = dict(dtype=torch.float32, device=device)
        # TODO 修改路径
        with open('/data1/home/suweikang/common_client/bs_site_224bs/envs/site_bs_info.json', 'r') as file:
            js = file.read()
            bs = json.loads(js)
        self.bs = bs  # 基站信息

        self.actor_optimizer = torch.optim.Adam(
            [{'params': self.actor.parameters(), },
             {'params': self.Unet.parameters()}, ],
            lr=self.lr, eps=self.opti_eps,
            weight_decay=self.weight_decay)

        self.critic_optimizer = torch.optim.Adam([{'params': self.critic.parameters(), },
                                                  {'params': self.Unet.parameters()}, ],
                                                 lr=self.critic_lr,
                                                 eps=self.opti_eps,
                                                 weight_decay=self.weight_decay)

        self.present_optimizer = torch.optim.Adam(self.present.parameters(),
                                                  lr=self.critic_lr,
                                                  eps=self.opti_eps,
                                                  weight_decay=self.weight_decay)

    def lr_decay(self, episode, episodes):
        """
        Decay the actor and critic learning rates.
        :param episode: (int) current training episode.
        :param episodes: (int) total number of training episodes.
        """
        update_linear_schedule(self.actor_optimizer, episode, episodes, self.lr)
        update_linear_schedule(self.critic_optimizer, episode, episodes, self.critic_lr)

    def get_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, masks,
                    available_actions=None,
                    deterministic=False):
        """
        Compute actions and value function predictions for the given inputs.
        :param cent_obs (np.ndarray): centralized input to the critic.
        :param obs (np.ndarray): local agent inputs to the actor.
        :param rnn_states_actor: (np.ndarray) if actor is RNN, RNN states for actor.
        :param rnn_states_critic: (np.ndarray) if critic is RNN, RNN states for critic.
        :param masks: (np.ndarray) denotes points at which RNN states should be reset.
        :param available_actions: (np.ndarray) denotes which actions are available to agent
                                  (if None, all actions available)
        :param deterministic: (bool) whether the action should be mode of distribution or should be sampled.

        :return values: (torch.Tensor) value function predictions.
        :return actions: (torch.Tensor) actions to take.
        :return action_log_probs: (torch.Tensor) log probabilities of chosen actions.
        :return rnn_states_actor: (torch.Tensor) updated actor network RNN states.
        :return rnn_states_critic: (torch.Tensor) updated critic network RNN states.
        """

        obs = check(obs).to(**self.tpdv)
        unet_obs = obs[0][8:-500].reshape(1, 6, self.row, self.column)
        unet_result = self.Unet(unet_obs)
        unet_result = unet_result.cpu().numpy()

        # 从UNET网络中提取27个基站的信息
        bs_info = np.zeros(64)
        for i, info in enumerate(self.bs):
            row = int(self.bs[info]["poi_grid"] / self.column)
            col = self.bs[info]["poi_grid"] % self.column
            bs_info = np.vstack((bs_info, unet_result[0, :, row, col]))

        final_obs = np.concatenate((obs[:, :8].cpu(), bs_info[1:, :]), axis=1)
        final_obs = check(final_obs).to(**self.tpdv)

        actions, action_log_probs, rnn_states_actor = self.actor(final_obs,
                                                                 rnn_states_actor,
                                                                 masks,
                                                                 available_actions,
                                                                 deterministic)

        values, rnn_states_critic = self.critic(final_obs, rnn_states_critic, masks)
        return values, actions, action_log_probs, rnn_states_actor, rnn_states_critic

    def get_values(self, cent_obs, rnn_states_critic, masks):
        """
        Get value function predictions.
        :param cent_obs (np.ndarray): centralized input to the critic.
        :param rnn_states_critic: (np.ndarray) if critic is RNN, RNN states for critic.
        :param masks: (np.ndarray) denotes points at which RNN states should be reset.

        :return values: (torch.Tensor) value function predictions.
        """
        # 用来计算每个回合中最后一个观测值的value
        obs = check(cent_obs).to(**self.tpdv)
        unet_obs = obs[0][8:-500].reshape(1, 6, self.row, self.column)
        unet_result = self.Unet(unet_obs)
        unet_result = unet_result.cpu().numpy()

        # 从UNET网络中提取27个基站的信息
        bs_info = np.zeros(64)
        for i, info in enumerate(self.bs):
            row = int(self.bs[info]["poi_grid"] / self.column)
            col = self.bs[info]["poi_grid"] % self.column
            bs_info = np.vstack((bs_info, unet_result[0, :, row, col]))

        final_obs = np.concatenate((obs[:, :8].cpu(), bs_info[1:, :]), axis=1)
        final_obs = check(final_obs).to(**self.tpdv)

        values, _ = self.critic(final_obs, rnn_states_critic, masks)
        return values

    def evaluate_actions(self, cent_obs, obs, rnn_states_actor, rnn_states_critic, action, masks,
                         available_actions=None, active_masks=None):
        """
        Get action logprobs / entropy and value function predictions for actor update.
        :param cent_obs (np.ndarray): centralized input to the critic.
        :param obs (np.ndarray): local agent inputs to the actor.
        :param rnn_states_actor: (np.ndarray) if actor is RNN, RNN states for actor.
        :param rnn_states_critic: (np.ndarray) if critic is RNN, RNN states for critic.
        :param action: (np.ndarray) actions whose log probabilites and entropy to compute.
        :param masks: (np.ndarray) denotes points at which RNN states should be reset.
        :param available_actions: (np.ndarray) denotes which actions are available to agent
                                  (if None, all actions available)
        :param active_masks: (torch.Tensor) denotes whether an agent is active or dead.

        :return values: (torch.Tensor) value function predictions.
        :return action_log_probs: (torch.Tensor) log probabilities of the input actions.
        :return dist_entropy: (torch.Tensor) action distribution entropy for the given inputs.
        """
        obs = check(cent_obs).to(**self.tpdv)
        unet_obs = obs[[i * self.agent_num for i in range(self.episode_length)]] \
            [:, 8:-500].reshape(self.episode_length, 6, self.row, self.column)
        unet_result = self.Unet(unet_obs)

        # 从UNET网络中提取27个基站的信息
        bs_info = torch.zeros(64).to(**self.tpdv).unsqueeze(0)
        for i in range(self.episode_length):
            for j, info in enumerate(self.bs):
                row = int(self.bs[info]["poi_grid"] / self.column)
                col = self.bs[info]["poi_grid"] % self.column
                bs_info = torch.cat((bs_info, unet_result[i, :, row, col].unsqueeze(0)), 0)

        final_obs = torch.cat((obs[:, :8], bs_info[1:, :]), 1)
        final_obs = check(final_obs).to(**self.tpdv)

        action_log_probs, dist_entropy = self.actor.evaluate_actions(final_obs,
                                                                     rnn_states_actor,
                                                                     action,
                                                                     masks,
                                                                     available_actions,
                                                                     active_masks)

        values, _ = self.critic(final_obs, rnn_states_critic, masks)

        return values, action_log_probs, dist_entropy, final_obs

    def act(self, obs, rnn_states_actor, masks, available_actions=None, deterministic=False):
        """
        Compute actions using the given inputs.
        :param obs (np.ndarray): local agent inputs to the actor.
        :param rnn_states_actor: (np.ndarray) if actor is RNN, RNN states for actor.
        :param masks: (np.ndarray) denotes points at which RNN states should be reset.
        :param available_actions: (np.ndarray) denotes which actions are available to agent
                                  (if None, all actions available)
        :param deterministic: (bool) whether the action should be mode of distribution or should be sampled.
        """
        obs = check(obs).to(**self.tpdv)
        unet_obs = obs[0][8:-500].reshape(1, 6, self.row, self.column)
        unet_result = self.Unet(unet_obs)
        unet_result = unet_result.cpu().numpy()

        # 从UNET网络中提取24个基站的信息
        bs_info = np.zeros(64)
        for i, info in enumerate(self.bs):
            row = int(self.bs[info]["poi_grid"] / self.column)
            col = self.bs[info]["poi_grid"] % self.column
            bs_info = np.vstack((bs_info, unet_result[0, :, row, col]))

        final_obs = np.concatenate((obs[:, :8].cpu(), bs_info[1:, :]), axis=1)
        final_obs = check(final_obs).to(**self.tpdv)
        actions, _, rnn_states_actor = self.actor(final_obs, rnn_states_actor, masks, available_actions, deterministic)
        return actions, rnn_states_actor
