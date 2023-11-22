# pycomm

Python强化学习端client，实现与模拟器的通信功能。

## 运行

### 引用：

```
	from pycomm.pycomm import DynamicEnv
	env = DynamicEnv(
		  base_info_file: str, #基站信息文件
      	  horizon,  #模拟次数
      	  sim_dir,  #模拟器目录
      	  log_dir,  #日志目录
      	  change_config: bool = False, #是否改变配置文件 若为True，使用更新的config文件，否则使用默认的config文件
   	 )
```

### 初始化： 启动模拟器,实现与模拟器通信。将环境设置为初始状态，并返回初试观测值。

#### 返回值 ：

 - state:初始状态。
 
 - bs_info:基站基本信息
 
```
	state, bs_info = await env.init()
```

###  模拟器步进： 控制模拟器模拟步数

#### 参数：

 - action:由rl提供的动作
 
 - step:模拟器得到rl提供的动作，并往下执行的步数
 
#### 返回值：

 - async_coroutine_step:包含state，reward
 
 - state:模拟器返回状态，rl可根据此状态进行优化训练
 
 - reward:模拟器采取action行动的结果，返回奖励
 
 - terminated:模拟器告知rl端，模拟结束。
 
```
	async_coroutine_step, terminated, _ = await env.step(action, step)
```

### 关闭模拟器：rl训练结束时，结束模拟器进程。
```
	 await env.reset()
```

## 参数说明：

### config: 模拟器控制参数

- step:模拟器起始步数<br>


- total:模拟器总步数，结束步数为起始步+总步数

- interval:每步的时间间隔

- microscopic_range:  微观区域范围             
    min_longitude: 说明微观的经纬度范围  
    min_latitude:   
    max_longitude:   
    max_latitude:   
    
- macroscopic_range:  宏观区域范围  
    min_longitude:说明宏观的经纬度范围  
    min_latitude:   
    max_longitude：  
    max_latitude:  
    
- enable_controlled: 模拟器是否受到外部控制，若为true需要外部控制模拟器步进

- enable_optimize：通信是否使用优化分配

- display_guomao: 选择模拟范围，微观或者宏观

- coverage_range: 初始化划分网格长度（单位：米），实现并行计算

- handover_interval: 基站切换频率(单位:秒)

- channel_type: 信道模型选择，默认值，equation,raytracing,3GPP,free_space

- antenna_type: 天线类型选择，siso,mimo

### data文件说明：

- log: 终端位置数据

- mask: 热力图展示区域

- raytracing: 射线跟踪数据

### comm_docker:

- 打包的comm二进制文件。
