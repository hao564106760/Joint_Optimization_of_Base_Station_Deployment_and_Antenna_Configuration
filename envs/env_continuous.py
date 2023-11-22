import gym
from gym import spaces
import numpy as np
from envs.env_core import EnvCore


class ContinuousActionEnv(object):
    """对于连续动作环境的封装"""
    def __init__(self):
        self.env = EnvCore()
        self.num_agent = self.env.agent_num

        self.signal_obs_dim = self.env.obs_dim
        self.signal_action_dim = self.env.action_dim

        # if true, action is a number 0...N, otherwise action is a one-hot N-dimensional vector
        self.discrete_action_input = True

        self.movable = True

        # configure spaces
        self.action_space = []
        self.observation_space = []
        self.share_observation_space = []

        share_obs_dim = 0
        total_action_space = []
        for agent in range(self.num_agent):
            # physical action space
            # TODO  改变上下限
            u_action_space = spaces.Box(low=0.0, high=90.0, shape=(self.signal_action_dim,), dtype=np.float32)

            if self.movable:
                total_action_space.append(u_action_space)

            # total action space
            self.action_space.append(total_action_space[0])

            # observation space
            share_obs_dim += self.signal_obs_dim

            # TODO 修改过
            # self.observation_space.append(spaces.Box(low=-np.inf, high=+np.inf, shape=(self.signal_obs_dim,),
            #                                          dtype=np.bool))  # [-inf,inf]

            self.observation_space.append(spaces.Box(low=0, high=1, shape=(self.signal_obs_dim,),
                                                     dtype=np.int))  # [-inf,inf]
        # TODO  修改过
        # self.share_observation_space = [spaces.Box(low=-np.inf, high=+np.inf, shape=(share_obs_dim,),
        #                                            dtype=np.bool) for _ in range(self.num_agent)]

        self.share_observation_space = [spaces.Box(low=0, high=1, shape=(self.signal_obs_dim,),
                                                   dtype=np.int)]


    def step(self, actions):
        """
        输入actions纬度假设：
        # actions shape = (5, 2, 5)
        # 5个线程的环境，里面有2个智能体，每个智能体的动作是一个one_hot的5维编码
        """

        results = self.env.step(actions)
        obs, rews, dones, infos = results
        return np.stack(obs), np.stack(rews), np.stack(dones), infos

    def reset(self):
        obs = self.env.reset()
        return np.stack(obs)

    def close(self):
        pass

    def render(self, mode="rgb_array"):
        pass

    def seed(self, seed):
        pass