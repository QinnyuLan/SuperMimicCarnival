# SuperMimic 社区新任务时间线

汇总 **2026-10-20** 以来 Bilibili、小红书上与 SuperMimic 有关的新任务、新本体和训练方式改造，按内容公开发布时间升序排列。时间为 **UTC+8**；最近核查：**2026-10-25 20:45**。

## 状态口径

- **训练已核实**：内容简介、作者评论或其直接给出的主页能定位到仓库／分支，并已静态核查到训练入口、世界模型／策略／价值网络学习代码及配置或数据流程。
- **相关仓库已核实**：存在主题相关的公开训练仓库，但内容没有明确证明它就是该条内容的专用源码。
- **任务展示**：看到了任务或效果，但尚未核实对应改造已公开完整训练实现；不等于该项目没有训练，也不把演示效果当作开源证据。

## 时间线

| 发布时间 | 平台／内容 | 新任务或改造 | 代码状态与证据 |
|---|---|---|---|
| 2026-10-22 00:13:31 | Bilibili · [SuperMimic: 单一可微世界模型的人形机器人规模化全身控制](https://www.bilibili.com/video/BV1Mjn66jE9n/) | 论文官方介绍视频 | **任务展示**。视频简介为论文摘要；公开评论中观众贴出 `zita-ch/supermimic_vibed` 链接（非作者给出），不作为视频本身的源码证据。 |
| 2026-10-22 17:29:23 | Bilibili · [简单复现supermimic用的lafan1数据集，4090单卡3个小时，是真的牛](https://www.bilibili.com/video/BV11Lnm6FEDt/) | LAFAN1 复现；标题称 4090 单卡 3 h | **任务展示**。简介未给仓库或主页；评论追问抗 push 能力未获作者回应，时长为作者自报。 |
| 2026-10-23 00:06:47 | Bilibili · [SuperMimic已经复现 单卡40分钟速通lafan](https://www.bilibili.com/video/BV1AQnn6DEBE/) | 单卡 40 分钟速通 LAFAN1 | **训练已核实**。Motphys 官方账号发布，简介直达 [Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)，已收录主表。 |
| 2026-10-23 10:23:06 | 小红书 · [来蹭一波supermimic的hoi](https://www.xiaohongshu.com/explore/6adac50a000000003102d11b) | **HOI：简单搬箱**；作者称只训练数小时，4090 单卡、参考轨迹不多、单任务，未做 scale-up；评论讨论物体角点观测，碰撞与 scale-up 仍待验证 | **任务展示**。作者称由几个开源 SuperMimic 复现与另一个搬箱项目缝合，但未给专用仓库；与下方 B 站 HOI 内容相互参照。 |
| 2026-10-23 10:25:53 | Bilibili · [Supermimic适配DroidUp E1机器人](https://www.bilibili.com/video/BV1Nfn46gECZ/) | DroidUp E1 21DoF 新本体适配 | **训练已核实**。简介直达 [SuperMimic_e1](https://github.com/wenconggan/SuperMimic_e1)，已收录主表。 |
| 2026-10-23 10:53:38 | Bilibili · [Supermimic和RGMT效果对比](https://www.bilibili.com/video/BV1ZGnt68EEZ/) | 相同数据集下对比 SuperMimic 与 RGMT 的训练效果 | **训练已核实**。简介直达 [Supermimic_mod](https://github.com/YanYuan98/Supermimic_mod)，已收录主表；视频效果不作为独立复跑结论。 |
| 2026-10-23 10:59:44 | Bilibili · [Supermimic深度图20cm地形codex版本](https://www.bilibili.com/video/BV1n3nt6wEKn/) | 深度图输入、20 cm 地形；发布者称使用 Codex 复现 | **任务展示**。简介未给仓库或主页，未核实该版本的公开训练代码。 |
| 2026-10-23 11:35:29 | Bilibili · [灵龙2.0 4h 双4090 superminic](https://www.bilibili.com/video/BV1den464EBz/) | 灵龙 2.0 新本体；标题称双 4090 训练 4 h，原标签使用 `superminic` 拼写 | **任务展示**。简介未给仓库或主页，未核实该本体改造的公开训练代码。 |
| 2026-10-23 11:46:22 | Bilibili · [继续复现supermimic，还是用lafan1数据集](https://www.bilibili.com/video/BV1t9n46CEWY/) | LAFAN1 复现续作 | **任务展示**。简介为“-”，未给仓库；评论询问世界模型是否需重训，未获作者答复。 |
| 2026-10-23 11:47:29 | 小红书 · [instinct-supermimic 蹭一波supermimic热度](https://www.xiaohongshu.com/explore/6adad8d1000000002c03430f) | Instinct 路线改造；作者称 RTX 3090 上训练一晚 | **相关仓库已核实**。简介与公开评论未给链接；主表已有 [InstinctMJ supermimic 分支](https://github.com/project-instinct/InstinctMJ/tree/supermimic)，但不据此断言为该笔记专用源码。 |
| 2026-10-23 11:59:22 | Bilibili · [superinstinct mimic深度图版本](https://www.bilibili.com/video/BV1Tdn46GEzH/) | G1 深度视觉地形跑酷；视频对应旧版在 RTX 3090 上训练 5.7 h | **训练已核实**。简介直达 [InstinctMJ 的 supermimic 分支](https://github.com/project-instinct/InstinctMJ/tree/supermimic)，已收录主表；分支包含完整 WM、策略、critic、配置、训练与评测链路。 |
| 2026-10-23 12:00:45 | Bilibili · [SuperMimic HOI 之搬搬箱](https://www.bilibili.com/video/BV1Tdn46GEaj/) | **HOI／手物交互：搬箱**；作者称训练 5 h 收敛，并指出 scale-up 与碰撞建模仍需验证 | **任务展示**。简介未给该 HOI 改造的仓库或主页；上方小红书评论进一步说明单任务、单卡训练与待验证项，仍不能据此标记为已开源复现。 |
| 2026-10-23 12:27:44 | Bilibili · [supermimic➕rgmt有没有搞头](https://www.bilibili.com/video/BV1pnn46KEjh/) | 探索 SuperMimic 与 RGMT 结合 | **任务展示**。简介无仓库或主页，未核实该组合改造的公开训练代码。 |
| 2026-10-23 12:40:24 | Bilibili · [USTC旧版一代人形机器人+supermimic](https://www.bilibili.com/video/BV1bun46CEPW/) | USTC 旧版一代人形机器人本体适配 | **任务展示**。简介为空，未核实该本体改造的公开训练代码。 |
| 2026-10-23 13:07:19 | 小红书 · [Supermimic H2 Reproduction](https://www.xiaohongshu.com/explore/6adaeb87000000002c0390da) | H2 本体与 BONES-SEED；作者置顶评论自报 4 h 37 min、达成率 98.56%，部分高动态动作仍失败 | **任务展示**。正文只给论文主页，公开评论未给 H2 专用仓库；自报指标未独立复跑。 |
| 2026-10-23 17:24:37 | 小红书 · [supermimic滑滑板](https://www.xiaohongshu.com/explore/6adb27d500000000310361e1) | 人形机器人滑板任务 | **任务展示**。简介与公开评论未给专用仓库；不与主表现有滑板项目强行绑定。 |
| 2026-10-23 17:48:20 | Bilibili · [给mbrl磕一个，supermimic太厉害了](https://www.bilibili.com/video/BV1RFnb6tENb/) | SuperMimic 复现展示 | **任务展示**。简介为“-”；评论询问基于哪个仓库改造，未获作者答复。 |
| 2026-10-23 18:34:34 | 小红书 · [supermimic多本体适配](https://www.xiaohongshu.com/explore/6adb383a000000003102c4aa) | G1／X2 Ultra／A3 Ultra 多本体动作重定向与跟踪 | **训练已核实**。正文直达 [supermimic-retargeted](https://github.com/tianshuwu/supermimic-retargeted)，已收录主表。 |
| 2026-10-23 19:12:45 | 小红书 · [在m5Mac上复现了一下supermimic](https://www.xiaohongshu.com/explore/6adb412d000000002c015510) | Apple M5 Mac 训练；作者评论确认使用 mjlab | **训练已核实**。作者评论直接给出 [supermimic-m5](https://github.com/WXyuany/supermimic-m5)，已收录主表。 |
| 2026-10-23 19:27:50 | Bilibili · [supermimic复现](https://www.bilibili.com/video/BV18jnh6sEts/) | 作者称 4 h 全量训练收敛 BONES-SEED 高动态动作（训练时剔除强环境和物体交互动作） | **任务展示**。简介未给仓库；高动态收敛为作者自报。 |
| 2026-10-23 21:35:36 | Bilibili · [Mac Studio 上训练 SuperMimic](https://www.bilibili.com/video/BV1uin86XEDR/) | Apple M5 Ultra 训练；作者称单台训练 5 h | **任务展示**。简介未给仓库；主表虽另有 M5 训练仓库，但没有证据把该视频与其直接绑定。 |
| 2026-10-23 21:46:58 | 小红书 · [给supermimic喂点omniretarget数据](https://www.xiaohongshu.com/explore/6adb6552000000002c0141f7) | 将 OmniRetarget 数据用于 SuperMimic 训练 | **任务展示**。简介与公开评论未给仓库或主页。 |
| 2026-10-23 22:19:25 | Bilibili · [supermimic复现玩玩](https://www.bilibili.com/video/BV11zn86SE2S/) | SuperMimic 复现展示 | **任务展示**。简介称复现较晚，未给仓库或主页。 |
| 2026-10-23 22:27:10 | Bilibili · [宇树机器人闪身步](https://www.bilibili.com/video/BV14kn86UEVU/) | 宇树人形机器人仿真闪身步 | **任务展示**。简介给出论文主页和通用上游 `zita-ch/supermimic_vibed`，未给闪身步专项改造仓库。 |
| 2026-10-23 23:04:32 | 小红书 · [supermimic训练parkour](https://www.xiaohongshu.com/explore/6adb7780000000002502360d) | PHP 全套跑酷动作；作者称单 4090 训练 1 h，评论说明将原 PPO 框架替换为 SuperMimic，障碍物信息进入 WM，mimic 阶段无感知 | **任务展示**。作者评论确认使用 PHP 开源 motion，但未给改造仓库；训练时长为作者自报。 |
| 2026-10-23 23:36:46 | Bilibili · [给supermimic磕了，单卡4090训练100分钟](https://www.bilibili.com/video/BV1ZEn86PE9D/) | 自制机器人本体适配；作者称参考 Uni-SuperMimic 实现，单卡 4090 训练 100 分钟 | **相关仓库已核实**。简介称参考 [Uni-SuperMimic](https://github.com/Motphys/Uni-SuperMimic)（已收录主表），但自制本体适配未给专用仓库；时长为作者自报。 |
| 2026-10-24 02:13:09 | Bilibili · [冰冷的 token 化作了温暖的 SuperMimic](https://www.bilibili.com/video/BV1cVna6jEFA/) | 人形全身动作跟踪；发布者与 Oli 适配仓库所有者同名 | **相关仓库已核实**。简介仅给论文与通用上游；[supermimic_oli](https://github.com/liuskywalkerjskd/supermimic_oli) 已有完整 Oli／G1 训练实现，但不把它断言为该视频专用源码。 |
| 2026-10-24 04:04:48 | 小红书 · [Code for go2-supermimic](https://www.xiaohongshu.com/explore/6adbbde00000000032016d45) | Go2 四足平地／障碍／复杂地形追逐与闪避 | **训练已核实**。正文直达 [go2-supermimic](https://github.com/Zhengtianjin/go2-supermimic)，已收录主表。 |
| 2026-10-24 04:23:02 | Bilibili · [SuperMimic-Overview](https://www.bilibili.com/video/BV1Dzne6KEgN/) | 论文解读系列（Overview） | **任务展示**。无简介与仓库链接，属论文讲解内容。 |
| 2026-10-24 10:07:12 | 小红书 · [supermimic跨本体尝试](https://www.xiaohongshu.com/explore/6adc12d0000000002d006924) | Booster T1 29DoF 跨本体；LAFAN walk 重定向，作者称约 3000 轮不足 10 min，基于 `supermimic_vibe` 粗糙改造 | **任务展示**。正文只指通用上游，公开评论未给 T1 专用仓库；训练时长为作者自报。 |
| 2026-10-24 10:23:30 | Bilibili · [SuperMimic：单卡3小时训练人形机器人全身控制｜2026 CoRL【UC Berkeley】](https://www.bilibili.com/video/BV1vFHA6xEJu/) | 论文新闻解读 | **任务展示**。媒体解读视频，简介给论文主页与 arXiv，无新训练证据。 |
| 2026-10-24 13:00:18 | 小红书 · [MorphMimic：一世界🌏，一模型🤖](https://www.xiaohongshu.com/explore/6adc3b62000000001901ec00) | G1／X2 Ultra／T2 共享形态条件化 WM／策略，支持五点稀疏跟踪 | **训练已核实**。正文给出 [MorphMimic 主页](https://lzyang2000.github.io/morphmimic/)，对应 [morphmimic](https://github.com/lzyang2000/morphmimic) 已收录主表。 |
| 2026-10-24 16:21:40 | Bilibili · [36 分钟速通高难度动作](https://www.bilibili.com/video/BV1XaHP6pEMW/) | BONES-SEED 高难动作、LAFAN1、AMASS／MotionDecode 泛化与 single-clip adaptation；包含多项训练改动 | **训练已核实**。简介直达 [Shimingyi/allmimic](https://github.com/Shimingyi/allmimic)，已收录主表；作者所述速度与成功率属于自报结果，未作独立复跑。 |
| 2026-10-24 16:25:30 | 小红书 · [SuperMimic复现36分钟速通高难动作](https://www.xiaohongshu.com/explore/6adc6b7a0000000013033800) | 高难动作与泛化评测，强调可行性过滤和 held-out 划分 | **训练已核实**。正文直达 [allmimic](https://github.com/Shimingyi/allmimic)，已收录主表。 |
| 2026-10-24 16:37:21 | 小红书 · [supermimic高动态parkour](https://www.xiaohongshu.com/explore/6adc6e410000000033019df5) | G1 高动态跑酷、130 cm 上箱；评论称使用 PHP 开源 motion、纯 mimic，障碍物位置／朝向输入 WM，未输入感知 | **任务展示**。简介与公开评论未给改造仓库。 |
| 2026-10-24 21:22:32 | 小红书 · [supermimic喂点php数据，高难度时会有失败](https://www.xiaohongshu.com/explore/6adcb1180000000024034dfe) | PHP 数据上的高难动作实验，展示失败情形 | **任务展示**。简介与公开评论未给仓库或主页，评论中视觉问题未获作者确认。 |
| 2026-10-24 22:00:33 | 小红书 · [supermimic上做smp](https://www.xiaohongshu.com/explore/6adcba01000000002c01ba21) | SMP 方向改造展示；原内容未展开 SMP 含义，不作额外推断 | **任务展示**。无公开评论，简介未给仓库或主页。 |
| 2026-10-24 23:34:39 | Bilibili · [SuperMimic](https://www.bilibili.com/video/BV1o8HM6gEYp/) | SuperMimic 相关展示 | **任务展示**。简介给出的 [catbrain](https://github.com/ZiwenZhuang/catbrain) 为视频生成工具，非 SuperMimic 训练代码。 |
| 2026-10-25 03:49:24 | Bilibili · [SuperMimic-Training_Loop](https://www.bilibili.com/video/BV1PLHg6bEUT/) | 训练循环讲解（Training_Loop） | **任务展示**。无简介与仓库链接，属论文讲解内容。 |
| 2026-10-25 09:14:11 | Bilibili · [AI十分钟复现supermimic](https://www.bilibili.com/video/BV1zuH36HEXB/) | 作者称 5080 一晚上训出 | **任务展示**。简介未给仓库；时长为作者自报。 |
| 2026-10-25 09:50:54 | Bilibili · [当rgmt和supermimic杂交](https://www.bilibili.com/video/BV1mSHg6NEdE/) | 探索 RGMT 与 SuperMimic 结合；作者评论称对 pico 低质数据适应良好（蹲走、正步、跳远等） | **任务展示**。简介为“-”，未给改造仓库；效果为作者自报。 |
| 2026-10-25 13:06:16 | Bilibili · [复现 SuperMimic：一张显卡两小时，让 G1 成为职业羽毛球运动员](https://www.bilibili.com/video/BV1RxHV6EEcG/) | **羽毛球全身跟踪新任务**：GVHMR 重建 ShuttleSet 职业比赛动作→GMR 重定向到 G1→SuperMimic 训练；作者称单卡 2 h、255 个回合九成以上整段跟踪 | **任务展示**。简介未给仓库；训练时长与成功率为作者自报。 |
| 2026-10-25 13:51:43 | Bilibili · [supermimic-go2-locomotion](https://www.bilibili.com/video/BV1CPHV6YEfh/) | Go2 四足 locomotion | **任务展示**。简介只给论文主页，未给仓库；评论询问训练时长与数据来源，未获作者答复。 |
| 2026-10-25 17:07:03 | Bilibili · [SuperMimic在2D场景复现，消费级显卡15分钟就可以](https://www.bilibili.com/video/BV1DQH56JEqi/) | 自研 2D 引擎 FlatWorld 上的 SuperMimic 复现：共享刚体 WM＋短想象 BPTT 策略改进；作者称 5060 消费级显卡 15 min 训练完成 | **训练已核实**。简介与作者评论均直链 [FlatWorld](https://github.com/swaggyliu/FlatWorld)，已静态核查 `supermimic2d` 训练闭环（train.py、WM／策略／critic、参考动作烘焙管线）并收录主表；训练时长为作者自报。 |

## 检索与访问记录

- **Bilibili**：使用 `community_collect.py` 经公开 HTTP API 无浏览器采集（未调用 InAppBrowser），检索 SuperMimic／super mimic／superminic，按发布时间检查前 3 页，抓取新候选详情与公开评论；接口失败时不得把缓存当实时结果。15:35 轮实时采集成功：28 条候选、16 条新条目进入时间线，引用评论的条目 comments_status 均为 ok；14:40 轮遗留的 Motphys“单卡 40 分钟速通 LAFAN”线索核实为 BV1AQnn6DEBE（10-23 00:06），简介直链 Uni-SuperMimic，标“训练已核实”。17:45 轮实时采集成功（cache_hits=0）：29 条候选、1 条新条目（SuperMimic 2D 复现，BV1DQH56JEqi，10-25 17:07），简介与作者评论直链 FlatWorld 并收录主表。20:45 轮实时采集成功（cache_hits=0）：29 条候选、0 条新条目，时间线无变化。
- **小红书**：2026-10-25 15:35、17:45 与 20:45 轮脚本采集状态均为 **needs_auth**：本机 `.secrets/xiaohongshu_cookie.txt` 缺失（报错明确提示配置文件），小红书记为未检索成功，无新增条目，既有 15 条全部保留；请更新本机 Cookie 文件后下轮重试，不读取、不打印、不提交 Cookie，不绕过登录与访问控制。文档只保存不含访问令牌的规范笔记链接。
- 简介和评论中的仓库、主页只是候选线索；只有完成训练链路静态核查后才标“训练已核实”。登录失效或评论不可访问时记录限制并留待下轮，不绕过访问控制。

## 后续增量规则

1. 检查新内容的简介及公开可访问评论中的 homepage、GitHub 和分支链接，同时覆盖 HOI、地形、跑酷、移动操作、各种 humanoid task，以及四足等其他机器人。
2. 每轮运行 `community_collect.py`，通过公开 HTTP API 与本地只读命令行采集，不调用浏览器；保存不含访问令牌的规范链接。小红书 Cookie 缺失或失效时明确降级并保留下轮重试，不影响其他来源。
3. 新内容按上述时间线追加；旧内容只有获得新证据时才修订状态，并保留原始发布时间。
4. 对候选仓库显式枚举分支，检查 `supermimic` 等非默认分支中的 README、训练入口和学习代码，避免只搜仓库主页面。
5. 只有训练链路通过静态核查的仓库才进入主 README；社区演示可以继续留在这里，但必须保留“任务展示”状态。
