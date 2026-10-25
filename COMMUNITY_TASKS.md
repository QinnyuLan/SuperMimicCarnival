# SuperMimic 社区新任务时间线

汇总 **2026-10-20** 以来 Bilibili、小红书上与 SuperMimic 有关的新任务、新本体和训练方式改造，按内容公开发布时间升序排列。时间为 **UTC+8**；最近核查：**2026-10-25**。

## 状态口径

- **训练已核实**：内容简介直接给出仓库或分支，并已静态核查到训练入口、世界模型／策略／价值网络学习代码及配置或数据流程。
- **相关仓库已核实**：存在主题相关的公开训练仓库，但简介没有明确证明它就是该内容的专用源码。
- **任务展示**：看到了任务或效果，但尚未核实对应改造已公开完整训练实现；不等于该项目没有训练，也不把演示效果当作开源证据。

## 时间线

| 发布时间 | 平台／内容 | 新任务或改造 | 代码状态与证据 |
|---|---|---|---|
| 2026-10-23 10:59:44 | Bilibili · [Supermimic深度图20cm地形codex版本](https://www.bilibili.com/video/BV1n3nt6wEKn/) | 深度图输入、20 cm 地形；发布者称使用 Codex 复现 | **任务展示**。简介未给仓库或主页，未核实该版本的公开训练代码。 |
| 2026-10-23 11:59:22 | Bilibili · [superinstinct mimic深度图版本](https://www.bilibili.com/video/BV1Tdn46GEzH/) | G1 深度视觉地形跑酷；视频对应旧版在 RTX 3090 上训练 5.7 h | **训练已核实**。简介直达 [InstinctMJ 的 supermimic 分支](https://github.com/project-instinct/InstinctMJ/tree/supermimic)，已收录主表；分支包含完整 WM、策略、critic、配置、训练与评测链路。 |
| 2026-10-23 12:00:45 | Bilibili · [SuperMimic HOI 之搬搬箱](https://www.bilibili.com/video/BV1Tdn46GEaj/) | **HOI／手物交互：搬箱**；作者称训练 5 h 收敛，并指出 scale-up 与碰撞建模仍需验证 | **任务展示**。简介未给该 HOI 改造的仓库或主页，不能据此标记为已开源复现。 |
| 2026-10-23 12:40:24 | Bilibili · [USTC旧版一代人形机器人+supermimic](https://www.bilibili.com/video/BV1bun46CEPW/) | USTC 旧版一代人形机器人本体适配 | **任务展示**。简介为空，未核实该本体改造的公开训练代码。 |
| 2026-10-23 21:35:36 | Bilibili · [Mac Studio 上训练 SuperMimic](https://www.bilibili.com/video/BV1uin86XEDR/) | Apple M5 Ultra 训练；作者称单台训练 5 h | **任务展示**。简介未给仓库；主表虽另有 M5 训练仓库，但没有证据把该视频与其直接绑定。 |
| 2026-10-23 22:27:10 | Bilibili · [宇树机器人闪身步](https://www.bilibili.com/video/BV14kn86UEVU/) | 宇树人形机器人仿真闪身步 | **任务展示**。简介给出论文主页和通用上游 `zita-ch/supermimic_vibed`，未给闪身步专项改造仓库。 |
| 2026-10-24 02:13:09 | Bilibili · [冰冷的 token 化作了温暖的 SuperMimic](https://www.bilibili.com/video/BV1cVna6jEFA/) | 人形全身动作跟踪；发布者与 Oli 适配仓库所有者同名 | **相关仓库已核实**。简介仅给论文与通用上游；[supermimic_oli](https://github.com/liuskywalkerjskd/supermimic_oli) 已有完整 Oli／G1 训练实现，但不把它断言为该视频专用源码。 |
| 2026-10-24 16:21:40 | Bilibili · [36 分钟速通高难度动作](https://www.bilibili.com/video/BV1XaHP6pEMW/) | BONES-SEED 高难动作、LAFAN1、AMASS／MotionDecode 泛化与 single-clip adaptation；包含多项训练改动 | **训练已核实**。简介直达 [Shimingyi/allmimic](https://github.com/Shimingyi/allmimic)，已收录主表；作者所述速度与成功率属于自报结果，未作独立复跑。 |

## 小红书

2026-10-20、2026-10-25 06:50 与 2026-10-25 08:40 三轮公开网页搜索均未返回可核验的新任务条目，内置搜索页持续显示“登录后查看搜索结果”。因此目前没有可靠列入时间线的小红书条目；后续增量任务会继续重试公开可访问的简介和评论，并记录访问限制，不绕过登录或反爬。

## 后续增量规则

1. 检查新内容的简介及公开可访问评论中的 homepage、GitHub 和分支链接，同时覆盖 HOI、地形、跑酷、移动操作、各种 humanoid task，以及四足等其他机器人。
2. 新内容按上述时间线追加；旧内容只有获得新证据时才修订状态，并保留原始发布时间。
3. 对候选仓库显式枚举分支，检查 `supermimic` 等非默认分支中的 README、训练入口和学习代码，避免只搜仓库主页面。
4. 只有训练链路通过静态核查的仓库才进入主 README；社区演示可以继续留在这里，但必须保留“任务展示”状态。
