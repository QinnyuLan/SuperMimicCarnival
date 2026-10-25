# SuperMimic 社区新任务时间线

汇总 **2026-10-20** 以来 Bilibili、小红书上与 SuperMimic 有关的新任务、新本体和训练方式改造，按内容公开发布时间升序排列。时间为 **UTC+8**；最近核查：**2026-10-25 08:57**。

## 状态口径

- **训练已核实**：内容简介、作者评论或其直接给出的主页能定位到仓库／分支，并已静态核查到训练入口、世界模型／策略／价值网络学习代码及配置或数据流程。
- **相关仓库已核实**：存在主题相关的公开训练仓库，但内容没有明确证明它就是该条内容的专用源码。
- **任务展示**：看到了任务或效果，但尚未核实对应改造已公开完整训练实现；不等于该项目没有训练，也不把演示效果当作开源证据。

## 时间线

| 发布时间 | 平台／内容 | 新任务或改造 | 代码状态与证据 |
|---|---|---|---|
| 2026-10-23 10:23:06 | 小红书 · [来蹭一波supermimic的hoi](https://www.xiaohongshu.com/explore/6adac50a000000003102d11b) | **HOI：简单搬箱**；作者称只训练数小时，4090 单卡、参考轨迹不多、单任务，未做 scale-up；评论讨论物体角点观测，碰撞与 scale-up 仍待验证 | **任务展示**。作者称由几个开源 SuperMimic 复现与另一个搬箱项目缝合，但未给专用仓库；与下方 B 站 HOI 内容相互参照。 |
| 2026-10-23 10:25:53 | Bilibili · [Supermimic适配DroidUp E1机器人](https://www.bilibili.com/video/BV1Nfn46gECZ/) | DroidUp E1 21DoF 新本体适配 | **训练已核实**。简介直达 [SuperMimic_e1](https://github.com/wenconggan/SuperMimic_e1)，已收录主表。 |
| 2026-10-23 10:53:38 | Bilibili · [Supermimic和RGMT效果对比](https://www.bilibili.com/video/BV1ZGnt68EEZ/) | 相同数据集下对比 SuperMimic 与 RGMT 的训练效果 | **训练已核实**。简介直达 [Supermimic_mod](https://github.com/YanYuan98/Supermimic_mod)，已收录主表；视频效果不作为独立复跑结论。 |
| 2026-10-23 10:59:44 | Bilibili · [Supermimic深度图20cm地形codex版本](https://www.bilibili.com/video/BV1n3nt6wEKn/) | 深度图输入、20 cm 地形；发布者称使用 Codex 复现 | **任务展示**。简介未给仓库或主页，未核实该版本的公开训练代码。 |
| 2026-10-23 11:35:29 | Bilibili · [灵龙2.0 4h 双4090 superminic](https://www.bilibili.com/video/BV1den464EBz/) | 灵龙 2.0 新本体；标题称双 4090 训练 4 h，原标签使用 `superminic` 拼写 | **任务展示**。简介未给仓库或主页，未核实该本体改造的公开训练代码。 |
| 2026-10-23 11:47:29 | 小红书 · [instinct-supermimic 蹭一波supermimic热度](https://www.xiaohongshu.com/explore/6adad8d1000000002c03430f) | Instinct 路线改造；作者称 RTX 3090 上训练一晚 | **相关仓库已核实**。简介与公开评论未给链接；主表已有 [InstinctMJ supermimic 分支](https://github.com/project-instinct/InstinctMJ/tree/supermimic)，但不据此断言为该笔记专用源码。 |
| 2026-10-23 11:59:22 | Bilibili · [superinstinct mimic深度图版本](https://www.bilibili.com/video/BV1Tdn46GEzH/) | G1 深度视觉地形跑酷；视频对应旧版在 RTX 3090 上训练 5.7 h | **训练已核实**。简介直达 [InstinctMJ 的 supermimic 分支](https://github.com/project-instinct/InstinctMJ/tree/supermimic)，已收录主表；分支包含完整 WM、策略、critic、配置、训练与评测链路。 |
| 2026-10-23 12:00:45 | Bilibili · [SuperMimic HOI 之搬搬箱](https://www.bilibili.com/video/BV1Tdn46GEaj/) | **HOI／手物交互：搬箱**；作者称训练 5 h 收敛，并指出 scale-up 与碰撞建模仍需验证 | **任务展示**。简介未给该 HOI 改造的仓库或主页；上方小红书评论进一步说明单任务、单卡训练与待验证项，仍不能据此标记为已开源复现。 |
| 2026-10-23 12:27:44 | Bilibili · [supermimic➕rgmt有没有搞头](https://www.bilibili.com/video/BV1pnn46KEjh/) | 探索 SuperMimic 与 RGMT 结合 | **任务展示**。简介无仓库或主页，未核实该组合改造的公开训练代码。 |
| 2026-10-23 12:40:24 | Bilibili · [USTC旧版一代人形机器人+supermimic](https://www.bilibili.com/video/BV1bun46CEPW/) | USTC 旧版一代人形机器人本体适配 | **任务展示**。简介为空，未核实该本体改造的公开训练代码。 |
| 2026-10-23 13:07:19 | 小红书 · [Supermimic H2 Reproduction](https://www.xiaohongshu.com/explore/6adaeb87000000002c0390da) | H2 本体与 BONES-SEED；作者置顶评论自报 4 h 37 min、达成率 98.56%，部分高动态动作仍失败 | **任务展示**。正文只给论文主页，公开评论未给 H2 专用仓库；自报指标未独立复跑。 |
| 2026-10-23 17:24:37 | 小红书 · [supermimic滑滑板](https://www.xiaohongshu.com/explore/6adb27d500000000310361e1) | 人形机器人滑板任务 | **任务展示**。简介与公开评论未给专用仓库；不与主表现有滑板项目强行绑定。 |
| 2026-10-23 18:34:34 | 小红书 · [supermimic多本体适配](https://www.xiaohongshu.com/explore/6adb383a000000003102c4aa) | G1／X2 Ultra／A3 Ultra 多本体动作重定向与跟踪 | **训练已核实**。正文直达 [supermimic-retargeted](https://github.com/tianshuwu/supermimic-retargeted)，已收录主表。 |
| 2026-10-23 19:12:45 | 小红书 · [在m5Mac上复现了一下supermimic](https://www.xiaohongshu.com/explore/6adb412d000000002c015510) | Apple M5 Mac 训练；作者评论确认使用 mjlab | **训练已核实**。作者评论直接给出 [supermimic-m5](https://github.com/WXyuany/supermimic-m5)，已收录主表。 |
| 2026-10-23 21:35:36 | Bilibili · [Mac Studio 上训练 SuperMimic](https://www.bilibili.com/video/BV1uin86XEDR/) | Apple M5 Ultra 训练；作者称单台训练 5 h | **任务展示**。简介未给仓库；主表虽另有 M5 训练仓库，但没有证据把该视频与其直接绑定。 |
| 2026-10-23 21:46:58 | 小红书 · [给supermimic喂点omniretarget数据](https://www.xiaohongshu.com/explore/6adb6552000000002c0141f7) | 将 OmniRetarget 数据用于 SuperMimic 训练 | **任务展示**。简介与公开评论未给仓库或主页。 |
| 2026-10-23 22:27:10 | Bilibili · [宇树机器人闪身步](https://www.bilibili.com/video/BV14kn86UEVU/) | 宇树人形机器人仿真闪身步 | **任务展示**。简介给出论文主页和通用上游 `zita-ch/supermimic_vibed`，未给闪身步专项改造仓库。 |
| 2026-10-23 23:04:32 | 小红书 · [supermimic训练parkour](https://www.xiaohongshu.com/explore/6adb7780000000002502360d) | PHP 全套跑酷动作；作者称单 4090 训练 1 h，评论说明将原 PPO 框架替换为 SuperMimic，障碍物信息进入 WM，mimic 阶段无感知 | **任务展示**。作者评论确认使用 PHP 开源 motion，但未给改造仓库；训练时长为作者自报。 |
| 2026-10-24 02:13:09 | Bilibili · [冰冷的 token 化作了温暖的 SuperMimic](https://www.bilibili.com/video/BV1cVna6jEFA/) | 人形全身动作跟踪；发布者与 Oli 适配仓库所有者同名 | **相关仓库已核实**。简介仅给论文与通用上游；[supermimic_oli](https://github.com/liuskywalkerjskd/supermimic_oli) 已有完整 Oli／G1 训练实现，但不把它断言为该视频专用源码。 |
| 2026-10-24 04:04:48 | 小红书 · [Code for go2-supermimic](https://www.xiaohongshu.com/explore/6adbbde00000000032016d45) | Go2 四足平地／障碍／复杂地形追逐与闪避 | **训练已核实**。正文直达 [go2-supermimic](https://github.com/Zhengtianjin/go2-supermimic)，已收录主表。 |
| 2026-10-24 10:07:12 | 小红书 · [supermimic跨本体尝试](https://www.xiaohongshu.com/explore/6adc12d0000000002d006924) | Booster T1 29DoF 跨本体；LAFAN walk 重定向，作者称约 3000 轮不足 10 min，基于 `supermimic_vibe` 粗糙改造 | **任务展示**。正文只指通用上游，公开评论未给 T1 专用仓库；训练时长为作者自报。 |
| 2026-10-24 13:00:18 | 小红书 · [MorphMimic：一世界🌏，一模型🤖](https://www.xiaohongshu.com/explore/6adc3b62000000001901ec00) | G1／X2 Ultra／T2 共享形态条件化 WM／策略，支持五点稀疏跟踪 | **训练已核实**。正文给出 [MorphMimic 主页](https://lzyang2000.github.io/morphmimic/)，对应 [morphmimic](https://github.com/lzyang2000/morphmimic) 已收录主表。 |
| 2026-10-24 16:21:40 | Bilibili · [36 分钟速通高难度动作](https://www.bilibili.com/video/BV1XaHP6pEMW/) | BONES-SEED 高难动作、LAFAN1、AMASS／MotionDecode 泛化与 single-clip adaptation；包含多项训练改动 | **训练已核实**。简介直达 [Shimingyi/allmimic](https://github.com/Shimingyi/allmimic)，已收录主表；作者所述速度与成功率属于自报结果，未作独立复跑。 |
| 2026-10-24 16:25:30 | 小红书 · [SuperMimic复现36分钟速通高难动作](https://www.xiaohongshu.com/explore/6adc6b7a0000000013033800) | 高难动作与泛化评测，强调可行性过滤和 held-out 划分 | **训练已核实**。正文直达 [allmimic](https://github.com/Shimingyi/allmimic)，已收录主表。 |
| 2026-10-24 16:37:21 | 小红书 · [supermimic高动态parkour](https://www.xiaohongshu.com/explore/6adc6e410000000033019df5) | G1 高动态跑酷、130 cm 上箱；评论称使用 PHP 开源 motion、纯 mimic，障碍物位置／朝向输入 WM，未输入感知 | **任务展示**。简介与公开评论未给改造仓库。 |
| 2026-10-24 21:22:32 | 小红书 · [supermimic喂点php数据，高难度时会有失败](https://www.xiaohongshu.com/explore/6adcb1180000000024034dfe) | PHP 数据上的高难动作实验，展示失败情形 | **任务展示**。简介与公开评论未给仓库或主页，评论中视觉问题未获作者确认。 |
| 2026-10-24 22:00:33 | 小红书 · [supermimic上做smp](https://www.xiaohongshu.com/explore/6adcba01000000002c01ba21) | SMP 方向改造展示；原内容未展开 SMP 含义，不作额外推断 | **任务展示**。无公开评论，简介未给仓库或主页。 |

## 检索与访问记录

- **Bilibili**：利用登录态网页检索 `SuperMimic`，并补充检查相关推荐中的 `superminic` 拼写变体；本轮新增 E1、RGMT 对比、RGMT 组合探索与灵龙 2.0 条目。公开抓取接口返回 412 时使用已登录页面读取，不绕过反爬。
- **小红书**：已利用用户登录态检索，批量提取公开笔记正文与时间，并逐条打开重点笔记核查可访问评论。本轮新增 **15 条**，其中 M5 从作者评论获得仓库直链；HOI、跑酷、SMP、滑板等未发现专用公开训练仓库的仍保留“任务展示”。文档只保存不含访问令牌的规范笔记链接。
- 简介和评论中的仓库、主页只是候选线索；只有完成训练链路静态核查后才标“训练已核实”。登录失效或评论不可访问时记录限制并留待下轮，不绕过访问控制。

## 后续增量规则

1. 检查新内容的简介及公开可访问评论中的 homepage、GitHub 和分支链接，同时覆盖 HOI、地形、跑酷、移动操作、各种 humanoid task，以及四足等其他机器人。
2. 在内置浏览器登录态可用时，使用页面状态／DOM 提取与逐页评论核查；保存不含访问令牌的规范链接。登录失效则记录并下轮重试。
3. 新内容按上述时间线追加；旧内容只有获得新证据时才修订状态，并保留原始发布时间。
4. 对候选仓库显式枚举分支，检查 `supermimic` 等非默认分支中的 README、训练入口和学习代码，避免只搜仓库主页面。
5. 只有训练链路通过静态核查的仓库才进入主 README；社区演示可以继续留在这里，但必须保留“任务展示”状态。
