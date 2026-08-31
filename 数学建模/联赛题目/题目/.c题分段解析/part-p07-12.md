<table border="1" ><tr>
<td>表格</td>
<td>主要用途</td>
</tr><tr>
<td>actualscheduletemplate.csv</td>
<td>问题4 实际赛程整理模板</td>
</tr><tr>
<td>result1testpredictiontemplate.csv</td>
<td>问题1 测试集预测输出模板</td>
</tr><tr>
<td>result1matchpredictiontemplate.csv</td>
<td>问题1 的72 场小组赛预测输出模板</td>
</tr><tr>
<td>result2template.csv</td>
<td>问题2 输出模板</td>
</tr><tr>
<td>result3template.csv</td>
<td>问题3 输出模板</td>
</tr><tr>
<td>result4template.csv</td>
<td>问题4 输出模板</td>
</tr></table>

# 输入数据附件

下列字段说明与Excel工作表逐项对应。每一字段均给出字段名、中文名称及解释。

1.README

<table border="1" ><tr>
<td>字段名</td>
<td>详细解释</td>
</tr><tr>
<td>项目</td>
<td>说明该行描述的数据包主题。</td>
</tr><tr>
<td>说明</td>
<td>提供赛制、时间、约束及数据规模的阅读提示。</td>
</tr></table>

2.historicalmatches

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchid</td>
<td>历史比赛编号</td>
<td>历史比赛的唯一标识，如H0001。</td>
</tr><tr>
<td>date</td>
<td>比赛日期</td>
<td>历史比赛的实际或模拟日期。</td>
</tr><tr>
<td>competition</td>
<td>赛事类别</td>
<td>比赛所属赛事类别，如友谊赛、世界杯预选赛、洲际杯或世界杯。</td>
</tr><tr>
<td>stage</td>
<td>比赛阶段</td>
<td>比赛在所属赛事中的阶<br>段，如小组赛、预选赛、<br>四分之一决赛或决赛。</td>
</tr><tr>
<td>teama</td>
<td>A 队名称</td>
<td>为统一记录顺序而标记的第一支球队；A /B 不代表主客场。</td>
</tr><tr>
<td>teamb</td>
<td>B 队名称</td>
<td>为统一记录顺序而标记的第二支球队；A /B 不代表主客场。</td>
</tr><tr>
<td>neutral</td>
<td>是否中立场</td>
<td>TRUE 表示比赛不在任何一方通常的主场环境进行；FALSE 表示非中立场。</td>
</tr><tr>
<td>goalsa</td>
<td>A 队实际进球</td>
<td>比赛结束后A 队的实际进球数。</td>
</tr><tr>
<td>goalsb</td>
<td>B 队实际进球</td>
<td>比赛结束后B 队的实际进球数。</td>
</tr><tr>
<td>xga</td>
<td>A 队期望进球</td>
<td>根据射门位置、方式和情境估计的理论进球数；它衡量机会质量，不等同于实际进球。</td>
</tr><tr>
<td>xgb</td>
<td>B 队期望进球</td>
<td>根据射门机会质量估计的B 队理论进球数。</td>
</tr><tr>
<td>shotsa</td>
<td>A 队射门次数</td>
<td>A 队在该场比赛中的射门总次数。</td>
</tr><tr>
<td>shotsb</td>
<td>B 队射门<br>次数</td>
<td>B 队在该场比赛中的射门总次数。</td>
</tr><tr>
<td>possessiona</td>
<td>A 队控球率</td>
<td>A 队控制比赛用球时间占有效比赛时间的百分比。</td>
</tr><tr>
<td>possessionb</td>
<td>B 队控球率</td>
<td>B 队控球率；通常与<br>possessiona 之和约为<br>100%。</td>
</tr><tr>
<td>strengthranka</td>
<td>A 队模拟实力排名</td>
<td>赛前模拟综合实力名次，<br>不是FIFA 官方排名。</td>
</tr><tr>
<td>strengthrankb</td>
<td>B 队模拟实力排名</td>
<td>赛前模拟综合实力名次，<br>不是FIFA 官方排名。</td>
</tr><tr>
<td>eloa</td>
<td>A 队赛前Elo 评分</td>
<td>球队基准Elo ，数值越大通常表示实力越强。</td>
</tr><tr>
<td>elob</td>
<td>B 队赛前Elo 评分</td>
<td>B 队赛前Elo 评分。</td>
</tr><tr>
<td>oddsa</td>
<td>A 队获胜欧赔</td>
<td>赛前市场对A 队获胜给出的十进制赔率。可用<br>1 /odds 计算未归一化隐含概率。</td>
</tr><tr>
<td>oddsdraw</td>
<td>平局欧赔</td>
<td>赛前市场对平局给出的十进制赔率。</td>
</tr><tr>
<td>oddsb</td>
<td>B 队获胜欧赔</td>
<td>赛前市场对B 队获胜给出的十进制赔率。</td>
</tr><tr>
<td>attendance</td>
<td>现场观众人数</td>
<td>进入比赛场馆现场观赛的人数。</td>
</tr><tr>
<td>tvviewers</td>
<td>转播观看人数</td>
<td>通过电视或网络等渠道观看比赛的估计总人数。</td>
</tr><tr>
<td>datasetsplit</td>
<td>数据集划分</td>
<td>按比赛日期固定划分训练数据（train ）和检验数据(test)。</td>
</tr></table>

3.teams

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>teamid</td>
<td>球队编号</td>
<td>48 支参赛球队的唯一编号。</td>
</tr><tr>
<td>teamname</td>
<td>球队名称</td>
<td>球队名称。</td>
</tr><tr>
<td>confederation</td>
<td>所属洲际足联</td>
<td>球队所属的国际足联地区组织。</td>
</tr><tr>
<td>strengthrank</td>
<td>模拟综合实力排名</td>
<td>根据模拟综合实力生成的赛前排名，不是FIFA 官方排名。</td>
</tr><tr>
<td>elorating</td>
<td>Elo 评分</td>
<td>根据历史比赛结果动态刻画球队的相对实力，赛前球队Elo 实力评分，数值越大通常表示实力越强。</td>
</tr><tr>
<td>marketvaluemusd</td>
<td>球队市场价值</td>
<td>全队球员市场价值的模拟总额，musd 表示百万美元。</td>
</tr><tr>
<td>avgage</td>
<td>平均年龄</td>
<td>球队球员平均年龄。</td>
</tr><tr>
<td>starindex</td>
<td>球星指数</td>
<td>综合刻画队内高影响力球员数量与知名度的模拟指标。</td>
</tr><tr>
<td>fanbaseindex</td>
<td>球迷基础指数</td>
<td>衡量球队全球或区域球迷规模的模拟指<br>标，越大表示潜在关注人群越多。</td>
</tr><tr>
<td>styleattack</td>
<td>进攻风格指数</td>
<td>数值越大表示球队整体进攻倾向或进攻能力越强。</td>
</tr><tr>
<td>styledefense</td>
<td>防守风格指数</td>
<td>数值越大表示球队整体防守能力或防守倾向越强。</td>
</tr><tr>
<td>hometimezoneregion</td>
<td>球队基准时区区域</td>
<td>将球队主要球迷所在地归入三个时区区<br>域，用于估计转播时段匹配。</td>
</tr><tr>
<td>hostflag</td>
<td>东道主标识</td>
<td>TRUE 表示该球队属于本届赛事承办国之<br>一；可体现东道主关注度、现场支持与旅行优势。</td>
</tr><tr>
<td>strengthscore</td>
<td>模拟综合实力得分</td>
<td>由多个球队属性合成的基准综合实力分，<br>用于生成附件中的基准预测；参赛队可自行重新构造。</td>
</tr><tr>
<td>homelatitude</td>
<td>球队代表地纬度</td>
<td>球队代表地或主要主场城市的纬度。</td>
</tr><tr>
<td>homelongitude</td>
<td>球队代表地经度</td>
<td>球队代表地或主要主场城市的经度。</td>
</tr></table>

4.groupsmatches

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchid</td>
<td>小组赛编号</td>
<td>72 场小组赛的唯一编号；<br>字母表示小组。</td>
</tr><tr>
<td>groupid</td>
<td>小组编号</td>
<td>48 支球队被划分为12 个小组，每组4 队。</td>
</tr><tr>
<td>roundingroup</td>
<td>小组赛轮次</td>
<td>每组共3 轮：1 为第一<br>轮、2 为第二轮、3 为最后一轮。每支球队每轮只参加一场比赛。</td>
</tr><tr>
<td>teamaid</td>
<td>A 队编号</td>
<td>该场比赛A 队在teams 表中的编号。</td>
</tr><tr>
<td>teama</td>
<td>A 队名称</td>
<td>该场比赛第一支球队。<br>A /B 仅用于记录，不代表主客场。</td>
</tr><tr>
<td>teambid</td>
<td>B 队编号</td>
<td>该场比赛B 队在teams 表中的编号。</td>
</tr><tr>
<td>teamb</td>
<td>B 队名称</td>
<td>该场比赛第二支球队。</td>
</tr></table>

5.groupmembership

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>groupid</td>
<td>小组编号</td>
<td>球队所属小组。</td>
</tr><tr>
<td>teamid</td>
<td>球队编号</td>
<td>球队唯一编号。</td>
</tr><tr>
<td>teamname</td>
<td>球队名称</td>
<td>球队名称。</td>
</tr><tr>
<td>pot</td>
<td>分档编号</td>
<td>模拟抽签分档；pot =1 通常代表赛前较强或种子球<br>队，pot =4 通常代表较低档球队。分档只描述抽签结构，不直接决定比赛结<br>果。</td>
</tr></table>

6.venues

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>venueid</td>
<td>场馆编号</td>
<td>候选承办场馆唯一编<br>号。</td>
</tr><tr>
<td>city</td>
<td>承办城市</td>
<td>场馆所在城市。</td>
</tr><tr>
<td>country</td>
<td>承办国家</td>
<td>场馆所在承办国家。</td>
</tr><tr>
<td>capacity</td>
<td>场馆容量</td>
<td>场馆允许的最大现场观众人数。预计上座人数原则上不得超过该值。</td>
</tr><tr>
<td>latitude</td>
<td>场馆纬度</td>
<td>场馆地理坐标中的纬<br>度。</td>
</tr><tr>
<td>longitude</td>
<td>场馆经度</td>
<td>场馆地理坐标中的经<br>度。</td>
</tr><tr>
<td>timezone</td>
<td>IANA 时<br>区</td>
<td>标准时区名称，用于把统一参考时刻换算为场馆当地时间。</td>
</tr><tr>
<td>maxmatchesperday</td>
<td>单日最大承办场次</td>
<td>同一场馆在任一当地日期最多可承办的比赛数量。</td>
</tr><tr>
<td>mintotalmatches</td>
<td>阶段最少承办场次</td>
<td>该场馆在72 场小组赛中必须承办的最少场次。</td>
</tr><tr>
<td>maxtotalmatches</td>
<td>阶段最多承办场次</td>
<td>该场馆在小组赛阶段可承办的最大场次。</td>
</tr><tr>
<td>setupcostmusd</td>
<td>场馆启用成本</td>
<td>若场馆至少承办一场比赛所产生的一次性模拟启用成本。</td>
</tr><tr>
<td>operationcostmusdpermatch</td>
<td>单场运营成本</td>
<td>该场馆每承办一场比赛产生的模拟运营成本。</td>
</tr><tr>
<td>securitylevel</td>
<td>场馆安保能力等级</td>
<td>场馆能够支持的最高安保保障等级。动态推荐安保等级不得高于该<br>值。</td>
</tr><tr>
<td>securitycostindex</td>
<td>安保成本指数</td>
<td>在同等安保等级下的相对成本系数，越大表示安保投入成本越高。</td>
</tr><tr>
<td>climaterisk</td>
<td>气候风险指数</td>
<td>综合考虑高温、降雨等潜在天气影响的模拟风险。</td>
</tr><tr>
<td>transportindex</td>
<td>交通便利指数</td>
<td>综合衡量机场、公共交通和城市接驳条件的模拟指标。辅助变量，不进入基准评分公式。</td>
</tr></table>

7.timeslots

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>slotid</td>
<td>候选时段编号</td>
<td>候选比赛开球时段的唯一编号。</td>
</tr><tr>
<td>date</td>
<td>参考日期</td>
<td>在referencetimezone 下的日期。</td>
</tr><tr>
<td>referencekickofftime</td>
<td>参考时区开球时间</td>
<td>以referencetimnezone 表示的开球时间。</td>
</tr><tr>
<td>referenceutctime</td>
<td>UTC 开球时刻</td>
<td>将参考开球时间换算为协调世界时后的统一时刻。</td>
</tr><tr>
<td>referencetimezone</td>
<td>统一参考时区</td>
<td>附件统一展示候选时段所采用的参考时区。</td>
</tr><tr>
<td>weekday</td>
<td>星期</td>
<td>参考日期对应的星期。</td>
</tr><tr>
<td>americaprime</td>
<td>美洲黄金时段标记</td>
<td>1 表示该时段对美洲主要观众较友好，0 表示非黄金时段。</td>
</tr><tr>
<td>europeprime</td>
<td>欧洲非洲黄金时段标记</td>
<td>1 表示该时段对欧洲和非洲主要观众较友好。</td>
</tr><tr>
<td>asiaprime</td>
<td>亚洲大洋洲黄金时<br>段标记</td>
<td>1 表示该时段对亚洲和大洋洲主要观众较友好。</td>
</tr><tr>
<td>globalprimescore</td>
<td>全球时段价值</td>
<td>综合三个主要观众区域后得到的模拟全球转播时段价值。</td>
</tr><tr>
<td>broadcastcapacity</td>
<td>可转播容量</td>
<td>该参考时段最多可获得转播资源的比赛数量。</td>
</tr></table>

8.distancematrix

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>originid</td>
<td>起点编号</td>
<td>起点实体编号；可能是球队代表地或上一场比赛场馆。</td>
</tr><tr>
<td>originname</td>
<td>起点名称</td>
<td>起点实体名称。</td>
</tr><tr>
<td>destinationid</td>
<td>终点编号</td>
<td>目的场馆编号。</td>
</tr><tr>
<td>destinationname</td>
<td>终点名称</td>
<td>目的地名称。</td>
</tr><tr>
<td>distancekm</td>
<td>旅行距离</td>
<td>起点与终点之间的模拟旅行距离。第一轮使用teamtovenue，后续轮次使用venuetovenue。</td>
</tr><tr>
<td>traveltimehour</td>
<td>预计旅行时间</td>
<td>综合飞行和接驳的模拟旅行时间。</td>
</tr><tr>
<td>timezonediff</td>
<td>时区差</td>
<td>模拟时区跨越负担。</td>
</tr><tr>
<td>relationtype</td>
<td>距离关系类型</td>
<td>teamtovenue 用于球队出发地到首场场馆；<br>venuetovenue 用于相邻两轮场馆之间。</td>
</tr></table>

9.ticketbroadcast

<table border="1" ><tr>
<td>字段名</td>
<td>中文名称</td>
<td>详细解释</td>
</tr><tr>
<td>matchstage</td>
<td>比赛阶段代码</td>
<td>票务与转播参数对应的比赛阶段。<br>GroupMatchR1/R2/R3分别对应小组赛第一、第二和第三轮。</td>
</tr><tr>
<td>baseticketpriceusd</td>
<td>基础票价</td>
<td>未考虑球队、场馆和动态调整时的模拟基础票价，<br>usd 表示美元。</td>
</tr><tr>
<td>priceelasticity</td>
<td>价格弹性</td>
<td>票价相对变化引起需求相对变化的敏感程度。绝对值越大表示观众需求对价格越敏感。</td>
</tr><tr>
<td>broadcastunitvalueusd</td>
<td>单位观看价值</td>
<td>每一预计转播观看人次对应的模拟商业价值。</td>
</tr><tr>
<td>sponsorweight</td>
<td>赞助权重</td>
<td>该阶段对赞助权益价值的相对放大系数。</td>
</tr><tr>
<td>localinterestweight</td>
<td>本地关注权重</td>
<td>该阶段对承办地现场及本地市场关注的相对权重。</td>
</tr></table>

