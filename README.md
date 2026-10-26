# SuperMimic Carnival

从 **2026-10-20** 起，持续汇总 [SuperMimic](https://supermimic.github.io/)（arXiv:2610.28480）的开源复现与改造。

> 最近核查：2026-10-27 05:45（UTC+8） · 已确认完整训练实现：**48 个仓库**  
> Star 为本次核查快照，每 3 小时随增量检索刷新。

## 收录口径

“完整训练实现”指仓库中同时能找到：训练入口、世界模型／策略／价值网络学习代码，以及可执行配置或数据接入流程。这里做**代码与文档静态核查**，不代表已在本机复跑训练，也不把作者自报指标视为独立验证。

仅视频、论文列表、部署／导出、简单 Fork 且无实质训练代码、只有环境冒烟或规划文档的项目不进入主表。训练范围仅限 LAFAN1 也可收录，但不等同于复现论文全部 BONES-SEED、速度接口、蒸馏或真机实验。

## 总览

- **论文主任务／通用动作跟踪**：G1 平地全身跟踪是主流；部分项目扩展到 BONES-SEED、多卡、完整评测和分布外动作。
- **地形与感知**：InstinctMJ 分支实现深度视觉跑酷，另有 Go2 平地／障碍／复杂地形追逐闪避、G1 高程图台阶、HoloMotion 多后端跟踪；暂未确认基于 BFM-Zero 的完整改造。
- **跨本体**：G1、Go2、H1、H2、A3、X2 Ultra、T2、E1、Oli、Q1、天工 3.0、无界灵巧手 Wuji Hand 2（Dex-Supermimic 手上立方体重定向）、RoboParty RPO 23-DoF 等。
- **新任务**：多机器人共享世界模型、五点稀疏跟踪、追逐闪避、滑板与 HOI／手物交互、高动态动作（含单卡 5090 后空翻）、PHP 跑酷（supermimic_parkour）、Apple M5 训练、2D 简化人形复现（FlatWorld）等；社区展示与开源训练状态见[社区新任务时间线](COMMUNITY_TASKS.md)。

## 已确认包含训练实现

### A. 通用复现、训练框架与算法实验

| 仓库 | ⭐ | 精简总结 | 主要训练任务 | 底座／来源 |
|---|---:|---|---|---|
| [HorizonRobotics/HoloMotion](https://github.com/HorizonRobotics/HoloMotion) | 738 | HoloMotion 内新增完整 SuperMimic 算法、配置、训练与评测文档 | 人形全身动作跟踪，MuJoCo Warp／Isaac PhysX | HoloMotion |
| [zita-ch/supermimic_vibed](https://github.com/zita-ch/supermimic_vibed) | 606 | 早期高影响力独立复现，完整 WM＋BPTT＋critic | G1，40 条 LAFAN1 平地全身跟踪 | Isaac Lab 3 kit-less、Newton／MuJoCo Warp |
| [CuboiLeo/SuperMimic-Reproduced](https://github.com/CuboiLeo/SuperMimic-Reproduced) | 253 | 从零实现数据、可微 FK、WM、想象训练、分布式与评测 | G1，LAFAN1＋BONES-SEED 全身跟踪 | mjlab／MuJoCo Warp |
| [Motphys/Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic) | 157 | UniLab 工程化复现，支持三种仿真后端和 ROCm 路径 | G1，40 条 LAFAN1 全身跟踪 | UniLab；参考 supermimic_vibed |
| [lzyang2000/morphmimic](https://github.com/lzyang2000/morphmimic) | 116 | 形态条件化 WM／策略共享，支持五点稀疏目标与部署 | G1／X2 Ultra／T2，BONES-SEED，多机器人跟踪 | 独立实现；mjlab |
| [btx0424/rethinking-supermimic](https://github.com/btx0424/rethinking-supermimic) | 23 | 重思网络与训练实现，含多种 actor 配置和梯度检查 | G1，40 条 LAFAN1 跟踪 | mjlab |
| [YanYuan98/Supermimic_mod](https://github.com/YanYuan98/Supermimic_mod) | 9 | 完整训练评测，并提供与 RGMT 的效果对比 | G1，40 条 LAFAN1 跟踪 | mjlab／MuJoCo Warp |
| [Shimingyi/allmimic](https://github.com/Shimingyi/allmimic) | 18 | 强调可行性过滤及内容／演员／随机三类 held-out 划分 | G1，LAFAN1＋BONES-SEED 跟踪与泛化评测 | mjlab；参考 supermimic_vibe |
| [kangzejian1896/supermimic-g1-reproduction](https://github.com/kangzejian1896/supermimic-g1-reproduction) | 4 | 增加验证动作、同协议对比和训练脚本 | G1，LAFAN1＋BONES-SEED 验证 | CuboiLeo/SuperMimic-Reproduced |
| [humble02/supermimic_mjlab_vibed](https://github.com/humble02/supermimic_mjlab_vibed) | 4 | mjlab 移植，训练、续训、评估和离线服务器流程齐全 | G1，40 条 LAFAN1 跟踪 | zita-ch/supermimic_vibed |
| [RaraAlu/Supermimic](https://github.com/RaraAlu/Supermimic) | 4 | 支持 CSV／HDF5、多卡分片、数据指纹与完整评估 | G1，LAFAN1 及大规模 HDF5 动作库 | zita-ch／mjlab |
| [fan-ziqi/supermimic-agy](https://github.com/fan-ziqi/supermimic-agy) | 2 | 覆盖主实验、critic／视界消融、吞吐和速度接口 | G1，LAFAN1＋下游速度控制 | mjlab／PyTorch |
| [KunYing-Lee/SuperMimic](https://github.com/KunYing-Lee/SuperMimic) | 1 | mjlab 复现，补固定动作库评测和论文对齐审计 | G1，LAFAN1 跟踪 | zita-ch／mjlab |
| [dhmbb2/supermimic_vibe](https://github.com/dhmbb2/supermimic_vibe) | 1 | 包含 PPO-Sim 基线、视界×critic 消融及双卡训练 | G1，LAFAN1 与论文消融 | mjlab |
| [Breezewrf/supermimic_mjlab](https://github.com/Breezewrf/supermimic_mjlab) | 2 | 在线 WM／策略训练、离线 WM 训练、回放和 W&B | G1，LAFAN1 跟踪 | mjlab；参考 RoboJudo++ |
| [HighTorque-Dev/supermimic-colab](https://github.com/HighTorque-Dev/supermimic-colab) | 1 | 保留完整训练代码，面向 Colab／A100 复现记录 | G1，40 条 LAFAN1 跟踪 | Isaac Lab 3／MuJoCo Warp |
| [samindaa/supermimic_mjlab](https://github.com/samindaa/supermimic_mjlab) | 1 | 从 Isaac Lab 版迁至 mjlab，含同迭代对照 | G1，40 条 LAFAN1 跟踪 | supermimic_vibed／mjlab |
| [enffft/supermimic](https://github.com/enffft/supermimic) | 0 | 保留完整 WM／BPTT／数据管线，增加 Q1 训练文档 | G1／Q1，LAFAN1 跟踪 | CuboiLeo/SuperMimic-Reproduced |
| [tianny0078/supermimic-repro](https://github.com/tianny0078/supermimic-repro) | 0 | 完整复现代码、Slurm 入口和调研记录 | G1，LAFAN1／BONES-SEED | 综合 CuboiLeo、zita-ch 等实现 |
| [Go-Youngster/supermimic-reproduce](https://github.com/Go-Youngster/supermimic-reproduce) | 0 | 论文从零复现：可微 WM＋BPTT＋critic，含 PPO-Sim／PPO-WM 基线、消融与 A100 训练记录 | G1（29 DoF），40 条 LAFAN1 全身跟踪 | 论文从零实现；mjlab／MuJoCo Warp |
| [CesarLiu/smimic（UniSuperMimic）](https://github.com/CesarLiu/smimic) | 0 | UniLab 下游独立复现，mjwarp／MuJoCo／Motrix 三后端、Hydra 配置与 Hugging Face 数据管线 | G1，40 条 LAFAN1 全身跟踪 | UniLab；参考 supermimic_vibed |
| [LaoYang1994/SuperMimic-Rep](https://github.com/LaoYang1994/SuperMimic-Rep) | 0 | CuboiLeo 改造：同迭代数对齐论文协议、BONES-SEED 全量评测、2 倍训练提速与修正 reset sampler | G1，LAFAN1＋全量 BONES-SEED（129k 条）跟踪 | CuboiLeo/SuperMimic-Reproduced／mjlab |
| [Noetix-Research-Lab/Supermimic](https://github.com/Noetix-Research-Lab/Supermimic) | 0 | 论文从零复现＋扩展：MotionAtlas 全量数据、G1／E2 双本体、torchrun 多卡与真机部署链路，评测站 G1 榜 #1（自报） | G1／E2，MotionAtlas 25.5 万／37 万条动作库跟踪 | 论文从零实现；mjlab 固定 commit；unitree_mujoco 部署 |

### B. 新本体、地形、感知与新任务

| 仓库 | ⭐ | 精简总结 | 主要训练任务 | 底座／来源 |
|---|---:|---|---|---|
| [project-instinct/InstinctMJ（supermimic 分支）](https://github.com/project-instinct/InstinctMJ/tree/supermimic) | 280 | 将机器人状态与深度编码视觉潜变量共同纳入 WM，在想象中训练原深度策略，无 PPO；10-25 更新新增目标点跑酷任务与公开数据／权重 release | G1 深度视觉地形跑酷：翻滚、跪膝爬 50 cm 台阶、跳坐、滚翻越过障碍；目标点跑酷（AMP 风格奖励，地形课程约 6 级） | InstinctMJ／InstinctLab、mjlab；适配 zita-ch |
| [Zhengtianjin/go2-supermimic](https://github.com/Zhengtianjin/go2-supermimic) | 50 | 将 WM＋想象 rollout 用于追逐与闪避，含 LiDAR／高程输入 | Go2 平地、障碍、楼梯／坡面／粗糙地形 | mjlab；参考 go2_rl_gym |
| [swaggyliu/FlatWorld（supermimic2d）](https://github.com/swaggyliu/FlatWorld) | 38 | 自研 2D 引擎上的 SuperMimic 完整复现：共享刚体 WM＋BPTT＋critic 训练闭环、参考动作烘焙与渲染导出 | 2D 十杆人形（8 驱动关节），LAFAN-like 动作库（走／跑／冲刺／舞蹈／跳／蹲／格斗／跌倒起身） | FlatWorld（Warp 2D 物理引擎）；SuperMimic 思路复刻 |
| [JackMin7/supermimic_whole_body_tracking](https://github.com/JackMin7/supermimic_whole_body_tracking) | 19 | 同任务 MBRL 与 PPO 对照，附逐 10 分钟训练数据 | G1 静态站立／全身控制 | BeyondMimic／SuperMimic |
| [panhainan2020/SuperMimic-MuJoCo](https://github.com/panhainan2020/SuperMimic-MuJoCo) | 13 | 脱离 Isaac Lab，支持原生 MuJoCo／MJLab 与两种 G1 模型 | G1，LAFAN1＋100STYLE 分布外评测 | zita-ch／MJLab |
| [Renforce-Dynamics/trackerlab-supermimic](https://github.com/Renforce-Dynamics/trackerlab-supermimic) | 9 | TrackerLab 数据到训练、评测、导出全链路 | G1 LAFAN1；Go2 trot 跟踪 | TrackerLab、IsaacLab／PhysX、zita-ch |
| [Baojch/SuperMimic_Dyn](https://github.com/Baojch/SuperMimic_Dyn) | 17 | 面向高动态与低姿态动作，保留完整可复现训练记录 | G1 空翻、爬行、跌倒起身及通用跟踪 | CuboiLeo／mjlab |
| [tianshuwu/supermimic-retargeted](https://github.com/tianshuwu/supermimic-retargeted) | 8 | 多本体动作重定向与训练，支持 A3／X2／G1 | 多本体 LAFAN1／BONES 跟踪 | CuboiLeo／zita-ch |
| [CumulusAlpha/Dex-Supermimic](https://github.com/CumulusAlpha/Dex-Supermimic) | 26 | SuperMimic 迁移到无界灵巧手：WM＋想象 BPTT 训练入口、预训练权重与 Viser 可视化 | Wuji Hand 2 手上立方体重定向 | InstinctMJ／mjlab；wuji-mjlab；supermimic_vibed |
| [wenconggan/SuperMimic_e1](https://github.com/wenconggan/SuperMimic_e1) | 4 | E1 21DoF 适配，训练后可在原生 MuJoCo sim2sim | DroidUp E1，40 条 LAFAN1 跟踪 | Isaac Lab 3／Newton／MuJoCo Warp |
| [OMEGA-i/SuperMimicKit](https://github.com/OMEGA-i/SuperMimicKit) | 3 | 多本体工具包，含重定向、训练、ONNX 和 WebGPU 演示 | G1／H2／A3，LaFAN 跟踪 | PyTorch／MuJoCo Warp；参考 zita-ch |
| [liuskywalkerjskd/supermimic_oli](https://github.com/liuskywalkerjskd/supermimic_oli) | 3 | Oli 31DoF 重定向、训练和完整 rollout 导出，保留 G1 | LimX Oli／G1，40 条 LAFAN1 | zita-ch／Isaac Lab 3 |
| [mode1223345/SuperMimic-perceptive](https://github.com/mode1223345/SuperMimic-perceptive) | 4 | 预训练并冻结共享高程图 AE，含平地／台阶对照 | G1 平地与 4/8/4 cm 台阶感知跟踪 | zita-ch／Isaac Lab 3 |
| [NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real](https://github.com/NJU-R-L-Group-Embodied-Lab/SuperMimic-Repro-Sim2Real) | 8 | CuboiLeo 改造：大数据集训练、自定义舞蹈动作、视频提取动作工具与整套 G1 真机部署 | G1，LAFAN1／BONES-SEED 跟踪＋真机部署 | CuboiLeo/SuperMimic-Reproduced |
| [liudi159/supermimic-backflip-5090](https://github.com/liudi159/supermimic-backflip-5090) | 2 | 单张 RTX 5090 G1 后空翻从零训练：固定 supermimic_vibed 提交＋训练适配、接触力校验与评测（作者自报严格验收仍有 1 帧穿透） | G1 后空翻单动作高动态训练 | zita-ch/supermimic_vibed（固定提交）／Isaac Lab |
| [yhx1203/supermimic_parkour](https://github.com/yhx1203/supermimic_parkour) | 6 | PHP 跑酷五技能训练（130 cm 障碍，单 GPU 约 4 h），含地形、teacher 与评测 | G1 PHP 跑酷：low／high step、climb 76／130 | 参考 SuperMimic 思路；PHP parkour motion_matching；mjlab |
| [WXyuany/supermimic-m5](https://github.com/WXyuany/supermimic-m5) | 1 | Apple Silicon 适配，MPS 学习＋CPU MuJoCo | G1，40 条 LAFAN1，Mac 从零训练 | CuboiLeo／mjlab |
| [coolcooldiyang/RPO-SuperMimic](https://github.com/coolcooldiyang/RPO-SuperMimic) | 1 | Uni-SuperMimic 移植到 RoboParty RPO 23-DoF 新本体，含跑步与后空翻两套策略、并联踝控制与重定向工具 | RPO 23-DoF，跑步／后空翻动作跟踪 | Motphys/Uni-SuperMimic；MJWarp／MuJoCo |
| [Alchedata/supermimic-locomujoco](https://github.com/Alchedata/supermimic-locomujoco) | 1 | JAX 独立移植，含 WM 基线与残差专家等变体、评测与断点续训 | Unitree H1，40 条 LAFAN1 全身跟踪 | 独立 LocoMuJoCo 移植（JAX）；参考 SuperMimic 原论文 |
| [PrimebotTech/SuperMimic](https://github.com/PrimebotTech/SuperMimic) | 1 | Q1 V2 独立训练栈，单／八卡、续训、筛选和录像 | Q1 V2 全身动作跟踪 | PyTorch／MuJoCo／MuJoCo Warp |
| [chu-fa/isaaclab-supermimic](https://github.com/chu-fa/isaaclab-supermimic) | 1 | 通用任务接口与 A3 示例，含数据处理、训练和评测 | 自定义任务；Agibot A3 LAFAN1 跟踪 | Isaac Lab |
| [yuntian137/supermimic_lab](https://github.com/yuntian137/supermimic_lab) | 0 | 工程化安装、配置、训练恢复、评测与录像 | G1，40 条 LAFAN1 | zita-ch／Isaac Lab 3 |
| [shangchaohu718/supermimic-pera](https://github.com/shangchaohu718/supermimic-pera) | 0 | 从跟踪扩展到交互，含独立滑板技能训练与残差原型 | G1 跟踪、滑板；楼梯／搬箱仍在研发 | Motphys/Uni-SuperMimic |
| [Mark054/SuperMimic_TienKung](https://github.com/Mark054/SuperMimic_TienKung) | 0 | 天工 3.0 独立适配，附模型、数据、转换和多卡训练 | 天工 3.0 全身跟踪 | mjlab；GMR 重定向 |
| [sxh-kk/SuperMimic_Recurrence](https://github.com/sxh-kk/SuperMimic_Recurrence) | 0 | RTX 4090／CUDA 12 适配，并探索 Ollie／滑板路线 | G1 LAFAN1／BONES-SEED；Ollie 实验 | CuboiLeo／mjlab |

## 已核查但暂不收录主表

| 仓库 | 原因 |
|---|---|
| [KyrieYoung926/supermimic_deploy](https://github.com/KyrieYoung926/supermimic_deploy) | 部署／真机项目，未发现训练入口；其训练上游已单列。 |
| [jackzedgar/SuperDex](https://github.com/jackzedgar/SuperDex) | 当前只有概念 README，未见完整训练代码。 |
| [yagami-light7/SuperMimic-codex](https://github.com/yagami-light7/SuperMimic-codex) | 当前为 M0 环境冒烟，README 明确等待后续训练实现。 |
| [zzhanYoung/supermimic-lite](https://github.com/zzhanYoung/supermimic-lite) | 当前内容主要是 mjlab 上游框架，未核实到 SuperMimic WM 训练闭环。 |
| [Tianao-Zhang/supermimic_dualhand](https://github.com/Tianao-Zhang/supermimic_dualhand) | 仓库当前为空（GitHub 返回 empty repository），无可核查的训练代码；下轮复查。 |
| [yangkunpeng-coder/supermimic_reproduce](https://github.com/yangkunpeng-coder/supermimic_reproduce) | 仓库当前仅有 LICENSE，无任何训练代码；下轮复查。 |
| [BlackOtters/supermimicA3](https://github.com/BlackOtters/supermimicA3) | 原主表条目；本轮核查仓库返回 404（可能已删除或转私有），无法复核训练代码，移出主表；如下轮恢复可重新核查。 |
| [Green-Fr0g/supermimic](https://github.com/Green-Fr0g/supermimic) | 10-26 新增工程骨架（Isaac Lab 3.0 任务包＋vendored rsl_rl PPO 库＋数据转换脚本），但注册任务仍为 Cartpole 占位，未核实到 SuperMimic WM／BPTT 训练闭环。 |
| [huangkiki/awesome-supermimic](https://github.com/huangkiki/awesome-supermimic) | SuperMimic 资源合集（实现／演示／资料列表），本身无训练代码。 |
| [DiaoOrg/awesome-supermimic](https://github.com/DiaoOrg/awesome-supermimic) | SuperMimic 资源合集（与 huangkiki 列表同类的实现／演示／资料列表），本身无训练代码。 |

## 社区平台检索记录

社区内容的发布时间、任务类型和代码状态单独维护在 **[COMMUNITY_TASKS.md](COMMUNITY_TASKS.md)**。

- **GitHub**：组合检索 `supermimic`、`super mimic`、arXiv 编号及底座关键词，覆盖仓库名称、简介、README、文档和代码；对候选仓库显式枚举分支，检查 `supermimic` 等非默认分支的说明文件与训练实现。
- **Bilibili**：2026-10-25 15:35 轮起改用 `community_collect.py` 经公开 HTTP API 采集（检索 SuperMimic／super mimic／superminic，按发布时间前 3 页，含候选详情与公开评论，评论状态非 ok 不声称已核查）。15:35 轮实时采集成功（28 条候选、16 条新条目），Motphys 官方“单卡 40 分钟速通 LAFAN”视频经简介直链 Uni-SuperMimic 核实并入时间线；17:45 轮实时采集成功（29 条候选、1 条新条目），SuperMimic 2D 复现视频（BV1DQH56JEqi）经简介与作者评论直链 FlatWorld，静态核查 `supermimic2d` 训练闭环后收录主表；20:45 轮实时采集成功（29 条候选、0 条新条目，无缓存依赖），时间线无变化；23:45 轮实时采集成功（30 条候选、1 条新条目：感知行走 1 小时出炉，BV1NPHL6GEat，作者称在 zita-ch 复现库上经 Codex 修改、无 locomotion／style reward，未给仓库，标“任务展示”）；2026-10-26 02:45 轮实时采集成功（31 条候选、3 条新条目：Day 54 学习日志、unisupermimic 复现展示、论文方法讲解各 1 条，均未给仓库，标“任务展示”）；05:45 轮实时采集成功（34 条候选、1 条新条目：5070Ti 跑通 mjlab 复现 12000 轮，BV1U5nS6zETw，未指明仓库，标“任务展示”）；05:50 轮实时采集（cache_hits=0）但覆盖面收窄：仅返回 14 条候选且全部为 10-22／10-23 早期内容、0 条新条目，时间线无变化，下轮复核覆盖面；08:45 轮实时采集成功（cache_hits=0，覆盖面恢复）：34 条候选、0 条新条目；11:45 轮实时采集成功（cache_hits=0）：34 条候选、1 条新条目（SuperMimic 原理讲解 BV1TEnQ6yEYi，10-26 10:00，未给仓库，标“任务展示”）；14:45 轮实时采集成功（cache_hits=0）：35 条候选、0 条新条目；17:45 轮实时采集成功（cache_hits=0）：35 条候选、0 条新条目；23:45 轮实时采集成功（cache_hits=0）：37 条候选、2 条新条目（BV1ZSnU6REij 太空步微调、BV1EPnZ6EE9b 闪身步，均未给仓库，标“任务展示”）；2026-10-27 02:45 轮实时采集成功（cache_hits=0）：39 条候选、2 条新条目（BV1i4no6CEzs 闪身步 2.0、BV1f3HF6nE7A 方法讲解，均未给仓库）；05:45 轮实时采集（cache_hits=0）但覆盖面收窄：仅返回 19 条候选、0 条新条目，时间线无变化，下轮复核覆盖面。此前登录态网页轮次已整理深度图地形、HOI 搬箱、E1、灵龙 2.0、RGMT、Oli、Mac Studio、闪身步和高难动作等任务；只把能回溯到公开仓库且通过训练代码核查的项目并入主表，不绕过反爬。
- **小红书**：已利用用户登录态检索，通过页面状态／DOM 提取正文和时间，并核查重点笔记的公开可访问评论；已有 15 条社区记录，M5 等条目由作者评论或正文定位到已核实仓库。2026-10-25 15:35 起连续各轮（含 2026-10-27 05:45）脚本采集状态均为 needs_auth（本机 `.secrets/xiaohongshu_cookie.txt` 缺失），均未新增小红书条目，既有的 15 条全部保留；需更新本机 Cookie 文件后下轮重试，不绕过登录与访问控制。文档只保存不含访问令牌的规范链接。
- 平台简介及公开可访问评论中的 homepage／GitHub 仅作为候选线索，不作为“训练完整”的证据；HOI、地形、跑酷、各种 humanoid task 和其他机器人任务均纳入检索范围。

## 更新约定

每 3 小时执行一次增量检索：读取旧版主表与社区时间线，去重候选，显式枚举候选仓库的默认及相关非默认分支，复核训练链路，提炼任务和上游底座，并刷新所有主表仓库 Star。新增仓库、HOI 等新任务或社区条目时同步更新对应文档和“最近核查”时间；仅有 Star 变化也提交更新，完全无变化则不制造空提交。
