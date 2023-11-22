import copy
import numpy as np
import json
import math
from .pycomm import CoverageEnv


class EnvCore(object):
    """
    # 环境中的智能体
    """

    def __init__(self):

        # TODO 要改
        self.env = CoverageEnv(job="coverage_job_0620_inference", store_keep=False)
        self.time = 25200
        self.interval = 1

        self.aiz = 36  # 设置基站的水平角抽样数量 水平角度范围是0-360度
        self.tilt = 19  # 设置基站的垂直角抽样数量 垂直角度范围是0-90度
        self.agent_num = 224  # 设置智能体(天线)的个数
        self.grid_num = 177 * 156
        # TODO 改动下面两个参数来调整策略网络和Unet网络的输入维度
        self.obs_dim = 72   # 策略网络的观测维度
        self.buffer_obs_dim = (3 + 4 + 1 + self.grid_num * 6 + 500)  # UNET特征提取网络观测维度
        self.action_dim = self.aiz * self.tilt + 2  # 设置智能体的动作维度
        # TODO 设置人数

        # a = []  # 人员密集区域网格范围
        # num = 1215
        # for i in range(50):
        #     for j in range(50):
        #         a.append(num + i * 80 + j)
        # b = range(6400)
        # c = set(b).difference(a)
        # c = list(c)  # 人员稀疏区域网格范围
        #
        # self.dense_range = np.array(random.sample(a, 1000))  # 密集网格编号
        # self.sparse_range = np.array(random.sample(c, 1000))  # 稀疏网格编号

        self.cover_his = []
        self.reward_his = []
        self.throughput_his = []
        self.punish_his = []

        self.present_sig = np.zeros((self.agent_num, 500))
        self.sig_grid_list = 50 * np.array(range(0, 500))

        with open('/data1/home/suweikang/common_client/bs_site_224bs/envs/site_bs_info.json', 'r') as file:
            js = file.read()
            bs = json.loads(js)
        self.bs = bs  # 基站信息

        with open('/data1/home/suweikang/common_client/bs_site_224bs/envs/site_sg_info.json', 'r') as file:
            js = file.read()
            grid = json.loads(js)
        self.grid = grid  # 网格信息

        with open('/data1/home/suweikang/common_client/bs_site_224bs/envs/site_is_grid_bs.json', 'r') as file:
            js = file.read()
            is_grid_bs = json.loads(js)
        self.is_grid_bs = np.array(is_grid_bs["is_grid_bs"])  # 每个网格是否有基站

        with open('/data1/home/suweikang/common_client/bs_site_224bs/envs/site_is_indoor.json', 'r') as file:
            js = file.read()
            is_grid_indoor = json.loads(js)
        self.is_indoor = np.array(is_grid_indoor["is_indoor"])  # 每个网格是否在室内

        self.people_1 = np.zeros(self.grid_num)  # 前一个时间步用户数量
        self.people_2 = np.zeros(self.grid_num)  # 前两个时间步用户数量
        self.people_3 = np.zeros(self.grid_num)  # 前三个时间步用户数量
        # self.n = math.pow(10, (-174 / 10 + math.log10(1.8e5)))  # 噪声值

        # self.f = 7

    def reset(self):
        """
        # self.agent_num设定为2个智能体时，返回值为一个list，每个list里面为一个shape = (self.obs_dim, )的观测数据
        """
        sub_agent_obs = []
        s2 = np.concatenate((np.array([0, 0, 0]), np.array([63, 6.5])))
        s0 = np.zeros(self.grid_num)
        s3 = np.concatenate((s0, self.is_indoor, self.is_grid_bs, s0, s0, s0))
        for i in self.bs:
            s1 = np.append(self.bs[i]["longlat_position"], self.bs[i]["transmit_power"])
            s = np.concatenate((s1, s2, s3, np.zeros(500)))
            sub_agent_obs.append(s)
        return sub_agent_obs

    def step(self, actions):
        """
        # self.agent_num设定为2个智能体时，actions的输入为一个2纬的list，每个list里面为一个shape = (self.action_dim, )的动作数据
        # 默认参数情况下，输入为一个list，里面含有两个元素，因为动作纬度为5，所里每个元素shape = (5, )
        """

        actions = np.array(actions)
        sig = np.zeros(self.grid_num)
        rate = np.zeros(self.grid_num)

        self.people_3 = self.people_2
        self.people_2 = self.people_1
        self.people_1 = np.zeros(self.grid_num)

        # 计算当前动作下每个网格是否覆盖
        # dense_people = np.array(random.sample(self.dense_range, self.dense_people_num))  # 选择网格，设置人数为3人
        # sparse_people = np.array(random.sample(self.sparse_range, self.sparse_people_num))  # 选择网格，设置人数为1人
        # self.people_1[self.dense_range] = np.random.randint(10, 20, size=1000)
        # self.people_1[self.sparse_range] = np.random.randint(2, 5, size=1000)

        num_bs = 0
        for j in self.bs:  # 遍历每个基站，求得角度
            act = np.argmax(actions[num_bs][2:])
            act2 = np.argmax(actions[num_bs][:2])
            if act2 == 0:
                bs_azi = int(act / self.tilt) * 360 / self.aiz
                bs_tilt = (act % self.tilt) * 90 / (self.tilt - 1)
                self.bs[j]['azi_tile'] = [bs_azi, bs_tilt]
                self.bs[j]['open'] = 1
            else:
                self.bs[j]['azi_tile'] = [0, 0]
                self.bs[j]['open'] = 0
            num_bs += 1
        #
        action = []
        for i in self.bs:
            d = {}
            d['id'] = i
            d['bs_azi'] = self.bs[i]['azi_tile'][0]
            d['bs_tilt'] = self.bs[i]['azi_tile'][1]
            d['bs_control_state'] = self.bs[i]['open']
            d['bw_azi'] = 63
            d['bw_tilt'] = 6.5
            action.append(d)

        async_coroutine_step, terminated, _ = self.env.step(action, self.time, self.interval, 1)
        #print(async_coroutine_step)
        state, reward,_ = async_coroutine_step
        for i in state:
            i["signals"] = list(i["signals"])

        self.time = self.time + self.interval

        for i in state:
            self.people_1[i['grid_id']] = i['user_number']
            sig[i['grid_id']] = max(i['signals'])
            #if i['grid_id'] in self.sig_grid_list:
             #   self.present_sig[int(i['grid_id']/50)] = max(i['signals'])
        for j in reward:
            rate[j['grid_id']] = j['mean_rate']
            # sig[j['grid_id']] = j['coverage']

        # for i in self.grid:  # 遍历每一个网格
        #     usr_lon = self.grid[i]['ll'][0]
        #     usr_lat = self.grid[i]['ll'][1]
        #     grid_is_indoor = self.grid[i]['is_indoor']
        #     sig_unit = -100000000
        #     num_bs = 0
        #     store_sig = False
        #     if int(i) in self.sig_grid_list:
        #         store_sig = True
        #
        #     for j in self.bs:  # 遍历每个基站，求得该网格最大信号强度
        #         act = np.argmax(actions[num_bs][2:])
        #         act2 = np.argmax(actions[num_bs][:2])
        #
        #         if act2 == 0:
        #             bs_azi = int(act / self.tilt) * 360 / self.aiz
        #             bs_tilt = (act % self.tilt) * 90 / (self.tilt - 1)
        #             self.bs[j]['azi_tile'] = [bs_azi, bs_tilt]
        #             self.bs[j]['open'] = 1
        #             glo_act[int(j)] = 1
        #
        #             bs_lon = self.bs[j]['longlat_position'][0]
        #             bs_lat = self.bs[j]['longlat_position'][1]
        #             loss = calculate_path_loss(bs_lon, bs_lat, usr_lon, usr_lat, bs_azi, bs_tilt,
        #                                        is_indoor=grid_is_indoor)
        #             sig_bs = self.bs[j]["transmit_power"] - math.log10(45) - loss
        #             if store_sig == True:
        #                 grid_num = int(int(i) / 10)
        #                 self.present_sig[num_bs, grid_num] = sig_bs
        #
        #             if sig_bs > sig_unit:
        #                 sig_unit = sig_bs
        #         else:
        #             self.bs[j]['azi_tile'] = [0, 0]
        #             self.bs[j]['open'] = 0
        #         num_bs = num_bs + 1
        #     sig.append(sig_unit)  # 存储该网格的信号强度dbm
        #     sig_power = math.pow(10, (sig_unit / 10))  # 将dbm转化为mw
        #     sg_rate = self.people_1[int(i)] * 1.8e5 * (math.log2(1 + sig_power / self.n))  # 计算该网格的吞吐量
        #     rate.append(sg_rate)  # 存储每个网格的吞吐量

        # 计算覆盖率
        sig1 = copy.deepcopy(np.array(sig))
        # TODO -105为阈值，可以调整，下面两行都要调整
        cover = (np.sum(sig1 > -110)) / self.grid_num
        # json.dump({'sig': sig}, fp=open('./'+str(cover)+'sig' + '.json', 'w'))
        sig = sig1 > -110  # 将每个网格是否覆盖转化为布尔型

        # 计算平均吞吐量
        rate_average = sum(rate) / len(rate)

        # 计算惩罚
        open_bs = 0
        for i in self.bs:
            if self.bs[i]['open'] == 1:
                open_bs += 1
        if open_bs <= 180:
            punish = 0.00025 * open_bs
        else:
            punish = 0.00004 * math.exp(open_bs / 25)

        # 计算reward
        reward = cover * 0.9 + rate_average * 0.000005 - punish
        print("覆盖率:{},吞吐量：{},惩罚：{},奖励：{},开启基站：{}".format(cover, rate_average, punish, reward, open_bs))
        # 存储一下
        self.cover_his.append(cover)
        self.reward_his.append(reward)
        self.throughput_his.append(rate_average)
        self.punish_his.append(punish)
        json.dump({'cover_his': self.cover_his}, fp=open('./cover_his' + '.json', 'w'))
        json.dump({'reward_his': self.reward_his}, fp=open('./reward_his' + '.json', 'w'))
        json.dump({'throughput_his': self.throughput_his}, fp=open('./throughput_his' + '.json', 'w'))
        json.dump({'punish_his': self.punish_his}, fp=open('./punish_his' + '.json', 'w'))

        sub_agent_obs = []
        sub_agent_reward = []
        sub_agent_done = []  # dones表示本回合的结束，dones默认为false，在实例型的代码中，dones在智能体死亡或满足特定条件时为true
        sub_agent_info = []  # 不重要，只有在可视化环境时才用到

        s3 = np.concatenate((sig, self.is_indoor, self.is_grid_bs, self.people_1, self.people_2, self.people_3))
        num_bs = 0
        for i in self.bs:
            s1 = np.append(self.bs[i]["longlat_position"], self.bs[i]["transmit_power"])
            s1 = np.append(s1, self.bs[i]['open'])
            s2 = np.concatenate((self.bs[i]['azi_tile'], np.array([63, 6.5])))
            # s2 = np.concatenate(([0, 30], np.array([63, 6.5])))
            s4 = self.present_sig[num_bs]
            s = np.concatenate((s1, s2, s3, s4))
            sub_agent_obs.append(s)
            sub_agent_reward.append(reward)
            sub_agent_done.append(False)
            sub_agent_info.append({})
            num_bs = num_bs + 1
        return [sub_agent_obs, sub_agent_reward, sub_agent_done, sub_agent_info]
