<table border="1" ><tr>
<td></td>
<td></td>
<td>辅助变量，不进入基准评分公式</td>
</tr></table>

10.basepredictions

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchid</td>
<td>比赛编号</td>
<td>小组赛编号。</td>
</tr><tr>
<td>groupid</td>
<td>小组编号</td>
<td>比赛所属小组。</td>
</tr><tr>
<td>roundingroup</td>
<td>小组赛轮次</td>
<td>比赛所属轮次。</td>
</tr><tr>
<td>teama</td>
<td>A 队名称</td>
<td>比赛A 队。</td>
</tr><tr>
<td>teamb</td>
<td>B 队名称</td>
<td>比赛B 队。</td>
</tr><tr>
<td>expectedgoalsa</td>
<td>A 队基准期望进球</td>
<td>附件提供的基准模型预测值。</td>
</tr><tr>
<td>expectedgoalsb</td>
<td>B 队基准期望进球</td>
<td>附件提供的B 队基准期望进球。</td>
</tr><tr>
<td>pawin</td>
<td>A 队获胜概率</td>
<td>基准预测中A 队获胜概<br>率。</td>
</tr><tr>
<td>pdraw</td>
<td>平局概率</td>
<td>基准预测中平局概率。</td>
</tr><tr>
<td>pbwin</td>
<td>B 队获胜概率</td>
<td>基准预测中B 队获胜概<br>率；三项概率之和应为<br>1。</td>
</tr><tr>
<td>uncertaintyindex</td>
<td>竞技悬念指数</td>
<td>用于衡量比赛结果的不确定程度，定义为1 减去三种结果概率中的最大值；<br>越大表示结果越不确定。</td>
</tr><tr>
<td>attractivenessindex</td>
<td>比赛吸引力指数</td>
<td>综合球队实力、球迷基础和悬念等因素生成的模拟热度分。</td>
</tr><tr>
<td>expectedattendancebase</td>
<td>基准预计现场观众</td>
<td>不绑定具体场馆和动态票价的基准现场需求预测。</td>
</tr><tr>
<td>commercialvalueindex</td>
<td>基准商业价值指数</td>
<td>综合票务、转播、赞助和关注度的模拟商业价值<br>分。</td>
</tr></table>

11.securityrequirements

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchid</td>
<td>比赛编号</td>
<td>72 场小组赛的唯一编号。</td>
</tr><tr>
<td>groupid</td>
<td>小组编号</td>
<td>比赛所属小组。</td>
</tr><tr>
<td>teama</td>
<td>A 队名称</td>
<td>比赛记录中的第一支球队，A /B 不代表主客场。</td>
</tr><tr>
<td>teamb</td>
<td>B 队名称</td>
<td>比赛记录中的第二支球队。</td>
</tr><tr>
<td>crowdrisk</td>
<td>观众规模风险</td>
<td>由基准预计现场观众人数在72 场比赛中进行min -max 标准化得到。</td>
</tr><tr>
<td>attentionrisk</td>
<td>关注度风险</td>
<td>由比赛吸引力和双方球迷基础合成的关注度压力。</td>
</tr><tr>
<td>securitydemandscore</td>
<td>安保需求得分</td>
<td>0.55xcrowdrisk+0.45xattentionrisk。</td>
</tr><tr>
<td>requiredsecuritylevel</td>
<td>最低安保需求等级</td>
<td>根据 securitydemandscore 阈值生成；数值越大需求越高。</td>
</tr><tr>
<td>securityreason</td>
<td>安保需求说明</td>
<td>说明该比赛安保需求主要来自观众规模、关注度或二者共同作用。</td>
</tr></table>

12.livegroupresults

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchid</td>
<td>已结束比赛编号</td>
<td>已完成小组赛的唯一编<br>号。</td>
</tr><tr>
<td>groupid</td>
<td>小组编号</td>
<td>比赛所属小组。</td>
</tr><tr>
<td>roundingroup</td>
<td>已结束轮次</td>
<td>该动态数据仅包含前两轮已完成比赛。</td>
</tr><tr>
<td>teama</td>
<td>A 队名称</td>
<td>比赛A 队。</td>
</tr><tr>
<td>teamb</td>
<td>B 队名称</td>
<td>比赛B 队。</td>
</tr><tr>
<td>goalsa</td>
<td>A 队实际进球</td>
<td>已结束比赛中A 队进球数。</td>
</tr><tr>
<td>goalsb</td>
<td>B 队实际进球</td>
<td>已结束比赛中B 队进球<br>数。</td>
</tr><tr>
<td>xga</td>
<td>A 队实际xG</td>
<td>比赛中A 队创造机会质量对应的期望进球。</td>
</tr><tr>
<td>$xg_b$</td>
<td>B 队实际xG</td>
<td>比赛中B 队创造机会质量对应的期望进球。</td>
</tr><tr>
<td>redcardsa</td>
<td>A 队红牌数</td>
<td>A 队被罚出场的球员数<br>量；红牌会显著影响当场表现，也可作为后续状态和风险的更新信息。</td>
</tr><tr>
<td>redcardsb</td>
<td>B 队红牌数</td>
<td>B 队红牌数。</td>
</tr><tr>
<td>injuryupdate</td>
<td>伤病状态代码</td>
<td>对影响下一轮阵容的主要伤病或体能情况进行标准化编码，不要求参赛者识别具体球员姓名。</td>
</tr><tr>
<td>injuryupdatedescription</td>
<td>伤病状态说明</td>
<td>用通俗语言说明受影响的球员角色及状态，例如<br>“关键前锋出场存疑”。</td>
</tr><tr>
<td>injuryimpactlevel</td>
<td>伤病影响等级</td>
<td>0 无明显影响，1 低，2<br>中，3 高。表示对下一轮球队整体实力的建议影响程度。</td>
</tr><tr>
<td>attendance</td>
<td>实际现场观众人数</td>
<td>已结束比赛的实际模拟现场观众人数。</td>
</tr><tr>
<td>tvviewers</td>
<td>实际转播观看人数</td>
<td>已结束比赛的实际模拟转播观看人数。</td>
</tr></table>

13.dynamicresourcelimits

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>referencedate</td>
<td>资源配置日期</td>
<td>以统一参考时区表示的日期；与timeslots.date 对应。</td>
</tr><tr>
<td>highbroadcastcapacity</td>
<td>最高转播优先级容量</td>
<td>该参考日期最多可设置为3 级转播优先级的第三轮比赛数量。</td>
</tr><tr>
<td>highsecuritycapacity</td>
<td>高等级安保容量</td>
<td>该日最多可配置3 级及以上安保方案的比赛数量。</td>
</tr><tr>
<td>enhancedtransportcapacity</td>
<td>增强交通保障容量</td>
<td>该日最多可配置3 级交通保障的比赛数量。</td>
</tr><tr>
<td>dailyresourcebudgetindex</td>
<td>每日资源预算指数</td>
<td>用于限制广播、安保和交通等级组合的模拟总预算。</td>
</tr><tr>
<td>maxticketincreaserate</td>
<td>最大涨价比例</td>
<td>单场动态票价相对基础票价的最大上调比例。</td>
</tr><tr>
<td>maxticketdiscountrate</td>
<td>最大降价比例</td>
<td>单场动态票价相对基础票价的最大下调比例的绝对值。</td>
</tr></table>

14.dynamicresourcecosts

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>resourcetype</td>
<td>资源类型</td>
<td>需要动态配置的资源类别。</td>
</tr><tr>
<td>resourcelevel</td>
<td>资源等级</td>
<td>该类资源的配置等级。</td>
</tr><tr>
<td>unitcostindex</td>
<td>单位成本指数</td>
<td>选择该等级产生的相对资源成本。</td>
</tr><tr>
<td>demandmultiplier</td>
<td>需求修正系数</td>
<td>转播等级作用于转播需求，交通等级作用于现场需求；安保等级取<br>1。</td>
</tr><tr>
<td>riskmultiplier</td>
<td>剩余风险系数</td>
<td>安保等级越高，剩余运营风险系数越低；其他资源取1 。</td>
</tr><tr>
<td>description</td>
<td>等级说明</td>
<td>解释该资源等级的业务含义和容量限制。</td>
</tr></table>

15.objectiveweights

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>problemid</td>
<td>问题编号</td>
<td>权重适用的赛题问题。</td>
</tr><tr>
<td>indicatorname</td>
<td>指标名称</td>
<td>目标函数中的评价指标。</td>
</tr><tr>
<td>direction</td>
<td>优化方向</td>
<td>说明指标应最大化或最小化。</td>
</tr><tr>
<td>weight</td>
<td>基准权重</td>
<td>正式方案必须首先采用的固定权重。</td>
</tr><tr>
<td>normalizationmethod</td>
<td>标准化方法</td>
<td>将不同量纲指标转换到0 -1<br>的统一口径。</td>
</tr><tr>
<td>datasource</td>
<td>数据来源</td>
<td>说明指标由哪些字段或结果计算。</td>
</tr><tr>
<td>explanation</td>
<td>指标解释</td>
<td>说明该指标在综合目标中的业务含义。</td>
</tr></table>

# 输出数据附件

输出文件应保持模板中的字段名、字段顺序、单位和取值规范不变。

1.actualscheduletemplate

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchid</td>
<td>实际赛程比赛编号</td>
<td>从公开来源采集的比赛编号；若来源无统一编号，<br>可自行编码并保持唯一。</td>
</tr><tr>
<td>competition</td>
<td>赛事名称及届次</td>
<td>实际赛程所属赛事。</td>
</tr><tr>
<td>stage</td>
<td>比赛阶段</td>
<td>实际比赛阶段。</td>
</tr><tr>
<td>groupid</td>
<td>小组编号</td>
<td>小组赛填写组别：淘汰赛可留空。</td>
</tr><tr>
<td>roundingroup</td>
<td>小组赛轮次</td>
<td>仅小组赛填写第几轮；淘汰赛可留空。</td>
</tr><tr>
<td>teama</td>
<td>A 队名称</td>
<td>实际比赛第一支球队。</td>
</tr><tr>
<td>teamb</td>
<td>B 队名称</td>
<td>实际比赛第二支球队。</td>
</tr><tr>
<td>venue</td>
<td>场馆名称</td>
<td>实际比赛场馆。</td>
</tr><tr>
<td>city</td>
<td>承办城市</td>
<td>实际比赛所在城市。</td>
</tr><tr>
<td>country</td>
<td>承办国家</td>
<td>实际比赛所在国家。</td>
</tr><tr>
<td>date</td>
<td>当地比赛日期</td>
<td>按场馆当地时区记录的日期。</td>
</tr><tr>
<td>localkickofftime</td>
<td>当地开球时间</td>
<td>按场馆当地时区记录的开球时间。</td>
</tr><tr>
<td>utcdatetime</td>
<td>UTC 开球时刻</td>
<td>统一换算后的开球时刻，<br>可用于休息比较。</td>
</tr><tr>
<td>goalsa</td>
<td>A 队实际进球</td>
<td>已结束比赛填写；未来赛程可留空。</td>
</tr><tr>
<td>goalsb</td>
<td>B 队实际进球</td>
<td>已结束比赛填写；未来赛程可留空。</td>
</tr><tr>
<td>sourceurl</td>
<td>数据来源网址</td>
<td>能够验证该行赛程信息的公开来源。</td>
</tr><tr>
<td>retrievaldlate</td>
<td>数据获取日期</td>
<td>采集该条数据的日期。</td>
</tr></table>

2.result1testpredictiontemplate.cSV

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchidtest</td>
<td>测试集比赛编号</td>
<td>与historicalmatches 中保持一致</td>
</tr><tr>
<td>predictedtesttvviewers</td>
<td>测试集预测转播观看人数</td>
<td>问题1 模型对test 集比赛转播观看人数的最终预测值。（百万人）</td>
</tr></table>

3.result1matchpredictiontemplate.csv

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchid</td>
<td>比赛编号</td>
<td>每行对应一场小组赛。</td>
</tr><tr>
<td>teama</td>
<td>A 队名称</td>
<td>与groupsmatches 一致。</td>
</tr><tr>
<td>teamb</td>
<td>B 队名称</td>
<td>与groupsmatches 一致。</td>
</tr><tr>
<td>predictedtvviewers</td>
<td>预测转播观看人数</td>
<td>问题1 模型对该场小组赛转播观看人数的最终预测值。（人）</td>
</tr></table>

4.result2template.csv

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchid</td>
<td>比赛编号</td>
<td>被安排的比赛。</td>
</tr><tr>
<td>groupid</td>
<td>小组编号</td>
<td>比赛所属小组。</td>
</tr><tr>
<td>roundingroup</td>
<td>小组赛轮次</td>
<td>与groupsmatches 完全一致</td>
</tr><tr>
<td>teama</td>
<td>A 队名称</td>
<td>A 队名称。</td>
</tr><tr>
<td>teamb</td>
<td>B 队名称</td>
<td>B 队名称。</td>
</tr><tr>
<td>venueid</td>
<td>承办场馆编号</td>
<td>模型选择的场馆。</td>
</tr><tr>
<td>slotid</td>
<td>候选时段编号</td>
<td>模型选择的开球时段编号。</td>
</tr><tr>
<td>city</td>
<td>承办城市</td>
<td>与venueid 对应。</td>
</tr><tr>
<td>country</td>
<td>承办国家</td>
<td>与venueid 对应。</td>
</tr><tr>
<td>referencedate</td>
<td>参考日期</td>
<td>与所选slotid 对应的<br>timeslots.date。</td>
</tr><tr>
<td>referencekickofftime</td>
<td>参考开球时间</td>
<td>与所选时段对应的参考时区时间。</td>
</tr><tr>
<td>localdatetime</td>
<td>场馆当地开球时刻</td>
<td>将UTC 时刻按<br>venues.timezone 换算后的场馆当地时间。</td>
</tr><tr>
<td>utcdatetime</td>
<td>UTC 开球时刻</td>
<td>用于检查轮次顺序、60 小时休息。</td>
</tr><tr>
<td>requiredsecuritylevel</td>
<td>最低安保需求等级</td>
<td>来自 securityrequirements。</td>
</tr><tr>
<td>expectedattendance</td>
<td>场馆时段预计观众</td>
<td>min(expectedattendancebase, venue.capacity)</td>
</tr><tr>
<td>expectedtvviewers</td>
<td>场馆时段预计转播观众</td>
<td>问题一的输入</td>
</tr><tr>
<td>ticketrevenueusd</td>
<td>预计票务收入</td>
<td>由预计售票量与对应轮次的基础票价计算。</td>
</tr><tr>
<td>broadcastvalueusd</td>
<td>预计转播价值</td>
<td>建议由预计观看人数、单位观看价值和阶段权重计算。</td>
</tr><tr>
<td>travelcostindex</td>
<td>旅行负担指数</td>
<td>综合距离、旅行时间和时区差得到的标准化旅行成本。</td>
</tr><tr>
<td>fairnesspenalty</td>
<td>公平性惩罚</td>
<td>0 . 5x 黄金时段次数极差／3 ＋<br>0 . 5x 大容量场馆次数极差／3 。</td>
</tr><tr>
<td>riskindex</td>
<td>综合风险指数</td>
<td>综合气候、安保和执行风<br>险。</td>
</tr><tr>
<td>totalobjectivevalue</td>
<td>目标函数值</td>
<td>整套赛程方案的总目标函数值。仅在该列的第一条数据记录中填写，其余行留空。</td>
</tr></table>

5.result3template.csv

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchid</td>
<td>第三轮比赛编号</td>
<td>每行对应一场第三轮比赛。</td>
</tr><tr>
<td>groupid</td>
<td>小组编号</td>
<td>比赛所属小组。</td>
</tr><tr>
<td>teama</td>
<td>A 队名称</td>
<td>固定赛程中的A 队。</td>
</tr><tr>
<td>teamb</td>
<td>B 队名称</td>
<td>固定赛程中的B 队。</td>
</tr><tr>
<td>updatedpteamaa dvance</td>
<td>A 队更新后晋级概率</td>
<td>结合前两轮结果后进入32 强的总概率。</td>
</tr><tr>
<td>updatedpteamb<br>advance</td>
<td>B 队更新后晋级概率</td>
<td>结合前两轮结果后进入32 强的总概率。</td>
</tr><tr>
<td>updatedexpectedat tendance</td>
<td>更新后预计现场观众</td>
<td>结合前两轮表现、伤病和资源配置后的预计现场人数。</td>
</tr><tr>
<td>updatedexpectedtv viewers</td>
<td>更新后预计转播观众</td>
<td>结合前两轮信息和转播等级后的预计观看人数。</td>
</tr><tr>
<td>stakelessrisk</td>
<td>无激励风险</td>
<td>至少一方因晋级或淘汰形势基本确定而降低竞争动机的风险。</td>
</tr><tr>
<td>collusionrisk</td>
<td>默契风险</td>
<td>某些结果区间同时有利于双方、可能削弱主动争胜动力的风险。</td>
</tr><tr>
<td>updatedattractivene SS</td>
<td>更新后比赛吸引力</td>
<td>结合出线形势、近期表现和伤病信息更新的比赛热度。</td>
</tr><tr>
<td>recommendedbroad castpriority</td>
<td>建议转播优先级</td>
<td>1 低、2 中、3 高；3 级数量受每日容量限制。</td>
</tr><tr>
<td>recommendedsecur itylevel</td>
<td>建议安保等级</td>
<td>不得高于场馆<br>securitylevel，且不得低于合理需求。</td>
</tr><tr>
<td>recommendedtrans portlevel</td>
<td>建议交通保障等级</td>
<td>1 基础、2 增强、3 最<br>高；3 级受每日容量限制。</td>
</tr><tr>
<td>recommendedticket adjustment</td>
<td>建议票价调整比例</td>
<td>相对基础票价的调整比例，受每日上下限约束。</td>
</tr><tr>
<td>updatedticketreve nueusd</td>
<td>更新后票务收入</td>
<td>考虑动态价格和现场需求后的预计票务收入。</td>
</tr><tr>
<td>updatedbroadcastv alueusd</td>
<td>更新后转播价值</td>
<td>考虑更新观看人数和转播优先级后的预计转播价值。</td>
</tr><tr>
<td>resourcecostindex</td>
<td>资源成本指数</td>
<td>转播、安保和交通等级对应成本指数之和。</td>
</tr><tr>
<td>riskexposureindex</td>
<td>剩余风险暴露</td>
<td>在资源配置后仍保留的综合风险。</td>
</tr><tr>
<td>staticnetvalue</td>
<td>静态方案净效益</td>
<td>赛前按静态信息优化得到资源方案；前两轮结束后保持该资源决策不变，并在更新环境下重新计算的该场目标贡献。</td>
</tr><tr>
<td>dynamicnetvalue</td>
<td>动态方案净效益</td>
<td>按P3 基准目标函数得到的动态方案净效益。</td>
</tr><tr>
<td>improvementrate</td>
<td>动态改善率</td>
<td>(dynamicnetvalue<br>-staticnetvalue)<br>/|staticnetvalue|</td>
</tr></table>

6.result4template.csv

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>indicatorname</td>
<td>指标名称</td>
<td>如总旅行距离、平均休息时间、黄金时段覆盖率。</td>
</tr><tr>
<td>indicatorcategory</td>
<td>指标类别</td>
<td>指标所属评价维度。</td>
</tr><tr>
<td>actualschedulevalue</td>
<td>实际赛程值</td>
<td>实际公开赛程按统一定义计算得到的指标值。</td>
</tr><tr>
<td>optimizedschedulevalue</td>
<td>优化赛程值</td>
<td>本队优化方案的同口径指标值。</td>
</tr><tr>
<td>absolutedifference</td>
<td>绝对差值</td>
<td>统一定义为优化值减实际值。</td>
</tr><tr>
<td>relativeimprovement</td>
<td>相对改善率</td>
<td>必须结合<br>preferreddirection 定义；实际值为0 时应说明处理方法。</td>
</tr><tr>
<td>preferreddirection</td>
<td>偏好方向</td>
<td>higher 越大越好，lower越小越好，target 越接近目标值越好。</td>
</tr><tr>
<td>evaluationresult</td>
<td>评价结论</td>
<td>依据统一指标方向给出的比较结论。</td>
</tr></table>

### 提交文件

1．完整建模论文PDF

2.result1testprediction.csv,result1rmatchprediction.csv

3.result2groupschedule.csv

4.result3dynamicstrategy.csv

5．问题4使用的实际赛程数据、数据采集程序和运行说明及result4schedulecomparison.csv（可选）

6．全部可复现代码、软件环境、随机种子和主要参数说明（注意将各问题分别建立文件并将代码和数据放在同一目录下）

