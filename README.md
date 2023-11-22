# Joint_Optimization_of_Base_Station_Deployment_and_Antenna_Configuration-in-Large-Scale-Networks
Joint Optimization of Base Station Deployment and Antenna Configuration in Large-Scale Networks using Hierarchical Reinforcement Learning

# RL算法与模拟器交互

## 覆盖优化RL算法与模拟器交互
选取北京国贸区域按照10m*10m的范围划分网格，基于信道模型计算每个网格和所有基站的信号强度，选取信号最强的基站进行连接，并判断该信号是否超过预定义阈值，若超过则该网格被覆盖，若没超过则是没有被覆盖。
说明：网格编号从区域左下角到右上角序号依次递增，序号从0开始。
每个网格内认为信号强度一致，该信号强度定义为基站到网格中心的信号强度。
预定义阈值可自行设定，依据广泛调研，本项目定义为-110dBm。

基站覆盖优化旨在最大限度地覆盖所有网格和最大化用户总吞吐量。
基站方位角、下行角、波束宽度的配置都会影响到基站信号传播与接收质量，进而影响基站的覆盖范围。例如，当基站方位角较小时，基站的信号主要沿着基站朝向的方向传播，其他方向的信号衰减较快，覆盖范围较小，然而当基站方位角较大时，基站的信号可以沿着更广泛的方向传播，但也可能会导致信号强度分散和干扰增加，信号强度较弱。覆盖优化任务就可以通过优化基站的角度和波束宽度配置，以优化基站覆盖率和用户总吞吐量。该任务的状态信息包含系统中每个网格的状态，包含网格与所有基站的信号强度、是否室内等；奖励函数表示仿真引擎在接收不同策略反馈的奖励信号，即是否被覆盖与用户平均通信速率。基于返回的状态与奖励函数，网络优化器可调整基站的方位角、下行角与波束宽度的配置，以同时优化网格的总覆盖率与用户的总吞吐量。

模拟器将环境当前的状态（State）传到覆盖优化RL算法中，RL算法输出动作（Action）并传到模拟器中，得到当前的奖励值（Reward）和下一时刻的状态（State_），如此循环往复，直到达到终止状态或条件。其中，覆盖优化RL算法的三元素State、Action、Reward具有如下结构：

State: [
{"grid_id": xxx,                # 网格编号
"signals": [xxx],               # 每个基站到该网格的信号强度
"user_number": xxx,           # 该网格的用户数（每时刻在变化）
"is_indoor": true/false}         # 是否是室内（室内会对信号强度有影响）
]（返回T时间段最新状态）

Action: [
{"id": xxx,                  # 基站(天线)编号
"bs_open": xxx,             # 该天线是否开启
 "bs_power": xxx,            # 该基站的功率
 "bs_azi": xxx,              # 该天线的方位角 
 "bs_tilt": xxx,              # 该天线的下倾角
 "bw_azi": xxx,             # 水平波宽（文献中认为是既定值）
 "bw tilt": xxx}             # 垂直波宽（文献中认为是既定值）
]

Reward: [
{"grid_id": xxx,             # 网格编号
 "coverage": true/false,       # 是否覆盖到
 "mean_rate": xxx}          # T时段内的均值速率（速率和接受信号强度相关）
] (mean_rate为T时间段的均值速率）


附录1：模拟器使用说明
# pycomm
用于与模拟器进行通信的 Python 强化学习客户端。

## 使用
### 初始化：（以动态优化环境为例）
```python
from pycomm.pycomm import DynamicEnv
env = DynamicEnv(
    channel_type: int = 1,       # 信道类型
    antenna_type: int = 1,       # 天线类型
    job: str = 'job0',            # 作业名称
    output: bool = False,        # 启用输出
    display_micro: bool = True,  # 宏和微区域选择
    coverage_range: int = 1000,  # 覆盖范围
    handover_interval: int = 1,   # 切换间隔
)
```
### 模拟器步骤：控制模拟器的模拟步骤
#### 参数：
- action：由 RL（强化学习）提供的动作
- start：模拟器的起始步骤
- total：模拟器应执行的总步骤数（结束步骤 = 起始步骤 + 总步骤数）
- interval：每个步骤的时间间隔
- is_output：布尔值，是否保存可视化内容

#### 返回值：
- async_coroutine_step：包含状态和奖励
- state：模拟器返回的状态，用于 RL 优化训练
- reward：在模拟器中采取行动的结果，提供奖励反馈
- visualize：可视化内容
- terminated：指示模拟已完成

```python
async_coroutine_step, terminated, _ = await env.step(action, start, total, interval, is_output)
```
### 关闭模拟器：在 RL 训练完成时终止模拟器进程。
```python
await env.reset()
```

附录2：覆盖优化代码使用说明
## 覆盖优化代码使用步骤如下：
#### （1）使用以下命令激活客户端并建立与模拟器的连接：
./common_docker config/……/common_client/pycomm/pycomm/update_config.yml -rl true
#### （2）打开一个新的终端并激活 Conda 环境：
source activate torch-1.9.0-py37
#### （3）运行强化学习程序：
python Coverage_simulator/train.py
#### （4）在训练完成后，将保存三个 JSON 文件，分别是 reward_his.json、cover_his.json 和 throughput_his.json，它们分别保存了与模拟器互动后的奖励值、覆盖率和用户数据吞吐量数值。
