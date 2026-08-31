---
title: C题相关文献检索
stage: 文献检索与文件核验
status: 14-full-text-ready-2-missing
updated: 2026-08-13
tags:
  - 数学建模
  - 策联杯
  - 足球世界杯
  - 文献检索
---

# C题相关文献检索

题面：[[联赛题目/题目/2026年度“策联杯”数学建模精英联赛-C题.md]]  
问题拆解：[[联赛题目/C题/问题分析/C题总体与逐问分析.md]]

> [!info] 阶段边界
> 本文执行 `/math-model-solver` 的阶段1.5a：先保留8篇核心精读文献，再应后续需求扩展8篇专题文献，共16篇。这里只记录论文、论文实际采用的方法及其与赛题的客观对应关系，**不判断哪一种模型最适合C题**。模型取舍需在论文下载并精读后进入阶段2。

> [!warning] 2026-08-13精读前文件核验
> 16篇计划文献中，当前只有14篇不同论文完成Markdown转换。原 `08-Drayer-2012.md` 实际内容为#12 Van Bulck et al. (2020) 的RobinX论文，已按真实内容改名并修复图片引用；真正缺少的是#8 Drayer et al. (2012) 与#10 Schreyer et al. (2017)。已完成的精读结果见[[联赛题目/C题/问题分析/文献结果报告.md]]。

## 1. 检索策略

检索时间：2026-08-13。共执行5轮网络检索，达到skill规定上限后停止。

| 轮次 | 核心检索式 | 目的 | 主要信源 | 结果概况 |
|---:|---|---|---|---|
| 1 | `football television audience prediction`；`sports tournament scheduling venue time slot fairness travel`；`football qualification Poisson Monte Carlo`；`dynamic resource allocation sport ticket pricing` | 四问宽检索 | 出版商网页、期刊页面 | 找到收视需求、赛程、模拟、票价四类文献 |
| 2 | `football television audience demand uncertainty star quality` | 精确锁定Q1需求变量 | Elsevier、Taylor & Francis、SAGE | 得到世界杯/联赛电视需求实证论文 |
| 3 | `sports scheduling review`；`FIFA World Cup travel venue assignment optimization` | 锁定Q2赛程与现实对标 | EJOR、COR、Springer | 得到综述及世界杯48队赛程研究 |
| 4 | `Dixon Coles football scores`；`collusion risk World Cup Monte Carlo` | 锁定Q3进球与激励风险 | Wiley、EJOR、Journal of Sports Analytics | 得到泊松比分与末轮竞争性研究 |
| 5 | `dynamic ticket pricing sport demand elasticity`；`event security resource allocation` | 补充Q3动态票价/资源 | SAGE、AAAI、Springer | 得到体育动态票价与公共事件安保配置论文 |

### 核心关键词

**中文**：足球转播观看人数预测；赛事收视需求；体育赛程场馆时段优化；世界杯旅行负担；足球晋级概率泊松模拟；末轮默契风险；体育动态票价。

**英文**：football television audience demand；sports tournament venue time-slot assignment；FIFA World Cup travel scheduling；Poisson football tournament simulation；collusion risk tournament；dynamic ticket pricing sport。

## 2. 核心论文清单（8篇）

| # | 论文 | 作者/年份 | 期刊/级别 | 论文采用的方法 | 与C题的客观关联 |
|---:|---|---|---|---|---|
| 1 | *Uncertainty of Outcome or Star Quality? Television Audience Demand for English Premier League Football* | Buraimo & Simmons, 2015 | *International Journal of the Economics of Business*，同行评审期刊 | 使用8个赛季英超电视观看数据，实证比较赛前结果不确定性、明星/球队质量与电视受众 | 对应Q1的球队实力、球星、比赛悬念和转播观看人数关系；论文发现明星/人才质量比结果不确定性更稳定，属于待精读的实证证据 |
| 2 | *Uncertainty of Outcome, Team Quality or Star Players? What Drives TV Audience Demand for UEFA Champions League Football?* | Wills, Tacon & Addesa, 2022（在线2020） | *European Sport Management Quarterly*，主流体育管理期刊 | 分析2013/14—2018/19欧冠在6国的逐场电视观看数据，比较结果不确定性、球队质量和明星球员 | 与Q1的跨市场电视需求、比赛阶段、球队质量、球星特征高度对应 |
| 3 | *Scheduling in Sports: An Annotated Bibliography* | Kendall, Knust, Ribeiro & Urrutia, 2010 | *Computers & Operations Research*，运筹优化权威期刊综述 | 系统整理体育赛程中的物流、公平、时段、转播、场馆和裁判分配等问题及算法 | 覆盖Q2的赛程调度、硬软约束、旅行、公平、转播价值，也是Q4评价指标的领域背景 |
| 4 | *Sport Scheduling to Minimize Travels at the FIFA World Cup 2026* | Gutierrez, Cardoso & Validi, 2026 | *Optimization Letters*，同行评审优化期刊，开放获取 | 建立混合整数规划，将48队世界杯小组赛比赛分配至场馆/日期，在赛程结构和场馆工作量约束下最小化旅行 | 与本题同为48队世界杯小组赛；直接涉及场馆分配、旅行距离、时区跨越及与实际赛程对比，客观对应Q2/Q4 |
| 5 | *Modelling Association Football Scores and Inefficiencies in the Football Betting Market* | Dixon & Coles, 1997 | *Journal of the Royal Statistical Society: Series C (Applied Statistics)*，统计学经典期刊 | 动态球队表现下的泊松回归比分模型，并对低比分相关结构作处理 | 题面已引用该文；对应Q3从期望进球生成第三轮比分的概率基础 |
| 6 | *Fixing Match-Fixing: Optimal Schedules to Promote Competitiveness* | Chater, Arrondel, Gayant & Laslier, 2021/2022 | *European Journal of Operational Research*，运筹学权威期刊 | 建立比赛竞争性分类，结合比赛结果预测、Monte Carlo模拟和赛程安排，评价无激励与默契机会 | 与Q3的无激励风险、默契风险、末轮竞争性和模拟晋级条件直接相关 |
| 7 | *Risk of Collusion: Will Groups of 3 Ruin the FIFA World Cup?* | Guyon, 2020 | *Journal of Sports Analytics*，体育分析期刊 | 计算世界杯小组末轮出现双方共同获益赛果的概率，并分析赛程顺序与竞技平衡对风险的影响 | 对应Q3的条件晋级概率和默契风险定义；赛制为三队组，与本题四队组不同，差异需在精读阶段审查 |
| 8 | *Dynamic Ticket Pricing in Sport: An Agenda for Research and Practice* | Drayer, Shapiro & Lee, 2012 | *Sport Marketing Quarterly*，体育营销同行评审期刊 | 从收益管理视角讨论按需求变化调整体育票价的机制、实践条件和公平性问题 | 对应Q3的票价弹性、需求反馈和动态票价决策，并为局限性与观众公平讨论提供背景 |

## 3. 扩展论文清单（8篇）

> [!note] 扩展原则
> 8篇核心文献用于先建立每问的基本证据链；以下8篇用于补齐“现场—电视需求差异、统一赛程数据结构、旅行公平、四队组默契风险、晋级激励与足球动态票价”等更窄的专题。两表合计16篇，不再把补充文献只列标题而不给下载口径。

| # | 论文 | 作者/年份 | 期刊/级别 | 论文采用的方法 | 与C题的客观关联 |
|---:|---|---|---|---|---|
| 9 | *A Tale of Two Audiences: Spectators, Television Viewers and Outcome Uncertainty in Spanish Football* | Buraimo & Simmons, 2009 | *Journal of Economics and Business*，同行评审期刊 | 分别建立现场上座与电视观看需求方程，比较比赛结果不确定性对两类受众的作用 | 补充Q1/Q3的现场需求与转播需求差异，避免把两类观众视作同一需求机制 |
| 10 | *Game Outcome Uncertainty and the Demand for International Football Games: Evidence From the German TV Market* | Schreyer, Schmidt & Torgler, 2017 | *Journal of Media Economics*，同行评审期刊 | 利用德国电视市场国际足球比赛样本，实证分析赛前胜负不确定性与电视需求 | 补充Q1的国家队比赛、国际赛事和电视市场证据，可与联赛/欧冠样本交叉比较 |
| 11 | *Tournament Design: A Review from an Operational Research Perspective* | Devriesere, Csató & Goossens, 2025 | *European Journal of Operational Research*，运筹学权威期刊综述 | 从运筹学视角综述赛制设计中的效率、公平、吸引力、抽签、赛程和排名问题 | 为Q2目标与约束分类、Q4多维评价提供较新的综述性证据 |
| 12 | *RobinX: A Three-Field Classification and Unified Data Format for Round-Robin Sports Timetabling* | Van Bulck, Goossens, Schönberger & Guajardo, 2020 | *European Journal of Operational Research*，运筹学权威期刊 | 提出循环赛赛程问题的三字段分类体系与统一数据格式，并整理常见约束 | 对应Q2的循环赛约束编码、实例表示和可复现性，可用于核对硬约束/软约束是否漏项 |
| 13 | *How to Schedule the Volleyball Nations League* | Lambers, Rothuizen & Spieksma, 2023 | *Journal of Sports Analytics*，开放获取期刊 | 用整数规划和分解式安排国家与比赛周/场馆，重点控制总旅行并改善队伍间旅行公平 | 补充Q2的跨地旅行与公平权衡，并可支撑Q4旅行负担和资源公平解释；项目制与足球小组赛差异需说明 |
| 14 | *Quantifying Incentive (In)compatibility: A Case Study from Sports* | Csató, 2022 | *European Journal of Operational Research*，运筹学权威期刊 | 构造激励相容性度量，并以体育资格赛/排名规则为案例量化不当激励 | 对应Q3的无激励与策略性行为风险，也为Q4评价赛制规则影响提供理论背景 |
| 15 | *On Head-to-Head Results as Tie-Breaker and Consequent Opportunities for Collusion* | Csató, 2025 | *IMA Journal of Management Mathematics*，管理数学期刊 | 对四队单循环赛中由相互战绩破同分引发的合谋机会作数学刻画，并以2024欧洲杯开展模拟 | 与本题“四队组、每队三场、末轮默契风险”结构接近；但本题采用净胜球优先，需把差异作为边界条件 |
| 16 | *A Dynamic Ticket Pricing Approach for Soccer Games* | Şahin & Erol, 2017 | *Axioms*，开放获取同行评审期刊 | 建立足球比赛动态票价框架，根据销售期、需求和剩余容量更新票价并进行数值分析 | 直接补充Q3中票价调整、需求弹性、容量上限和票务收入之间的定量关系 |

## 4. 分问覆盖情况

| 分问 | 核心论文 | 当前覆盖内容 | 仍需精读核验的条件 |
|---|---|---|---|
| Q1 收视预测 | #1、#2、#9、#10 | 球队质量、明星、悬念、赛事/市场差异，以及现场与电视两类受众 | 变量定义、数据分布、估计方法能否迁移到题给模拟数据 |
| Q2 赛程优化 | #3、#4、#11、#12、#13 | 场馆/时段安排、约束分类、旅行、公平、转播和硬约束 | 本题特殊目标权重、60小时、安保/并发容量与文献约束差异 |
| Q3 动态优化 | #5、#6、#7、#8、#14、#15、#16 | 泊松比分、联合模拟、激励/默契风险、四队组风险与动态票价 | 最佳第三名的跨组耦合、题给风险公式、每日耦合资源和票价保底约束 |
| Q4 现实评价 | #3、#4、#11、#13、#14、#15 | 真实赛程对标、旅行及时区、公平、激励相容及现实未公开约束 | 赛事规模标准化和模拟商业/风险字段的可比代理 |

## 5. 关键检索发现（非模型推荐）

1. **电视受众文献结论并不一致**：西班牙、英超、欧冠和国家队样本对“悬念是否提高收视”的结论不同，而球队质量、明星和市场规模经常被识别为重要变量。因此Q1需要把这些因素分别构造并用题给数据验证，不能把“悬念必然提高收视”作为预设事实。
2. **赛程研究普遍把旅行、公平、场馆/时段可用性和转播要求共同视为硬软约束体系**；世界杯2026已有与48队、跨时区、场馆工作量直接相似的MIP研究。
3. **足球锦标赛模拟通常从比赛级进球概率出发，再通过Monte Carlo传播至排名和晋级事件**；这与Q3给定的20,000次联合模拟结构一致。
4. **末轮无激励与默契风险已有独立运筹研究**，但文献中的赛制和风险定义不完全等同于题面，必须按题面公式实现后再用文献解释。
5. **动态票价研究强调需求预测、价格弹性、收入与观众公平之间的关系**，可支撑Q3对价格—上座保底约束的讨论。

## 6. DOI与免费下载链接

> [!success] 合法开放路径
> 已逐篇复查出版社开放页、作者机构仓储和预印本。以下优先给出无需绕过付费墙的直接PDF；“作者公开版本”通常是接受稿，正文内容可用于精读和引用，但排版可能不同于出版社版本。

|   # | DOI                             | 免费全文/PDF                                                                                                                                                                                                                                                                              | 版本与备用入口                                                                                                                                                           |
| --: | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|   1 | `10.1080/13571516.2015.1010282` | [利物浦大学机构仓储PDF](https://livrepository.liverpool.ac.uk/3000079/1/Buraimo%20and%20Simmons%20%282015%29%20Outcome%20Uncertainty%20or%20Star%20Quality.pdf)                                                                                                                                | 作者公开版本；[仓储记录页](https://livrepository.liverpool.ac.uk/3000079/)                                                                                                    |
|   2 | `10.1080/16184742.2020.1836010` | [Leeds Beckett机构仓储PDF](https://eprints.leedsbeckett.ac.uk/id/eprint/7225/1/UncertaintyOfOutcomeTeamQualityOrStarPlayersWhatDrivesTVAudienceDemandForUEFAChampionsLeagueFootballAM-ADDESA.pdf)                                                                                         | 接受稿；[Birkbeck机构仓储镜像PDF](https://eprints.bbk.ac.uk/id/eprint/41024/1/Wills%20et%20al.%20-%20Pre-publication%20version.pdf)                                         |
|   3 | `10.1016/j.cor.2009.05.013`     | [作者公开PDF（Graham Kendall）](https://www.graham-kendall.com/papers/kkru2010.pdf)                                                                                                                                                                                                         | [UFF作者/机构镜像PDF](https://www2.ic.uff.br/~celso/artigos/Scheduling%20in%20sports%20C%26OR.pdf)                                                                      |
|   4 | `10.1007/s11590-026-02320-x`    | [Springer开放全文](https://link.springer.com/article/10.1007/s11590-026-02320-x)                                                                                                                                                                                                          | 出版社明确标注Open Access，页面提供Download PDF；[公开代码与结果](https://github.com/hamidrezavalidi/FIFA_World_Cup_2026)                                                             |
|   5 | `10.1111/1467-9876.00065`       | [公开PDF镜像（GitHub raw）](https://raw.githubusercontent.com/eddwebster/football_analytics/master/research/papers/%5B1997%5D%20Modelling%20Association%20Football%20Scores%20and%20Inefficiencies%20in%20the%20Football%20Betting%20Market%20by%20Mark%20Dixon%20and%20Stuart%20Coles.pdf) | 非出版社镜像；正式元数据以[Wiley DOI页](https://doi.org/10.1111/1467-9876.00065)为准                                                                                              |
|   6 | `10.1016/j.ejor.2021.02.006`    | [arXiv预印本PDF](https://arxiv.org/pdf/1810.09782)                                                                                                                                                                                                                                       | 免费预印本；[arXiv摘要页](https://arxiv.org/abs/1810.09782)，引用期刊版时仍使用DOI                                                                                                   |
|   7 | `10.3233/JSA-200414`            | [IOS Press/SAGE开放PDF](https://journals.sagepub.com/doi/pdf/10.3233/JSA-200414)                                                                                                                                                                                                       | 出版社标记Open Access；若直链触发403，可从[DOAJ记录页](https://doaj.org/article/4e18d1afb2e041a1bce3a0a609f33aa8)进入，或用[SSRN作者稿页面](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3190779) |
|   8 | `10.1177/106169341202100307`    | [ODU机构仓储记录页](https://digitalcommons.odu.edu/hms_fac_pubs/17/)                                                                                                                                                                                                                  | 页面内点击Download获取作者公开全文；[ODU PDF直链](https://digitalcommons.odu.edu/cgi/viewcontent.cgi?article=1032&context=hms_fac_pubs)备用，站点可能要求先打开记录页 |

### 扩展文献（#9—#16）

|   # | DOI                              | 免费全文/PDF                                                                                                 | 版本与备用入口                                                                                            |
| --: | -------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
|   9 | `10.1016/j.jeconbus.2008.10.002` | [Lancaster大学机构仓储PDF](https://eprints.lancs.ac.uk/id/eprint/45040/1/10.pdf)                               | 作者接受稿；[仓储记录页](https://eprints.lancs.ac.uk/id/eprint/45040/)                                        |
|  10 | `10.1080/08997764.2017.1281818`  | [Taylor & Francis开放全文页](https://doi.org/10.1080/08997764.2017.1281818)                                   | 出版元数据显示为CC BY开放文章；若当前网络触发出版商反爬/地区限制，从学校图书馆入口打开同一DOI，或向作者索取合法副本                                     |
|  11 | `10.1016/j.ejor.2024.10.044`     | [Corvinus大学机构仓储PDF](https://unipub.lib.uni-corvinus.hu/11153/1/1-s2.0-S0377221724008476-main.pdf)        | 公开作者稿；[arXiv预印本PDF](https://arxiv.org/pdf/2404.05034)备用                                            |
|  12 | `10.1016/j.ejor.2019.07.023`     | [Ghent大学机构仓储PDF](https://biblio.ugent.be/publication/8623970/file/8624025.pdf)                           | 公开作者稿；[仓储记录页](https://biblio.ugent.be/publication/8623970)                                         |
|  13 | `10.3233/JSA-220626`             | [TU/e机构仓储PDF](https://pure.tue.nl/ws/files/305689391/jsa_2023_9-2_jsa-9-2-jsa220626_jsa-9-jsa220626.pdf) | 公开全文；[出版社DOI页](https://doi.org/10.3233/JSA-220626)备用                                               |
|  14 | `10.1016/j.ejor.2022.01.042`     | [arXiv预印本PDF](https://arxiv.org/pdf/2104.03067)                                                          | [Corvinus大学机构仓储PDF](https://unipub.lib.uni-corvinus.hu/7307/1/1-s2.0-S0377221722000807-main.pdf)备用 |
|  15 | `10.1093/imaman/dpae016`         | [Corvinus大学机构仓储PDF](https://unipub.lib.uni-corvinus.hu/10201/1/dpae016.pdf)                              | 公开作者稿；[OUP DOI页](https://doi.org/10.1093/imaman/dpae016)备用                                         |
|  16 | `10.3390/axioms6040031`          | [MDPI直链PDF](https://mdpi-res.com/d_attachment/axioms/axioms-06-00031/article_deploy/axioms-06-00031.pdf) | CC BY出版社全文；[DOI页](https://doi.org/10.3390/axioms6040031)备用                                         |

### 下载注意

- 优先顺序：出版社开放PDF → 大学机构仓储 → arXiv/SSRN作者稿 → 作者公开镜像；
- 若点击PDF后浏览器只预览，可使用浏览器“另存为”，文件名建议采用“序号-第一作者-年份-短标题.pdf”；
- 第5篇当前找到的是公开GitHub镜像，并非出版社OA；若希望只使用权属最清晰的版本，可通过学校图书馆、馆际互借或联系作者获取；
- 第10篇有开放许可记录，但Taylor & Francis可能对自动访问或部分地区返回403；这属于访问层问题，不应改用绕过付费墙的站点；
- 第7、8篇的站点也可能拦截PDF直链；先打开同一行的记录页再点击下载，通常比直接粘贴PDF地址稳定；
- ResearchGate可能要求免费登录，不等于出版社开放获取；
- 不使用或提供绕过付费墙的下载站。

## 7. 下载与精读准备

请将上述论文PDF放入：

`联赛题目/C题/参考文献/`

转换后的Markdown放入：

`联赛题目/C题/参考文献/MD/`

精读阶段将逐篇提取：研究背景、核心模型、关键算法、参数与适用条件、主要结论、与C题的可复用部分和局限性；完成前不进入模型推荐。
