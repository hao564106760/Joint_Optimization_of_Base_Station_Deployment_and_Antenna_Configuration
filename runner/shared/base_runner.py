import os
import numpy as np
import torch
from tensorboardX import SummaryWriter
from utils.shared_buffer import SharedReplayBuffer
from utils.shared_buffer2 import SharedReplayBuffer2

def _t2n(x):
    """Convert torch tensor to a numpy array."""
    return x.detach().cpu().numpy()


class Runner(object):
    """
    Base class for training recurrent policies.
    :param config: (dict) Config dictionary containing parameters for training.
    """

    def __init__(self, config):

        self.all_args = config['all_args']
        self.envs = config['envs']
        self.eval_envs = config['eval_envs']
        self.device = config['device']
        self.num_agents = config['num_agents']
        if config.__contains__("render_envs"):
            self.render_envs = config['render_envs']

            # parameters
        self.env_name = self.all_args.env_name
        self.algorithm_name = self.all_args.algorithm_name
        self.experiment_name = self.all_args.experiment_name
        self.use_centralized_V = self.all_args.use_centralized_V
        self.use_obs_instead_of_state = self.all_args.use_obs_instead_of_state
        self.num_env_steps = self.all_args.num_env_steps
        self.episode_length = self.all_args.episode_length
        self.n_rollout_threads = self.all_args.n_rollout_threads
        self.n_eval_rollout_threads = self.all_args.n_eval_rollout_threads
        self.n_render_rollout_threads = self.all_args.n_render_rollout_threads
        self.use_linear_lr_decay = self.all_args.use_linear_lr_decay
        self.hidden_size = self.all_args.hidden_size
        self.use_render = self.all_args.use_render
        self.recurrent_N = self.all_args.recurrent_N

        # interval
        self.save_interval = self.all_args.save_interval
        self.use_eval = self.all_args.use_eval
        self.eval_interval = self.all_args.eval_interval
        self.log_interval = self.all_args.log_interval

        # dir
        self.model_dir = self.all_args.model_dir

        self.run_dir = config["run_dir"]
        self.log_dir = str(self.run_dir / 'logs')
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)
        self.writter = SummaryWriter(self.log_dir)
        self.save_dir = str(self.run_dir / 'models')
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)

        from algorithms.algorithm.r_mappo import RMAPPO as TrainAlgo
        from algorithms.algorithm.rMAPPOPolicy import RMAPPOPolicy as Policy
        from algorithms.algorithm.rMAPPOPolicy2 import RMAPPOPolicy2 as Policy2

        share_observation_space = self.envs.share_observation_space[0] if self.use_centralized_V else \
        self.envs.observation_space[0]

        # todo
        buffer_share_observation_space = self.envs.buffer_observation_space[0]

        # policy network
        self.policy = Policy(self.all_args,
                             self.envs.observation_space[0],
                             share_observation_space,
                             self.envs.action_space[0],
                             device=self.device)
        # todo
        self.policy2 = Policy2(self.all_args,
                             self.envs.observation_space[0],
                             share_observation_space,
                             self.envs.action_space[0],
                             device=self.device)

        if self.model_dir is not None:
            self.restore()

        # algorithm
        self.trainer = TrainAlgo(self.all_args, self.policy, device=self.device)
        # todo
        self.trainer2 = TrainAlgo(self.all_args, self.policy2, device=self.device)

        # buffer
        self.buffer = SharedReplayBuffer(self.all_args,
                                         self.num_agents,
                                         # todo
                                         self.envs.buffer_observation_space[0],
                                         buffer_share_observation_space,
                                         self.envs.action_space[0])

        self.buffer2 = SharedReplayBuffer2(self.all_args,
                                         self.num_agents,
                                         # todo
                                         self.envs.buffer_observation_space[0],
                                         buffer_share_observation_space,
                                         self.envs.action_space[0])

    def run(self):
        """Collect training data, perform training updates, and evaluate policy."""
        raise NotImplementedError

    def warmup(self):
        """Collect warmup pre-training data."""
        raise NotImplementedError

    def collect(self, step):
        """Collect rollouts for training."""
        raise NotImplementedError

    def insert(self, data):
        """
        Insert data into buffer.
        :param data: (Tuple) data to insert into training buffer.
        """
        raise NotImplementedError

    @torch.no_grad()
    def compute(self): # self.compute()函数计算这个episode的折扣回报
        """Calculate returns for the collected data."""
        self.trainer.prep_rollout()
        next_values = self.trainer.policy.get_values(np.concatenate(self.buffer.share_obs[-1]),
                                                     np.concatenate(self.buffer.rnn_states_critic[-1]),
                                                     np.concatenate(self.buffer.masks[-1]))
        next_values = np.array(np.split(_t2n(next_values), self.n_rollout_threads))#先算这个episode最后一个状态的状态值函数next_values
        self.buffer.compute_returns(next_values, self.trainer.value_normalizer)  #计算折扣回报

    @torch.no_grad()
    def compute2(self):  # self.compute()函数计算这个episode的折扣回报
        """Calculate returns for the collected data."""
        self.trainer2.prep_rollout()
        next_values = self.trainer2.policy.get_values(np.concatenate(self.buffer2.share_obs[-1]),
                                                     np.concatenate(self.buffer2.rnn_states_critic[-1]),
                                                     np.concatenate(self.buffer2.masks[-1]))
        next_values = np.array(
            np.split(_t2n(next_values), self.n_rollout_threads))  # 先算这个episode最后一个状态的状态值函数next_values
        self.buffer2.compute_returns(next_values, self.trainer2.value_normalizer)  # 计算折扣回报

    def train(self):
        """Train policies with data in buffer. """
        self.trainer.prep_training() # 将网络设置为train()的格式。
        train_infos = self.trainer.train(self.buffer)
        self.buffer.after_update() # 将buffer的第一个元素设置为其episode的最后一个元素
        return train_infos

    def train2(self):
        """Train policies with data in buffer. """
        self.trainer2.prep_training() # 将网络设置为train()的格式。
        train_infos = self.trainer2.train(self.buffer2)
        self.buffer2.after_update() # 将buffer的第一个元素设置为其episode的最后一个元素
        return train_infos

    def save(self):
        """Save policy's actor and critic networks."""
        policy_actor = self.trainer.policy.actor
        torch.save(policy_actor.state_dict(), str(self.save_dir) + "/actor.pt")
        policy_critic = self.trainer.policy.critic
        torch.save(policy_critic.state_dict(), str(self.save_dir) + "/critic.pt")
        policy_Unet = self.trainer.policy.Unet
        torch.save(policy_Unet.state_dict(), str(self.save_dir) + "/Unet.pt")

    def save2(self):
        """Save policy's actor and critic networks."""
        policy_actor2 = self.trainer2.policy.actor
        torch.save(policy_actor2.state_dict(), str(self.save_dir) + "/actor2.pt")
        policy_critic2 = self.trainer2.policy.critic
        torch.save(policy_critic2.state_dict(), str(self.save_dir) + "/critic2.pt")
        policy_Unet2 = self.trainer2.policy.Unet
        torch.save(policy_Unet2.state_dict(), str(self.save_dir) + "/Unet2.pt")

    def restore(self):  # 用不上
        """Restore policy's networks from a saved model."""
        policy_actor_state_dict = torch.load(str(self.model_dir) + '/actor.pt')
        self.policy.actor.load_state_dict(policy_actor_state_dict)
        if not self.all_args.use_render:
            policy_critic_state_dict = torch.load(str(self.model_dir) + '/critic.pt')
            self.policy.critic.load_state_dict(policy_critic_state_dict)

    def log_train(self, train_infos, total_num_steps):
        """
        Log training info.
        :param train_infos: (dict) information about training update.
        :param total_num_steps: (int) total number of training env steps.
        """
        for k, v in train_infos.items():
            self.writter.add_scalars(k, {k: v}, total_num_steps)

    def log_env(self, env_infos, total_num_steps):
        """
        Log env info.
        :param env_infos: (dict) information about env state.
        :param total_num_steps: (int) total number of training env steps.
        """
        for k, v in env_infos.items():
            if len(v) > 0:
                self.writter.add_scalars(k, {k: np.mean(v)}, total_num_steps)
