---
raw_title: 04-Gutierrez-2026
subject: 数学建模-策联杯C题
source: "s11590-026-02320-x.pdf"
status: mineru解析
parser: mineru
topics:
  - 世界杯2026
  - 混合整数规划
  - 旅行最小化
  - 场馆分配
---

ORIGINAL PAPER

![](04-Gutierrez-2026_images/9bd48ea6938398b44348fa5adf8cfa2cec0130242aaa94b2679109c63a8e43a2.jpg)

# Sport scheduling to minimize travels at the FIFA World Cup 2026

Rogelio Gutierrez<sup>1</sup> · Igor Cardoso<sup>1</sup> · Hamidreza Validi<sup>1</sup>

Received: 22 December 2025 / Accepted: 31 May 2026 / Published online: 14 June 2026 © The Author(s) 2026

## Abstract

Motivated by a recent FIFPRO (the International Federation of Professional Footballers’ Associations) report on the adverse efects of international travel load and time-zone crossings on player performance and physical well-being, this paper develops an optimization framework to reduce the total distance traveled by national teams in the FIFA World Cup 2026. We propose a mixed integer programming model that minimizes the total internal distance traveled by the 48 teams in the group stage, subject to the structural constraints implied by FIFA’s oficial schedule. Computational results yield a feasible schedule that reduces total internal travel distance by 50% and decreases the total number of time-zone crossings by 83%. To encourage the use of operations research tools and techniques in scheduling sports events and to promote transparency, our code and results are publicly available on GitHub. An interactive interface is also provided for soccer fans to explore and compare travel distances and time-zone crossings across teams at https://igorlucind o.github.io/ffa-world-cup-2026-scheduler-APP/.

Keywords Sport scheduling · Mixed integer programming · FIFA World Cup

## 1 Introduction

The FIFA World Cup is a global mega-event whose logistical design directly afects players’ performance and physical well-being, broadcast value, and costs. The 2026 edition, co-hosted by the United States, Mexico, and Canada, is unprecedented in geographic scale and operational complexity: 48 teams, a short group-stage horizon (11 June–19 July), a regionally distributed stadium footprint spanning multiple time zones, and stringent venue-availability constraints. This combination of compressed timelines as well as the long-distance and multi–time zone travels can exacerbate fatigue and recovery challenges, potentially undermining the performance and physical well-being of professional soccer players.

In line with these concerns, the recent FIFPRO Men’s Player Workload Monitoring (PWM) annual report highlights the recovery burden associated with international travel windows. In particular, it emphasizes that repeated cross-continental travel and multi-time zone crossings can amplify fatigue. These efects are especially pronounced when players are required to compete shortly after long-haul flights [1]. As an illustrative example, the report documents Moisés Caicedo’s October 2024 window: across a 14-day span, he played four matches while accumulating a total flight distance of 15,408 miles and crossing 10 time zones [1]. Notably, after playing 90 minutes in the English Premier League on 6 October, he reportedly traveled 5,732 miles between club and national-team fixtures (crossing five time zones). Then he undertook an additional 2,796 miles trip from Ecuador to Uruguay for the subsequent qualifier [1]. Taken together, these observations corroborate that long-distance travel concentrated into short recovery windows is not merely a theoretical concern, but a recurring workload stressor with adverse implications for player health.

Motivated by growing concerns about the workload burden created by longhaul international travel for elite soccer players, as highlighted by FIFPRO’s Player Workload Monitoring program [1], we study whether the group-stage assignment of matches in the 2026 FIFA World Cup can be redesigned to reduce aggregate team travel. In particular, we develop a mixed integer programming (MIP) model that minimizes total flight distance incurred by national teams during the group stage while enforcing the key structural requirements of the published FIFA match calendar (e.g., fixed dates, venues, and related operational constraints) [2]. Beyond distance, our travel-minimizing assignment has a direct implication for player recovery because long-haul trips often entail transmeridian travel that disrupts circadian rhythms (jet lag) and can impair sleep and performance, especially under short turnaround times [3–6]. Accordingly, by reducing the need for long cross-country legs, our approach also tends to reduce the cumulative number (and magnitude) of time-zone crossings teams experience across successive group-stage fixtures. As we show computationally, the resulting schedules yield substantial reductions not only in aggregate travel miles but also in cumulative time-zone crossings—a workload-related benefit that is not explicitly optimized in the objective but is induced by the structure of the distance-minimization formulation.

Since the original distance-minimization objective is cubic, we decompose it into the sum of two quadratic terms, yielding a more tractable mixed integer program (MIP). We also introduce symmetry-breaking constraints; empirically, these tighten the formulation and improve computational performance, leading to smaller final optimality gaps within a 4-hour time limit. Overall, we obtain a feasible schedule that reduces total travel by about 50% relative to the baseline, with savings in every group; moreover, it reduces the total number of time-zone crossings by about 83% relative to the oficial schedule of FIFA. To promote transparency, reproducibility, and broader adoption of operations research (OR) tools for mega-event sports scheduling, we release (i) an interactive web application that introduces non-OR audiences and soccer fans to the challenges of sports scheduling (https://igorlucindo.github.io/f ifa-world-cup-2026-scheduler-APP/), and (ii) our full implementation and computational results in a public GitHub repository (https://github.com/hamidrezavalidi/FIF A\_World\_Cup\_2026).

The remainder of the paper is organized as follows. Section 2 reviews the related literature, with an emphasis on sports and soccer scheduling. Section 3 describes the FIFA World Cup 2026 group-stage scheduling context and summarizes the relevant operational constraints for the travel-minimization problem studied in this paper. Section 4 presents our MIP formulation for the scheduling problem. Section 5 describes computational enhancements and reports the results. Section 6 concludes and discusses directions for future work.

Disclaimer Our MIP formulation is intended as a schedule-comparable redesign tool and therefore captures only the standard structural restrictions that can be directly inferred from the currently published FIFA match schedule (dates, rounds, and venues) available at https://www.ffa.com/en/tournaments/mens/worldcup/canadamexi cousa2026/articles/match-schedule-fxtures-results-teams-stadiums. We emphasize that additional practical “field” constraints—such as detailed stadium availability windows, local security/transportation considerations, contractual broadcast requirements, and other operational policies—are not publicly accessible to the authors and hence are not modeled explicitly. Nonetheless, such requirements can be incorporated in a straightforward way by adding the corresponding linear constraints (or by fixing/ forbidding specific match–venue–day assignments) within our formulation, without altering its core structure. We also do not model team-based camps, since base-camp selection is made by the participating teams (after the final draw in December 2025) rather than by the tournament organizers. This omission does not materially afect the organizer-facing insights: minimizing inter-round venue distances (Rounds 1 2 and 2 3) reduces the unavoidable travel component under any reasonable basecamp strategy adopted by teams. Moreover, by keeping a team’s match locations geographically compact, our assignments allow teams to choose nearby base camps that can further limit travel.

## 2 Background and literature review

Sports timetabling has long served as a flagship application area for OR, connecting graph theory, integer programming (IP), constraint programming (CP), decomposition methods, as well as heuristics and metaheuristic approaches. A foundational reference is de Werra [7], which frames round-robin scheduling using graph-based encodings and points to structural notions—such as home/away patterns and the counting of “breaks” (consecutive home or consecutive away games)—that remain central in modern models.

Two widely used entry points to the broader OR literature are the annotated bibliography of Kendall et al. [8] and the survey of round-robin scheduling by Rasmussen and Trick [9]. Kendall et al. [8] curate and classify a large body of work spanning many sports and formats, with emphasis on common objectives (i.e., travel, breaks, fairness, broadcast value) and on the solution paradigms that typically succeed in practice (IP/CP, metaheuristics, and hybrids). Rasmussen and Trick [9] focus more narrowly on round-robin structures and show how standard policies (i.e., mirrored rounds, no-repeat rules, limits on consecutive home/away games) shape the feasible space and drive model design.

When venues are geographically dispersed, travel minimization becomes a defining objective, and the Traveling Tournament Problem (TTP) has emerged as the canonical benchmark abstraction. Easton, Nemhauser, and Trick [10] introduced the TTP to crystallize the interaction between round-robin feasibility and travel cost, and the benchmark has since motivated both exact and heuristic methods. At the applied end of the spectrum, deployed decision-support systems in soccer illustrate how travel objectives are operationalized alongside fairness and television requirements, e.g., in the Belgian league [11].

Our setting follows this tradition but difers structurally from season-long league scheduling. The World Cup group stage is short-horizon (three matches per team), imposes concurrency in the final group round, and must respect a fixed calendar of venue/day/time windows. These features shift the emphasis from constructing an entire timetable to solving a tightly constrained assignment problem over a pre-specified match calendar.

## 2.1 Sports timetabling in OR: foundational structures and surveys

de Werra [7] is representative of early work that links sports schedules to discrete mathematics. Beyond the introduction of graph encodings, the paper articulates how the problem can be separated into (i) combinatorial feasibility of pairings and (ii) sequencing of those pairings over rounds, and it discusses how “pattern” constraints (home/away sequences and breaks) can be expressed in a disciplined way. This viewpoint is echoed in many later formulations that use pattern-based variables, side constraints on patterns, and decomposition between pairing/timetabling components.

Kendall et al. [8] provide an annotated bibliography intended to help practitioners and researchers quickly situate a new model. In addition to cataloging papers, they summarize, for each stream, the dominant constraints and objective functions, and they explain which algorithmic ideas tend to be efective (e.g., pure IP for smaller and highly constrained leagues; CP for complex logical constraints; metaheuristics for large instances with soft constraints; and hybrids for “best of both worlds”).

Rasmussen and Trick [9] survey round-robin scheduling with a modeling-centric lens. They formalize standard structural restrictions (mirroring, no-repeats, bounds on consecutive home/away games) and discuss feasibility implications via homeaway patterns (HAPs). They also review common objective components (travel, breaks, fairness) and show how these objectives can be coupled to the structural constraints in both exact and heuristic frameworks. The survey is particularly relevant for our setting because many World Cup policies resemble round-robin primitives when viewed at the group level (even though the overall tournament format is not a full league season). Ribeiro [12] complements the above surveys by emphasizing how practical constraints enter deployed systems. It discusses, among others, stadium availability windows, conflicting events in the same metro area, limits on simultaneous home games, and commercial/broadcast requirements.

## 2.2 Travel minimization and the traveling tournament problem (TTP)

Easton, Nemhauser, and Trick [10] introduced the TTP as a benchmark for travelaware league scheduling. In its standard form, the problem considers a double roundrobin tournament and minimizes total travel while enforcing canonical feasibility restrictions such as the no-repeat rule and bounds on consecutive home/away games. The benchmark is influential because it isolates a practically meaningful objective (travel) while retaining enough structure to stress-test algorithmic ideas across exact and heuristic paradigms.

The TTP benchmark catalyzed work on hybrid algorithm design. Easton et al. [13] propose a combined integer programming and constraint programming approach that uses CP to enforce intricate scheduling structure while leveraging IP to guide global decisions, illustrating a decomposition-like division of labor between modeling technologies. This line of work motivated later “matheuristic” strategies that treat feasibility enforcement, neighborhood definition, and objective improvement as distinct modules.

On the exact optimization side, Irnich [14] develops a branch-and-price algorithm for the TTP. The key contribution is to exploit route/schedule structure in a column generation framework, yielding stronger relaxations and enabling larger benchmark instances to be solved. Complementary complexity results clarify why such specialized algorithms are needed: Thielen and Westphal [15] establish hardness results for TTP variants, while Bhattacharyya [16] provides an earlier note emphasizing intractability considerations for the problem family.

High-quality heuristics are also central because real leagues often have far more side constraints than benchmark instances. Anagnostopoulos et al. [17] propose a simulated annealing approach with neighborhood moves designed to preserve core tournament feasibility while improving travel, showing that problem-tailored neighborhoods can close much of the gap to optimal schedules at much lower computational cost. Goerigk and Westphal [18] argue for a modern matheuristic perspective that couples large-neighborhood search with integer programming components, aiming to combine the scalability of local search with IP-based improvements and feasibility repair.

Travel objectives are typically balanced against fairness requirements that protect competitive integrity and stakeholder needs. A canonical fairness instrument is control of breaks—consecutive home games or consecutive away games—because uneven breaks can advantage some teams and burden others. Rasmussen and Trick [9] review break-related constraints and discuss how feasibility over HAP sets can become a subproblem inside larger models (e.g., via pattern generation or as a source of cutting planes and repair moves).

International tournaments bring an additional fairness dimension: concurrency in decisive rounds. It is standard practice that, within a group, the last two matches are played simultaneously to reduce incentives for strategic play and collusion. From a modeling viewpoint, concurrency introduces coupling constraints across matches that share a group and a round. A broader OR view of such tournament-design considerations (fairness, incentives, and stakeholder objectives) is surveyed by Devriesere et al. [19].

## 2.3 Time-zone crossings

Long-haul international travel across multiple time zones is widely recognized as a distinct workload stressor for elite athletes because it can induce circadian misalignment (“jet lag”), degrade sleep quantity and quality, and prolong recovery. The magnitude of this burden is largely driven by the number of time zones crossed, the direction of travel (eastward travel is typically more challenging than westward), and the time available for circadian re-entrainment before competition [3–5]. Recent sport-science syntheses further emphasize that transmeridian travel should be treated as an additional load alongside match congestion, particularly when short turnarounds constrain post-flight recovery [20, 21].

Evidence from professional leagues supports that time-zone travel can measurably afect competitive performance. For instance, observational analyses in Major League Baseball report performance degradation patterns consistent with jet-lag mechanisms, with efects often more pronounced after eastward travel [6]. Complementary studies in North American leagues connect game outcomes to “circadian disadvantage”—a mismatch between a team’s internal clock and local game time— showing associations that vary by travel direction, the number of time zones crossed, and game timing [22, 23]. Recently, league-scale evidence in the National Basketball Association links eastward jet lag to impaired performance and game outcomes [24].

In soccer, FIFPRO’s Player Workload Monitoring (PWM) program highlights repeated long-haul travel and multi-time-zone crossings as recurring features of the modern international calendar, and flags their potential to compound fatigue when players compete shortly after transmeridian flights [1]. These concerns are particularly salient for the 2026 FIFA World Cup, whose host geography spans multiple time zones and therefore creates an inherent trade-of between operational feasibility and travel/circadian burden [2]. In our setting, although the primary objective minimizes total flight distance, we also quantify time-zone crossings under each schedule; importantly, reduced travel typically translates into fewer (and smaller) transmeridian jumps, yielding a meaningful reduction in aggregate time-zone crossings relative to the baseline schedule reported in Sect. 5.

## 2.4 Applied soccer scheduling and related assignment problems

Deployed OR systems in professional soccer illustrate the translation from stylized models to policy-rich and stakeholder-driven constraints. Goossens and

Spieksma [11] describe the scheduling of the Belgian professional soccer league, showing how a mathematical programming model can integrate travel, fairness, and television/broadcast constraints and how such constraints are elicited and enforced in practice. Goossens and Spieksma [25] survey professional soccer scheduling in Europe and explain common league-specific rules and constraint types, providing useful context for how “broadcast-friendly” and “fairness” policies are operationalized. Bartsch, Drexl, and Kröger [26] study the professional soccer leagues of Austria and Germany under a rich set of constraints. Their work demonstrates how problem-specific modeling, together with algorithmic hybridization, is often necessary to achieve feasible and high-quality schedules in league settings.

Related assignment problems outside soccer further illustrate how travel interacts with frequency/exposure constraints and how hybrid methods scale. Trick, Yildiz, and Yunes [27] study Major League Baseball umpire scheduling through the traveling umpire problem, combining network optimization ideas with neighborhood search to respect assignment-frequency rules while controlling travel. Bonomo et al. [28] provide another example in the context of the Argentine volleyball league, where travel-aware tournament scheduling constraints produce instances closely related to TTP-like structures.

## 3 Problem description

The FIFA World Cup 2026 is co-hosted by Canada, Mexico, and the United States across 16 host cities and stadiums, and it is the first World Cup played with 48 national teams. The tournament format consists of 12 groups of four teams each, followed by an expanded knockout phase. In this paper, we focus exclusively on the group stage, which comprises 72 matches and is organized into three matchdays/ rounds. In particular, we consider the standard decomposition of the group stage into 24 matches in Round 1, 24 matches in Round 2, and 24 matches in Round 3, i.e., 72 total group-stage matches.

The 2026 group stage is played over a short and fixed planning horizon spanning June 11–27, 2026, which we partition into three round-specific date windows: Round 1 is held on June 11–17, Round 2 on June 18–23, and Round 3 on June 24–27. This fixed calendar is a key feature of the World Cup setting: rather than creating pairings and dates from scratch, the scheduler must assign each pre-defined groupstage match to an available (stadium, day) slot consistent with operational rules and fairness policies.

The core decision in our model is a structured assignment: (i) for each team and each of the three rounds, select the stadium where that team will play, and (ii) for each of the 72 group-stage matches, choose exactly one (stadium, day) pair within the round’s allowable date window. Travel costs are induced by these assignments, because each team may have to move from its Round 1 stadium to its Round 2 stadium, and then to its Round 3 stadium. The overall goal is to redesign the group-stage assignments to reduce total travel while remaining compatible with the published operational “shape” of the FIFA calendar.

Our objective is to minimize the total distance traveled by all teams between consecutive rounds—from Round 1 to Round 2 and from Round 2 to Round 3—where distances are computed between the assigned stadium locations (e.g., via great-circle distances as in our implementation). This objective directly targets the concentrated travel burden created by a geographically wide tournament footprint and a compressed group-stage timeline.

The assignment must satisfy several groups of operational constraints that reflect the FIFA group-stage calendar structure available at https://www.ffa.com/en/tourna ments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fxtures-resul ts-teams-stadiums and stadium feasibility:

1. Each match is scheduled exactly once (unique slot). Every group-stage match must be assigned to exactly one stadium on exactly one day within its round’s permissible date window.

2. Daily match-count requirements by round. The model enforces that the calendar “load” matches the expected World Cup rhythm: on each day of Rounds 1 and 2 (with explicit exceptions on the first two opening dates), exactly four matches are played; and on each day of Round 3, exactly six matches are played. This captures both the density of the group stage and the higher concurrency typical of the final group matchday.

3. Stadium utilization bounds over the group stage. Each stadium is required to host a reasonable number of matches over the full group stage, bounded between a minimum and a maximum load (to avoid under-utilized venues and to prevent over-concentration at a few sites).

4. Within-round pairing (“partner match”) synchronization. In a given group and round, the two matches of that group are treated as a paired unit (a “partner” relationship): if one of the paired matches is played on a given day, then its partner match must also be played on that same day (with explicitly listed early-calendar opening dates exceptions). This encodes the World Cup practice of organizing group play in coordinated daily blocks, and it creates the concurrency structure needed for competitive integrity and broadcast design.

5. Stadium recovery constraints. To reflect operational feasibility at venues, a stadium cannot host matches on consecutive days. Moreover, in the early and middle portion of the group stage (Rounds 1 and 2), we strengthen this notion by preventing a stadium from hosting within any three-day window, modeling additional turnaround needs such as pitch recovery, stafing, and security/logistics resets.

6. Minimum rest between a team’s consecutive group matches. The group stage is short, so rest windows matter. The model links each match to the next match in the same group “thread” and enforces that the next match must occur suficiently later in the calendar (at least a specified minimum number of days after the earlier match). In our computational implementation, we refine this to a bounded window (minimum and maximum gap) to reflect both recovery needs and the oficial FIFA schedule.

7. Match-to-team consistency. A match can only be placed in a stadium if both participating teams are assigned to that same stadium in that round. In other words, match placement decisions are linked to round-by-round team venue assignments to ensure consistency between the match schedule and the teams’ venue locations.

8. Exactly one stadium per team per round. In each round, every team is assigned to exactly one stadium, ensuring a unique venue assignment for that team within the round (and preventing a team from being “split” across multiple stadiums in the same round).

Having established the structural rules that define a schedule comparable to FIFA’s published group-stage blueprint, we now formalize the corresponding optimization problem. Section 4 presents a MIP formulation that simultaneously (i) enforces the calendar- and venue-driven constraints summarized above (unique match assignment, round-dependent daily match counts, partner-match synchronization, stadium workload and turnaround requirements, minimum rest windows, and consistency between match placements and team venue assignments) and (ii) optimizes a travel-minimization objective. Concretely, the model chooses round-by-round venue assignments for teams and assigns each match to an admissible (stadium, day) slot, so that the induced inter-round travels (Round 1 Round 2 and Round 2 Round 3) are minimized while preserving feasibility by construction.

## 4 A MIP formulation

Let S denote the set of stadiums and $\mathcal { G }$ the set of groups in the FIFA World Cup 2026. The set of teams is $T : = \textstyle \bigcup _ { G \in { \mathcal { G } } } G .$ , and the group stage unfolds over the round index set $R : = \{ 1 , 2 , 3 \}$ ∪ ∈G. Travel is measured by a nonnegative metric $\ell _ { s s ^ { \prime } } \geq 0$ for any pair of stadiums $\{ s , s ^ { \prime } \} \in \left( \begin{array} { l } { S } \\ { 2 } \end{array} \right)$ (i.e., the great–circle distance [29]). The US, Canada, and Mexico are host nations. We collect them in $H \subseteq T$ and, for each host team $h \in H$ , specify the admissible venue subset $S _ { h } \subseteq S$ in which h may appear. Because the stadium of host teams at every round of the group stage is fixed, we define $s _ { h r }$ as the stadium of host team $h \in H$ in round $r \in R$

Let M be the set of all 72 matches of the group stage, with $M _ { 1 } = \{ m _ { 1 } , \cdot \cdot \cdot , m _ { 2 4 } \}$ $M _ { 2 } = \{ m _ { 2 5 } , \cdot \cdot \cdot , m _ { 4 8 } \}$ , and $M _ { 3 } = \{ m _ { 4 9 } , \cdot \cdot \cdot , m _ { 7 2 } \}$ being the sets of matches in rounds 1, 2, and 3, respectively $( M = M _ { 1 } \cup M _ { 2 } \cup M _ { 3 } )$ . Also, we define D as the set of days in which the group stage games are held. We denote the days of the first round, second round, and the third round as $D _ { 1 } = \{ d _ { 1 } = 1 1 \mathrm { J u n e } , \cdot \cdot \cdot , d _ { 7 } = 1 7 \mathrm { J u n e } \}$ $D _ { 2 } = \{ d _ { 8 } = 1 8 { \mathrm { J u n e } } , \cdot \cdot \cdot , d _ { 1 3 } = 2 3 { \mathrm { J u n e } } \}$ and

$D _ { 3 } = \{ d _ { 1 4 } = 2 4 { \mathrm { J u n e } } , \cdot \cdot \cdot , d _ { 1 7 } = 2 7 { \mathrm { J u n e } } \}$ , respectively $( D = D _ { 1 } \cup D _ { 2 } \cup D _ { 3 } )$ For every round $r \in R$ , binary decision variable $y _ { s , d } ^ { m }$ is one if match $m \in M _ { r }$ is held in stadium $s \in S$ , on day $d \in D _ { r }$

To facilitate navigation between the narrative description and the mathematical formulation, we align the numbering of the constraints in this section with the numbering of the corresponding operational requirements introduced in Sect. 3.

Each match is played at exactly one stadium on exactly one eligible day in its round. So, for every round $r \in R$ and every match $m \in M _ { r }$ , we have

$$
\sum_ {s \in S} \sum_ {d \in D _ {r}} y _ {s, d} ^ {m} = 1.\tag{1}
$$

Our proposed schedule respects FIFA’s daily match pattern in the oficial schedule. In other words, we have four matches per day in Rounds 1 and 2 (with stated early-date exceptions) and six matches per day in Round 3. So, for every round $r \in \{ 1 , 2 \}$ and every day $d \in D _ { r }$ , except 11 June and 12 June, we have

$$
\sum_ {s \in S} \sum_ {m \in M _ {r}} y _ {s, d} ^ {m} = 4;\tag{2a}
$$

and for every day $d \in D _ { 3 }$ , we have

$$
\sum_ {s \in S} \sum_ {m \in M _ {3}} y _ {s, d} ^ {m} = 6.\tag{2b}
$$

Following the oficial FIFA schedule, we impose minimum and maximum hosting requirements per stadium during the group stage, ensuring equitable utilization while avoiding excessive clustering of matches at a few sites. For every stadium $s \in S$ , we impose the following inequality.

$$
3 \leq \sum_ {m \in M} \sum_ {d \in D} y _ {s, d} ^ {m} \leq 5.\tag{3}
$$

For each group in each round, the two matches are treated as a paired set according to the oficial FIFA schedule. In other words, if one is played on a day, the other is played that day as well (with stated early-date exceptions). This preserves FIFA’s block scheduling and the concurrency required for sporting integrity and media coverage. For every match $m \in M \setminus \{ m _ { 3 } , m _ { 4 } , m _ { 6 } , m _ { 8 } \}$ , we define the partner match function $p ( \cdot )$ that maps a match of a group to another match in the same round. For example, the partner of match A1 vs. A2 in Round 1 is A3 vs. A4. Then, for every day $d \in D \setminus \{ d _ { 1 } , d _ { 2 } , d _ { 3 } \}$ and every match $m \in M \setminus \{ m _ { 3 } , m _ { 4 } , m _ { 6 } , m _ { 8 } \}$ , we have

$$
\sum_ {s \in S} y _ {s, d} ^ {m} = \sum_ {s \in S} y _ {s, d} ^ {p (m)}.\tag{4}
$$

For operational reasons and in accordance with the oficial FIFA schedule, a stadium may not stage matches on consecutive days. In Rounds 1 and 2, it may host at most once in any three days to allow suficient turnaround (pitch, staf, and logistics). So, for every stadium $s \in S$ and every day index $i \in [ 1 3 ] : = \{ 1 , 2 , \cdot \cdot \cdot , 1 3 \}$ , we have

$$
\sum_ {m \in M} y _ {s, d _ {i}} ^ {m} + \sum_ {m \in M} y _ {s, d _ {i + 1}} ^ {m} + \sum_ {m \in M} y _ {s, d _ {i + 2}} ^ {m} \leq 1.\tag{5a}
$$

In Round 3, no two matches are allowed to be held in a stadium on two consecutive days. So, for every stadium $s \in S$ and every day index $i \in \{ 1 4 , 1 5 , 1 6 \}$ , we have

$$
\sum_ {m \in M} y _ {s, d _ {i}} ^ {m} + \sum_ {m \in M} y _ {s, d _ {i + 1}} ^ {m} \leq 1.\tag{5b}
$$

Because the group stage is tightly scheduled, adequate recovery time is essential. Following the FIFA oficial schedule, our model maps each team’s match to its next group-stage match and imposes lower and upper bounds on the number of days between consecutive matches. We also define next( ) as a function that maps a match of a group in a round to the next match in the next round.<sup>1</sup> For Round 1 and every day $d _ { i } \in D _ { 1 }$ with index $i \in [ 7 ]$ , and match $m \in M _ { 1 }$ , we have

$$
\sum_ {s \in S} y _ {s, d _ {i}} ^ {m} \leq \sum_ {s \in S} \sum_ {d ^ {\prime} \in D _ {2}: d _ {i + 5} \leq d ^ {\prime} \leq d _ {i + 7}} y _ {s, d ^ {\prime}} ^ {\mathrm{next} (m)};\tag{6a}
$$

and for Round 2 and every day $d _ { i } \in D _ { 2 }$ with index $i \in \{ 8 , \ldots , 1 3 \}$ , and match $m \in M _ { 2 }$ , we have

$$
\sum_ {s \in S} y _ {s, d _ {i}} ^ {m} \leq \sum_ {s \in S} \sum_ {d ^ {\prime} \in D _ {3}: d _ {i + 4} \leq d ^ {\prime} \leq d _ {i + 6}} y _ {s, d ^ {\prime}} ^ {\text { next } (m)}.\tag{6b}
$$

Furthermore, a match may be scheduled at a stadium only if both of its teams are designated to play at that venue in the corresponding round. In other words, the matchby-day venue choice is tied to the teams’ round-specific venue assignments, so the schedule and team locations remain consistent. To capture this set of constraints, we define new binary decision variables x. For each team $t \in T$ , stadium $s \in S$ , and round $r \in R _ { : }$ , we define binary decision variable $\boldsymbol { x } _ { t s } ^ { r }$ that equals 1 if team t plays its round-r match at stadium s, and 0 otherwise. So, for every round $r \in R ,$ , every match $m = \{ t , t ^ { \prime } \} \in M _ { \ i }$ between teams t and $t ^ { \prime }$ in the same group, and every stadium $s \in S$ , we have

$$
\begin{array}{l} \sum_ {d \in D _ {r}} y _ {s, d} ^ {m} \leq x _ {t s} ^ {r} \\ \sum_ {d \in D _ {r}} y _ {s, d} ^ {m} \leq x _ {t ^ {\prime} s} ^ {r}. \end{array}\tag{7}
$$

For every round $r \in R$ and every team $t \in T$ , the following constraint ensures that team t in round r plays in exactly one stadium.

$$
\sum_ {s \in S} x _ {t s} ^ {r} = 1.\tag{8}
$$

Finally, we have the following cubic objective function that minimizes the internal distances traveled by all teams of the tournament.

$$
\sum_ {t \in T} \sum_ {s _ {1} \in S} \sum_ {s _ {2} \in S} \sum_ {s _ {3} \in S} (\ell_ {s _ {1}, s _ {2}} + \ell_ {s _ {2}, s _ {3}}) x _ {t s _ {1}} ^ {1} x _ {t s _ {2}} ^ {2} x _ {t s _ {3}} ^ {3}.\tag{9}
$$

Here, ℓ denotes the travel distances between stadiums. We compute travel distances using city-level coordinates for each host venue and the great-circle (spherical) distance between successive match locations. Specifically, each stadium $s \in S$ is represented by latitude and longitude coordinates $\left( \varphi _ { s } , \lambda _ { s } \right)$ , and for any two venues $\{ s , s ^ { \prime } \} \in \left( \begin{array} { l } { S } \\ { 2 } \end{array} \right)$ , the distance in miles is computed via the haversine formula

$$
\ell_ {s, s ^ {\prime}} = 2 R \arcsin \left(\sqrt {\sin^ {2} \left(\frac {\varphi_ {s ^ {\prime}} - \varphi_ {s}}{2}\right) + \cos (\varphi_ {s}) \cos (\varphi_ {s ^ {\prime}}) \sin^ {2} \left(\frac {\lambda_ {s ^ {\prime}} - \lambda_ {s}}{2}\right)}\right),
$$

where R = 3, 958.8 is the Earth radius in miles and angles are measured in radians [30, 31]. For each team t, group-stage travel equals the sum of the two inter-round legs (Round 1 Round 2 and Round 2 Round 3) induced by the assigned venues.

Since objective function (9) is cubic (i.e., trilinear in the binary venue-assignment variables), it lies outside the standard MIP class that general-purpose solvers handle natively. In practice, state-of-the-art optimizers are designed for linear and (convex or nonconvex) quadratic objectives and constraints, whereas higher-order polynomial terms typically require an explicit reformulation (e.g., auxiliary variables and extra constraints) to be accepted and solved reliably. Proposition 1 exploits the “exactlyone-stadium-per-round” identities in constraints (8) to eliminate the third-order products without introducing new variables, yielding an equivalent quadratic objective that preserves the intended two-leg travel structure (Round 1 2 and Round 2 3) and is therefore much more amenable to modern MIP solvers.

Proposition 1 Let ˆx be a binary point that satisfies constraints (8). For every team $t \in T \setminus H$ , we have

$$
\begin{array}{r l r} & & {\sum_ {s _ {1} \in S} \sum_ {s _ {2} \in S} \sum_ {s _ {3} \in S} (\ell_ {s _ {1}, s _ {2}} + \ell_ {s _ {2}, s _ {3}}) \hat {x} _ {t s _ {1}} ^ {1} \hat {x} _ {t s _ {2}} ^ {2} \hat {x} _ {t s _ {3}} ^ {3} = \sum_ {s _ {1} \in S} \sum_ {s _ {2} \in S} \ell_ {s _ {1}, s _ {2}} \hat {x} _ {t s _ {1}} ^ {1} \hat {x} _ {t s _ {2}} ^ {2}} \\ & & {+ \sum_ {s _ {2} \in S} \sum_ {s _ {3} \in S} \ell_ {s _ {2}, s _ {3}} \hat {x} _ {t s _ {2}} ^ {2} \hat {x} _ {t s _ {3}} ^ {3}.} \end{array}
$$

Proof We start from the left side of the equation to reach the right side.

$$
\begin{array}{r l} & {\sum_ {s _ {1} \in S} \sum_ {s _ {2} \in S} \sum_ {s _ {3} \in S} (\ell_ {s _ {1}, s _ {2}} + \ell_ {s _ {2}, s _ {3}}) \hat {x} _ {t s _ {1}} ^ {1} \hat {x} _ {t s _ {2}} ^ {2} \hat {x} _ {t s _ {3}} ^ {3} = \sum_ {s _ {1} \in S} \sum_ {s _ {2} \in S} \sum_ {s _ {3} \in S} (\ell_ {s _ {1}, s _ {2}} \hat {x} _ {t s _ {1}} ^ {1} \hat {x} _ {t s _ {2}} ^ {2} \hat {x} _ {t s _ {3}} ^ {3}} \\ & {\qquad + \ell_ {s _ {2}, s _ {3}} \hat {x} _ {t s _ {1}} ^ {1} \hat {x} _ {t s _ {2}} ^ {2} \hat {x} _ {t s _ {3}} ^ {3})} \\ & {\qquad = \sum_ {s _ {1} \in S} \sum_ {s _ {2} \in S} \ell_ {s _ {1}, s _ {2}} \hat {x} _ {t s _ {1}} ^ {1} \hat {x} _ {t s _ {2}} ^ {2} (\sum_ {s _ {3} \in S} \hat {x} _ {t s _ {3}} ^ {3})} \\ & {\qquad + (\sum_ {s _ {1} \in S} \hat {x} _ {t s _ {1}} ^ {1}) \sum_ {s _ {2} \in S} \sum_ {s _ {3} \in S} \ell_ {s _ {2}, s _ {3}} \hat {x} _ {t s _ {2}} ^ {2} \hat {x} _ {t s _ {3}} ^ {3}} \\ & {\qquad = \sum_ {s _ {1} \in S} \sum_ {s _ {2} \in S} \ell_ {s _ {1}, s _ {2}} \hat {x} _ {t s _ {1}} ^ {1} \hat {x} _ {t s _ {2}} ^ {2}} \\ & {\qquad + \sum_ {s _ {2} \in S} \sum_ {s _ {3} \in S} \ell_ {s _ {2}, s _ {3}} \hat {x} _ {t s _ {2}} ^ {2} \hat {x} _ {t s _ {3}} ^ {3}.} \end{array}
$$

The last equality holds because $\begin{array} { r } { \sum _ { s _ { 1 } \in S } \hat { x } _ { t s _ { 1 } } ^ { 1 } = 1 } \end{array}$ and $\begin{array} { r } { \sum _ { s _ { 3 } \in S } \hat { x } _ { t s _ { 3 } } ^ { 3 } = 1 } \end{array}$ by constraints (8). □

## 5 Computational improvements and results

This section provides the computational pipeline used to solve the full 2026 groupstage instance and to quantify the benefits of the proposed travel-minimizing assignment. All experiments were conducted on a 64-bit, x64-based machine equipped with an Intel(R) Core(TM) Ultra 9 285 processor (2.50 GHz) and 64.0 GB of RAM. We implemented our algorithms in Python and solved the proposed MIP using Gurobi 13.0.0. We set a 4-hour time limit for running the MIP formulation with Gurobi. For transparency and to encourage future sport scheduling eforts, the full implementation and computational outputs are publicly available at https://github.co m/hamidrezavalidi/FIFA\_World\_Cup\_2026. Furthermore, we provide an interactive graphical interface for soccer fans at https://igorlucindo.github.io/ffa-world-cup-20 26-scheduler-APP/ that allows users to design their own schedule and directly compare it against both the oficial FIFA schedule and our MIP-based solution.

## 5.1 Computational improvements

Our MIP formulation sufers from symmetry: many distinct assignments of matches to (stadium, day) slots and of teams to round-by-round venues induce schedules that are equivalent from the solver’s perspective, difering only by permutations of labels (e.g., renaming groups) and by permutations of interchangeable daily “blocks” of Round 1 matches. Such symmetries are well known to severely degrade branch-andbound performance by creating large families of equivalent incumbent and fractional solutions, inflating the search tree, and slowing bound improvement in scheduling models [32–35]. Symmetry is particularly prominent in sports scheduling because repeated structures (e.g., rounds, blocks, and repeated constraint templates) naturally generate automorphisms of the formulation; exploiting and breaking these symmetries is often decisive for scalability [36].

In our setting, the symmetry is most acute in Round 1 because it is the first stage of the group phase: there is no prior-round placement to anchor the calendar, and many groups are structurally interchangeable under the model’s generic round/day constraints. To mitigate this, we implement a calendar anchoring strategy for Round 1 by fixing the day of play for specific Round 1 matches according to the oficial FIFA day-block order. Concretely, we enforce: (i) both Round 1 matches of Group A on June 11, (ii) one Round 1 match from each of Groups B and D on June 12, (iii) the remaining Round 1 matches of Groups B and D, together with both Round 1 matches of Group C, on June 13, and (iv) for June 14–17, we fix the Round 1 pattern so that groups $\{ E , F \}$ play on June 14, groups G, H on June 15, groups I, J on June 16, and groups K, L on June 17 (with both matches of each group occurring on the same day). These fixings are implemented by adding equalities of the following form for every match $m \in M _ { 1 }$ and every day $d \in D _ { 1 }$

$$
\sum_ {s \in S} y _ {s, d} ^ {m} = 1.
$$

This anchoring is a stronger symmetry-breaking mechanism than typical lexicographic ordering constraints: rather than selecting a representative solution from each symmetry class, we fix the Round 1 day-block structure as part of the input calendar that our study aims to respect. Under our problem definition, the Round 1 block order is not a decision to optimize; it is inherited from the oficial FIFA match-day schedule blueprint we adopt. Therefore, enforcing this order does not remove any schedule that would be admissible under that blueprint, but it eliminates a large set of solverequivalent permutations that would otherwise be explored. In addition, anchoring Round 1 is especially impactful because all inter-round rest-window constraints are defined relative to the Round 1 dates; fixing Round 1 removes “calendar-shift” ambiguity early in the search and stabilizes the implied feasible windows for Round 2 and Round 3.

Computationally, these Round 1 day fixings accelerate the solving process. Under the same solver configuration and time limit, anchoring Round 1 reduces the final optimality gap from 41.6% to 30.0%, i.e., 27.88% relative improvement in the gap.

## 5.2 Distance results

Using the MIP formulation of Sect. 4 and computational enhancements described in Sect. 5.1, we obtained a feasible group-stage schedule with total team travel of 30, 860.7 miles. For comparison, applying the same travel accounting method to the currently published 2026 FIFA World Cup match schedule yields 61, 324.3 miles for the group stage [2]. Thus, our solution reduces total group-stage team travel by 30, 463.6 miles, i.e., a 49.68% decrease relative to the baseline.

Figure 1 reports the total group travel (summed over the four teams) for each group under the oficial FIFA schedule (orange) and under our MIP solution (blue). The reductions are broad-based: nearly all groups exhibit sizeable improvements, with particularly large drops for Groups A, C, E, G, H, J, K, and L. A few groups show smaller changes (e.g., Group B and Group I). Overall, the figure indicates that the global improvement is not driven by a single outlier group, but rather by consistently shorter inter-round moves across the tournament.

Total group travel: Official (orange) vs MIP (blue  
![](04-Gutierrez-2026_images/192ed20f8cb8fe782d12fe35272e88708f4d91d9011bd1e5b007b4f8c2b21a1f.jpg)  
Fig. 1 Total group-stage travel by group under the oficial FIFA schedule (orange) and our MIP solution (blue). Totals are computed using great-circle distances and the inter-round legs (Round 1  Round 2 and Round 2  Round 3)

Figures 2 and 3 provide a team-by-team breakdown within each group. Several groups exhibit simultaneous reductions for most or all teams (e.g., Groups A, C, D, E, G, H, J, K, and L), suggesting that the optimized assignments can keep the group geographically coherent across rounds. In a small number of cases, one team’s travel can increase even when the group total decreases (e.g., Group F and Group I), which is a natural consequence of global feasibility trade-ofs: the model may accept a localized increase for a single team to unlock larger reductions elsewhere while satisfying the tournament-wide constraints.

## 5.3 Time-zone crossing results

Crossing time zones during a short tournament window can impose meaningful physiological and performance costs on elite soccer players, largely due to circadian misalignment (“jet lag”), disrupted sleep timing, and reduced recovery quality after travel. These efects can be amplified when travel occurs repeatedly with limited rest days between matches, which is a common feature of World Cup group-stage play. Accordingly, beyond total travel distance, an operationally relevant secondary metric is the number of time-zone crossings a team experiences across consecutive rounds, as frequent time-zone changes can hinder recovery routines and consistent match preparation (see, e.g., the broader workload and recovery concerns emphasized in recent FIFPRO monitoring reports [1]).

We partition the set of venues into three time zones—Pacific, Central, and Eastern—and define a time-zone crossing whenever a team plays in diferent time zones in two consecutive rounds (i.e., between Round 1  Round 2 and Round 2 Round 3). Hence, each team contributes an integer in 0, 1, 2 crossings over the group stage, and the tournament-wide total is the sum over all 48 teams.

![](04-Gutierrez-2026_images/2c7b4ffd51ddc091e2661830c8dc4abe7d8a925a3aed849b6d8886c589da6879.jpg)  
(a) Group A

![](04-Gutierrez-2026_images/90a0ac2370f4a80abec0c32aaa60b3279a9b29d374b67bb937d8c1c293e9c09f.jpg)  
(b) Group B

![](04-Gutierrez-2026_images/8f97f49a6db5f17e8969d404bac3d2ae9eccf8ccd3bb90b175ec7da0251a9f64.jpg)  
(c) Group C

![](04-Gutierrez-2026_images/5a5ec79eda725e17b2edb658d3b8ba68236b943d627a25bd835191b7b4baa718.jpg)  
(d) Group D

![](04-Gutierrez-2026_images/7813679f76cb967a7ba1ce521e84ca3ff6da4cd36ec70d6d256f378cda01ebad.jpg)  
(e) Group E

![](04-Gutierrez-2026_images/d4b5105ead280fcaa7962b6483cd3515965db75a67227ea1af0c02f015b5e28f.jpg)  
(f) Group F  
Fig. 2 Team-level group-stage travel (miles) under the oficial FIFA schedule (orange) and our MIP solution (blue), for Groups A–F

Across all teams, the oficial schedule induces a total of 24 time-zone crossings, while our travel-minimizing MIP schedule reduces this total to 4. This corresponds to an 83.33% reduction in time-zone crossings. This improvement is particularly notable because it targets a fatigue-related mechanism (repeated time-zone changes) that is not directly captured by distance alone.

Figures 4 and 5 visualize the induced time-zone transitions using 3 3 transition matrices, where entry (i, j) counts the number of teams that move from time zone i in the earlier round to time zone j in the next round. Diagonal entries (shaded)

![](04-Gutierrez-2026_images/9969f35f1223e40218a99d677f600349221ac43725fd3ada510a94aedb356e40.jpg)  
(a) Group G

![](04-Gutierrez-2026_images/15fd1d79da25bdbaaa44f59e0db465d4973eea134fa6df5bc423cfa020d160ca.jpg)  
(b) Group H

![](04-Gutierrez-2026_images/36f5ce1bbf38343eea209ad01c2770ce5c9b73739da4c17c46ec9a8528b8af12.jpg)  
(c) Group I

![](04-Gutierrez-2026_images/e6241417f7bf4187e1d60b27630db0b0165daf09c55c8807b9644dcb37ebe290.jpg)  
(d) Group J

![](04-Gutierrez-2026_images/cc5601196ac0436c188d5581786119d2597bcb27d9452cba9efa4b3718327928.jpg)  
(e) Group K

![](04-Gutierrez-2026_images/75f139df443c7c03ee81e56c9c3d201633389396c167b25a0eb87d0864a5d15e.jpg)  
(f) Group L  
Fig. 3 Team-level group-stage travel (miles) under the oficial FIFA schedule (orange) and our MIP solution (blue), for Groups G–L

correspond to no time-zone change, while of-diagonal entries represent time-zone crossings.

For Round 1  Round 2 in Fig. 4, the oficial schedule yields 10 crossings (sum of of-diagonal entries), including several Central  Eastern moves as well as movements into the Pacific time zone. In contrast, the MIP schedule reduces Round 1 Round 2 crossings to only 2, with nearly all teams staying within their original time zone between the first two rounds.

A similar pattern holds for Round 2  Round 3 in Fig. 5. The oficial schedule produces 14 crossings, driven primarily by Central  Eastern transitions. Under the MIP schedule, Round 2  Round 3 crossings drop to only 2, again concentrating the mass on the diagonal and keeping teams time-zone-consistent across consecutive rounds.

![](04-Gutierrez-2026_images/6ae08ee62a9b06cddc886b9fcc26e2994388e15ba52d65866378ab5a4f9ad0b8.jpg)  
(a) Oficial schedule (R1 R2).

![](04-Gutierrez-2026_images/a320c0b52f0f7c34a929c01d05abc5d2021cecbfd2db1ce7fed32459c204edee.jpg)  
(b) MIP schedule (R1 R2).

Fig. 4 Time-zone transition matrices from Round 1 to Round 2. Of-diagonal entries count time-zone crossings between rounds, while diagonal entries indicate that teams remain in the same time zone  
![](04-Gutierrez-2026_images/078c953b61da5ae0eae975cee9164e38b701680e47e16a6de8744d8fc3d60c67.jpg)  
(a) Oficial schedule (R2 R3).

![](04-Gutierrez-2026_images/b56d80574181640861befe3df96585b33d1521ce99428d05a4c2b4df42cc28ee.jpg)  
(b) MIP schedule (R2 R3).  
Fig. 5 Time-zone transition matrices from Round 2 to Round 3. Of-diagonal entries count time-zone crossings between rounds, while diagonal entries indicate that teams remain in the same time zone

Overall, these results show that our MIP-based schedule not only reduces travel distance, but also substantially stabilizes teams’ time-zone exposure during the group stage. This provides an additional, practically meaningful mechanism for improving player recovery conditions and potentially mitigating travel-related performance degradation.

## 6 Conclusion and future work

This paper developed a MIP optimization framework for redesigning the 2026 FIFA World Cup group-stage match-to-venue assignment to reduce team travel while respecting the FIFA oficial schedule structure and key operational constraints (including fixed match-day windows, venue workload restrictions, and within-group concurrency requirements in the final round). Computationally, we obtained a feasible schedule with total group-stage travel of 30, 860.7 miles, compared to 61, 324.3 miles under the currently published FIFA baseline, yielding a 49.68% reduction. Importantly, the same assignment also delivers a substantial reduction in cumulative time-zone crossings across teams’ successive group-stage matches (about 83% relative to the baseline), providing an additional workload-related benefit that is induced by distance minimization and directly relates to recovery and circadian disruption concerns. These savings are broadly distributed across groups, and the remaining trade-ofs reflect unavoidable global feasibility constraints, such as host-nation fixings and limited venue-day capacity.

Several extensions could further enhance realism and decision support for megaevents. First, the travel metric can be expanded beyond inter-round legs to incorporate pre-tournament arrivals and transitions into the knockout phase, and to model other notions of burden such as time-zone crossings, recovery time, and routing complexity. In particular, future work could treat time-zone crossings as an explicit optimization criterion in a single- or multi-objective framework alongside distance. Second, fairness objectives can be integrated in a multi-objective formulation. Finally, larger integrated variants motivate incorporating decomposition tools and techniques in MIP.

Funding No funding was received for conducting this study and/or for the preparation of this manuscript.

Code availability Our codes and results are available at: https://github.com/hamidrezavalidi/FIFA\_World \_Cup\_2026. Furthermore, we provide an interactive graphical interface for soccer fans at https://igorlucin do.github.io/ffa-world-cup-2026-scheduler-APP/.

## Declarations

Conflict of interest The authors declare that they have no conflict of interest.

Ethical approval This article does not contain any studies with human participants or animals performed by any of the authors.

Consent for publication Not applicable.

Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licen

ses/by/4.0/.

## References

1. FIFPRO: Overworked and Underprotected: The Player Health and Performance Impact. Men’s Player Workload Monitoring (PWM) annual report (PDF) (2025)

2. FIFA: Match schedule, fixtures & stadiums: FIFA World Cup 2026. https://www.ffa.com/en/tourn aments/mens/worldcup/canadamexicousa2026/articles/match-schedule-fxtures-results-teams-stadiu ms. Accessed: 2025-12-04 (2025)

3. Lee, A., Galvez, J.C.: Jet lag in athletes. Sports Health 4(3), 211–216 (2012). https://doi.org/10.1177 /1941738112442340

4. Leatherwood, W.E., Dragoo, J.L.: Efect of airline travel on performance: a review of the literature. Br. J. Sports Med. 47(9), 561–567 (2013). https://doi.org/10.1136/bjsports-2012-091449

5. Rensburg, D.C., et al.: Managing travel fatigue and jet lag in athletes: a review and consensus statement. Sports Med. 51(10), 2029–2050 (2021). https://doi.org/10.1007/s40279-021-01502-0

6. Song, A., Severini, T., Allada, R.: How jet lag impairs major league baseball performance. Proc. Natl. Acad. Sci. 114(6), 1407–1412 (2017). https://doi.org/10.1073/pnas.1608847114

7. Werra, D.: Scheduling in sports. In: Hansen, P. (ed.) Studies on Graphs and Discrete Programming. Annals of Discrete Mathematics, vol. 11, pp. 381–395. North-Holland, Amsterdam (1981)

8. Kendall, G., Knust, S., Ribeiro, C.C., Urrutia, S.: Scheduling in sports: an annotated bibliography. Comput. Operat. Res. 37(1), 1–19 (2010)

9. Rasmussen, R.V., Trick, M.A.: Round robin scheduling - a survey. Eur. J. Oper. Res. 188(3), 617–636 (2008)

10. Easton, K., Nemhauser, G., Trick, M.: The traveling tournament problem: Description and benchmarks. In: Principles and Practice of Constraint Programming (CP 2001). Lecture Notes in Computer Science, vol. 2239, pp. 580–584. Springer, Berlin and Heidelberg (2001)

11. Goossens, D., Spieksma, F.C.R.: Scheduling the Belgian soccer league. Interfaces 39(2), 109–118 (2009)

12. Ribeiro, C.C.: Sports scheduling: Problems and applications. Int. Trans. Oper. Res. 19(1–2), 201–226 (2012). https://doi.org/10.1111/j.1475-3995.2011.00819.x

13. Easton,K., Nemhauser, G., Trick, M.A.: Solving the travelling tournament problem: A combined integer programming and constraint programming approach. In: Burke, E., De Causmaecker, P. (eds.) Practice and Theory of Automated Timetabling IV (PATAT 2002). Lecture Notes in Computer Science, vol. 2740, pp. 100–109. Springer, Berlin and Heidelberg (2003). https://doi.org/10.1007/978- -540-45157-0\_6

14. Irnich, S.: A new branch-and-price algorithm for the traveling tournament problem. Eur. J. Oper. Res. 204(2), 218–228 (2010). https://doi.org/10.1016/j.ejor.2009.10.024

15. Thielen, C., Westphal, S.: The complexity of the traveling tournament problem. Theoret. Comput. Sci. 412(4–5), 345–351 (2011). https://doi.org/10.1016/j.tcs.2010.10.00

16. Bhattacharyya, R.: A note on the complexity of the traveling tournament problem, (2009). (Preprint)

17. Anagnostopoulos, A., Michel, L., Van Hentenryck, P., Vergados, Y.: A simulated annealing approach to the traveling tournament problem. In: Proceedings of the 18th International Joint Conference on Artificial Intelligence (IJCAI 2003), pp. 1357–1358. Poster Session (2003)

18. Goerigk, M., Westphal, S.: A combined local search and integer programming approach to the traveling tournament problem. Ann. Oper. Res. 239(1), 343–354 (2016). https://doi.org/10.1007/s10479-0 14-1586-6

19. Devriesere, N., Csató, L., Goossens, D.: Tournament design: A review from an operational research perspective. Eur. J. Oper. Res. 324(1), 1–21 (2025). https://doi.org/10.1016/j.ejor.2024.10.044

20. Rensburg, D.C.C., et al.: How to manage travel fatigue and jet lag in athletes? A systematic review of interventions. Br. J. Sports Med. 54(16), 960–968 (2020). https://doi.org/10.1136/bjsports-2019-101 635

21. Huyghe, T., Scanlan, A.T., Dalbo, V.J., Calleja-González, J.: The negative influence of air travel on health and performance in the national basketball association: A narrative review. Sports (Basel) 6(3), 89 (2018). https://doi.org/10.3390/sports6030089

22. Roy, J., Forest, G.: Greater circadian disadvantage during evening games for the national basketball association (NBA), national hockey league (NHL) and national football league (NFL) teams travel ling westward. J. Sleep Res. 27(1), 86–89 (2018). https://doi.org/10.1111/jsr.12565

23. McHill, A.W., Chinoy, E.D.: Utilizing the national basketball association’s COVID-19 restart ”bubble” to uncover the impact of travel and circadian disruption on athletic performance. Sci. Rep. 10(1), 21827 (2020). https://doi.org/10.1038/s41598-020-78901-2

24. Leota, J.: Eastward jet lag is associated with impaired performance and game outcome in the national basketball association. Front. Physiol. 13, 892681 (2022). https://doi.org/10.3389/fphys.2022.892681

25. Goossens, D., Spieksma, F.C.R.: Soccer schedules in Europe: An overview. J. Sched. 15(5), 641–651 (2012). https://doi.org/10.1007/s10951-011-0238-9

26. Bartsch, T., Drexl, A., Kröger, S.: Scheduling the professional soccer leagues of Austria and Ger many. Comput. Operat. Res. 33(7), 1907–1937 (2006). https://doi.org/10.1016/j.cor.2004.09.037

27. Trick, M.A., Yildiz, H., Yunes, T.: Scheduling major league baseball umpires and the traveling umpire problem. Interfaces 42(3), 232–244 (2012)

28. Bonomo, F., Cardemil, A., Durán, G., Marenco, J., Sabán, H.: Scheduling the Argentine volleyball league. Interfaces 42(3), 245–259 (2012). https://doi.org/10.1287/inte.1110.0587

29. Wikipedia contributors: Great-circle distance. https://en.wikipedia.org/wiki/Great-circle\_distance Accessed: 2025-12-06 (2025)

30. Sinnott, R.W.: Virtues of the haversine. Sky Telescope 68, 158 (1984)

31. Wikipedia contributors: Haversine formula. https://en.wikipedia.org/wiki/Haversine\_formula Accessed: 2025-12-04 (2025)

32. Margot, F.: Symmetry in integer linear programming. In: Jünger, M., Liebling, T.M., Naddef, D., Nemhauser, G.L., Pulleyblank, W.R., Reinelt, G., Rinaldi, G., Wolsey, L.A. (eds.) 50 Years of Integer Programming 1958–2008, pp. 647–686. Springer, Berlin and Heidelberg (2010). https://doi.org/10.1 007/978-3-540-68279-0\_17

33. Margot, F.: Exploiting orbits in symmetric ILP. Math. Program. 98(1–3), 3–21 (2003). https://doi.or g/10.1007/s10107-003-0394-6

34. Crawford, J.M., Ginsberg, M.L., Luks, E.M., Roy, A.: Symmetry-breaking predicates for search problems. In: Proceedings of the Fifth International Conference on Principles of Knowledge Repre sentation and Reasoning (KR’96), pp. 148–159. Morgan Kaufmann, San Francisco, CA (1996)

35. Gent, I.P., Smith, B.M.: Symmetry breaking in constraint programming. In: Proceedings of the 14th European Conference on Artificial Intelligence (ECAI 2000), pp. 599–603. IOS Press, Amsterdam, The Netherlands (2000)

36. Carlsson, M., Johansson, M., Larson, J.: Scheduling double round-robin tournaments with divisional play using constraint programming. Eur. J. Oper. Res. 259(3), 1180–1190 (2017). https://doi.org/10. 1016/j.ejor.2016.11.033

Publisher's Note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional afiliations.