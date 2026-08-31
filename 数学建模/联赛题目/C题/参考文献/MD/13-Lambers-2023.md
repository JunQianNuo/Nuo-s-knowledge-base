---
raw_title: 13-Lambers-2023
subject: 数学建模-策联杯C题
source: "jsa_2023_9-2_jsa-9-2-jsa220626_jsa-9-jsa220626.pdf"
status: mineru解析
parser: mineru
topics:
  - 排球国家联赛
  - 整数规划
  - 旅行公平
  - 赛程分解
---

# How to schedule the Volleyball Nations League

Citation for published version (APA): Lambers, R., Rothuizen, L., & Spieksma, F. C. R. (2023). How to schedule the Volleyball Nations League. , (2), 157-169. https://doi.org/10.3233/JSA-220626

Document license: CC BY-NC

DOI: 10.3233/JSA-220626

Document status and date: Published: 01/01/2023

## Document Version:

Publisher’s PDF, also known as Version of Record (includes final page, issue and volume numbers)

Please check the document version of this publication:

• A submitted manuscript is the version of the article upon submission and before peer-review. There can be important differences between the submitted version and the official published version of record. People interested in the research are advised to contact the author for the final version of the publication, or visit the DOI to the publisher's website.

• The final author version and the galley proof are versions of the publication after peer review.

• The final published version features the final layout of the paper including the volume, issue and page numbers.

Link to publication

## General rights

Copyright and moral rights for the publications made accessible in the public portal are retained by the authors and/or other copyright owners and it is a condition of accessing publications that users recognise and abide by the legal requirements associated with these rights.

• Users may download and print one copy of any publication from the public portal for the purpose of private study or research.

• You may not further distribute the material or use it for any profit-making activity or commercial gain

• You may freely distribute the URL identifying the publication in the public portal.

If the publication is distributed under the terms of Article 25fa of the Dutch Copyright Act, indicated by the “Taverne” license above, please follow below link for the End User Agreement:

www.tue.nl/taverne

## Take down policy

If you believe that this document breaches copyright please contact us at:

openaccess@tue.nl

providing details and we will investigate your claim.

# How to schedule the Volleyball Nations League

Roel Lambers<sup>∗</sup>, Laurent Rothuizen and Frits C.R. Spieksma

Department ofMathematics & Computer Science, Eindhoven University ofTechnology, Eindhoven, The Netherlands

Received 2 February 2022

Accepted 2 October 2022

Pre-press 12 June 2023

Published 3 July 2023

Abstract. The Volleyball Nations League is the elite annual international competition within volleyball, with the sixteen best nations per gender contesting the trophy in a tournament that spans over 6 weeks. The first five weeks contain a single round robin tournament, where matches are played in different venues across the globe. As a consequence, each team follows an intensive travel plan, where it happens quite often that there is a large discrepancy between travel burdens of opposing teams. This is considered a disadvantage for the team that travelled more. We analyse this problem, and find that it is closely related to the well-known Social Golfer Problem: we name the resulting problem the Traveling Social Golfer Problem (TSGP). We propose a decomposition approach for the TSGP, leading to the so-called Venue Assignment Problem and the Nation Assignment Problem. We prove that a solution to the Venue Assignment problem determines the amount of unfairness, and we also prove that any solution of the Venue Assignment problem can be extended to a solution to the Nation Assignment problem satisfying the so-called home-venue property. Using integer programming methods, we find, for real-life instances, the fairest schedules with respect to the difference in travel distance.

Keywords: Social golfer problem, integer programming, volleyball nations league, OR in sports

## Prologue

It is the beginning of June 2018 when the Italian men volleyball team go undefeated in the first round of the inaugural Volleyball Nations League. They played their three first-round matches in Kraljevo, Serbia, and for the next round of three matches they have to travel, via Belgrade, Rome, Buenos Aires, to reach the next venue in San Juan, Argentina, after more than 24 hours of traveling. Playing only a few days after this trip, their momentum seems lost and they lose two out of their three games, all played within a week, upon which they immediately need to fly to Japan for the third round.

Ultimately, the Italian team had to travel literally across the globe within a time span of four weeks, playing matches against the best volleyball teams in the world. Even though they started off with three victories, they ended eighth and did not qualify for the final stages. In comparison, the French team played all their matches within Europe and emerged as winner of the main event. Later that year however, during the World Championship, the Italian team outperformed the French team.

## 1. Introduction

The above example is just one of many that highlights how travel times, and specifically disparity in travel times, influence results in the Volleyball Nations League (VNL). It is well established within the scientific literature that extensive travelling has a negative impact on sport performance. Although we do not intend to survey the literature on this subject, this finding is reported for various sports ranging from rugby (Lo et al. (2020)) to baseball (Song et al. (2017), and Winter et al. (2009)) and from basketball (Huyghe et al. (2018)) to triathletes (Stevens et al. (2018)); see also the references contained in these papers. We close this paragraph by two quotes: one from an interview with Anne Buijs, professional volleyball player(see Volkskrant (2021)): “It is quite an advantage to play all VNL matches at the same location. In the original schedule we would have travelled from Serbia to Canada to Korea, which makes the schedule very hard for us.”, and one from Samuels (2012) who concludes: “Jet lag and travel fatigue are considered by high-performance athletic support teams to be a substantial source of disturbance to athletes.” This phenomenon is illustrated in the prologue of this paper, and serves as its motivation.

The Volleyball Nations League is a tournament organized every year by the FIVB (Fed´ eration Inter-´ nationale de Volleyball), for both men and women (see https://www.volleyball.world/en/vnl/2021). This tournament was first organized in 2018 to replace the World League/World Grand Prix as annual volleyball tournament. There are 16 teams participating in the tournament which consists of multiple phases. In the first phase, lasting for five weeks, all 16 teams play a single round robin, i.e., each team meets each other team once. The best 6 teams then qualify for the second phase, where out of two groups of three, four teams emerge to play cross finals. Our interest is exclusively on the first phase.

In the first phase of the VNL tournament, teams play in rounds. In each round, each team is in a group consisting of4 teams, and each team in a group plays a match against its three fellow group members. After 5 rounds, each of the 16 teams has played all the other teams exactly once, and a ranking is made based on the results in this single round robin tournament. All 6 matches in a single group are held at the same venue, however, every round has its 4 groups played out in different venues. As it is a disadvantage to have traveled more than your opponent going into a match, our main interest lies in minimizing a measure that captures the imbalance in travel times between opposing teams.

A priori, it is not clear how a round robin schedule that can be decomposed in groups is obtained. In fact, finding a schedule that fits this VNL-format is related to the so-called Social Golfer Problem (SGP). In this problem we are given gp golfers and w rounds (where g, p, w are positive integers), and the SGP-question is whether it is possible to let the gp golfers play in g groups of p golfers in each of the w rounds, in such a way that every pair of golfers plays in the same group in at most one round, see Triska & Musliu (2012), Liu et al. (2019), Dotu & van Hentenryck (2005). This question is far´ from innocent: only for restricted sets of values for $g , p ,$ w the answer to this question is known. For instance, when $g = p = w - 1$ , solutions are known to exist when g is a prime power - and no other solution to these type of instances has been found, nor has it been proven that these are the only instances for which a solution can exist (Harvey & Winterer (2005)).

Of course, in the context of the Volleyball Nations League, each golfer corresponds to a team (and groups remain groups and rounds remain rounds). Since the Volleyball Nations League has $g = p = 4$ and $w = 5$ , it follows that the answer to the SGPquestion is affirmative, and hence a schedule for the VNL that consists of 5 rounds, each round consisting of 4 groups, is known to exist. In this paper, we introduce the Traveling Social Golfer Problem (TSGP), as a generalization of the SGP; the TSGP allows us to take fairness, as measured by the difference in travel times between opposing teams, into account. Recent other variations of the SGP are discussed in Miller et al. (2021) and Lester (2021).

A well-known problem related to the TSGP that also focusses on distances is the Travelling Tournament Problem (TTP), see Easton et al. (2003) for a precise description. In contrast to our problem, in the TTP pairs of teams meet in the venue of one of the two opposing teams. Moreover, the objective in the TTP is to minimize total travel distance; difference in travel time between opposing teams is not considered in the TTP. We refer to Goerigk & Westphal (2016) and Duran et al. (2019) for an overview concerning´ the TTP.

A number of studies has been devoted to the scheduling of national volleyball leagues where mainly for cost reasons, the objective is to minimize total travel time. We mention Bonomo et al. (2012) who model the Argentine national volleyball league as an instance of the Traveling Tournament Problem, and Cocchi et al. (2018) who investigate the Italian volleyball league. Further, Raknes & Pettersen (2018) study the Norwegian Volleyball League; one of their models, motivated by a cost-objective, is devoted to minimizing total travel distance in that league. These leagues are organized in the format of a Double Round Robin, and as such differ from the VNL.

## 2. The Traveling Social Golfer Problem (TSGP)

## 2.1. Definition ofthe TSGP

As described in Section 1, the Social Golfer Problem is a well known combinatorial question, where the task is to schedule golfers in groups of size p over multiple rounds, such that no golfer plays with another golfer in the same group twice. In the Traveling Social Golfer Problem (TSGP), all groups have to play at (different) venues, where the objective is to create a schedule that minimizes the unfairness arising from golfers having different travel times between the venues.

In order to give a precise formulation of the TSGP, we use the following notation to describe the input:

• N: the number of teams,

• k: a group size,

$V { : }$ the set of venues,

$d ( v , w ) \colon$ a distance between each pair of venues $v , w \in V ,$ , and

$c _ { v } .$ a multiplicity for each $v \in V .$

The multiplicities $c _ { v }$ indicate the exact number of times venue $v \in V$ must host a group; indeed, in the practical situation of the VNL, it is not uncommon that a venue is host to different groups in different rounds. The multiplicities allow us to accommodate such situations.

Furthermore, we use the following notation to describe a solution:

• R: a set of rounds,

• $P _ { i } ^ { r }$ : the set of teams in group i in round $r , 1 \leq$ $\begin{array} { r } { i \le \frac { N } { k } , r \in R , } \end{array}$

$v _ { r } ( t ) \colon$ the venue of the group in which team $t \in$ $\{ 1 , \ldots , N \}$ plays in round $r \in R .$

Finally, we measure the value of a schedule S by its unfairness $u ( S )$ as follows:

$$
\begin{array}{l} u (S) = \sum_ {r \in R \backslash \{1 \}} \sum_ {i = 1} ^ {\frac {N}{k}} \\ \max _ {s, t \in P _ {i} ^ {r}} | d (v _ {r} (s), v _ {r - 1} (s)) - d (v _ {r} (t), v _ {r - 1} (t)) |. \end{array}\tag{1}
$$

Let us elaborate on this expression. For every group $P _ { i } ^ { r }$ in every round $r \in R \setminus \{ 1 \}$ , we consider the two teams (teams s and t) whose difference in travel distance needed to arrive at the corresponding venue, is maximum over all pairs of teams in the group; this quantity is summed over all groups, and all rounds (except the first round, as we assume that all teams have ample time to arrive at their first venue). Thus, a lower value of $u ( S )$ indicates that the difference in travel times between opposing teams was less and thus the schedule was more fair. The measure u is applicable to any schedule for N teams that has a group/round-structure.

Example 2.1. A tournament with $N = 4 .$ , teams 1, 2, 3, 4, is organized over three rounds, and groups of size $k = 2 ,$ . There are four venues, $V = \{ A , B , C , D \}$ , with multiplicities $c _ { A } = c _ { D } = 2$ and $c _ { B } = c _ { C } = 1$ . Distances between venues are $d ( A , B ) = d ( A , C ) = d ( B , D ) = d ( C , D ) = 1$ and $d ( A , D ) = d ( B , C ) = 2 .$

Consider the schedule S depicted in Table 1.

Thus, according to (1), the unfairness of this schedule S equals:

$$
u (S) = | 2 - 0 | + | 1 - 1 | + | 2 - 1 | + | 2 - 1 | = 4.
$$

We state the following optimization problem that we call the (N, k)-Traveling Social Golfer Problem, or $( N , k ) – \mathrm { T S G P }$ for short.

## Problem 2.1. (N, k)-TSGP

Input. A number ofteams $N \in \mathbb { N } ,$ , a group size $k \in \mathbb { N } .$ a set of venues V each with multiplicity $c _ { v } \ ( v \in V )$ and a distance function d $: V \times V \to \mathbb { R }$

Output. A schedule S consisting of |R| rounds minimizing u(S) such that:

• there is an equi-partitioning of N teams in groups $P _ { 1 } ^ { r } , \dots P _ { \frac { N } { \nu } } ^ { r }$ for each round $r \in R ,$ with for each pair of distinct teams, a single group containing both teams, i.e, for each $s , t ,$ $( s \neq t ) ) \exists !$ i, r with $s , t \in P _ { i } ^ { r }$

• an allocation of groups to venues that results in venues $v _ { r } ( t ) ( r \in R , t = 1 , \ldots , N )$ such that venue $v \in V$ acts $c _ { v }$ times as a host for a group.

It is clear that, depending on the input, a feasible schedule to (N, k)-TSGP need not exist; in fact, it is not difficult to find instances where there is no schedule S that satisfies all the constraints. Indeed, as the schedule asks for a partitioning of the N teams in groups of size k in each round, we immediately see that N should be a multiple of k, or $N \equiv _ { k } 0$ . In addition, as the schedule should correspond to a single round robin tournament, and as all teams play $k - 1$ matches per round, we conclude that $N - 1$ should be a multiple of $k - 1$ , or $( N - 1 ) \equiv _ { k - 1 } 0$ . Thus, a solution of the (N, k)-TSGP can only exist if there is an integral ρ such that $N = k \cdot ( ( k - 1 ) \rho + 1 )$ .

Table 1  
A schedule S for the instance in Example 2.1

<table><tr><td></td><td>group</td><td>venue</td><td>group</td><td>venue</td></tr><tr><td>round 1</td><td> $P_{1}^{1} = \{1, 2\}$ </td><td>A</td><td> $P_{2}^{1} = \{3, 4\}$ </td><td>D</td></tr><tr><td>round 2</td><td> $P_{1}^{2} = \{1, 3\}$ </td><td>A</td><td> $P_{2}^{2} = \{2, 4\}$ </td><td>B</td></tr><tr><td>round 3</td><td> $P_{1}^{3} = \{1, 4\}$ </td><td>D</td><td> $P_{2}^{3} = \{2, 3\}$ </td><td>C</td></tr></table>

The above are necessary conditions that need to be satisfied. In fact, the (N, k)-TSGP can only have a solution that satisfies the single round robin format, if the corresponding instance of the SGP is solvable. In general, solutions of the SGP are known to exist when $N = k ^ { 2 }$ and k is a prime power. Thus, for the Volleyball Nations League, the underlying $N = 1 6 , k = 4 { \cdot } \mathrm { S G P }$ problem will be solvable. In the remainder of the paper, we assume that $N = k ^ { 2 }$ and $| R | = k + 1$ ; this ensures that the above necessary conditions are fulfilled (and observe that the VNL case arises when $k = 4 )$ .

## 2.2. Decomposing the TSGP into Venue Assignment and Nation Assignment

The problem of solving an instance of $( N =$ $k ^ { 2 } , k ) { } - { T S G P }$ can be decomposed into two phases:

• Venue Assignment. In the first phase, we specify, for each round $r \in R .$ , which venues act as a host. Let $U _ { r } \subset V$ , with $| U _ { r } | = k , ~ r =$ $1 , \ldots , k + 1$ be the set of venues that act as hosts in round r.

• Nation Assignment. In the second phase, we decide upon the composition of the groups, i.e., we choose the sets $P _ { i } ^ { r }$ and allocate these groups to the venues in $U _ { r } , r = 1 , \ldots , k + 1$

By going through these two phases, we find a schedule S. It is crucial to observe that the unfairness of $S ,$ $\mathrm { i } . \mathrm { e } . , u ( S )$ , follows directly from the venue assignment when $N = k ^ { 2 }$ . We record this observation formally.

Theorem 2.1. For each schedule S ofa given instance 0 $\begin{array} { r } { \jmath f ( N = k ^ { 2 } , k ) - T S G P , } \end{array}$ , u(S) is determined only by the Venue Assignment,for each integer $k \geq 2 .$

Proof. We claim that for each schedule S:

$$
\begin{array}{l} u (S) = \sum_ {r \in R \backslash \{1 \}} \sum_ {i = 1} ^ {k} \max _ {s, t \in P _ {i} ^ {r}} | d (v _ {r} (s), v _ {r - 1} (s)) - d (v _ {r} (t), v _ {r - 1} (t)) | \\ = \sum_ {r \in [ 1, \dots , k ]} \sum_ {u \in U _ {r + 1}} \max _ {v, w \in U _ {r}} | d (v, u) - d (w, u) |. \end{array}
$$

The latter equality follows from the fact that, independent of the composition of the groups, the k teams that play in a group in some round, will not meet again in a next round, and hence these k teams will travel to each of the k distinct venues in the next round. -

Theorem 2.1 allows us to compute the unfairness of a schedule $S , u ( S )$ , without specifying the schedule S. As a consequence, it becomes much easier in practice to find schedules for which $u ( S )$ is minimum. Or, rephrasing Theorem 2.1, finding a Venue Assignment suffices to know the unfairness of any schedule compatible with the Venue Assignment. In fact, a similar statement can be made with respect to the total travel time (see Section 5).

## 3. The complexity of Venue Assignment

In this section, we formally establish the complexity of Venue Assignment. Given that feasible schedules to the $( N = k ^ { 2 } , k ) – \mathrm { T S G P }$ exist, Theorem 2.1 implies that our task of finding an optimal solution to $( N , k )$ -TSGP is reduced to finding an optimal venue assignment. Clearly, this is related to the differences in traveled distance between two opposing teams, which in turn follows from the venues that are selected in each round.

In an extreme case, if only a single venue v is given (with multiplicity $c _ { v } = k ( k + 1 ) )$ ), then all matches in all groups in all rounds are played in the same venue, and there is no travel distance. However, in general, the set of venues V and their pairwise distances, are instrumental in finding good venue assignments. Of course, we assume that $\textstyle \sum _ { v \in V } c _ { v } = k ( k + 1 )$ ). We now give a formal description.

## Problem 3.1. Venue Assignment (VA)

Input. A value $k \in \mathbb { N } ,$ , a set of venues V, an integral multiplicity $c _ { v }$ for $v \in V$ , and a distance matrix $d ( v , w )$ for each $v , w \in V .$

Output. For $r \in \{ 1 , \ldots , k + 1 \}$ , subsets $U _ { r } \subset V$ with $| U _ { r } | = k$ , such that $\forall v \in V , c _ { v } = | \{ r : v \in U _ { r } \} |$ | that

minimizes:

$$
\Delta = \sum_ {r \in \{1, \dots , k \}} \sum_ {u \in U _ {r + 1}} \max _ {v, w \in U _ {r}} | d (v, u) - d (w, u) |.\tag{2}
$$

To establish the hardness of Venue Assignment, we use the following decision problem.

Problem 3.2. Longest Hamiltonian Path on a Complete Graph (LHP)

Input. A complete graph $G = ( H , E ) , | H | = n$ with nonnegative, symmetric weights $w ( h _ { 1 } , h _ { 2 } )$ for each $h _ { 1 } , h _ { 2 } \in H$ , and an integer B.

Question. Does there exist a Hamiltonian Path $( h _ { i _ { 1 } } , \ldots , h _ { i _ { n } } )$ in G such that $\begin{array} { r } { \sum _ { j = 1 } ^ { n - 1 } w ( h _ { i _ { j } } , h _ { i _ { j + 1 } } ) \geq } \end{array}$ $B ?$

LHP is well-known to be NP-complete.

## Theorem 3.1. Venue-Assignment is NP-Hard.

Proof. We prove this statement by a reduction from Longest Hamiltonian Path on a Complete Graph.

Given an instance of LHP, with vertex set $H = \{ h _ { 1 } , \ldots , h _ { n } \}$ and weights w : $H \times H \to \mathbb { R }$ , we construct an instance of the decision problem corresponding to VA, using a parameter K, in the following way.

We choose $k : = n - 1$ . Further, the set of venues V consists of $V = V _ { 1 } \cup V _ { 2 }$ , where $V _ { 1 } : = H$ and $| V _ { 2 } | : =$ $n - 2$ . For each $v \in V _ { 1 } , c _ { v } : = 1$ and for each $v \in V _ { 2 }$ $c _ { v } : = n$ . Let $D = \operatorname* { m a x } _ { h _ { 1 } , h _ { 2 } \in H }$ w(h , h ) and define a symmetric distance function d in the following way:

$$
d (u, v) := \left\{ \begin{array}{c c} w (u, v) & u, v \in V _ {1} \\ 2 D & u \in V _ {1}, v \in V _ {2} \\ 0 & u, v \in V _ {2}. \end{array} \right.\tag{3}
$$

Notice that the resulting distances satisfy the triangle inequality when the instance of LHP does. Finally, we set $K : = k ^ { 2 } \cdot 2 D - B .$ , and ask whether there exists a venue assignment with unfairness at most K. We have now specified an instance of the decision version of VA.

Let us argue that if there exists a solution to VA with unfairness at most K, LHP is a yes-instance, and vice versa.

To find a solution to any instance of VA, we need to find $U _ { r } \subset V$ for each $r \in \{ 1 , \ldots , k + 1 \}$ such that $\forall v \in V , c _ { v } = | \{ r : v \in U _ { r } \} |$ . As we know that for all $v \in V _ { 2 } , c _ { v } = k + 1$ , we see that any feasible solution must have $V _ { 2 } \subset U _ { r }$ for each round r. Moreover, as ${ c _ { v } = 1 }$ for $v \in V _ { 1 }$ , we get that any feasible solution must schedule every venue $v \in V _ { 1 }$ exactly once.

Thus, any feasible solution to VA consists of $U _ { r } =$ $V _ { 2 } \cup v _ { i _ { r } }$ with $v _ { i _ { r } } \in V _ { 1 }$ and $v _ { i _ { r } } = v _ { i _ { r } ^ { \prime } } \Longleftrightarrow r = r ^ { \prime }$ . In other words, any feasible solution to $\mathrm { V A }$ corresponds to an ordering $( v _ { i _ { 1 } } , \ldots , v _ { i _ { k + 1 } } )$ of the venues in $V _ { 1 }$ Given such an ordering, we obtain the following expression for the unfairness of a schedule S that uses the ordering $( v _ { i _ { 1 } } , \ldots , v _ { i _ { k + 1 } } )$

$$
u (S) = \sum_ {r = 1} ^ {k} \left((k - 1) \cdot 2 D + (2 D - d (v _ {i _ {r}}, v _ {i _ {r + 1}})).\right)\tag{4}
$$

The first term in the summation results from the fact that there are $k - 1$ venues from $V _ { 2 }$ in every round and one from $V _ { 1 }$ , and since $d ( v , w ) - d ( v , v ^ { \prime } ) = 2 D - 0$ for all v, $v ^ { \prime } \in V _ { 2 } , w \in V _ { 1 }$ , we get k − 1 venues where the maximal travel difference is 2D. The second term equals the difference in travel distance between the teams traveling from any of the $v \in V _ { 2 }$ to the $v _ { i _ { r + 1 } } \in$ $V _ { 1 }$ , and the team traveling from $v _ { i _ { r } } \in V _ { 1 }$

Let us now suppose that the instance of LHP is a yes-instance, implying the existence ofa Hamiltonian Path such that $\begin{array} { r } { \dot { \sum _ { j = 1 } ^ { n - 1 } d } ( h _ { i _ { j } } , h _ { i _ { j + 1 } } ) \ge B } \end{array}$ . We choose as the ordering of venues in V the sequence of nodes in this Hamiltonian path. We find:

$$
u (S) = \sum_ {r = 1} ^ {k} \left((k - 1) \cdot 2 D + (2 D - d (v _ {i _ {r}}, v _ {i _ {r + 1}}))\right)\tag{5}
$$

$$
= k ^ {2} \cdot 2 D - \sum_ {r = 1} ^ {k} d (v _ {i _ {r}}, v _ {i _ {r + 1}})\tag{6}
$$

$$
= k ^ {2} \cdot 2 D - \sum_ {j = 1} ^ {n - 1} w (h _ {i _ {j}}, v _ {i _ {j + 1}})\tag{7}
$$

$$
\leq k ^ {2} \cdot 2 D - B = K.\tag{8}
$$

Hence, the unfairness of this schedule S is bounded by $K .$

Finally, suppose there exists a schedule S whose unfairness is bounded by K, we obtain:

$$
u (S) = k ^ {2} \cdot 2 D - \sum_ {r = 1} ^ {k} d (v _ {i _ {r}}, v _ {i _ {r + 1}}) \leq K,
$$

which is equivalent to

(9)

$$
\sum_ {j = 1} ^ {n - 1} w (h _ {i _ {j}}, v _ {i _ {j + 1}}) \geq k ^ {2} \cdot 2 D - K = B.\tag{10}
$$

Thus, solving this instance of the decision version of VA is equivalent to solving the corresponding instance of LHP, which implies that VA is NP-Hard. -

## 4. The VNL in practice: about the home-venue-property

Motivated by the current practice in the VNL, we incorporate the following issue in our problem formulation: each venue has a team that considers this venue as its home-venue. Next, in any feasible schedule for the VNL it must be the case that when a venue is hosting a group, the group must contain the team for which this venue is the home-venue. And in case there are multiple venues that are the home-venue of the same team, it is a fact that those venues are never a host of a group in the same round. Thus, each venue is a home venue to a single team; however, a team can have multiple home venues. In the context of the VNL, this property specifies that each venue always hosts a group that contains the national team; this team can be regarded as the home playing team, or host nation. As an aside, it is interesting to note here that Alexandros et al. (2012) find the presence of (a significant) home advantage in volleyball matches played in Italian and Greek national leagues.

We will refer to solutions having the property that the venue hosting a group is the home-venue for some member of the group, as the home-venue property. A relevant question now becomes:

Do feasible schedules satisfying the home-venue property exist?

In fact, solving the Venue Assignment problem does not automatically lead to a schedule that satisfies the home-venue property. In other words, it is not true that, when given an assignment of venues to rounds, a schedule is guaranteed to exist such that every venue is a home venue. Then, in such a case, a venue hosts a group of teams, none of which plays home. Example 4.1 shows how a feasible solution of the Venue-Assignment problem cannot be extended to a solution having the home-venue property.

Example 4.1. Let $N = 4$ be the number of teams with group size $k = 2$ , and let V be the set of home venues. All countries t have a venue $v _ { t } \in V .$ , where for countries $t = 1 , 2$ , their venue has a multiplicity of 2 and the other venues have a multiplicity of 1, i.e., $c _ { v _ { 1 } } = c _ { v _ { 2 } } = 2$ and $c _ { v _ { 3 } } = c _ { v _ { 4 } } = 1$ . Solving the corresponding instance of Venue-Assignment can result in a solution as is given in Table 2.

Table 2  
A venue-assignment that does not satisfy the home-venue property

<table><tr><td>Group</td><td>Round 1</td><td>Round 2</td><td>Round 3</td></tr><tr><td>1</td><td> $v_1$ </td><td> $v_1$ </td><td> $v_3$ </td></tr><tr><td>2</td><td> $v_2$ </td><td> $v_2$ </td><td> $v_4$ </td></tr></table>

The venue assignment in Table 2 clearly satisfies the given multiplicities. However, it is impossible to schedule match $( t _ { 1 } , t _ { 2 } )$ in any round when restricting teams to play at their home venue whenever it is scheduled in a round. Moreover, venue assignments satisfying the given multiplicities yielding a feasible schedule do exist for the given example.

Thus, we see that solving the Venue-Assignment alone is not necessarily the same as solving the VNLproblem in practice.

However, and perhaps surprisingly, the following theorem shows that for the particular dimensions of the VNL $( N = 1 6 , k = 4 )$ , a Venue-Assignment can always be extended to a solution for the Volleyball Nations League.

Theorem 4.1. Let $N = 1 6$ be the number of teams and $k = 4$ the group size. Let V be the set ofvenues, with corresponding multiplicities $c _ { v } ( v \in V )$ such that each team has at least one home venue, and all venues need to be scheduled at least once (never with two venues ofthe same team hosting simultaneously), i.e., $c _ { v } \geq 1$ for each $v \in V ,$ , and $\sum { } _ { v \in V } c _ { v } = 2 0$ . Then any solution of the corresponding Venue-Assignment instance, can be extended to afeasible solution ofthe VNL-instance satisfying the home-venue property.

Proof. We organize the proof as follows. First, we specify the groups (called our ‘blueprint’). Second, we provide a partial designation of home venues. Then we consider the possibilities that exist for the vector $c _ { v } ,$ and for each of these possibilities, we consider the set of distributions over the rounds. Finally, we outline how, for each of these distributions, we can arrive at a solution that satisfies the home-venue property.

Consider Table 3, where column $\ " \boldsymbol { R } _ { i } \ " $ stands for Round $i , i = 1 , \dots , 5$ , and where each number from $\{ 1 , \ldots , 1 6 \}$ stands for a team. We refer to this composition of groups as a ‘blueprint’, and we will argue that, for any possible set of multiplicities, and for any distribution of these multiplicities over the rounds, this blueprint can be turned into a venue assignment satisfying the home-venue property, and hence into a nation assignment.

Table 3  
Blueprint that specifies the composition of the groups

<table><tr><td> $R_1$ </td><td> $R_2$ </td><td> $R_3$ </td><td> $R_4$ </td><td> $R_5$ </td></tr><tr><td>1, 5, 9, 13</td><td>1, 6, 11, 16</td><td>1, 4, 10, 15</td><td>1, 3, 12, 14</td><td>1, 2, 7, 8</td></tr><tr><td>2, 6, 10, 14</td><td>2, 5, 12, 15</td><td>2, 3, 13, 16</td><td>2, 4, 9, 11</td><td>3, 4, 5, 6</td></tr><tr><td>3, 7, 11, 15</td><td>3, 8, 9, 10</td><td>6, 7, 9, 12</td><td>5, 7, 10, 16</td><td>10, 11, 12, 13</td></tr><tr><td>4, 8, 12, 16</td><td>4, 7, 13, 14</td><td>5, 8, 11, 14</td><td>6, 8, 13, 15</td><td>9, 14, 15, 16</td></tr></table>

Table 4  
Partial and provisional designation of teams that act as host

<table><tr><td> $R_1$ </td><td> $R_2$ </td><td> $R_3$ </td><td> $R_4$ </td><td> $R_5$ </td></tr><tr><td>1</td><td>.</td><td>.</td><td>.</td><td>.</td></tr><tr><td>2</td><td>12</td><td>16</td><td>11</td><td>6</td></tr><tr><td>3</td><td>10</td><td>9</td><td>5</td><td>13</td></tr><tr><td>4</td><td>7</td><td>8</td><td>15</td><td>14</td></tr></table>

Of course, Table 3 does not constitute a feasible solution, as it has not been specified for each group which team plays at its home-venue. This clearly depends on the multiplicities; in Table 4, we provide a partial specification of the teams that play at their home-venue.

In fact, Table 4 provides an initial assignment such that each team is the host in exactly 1 group, i.e., each of the numbers $1 , \ldots ,$ 16 occurs once.

We will now identify all possibilities for $c _ { v } ,$ the vector of multiplicities. Without loss of generality, we can assume that the entries in this vector are nonincreasing. As stipulated in Theorem 4.1, we have $c _ { v } \geq 1$ for each $v \in V$ , and $\sum { } _ { v \in V } c _ { v } = 2 0$ , which implies that there exist 5 distinct possibilities for the first four entries of $c _ { v } ,$ namely:

$$
(c _ {1}, c _ {2}, c _ {3}, c _ {4}) \in \{(5, 1, 1, 1), (4, 2, 1, 1),
$$

$$
(3, 3, 1, 1), (3, 2, 2, 1), (2, 2, 2, 2) \}.\tag{11}
$$

It is important to realize that, for each of these possibilities, the distribution of the multiplicities over the rounds may differ, and that each of these distributions should be considered separately. As an example, consider the case where $( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } ) = ( 3 , 3 , 1 , 1 )$ One possible solution of the Venue Assignment problem is that there are three rounds where the venues of both team 1 and team 2 are host. Another possible solution of the Venue Assignment problem is that in rounds 1, 2, 3, the venue of team 1 is host, whereas in rounds 3, 4, 5 the venue of team 2 is host. We refer to each such solution as a distribution. We call two distributions distinct when no permutation of the rounds maps one distribution to the other.

Given a particular choice for $( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } )$ , it is not immediately clear how many pairwise distinct distributions exist. Let $D ( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } )$ denote the set of pairwise distinct distributions compatible with $( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } )$ . By a case analysis, we claim that $| D ( 5 , 1 , 1 , 1 ) | = 1 , | D ( 4 , 2 , 1 , 1 ) | = 2$ $| D ( 3 , 3 , 1 , 1 ) | = 3 , ~ | D ( 3 , 2 , 2 , 1 ) | = 1 1 ,$ and $| D ( 2 , 2 , 2 , 2 ) | = 1 7$ . In fact, Table 5 displays the sets $D ( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } )$

We now describe how Table 5 can be read such that it provides a feasible solution satisfying the homevenue property for each distribution. To do so, we use the labels A, B, C, D for those teams whose home venues have a multiplicity higher than 1.

Each entry of Table 5 should be interpreted in the following way:

Use the group composition from the blueprint in Table 3 and the partial venue assignment from Table 4 as a start. Notice that the latter may be altered; the former will not change.

• The second column in Table 5 gives the set $D ( c _ { 1 } , c _ { 2 } , c _ { 3 } , c _ { 4 } )$ . Each of these entries indicates which labeled teams are hosts in round $R _ { 1 }$ to $R _ { 5 }$

The third column assigns a specific team to each label. As a consequence, this may induce a change to the partial venue assignment specified in Table 4. Indeed, the labeled team hosts a group in the rounds where it is supposed to be host according to its distribution specified in the second column.

• By exercising the previous step, some teams might lose their current group to host. In the fourth column “Altered Venues” additional changes to the schedule are denoted, where for every round altered compared to Table 4, the new hosting teams are given.

In this way, Table 5 gives, for every possible venue assignment, a schedule that satisfies the home-venue property, thereby completing the proof. - as specified in the blueprint from Table 3 is identical.

Table 5  
Extending the blueprint to a feasible schedule satisfying the home-venue property

<table><tr><td> $(c_1, c_2, c_3, c_4)$ </td><td>Multiplicity distribution over rounds  $(R_1, \ldots, R_5)$ ,i.e.,  $D(c_1, c_2, c_3, c_4)$ </td><td>Teams to label</td><td>Altered Venues</td></tr><tr><td>(5, 1, 1, 1)</td><td>(A, A, A, A, A)</td><td>A : 1</td><td></td></tr><tr><td>(4, 2, 1, 1)</td><td>(AB, A, A, A, B)(AB, AB, A, A, —)</td><td>A : 1, B : 2A : 1, B : 4</td><td> $R_5:7$ </td></tr><tr><td>(3, 3, 1, 1)</td><td>(AB, A, A, B, B)(AB, AB, A, B, —)(AB, AB, AB, —, —)</td><td>A : 1, B : 2A : 1, B : 2A : 1, B : 2</td><td> $R_1:11,R_4:3$  $R_3:11,R_4:12,R_5:8$  $R_1:16,R_2:4,R_4:12,R_5:7$ </td></tr><tr><td>(3, 2, 2, 1)</td><td>(ABC, ABC, A, —, —)(ABC, AB, AC, —, —)(ABC, AB, A, C, —)(AB, AB, AC, C, —)(ABC, A, A, BC, —)(ABC, A, A, B, C)(AB, AC, A, BC, —)(AB, AC, A, B, C)(AB, AB, A, C, C)(AB, A, A, BC, C)(A, A, A, BC, BC)</td><td>A : 1, B : 2, C : 4A : 1, B : 7, C : 8A : 1, B : 4, C : 3A : 1, B : 2, C : 12A : 1, B : 14, C : 11A : 1, B : 3, C : 2A : 1, B : 2, C : 12A : 1, B : 3, C : 7A : 1, B : 4, C : 14A : 1, B : 4, C : 14A : 1, B : 7, C : 14</td><td> $R_4:12,R_5:7$  $R_1:6,R_4:3,R_5:2,4$  $R_5:7$  $R_2:14,R_5:7,9$  $R_4:6,R_5:2,3,15$  $R_3:11,R_5:8$  $R_5:7$  $R_3:11,R_5:8$  $R_2:5,13,R_5:12$ </td></tr><tr><td>(2, 2, 2, 2)</td><td>(ABCD, ABCD, —, —, —)(ABCD, ABC, D, —, —)(ABC, ABC, D, D, —)(ABCD, AB, CD, —, —)(ABCD, AB, C, D, —)(ABC, ABD, CD, —, —)(ABC, ABD, C, D, —)(ABC, AB, CD, D, —)(ABC, AB, C, D, D)(AB, AB, CD, CD, —)(AB, AB, CD, C, D)(ABCD, A, B, C, D)(ABC, AD, BD, C, —)(ABC, AD, B, C, D)(AB, AC, BD, CD, —)(AB, AC, BC, D, D)(AB, AC, BD, C, D)</td><td>A : 1, B : 2, C : 3, D : 4A : 1, B : 2, C : 3, D : 4A : 1, B : 2, C : 4, D : 15A : 1, B : 2, C : 3, D : 4A : 1, B : 2, C : 4, D : 3A : 1, B : 2, C : 4, D : 8A : 1, B : 10, C : 4, D : 5A : 1, B : 2, C : 4, D : 11A : 1, B : 3, C : 8, D : 14A : 1, B : 4, C : 15, D : 16A : 1, B : 2, C : 15, D : 8A : 1, B : 4, C : 3, D : 2A : 1, B : 4, C : 3, D : 8A : 1, B : 4, C : 3, D : 7A : 1, B : 4, C : 12, D : 11A : 1, B : 16, C : 4, D : 14A : 1, B : 4, C : 12, D : 8</td><td> $R_3:10,R_4:12,R_5:7$  $R_3:5,R_4:10,12,R_5:8$  $R_4:12,R_5:7$  $R_3:5,R_4:16,12,R_5:8$  $R_2:13,R_5:7,12$  $R_2:13,R_4:12,R_5:7,10$  $R_4:12,R_5:2$  $R_4:12,R_5:8$  $R_2:4,R_3:10,R_5:7$  $R_2:5,R_4:12,R_5:7$  $R_4:12$  $R_1:10,R_5:2$  $R_5:8$  $R_5:7$ </td></tr></table>

Thus, Table 5 can be read as an instruction of how to find a feasible schedule satisfying the home-venue property for any solution of the Venue Assignment problem.

As an example, consider the distribution $( A B C , A B , A C , - , - )$ which is an element of D(3, 2, 2, 1). The corresponding entries in the third column of Table 5 imply that in $R _ { 1 }$ , teams 1, 7 and 8 act as host. Next the fourth column corresponding to this distribution, contains $^ { 6 6 } R _ { 1 } : 6 ^ { 3 }$ , implying that team 6 also acts as host in $R _ { 1 }$ . Continuing in this way, it follows that teams 1, 12, 10, and 7 act as hosts in $R _ { 2 }$ , teams 1, 16, 9, and 8 act as hosts in $R _ { 3 } .$ teams 3, 11, 5, and 15 act as hosts in $R _ { 4 }$ , and teams 2, 4, 13, and 14 act as hosts in $R _ { 5 }$ . It is interesting to observe that in each of the schedules needed in the proof of Theorem 4.1, the composition of the groups

Lastly, we like to point out that a nation might have multiple venues where it can/must host. In the proof of the previous theorem, we assumed every nation to have one venue with a specific multiplicity. When there are multiple venues, when calculating the travel distance it matters which one is used to host a group. To address this, we solve the Venue Assignment on the complete set of all venues, with the restriction that venues from the same nation cannot host in the same round. For the Nation Assignment however, it does not matter which venues are used specifically - in this stage, we only assign nations to groups, in such a way that a host nation will be scheduled to play in its own venue(s). Hence, when solving the Nation Assignment using the blueprint, we may assume that every nation has exactly one venue.

## 5. Solving real-life instances of the VNL

In Section 5.1, we give an integer programming formulation of the Venue-Assignment Problem. Section 5.2 presents the outcomes.

## 5.1. An Integer Programming Formulation

Let $x _ { v , r }$ be the binary variables that indicate whether venue $v \in V$ hosts a group in round $r \in$ $\left\{ 1 , \ldots , 5 \right\} = R .$ Further, we need real variables $s _ { v , w , r }$ (capturing distances between venues v and w acting as host in rounds r and r + 1), $m _ { v , r }$ (capturing the largest distance traveled to venue v in round r), and $K _ { v , r }$ (capturing the difference in travel distance to venue v in round r). Let $\Delta = \operatorname* { m a x } _ { v , w } d ( v , w )$ , and let $W \subset V \times V$ be the set of pairs of venues that cannot both host a group in the same round. The following IP minimizes u: the sum of the difference in travel distances per group, over the groups.

$$
\begin{array}{l l} \text {in} \sum_ {v \in V} \sum_ {r \in R} K _ {v, r} & \text {(12)} \quad \text {Assignme} \\ \text {t.} \sum_ {v \in V} x _ {v, r} = k & \forall r \in R, \\ & \text {(13)} \quad \text {is implement} \\ & \text {Core i7 - 77} \\ \sum_ {r \in R} x _ {v, r} = c _ {v} & \forall v \in V, \\ & \text {(14)} \quad \text {RAM. The} \\ x _ {v, r} + x _ {w, r} \leq 1 & \forall r \in R,   \forall (v, w) \in W, \\ & \text {(15)} \\ s _ {v, w, r} \geq d _ {v, w} (x _ {v, r} + x _ {w, r - 1} - 1) & \forall v,   w \in V,   \forall r \in R \setminus 1, \\ & \text {(16)} \\ s _ {v, w, r} \leq \min (d _ {v, w} x _ {v, r}, d _ {v, w} x _ {w, r - 1}) & \forall v,   w \in V,   \forall r \in R \setminus 1, \\ & \text {(17)} \\ m _ {v, r} \geq s _ {v, w, r} & \forall v,   w \in V,   \forall r \in R \setminus 1, \\ & \text {(18)} \\ K _ {v, r} \geq m _ {v, r} - s _ {v, w, r} - D (1 - x _ {w, r - 1}) & \forall v,   w \in V,   \forall r \in R \setminus 1, \\ & \text {(19)} \\ x _ {v, r} \in \{0, 1 \}, K _ {v, r} \geq 0 & \forall v \in V,   r \in R. \\ & \text {(20)} \end{array}
$$

First, observe that (12) captures the objective function, minimizing $\begin{array} { r } { u = \sum _ { v , r } K _ { v , r } . } \end{array}$ . Next, constraints (13) ensure that in every round, k venues are host; constraints (14) ensure that every venue hosts as often as required; constraints (15) ensure that two venues that should not host simultaneously, will not host simultaneously. Auxiliary variables $s _ { v , w , r }$ are at least as large as $d _ { v , w }$ , the distance traveled between venues w, v in rounds $r - 1$ and r if these venues host in the respective rounds, by constraints (16), but never larger than $d _ { v , w }$ by constraints (17). The variables $m _ { v , r }$ equal the maximum distances traveled to venue v in round r (can equal zero 0 if v does not host in round r), as defined by (18), and $K _ { v , r }$ resembles the difference in traveled distances towards v in round r compared to the maximum travel distance, where the terms $- D \cdot ( 1 - x _ { w , r - 1 } )$ in (19) nullify any influence caused by distances between a venue that does not host in round $r - 1$

As instances of VNL satisfy the conditions of Theorem 4.1, we can proceed applying the integer programming formulation (12)–(20) for the Venue-Assignment to the known instances of the Volleyball Nations League, and compare our solution to that of the schedules used in practice. Formulation (12)-(20) is implemented in Python 3 using Gurobi 9.0. All computations have been done on a laptop with an Intel Core i7-7700HQ CPU 2.8-GHz processor and 32 GB RAM. The distances between venues are obtained via https://www.distancecalculator.net/, and are divided by 100 and rounded down. The four instances that

## 5.2. Results

we analyse are the Women’s and Men’s tournaments of 2018 and 2019. All values resulting from solving (12)-(20) are mentioned to be optimal by the solver and are found within approximately 2 hours of computation time.

Table 6  
Unfairness of real life $S _ { r e a l }$ and optimal $S _ { o p t } ,$ , and their total travel distance

<table><tr><td>Instance</td><td> $u(S_{opt})$ </td><td> $u(S_{real})$ </td><td> $d(S_{opt})$ </td><td> $d(S_{real})$ </td><td>Computation time (s)</td></tr><tr><td>M2018</td><td>233</td><td>1366</td><td>4272</td><td>4806</td><td>5105s</td></tr><tr><td>W2018</td><td>381</td><td>1541</td><td>4956</td><td>4169</td><td>1036s</td></tr><tr><td>M2019</td><td>347</td><td>1239</td><td>5237</td><td>4657</td><td>7230s</td></tr><tr><td>W2019</td><td>491</td><td>1288</td><td>4214</td><td>3708</td><td>4650s</td></tr></table>

Table 7  
Optimal venue assignment for Men’s VNL 2018, with European venues in bold

<table><tr><td>Round 1</td><td>Round 2</td><td>Round 3</td><td>Round 4</td><td>Round 5</td></tr><tr><td>Melbourne (AUS)</td><td>Goiânia (BRA)</td><td>Katowicze (POL)</td><td>Aix-en-Prov. (FRA)</td><td>Hoffman Est. (USA)</td></tr><tr><td>Tehran (IRA)</td><td>Jiangmen (CHN)</td><td>Kraljevo (SRB)</td><td>Lodz (POL)</td><td>Ningbo (CHN)</td></tr><tr><td>Ufa (RUS)</td><td>Osaka (JPN)</td><td>Rouen (FRA)</td><td>Ludwigsb. (GER)</td><td>Ottawa (CAN)</td></tr><tr><td>Varna (BUL)</td><td>Seoul (KOR)</td><td>Sofia (BUL)</td><td>Modena (ITA)</td><td>San Juan (ARG)</td></tr></table>

![](13-Lambers-2023_images/4da934c8ad9727cc307f1e4f33882abc355a7938f1846341d6fa4000dbf6edb6.jpg)  
Fig. 1. Optimal venues per round, VNL Men 2018.

Table 8  
Real-life venue assignment for Men’s VNL 2018, with European venues in bold

<table><tr><td>Round 1</td><td>Round 2</td><td>Round 3</td><td>Round 4</td><td>Round 5</td></tr><tr><td>Rouen (FRA)</td><td>Goiânia (BRA)</td><td>Ottawa (CAN)</td><td>Seoul (KOR)</td><td>Melbourne (AUS)</td></tr><tr><td>Ningbo (CHN)</td><td>Sofia (BUL)</td><td>Osaka (JPN)</td><td>Ludwigsb. (GER)</td><td>Jiagmen (CHN)</td></tr><tr><td>Katowicze (POL)</td><td>Lodz (POL)</td><td>Ufa (RUS)</td><td>Hoffman Est. (USA)</td><td>Tehran (IRA)</td></tr><tr><td>Kraljevo (SRB)</td><td>San Juan (ARG)</td><td>Aix-en-Prov. (FRA)</td><td>Varna (BUL)</td><td>Modena (ITA)</td></tr></table>

In Table 6 we give the unfairness corresponding to the optimal venue assignment, $u ( S _ { o p t } )$ , and we give the unfairness that corresponds to the venue assignments used in practice, $u ( S _ { r e a l } )$ . Also we give the total travel distance for the two corresponding solutions, $d ( S _ { o p t } )$ and $d ( S _ { r e a l } )$ , where the distance is given in units of 100 km. The final column gives the computation time in seconds.

As is imminent from Table 6, the fairness of the schedules used in the Volleyball Nations League can be much improved in comparison to the schedules that have been used. Moreover, these improvements in fairness do not come at the expense of the total travel distance; indeed, total travel distance is similar for our schedules when compared to the real life schedules.

We now discuss our schedules in more detail. In Table 7, the optimal schedule for the 2018 Men’s tournament is shown, and the corresponding venue assignment is also visualized in Fig. 1 – the output for the other instances is given in Appendix A. For comparison, the schedule used in practice is shown in Table 8. In Tables 9–11 optimal venue assignments are shown for Men and Womens tournaments in 2018, 2019.

In Fig. 1 we see that the optimal schedule creates two specific European rounds, where all groups are played within Europe, and two rounds without any group in Europe. In contrast with that, the schedule that was used in practice had both European and non-European venues in every round – thus leading to a high amount of unfairness.

We point out that, as the unfairness in travel times (as well as total traveled distance) is completely determined by the venue assignment (see Theorem 2.1), any nation assignment is equally good with respect to these objectives. Thus, apart from satisfying the underlying SGP and assigning teams to their designated home venues, there is complete freedom to optimize the nations assignment to whatever other objectives the organizers see fit; this can be done without compromising on the original objectives.

To arrive at a solution from Table 7 one would still need to assign the labels to the teams in accordance with the home venue property. In this tournament, there are 4 countries who host twice - (2, 2, 2, 2) - and the resulting optimal distribution is a permutation of the rounds of (ABC, AB, C, D, D) given in Table 5.

## 6. Conclusion

We have introduced the Travelling Social Golfer Problem (TSGP), generalizing the well-known Social Golfer Problem, to model the scheduling of the Volleyball Nations League. The TSGP allows us to model the unfairness ofa schedule that focusses on minimizing the differences in travel time between opposing teams. We show that this problem can be decomposed into two subproblems, Venue Assignment and Nation Assignment, and we argue that solving the Venue Assignment determines the amount of unfairness. We describe the home-venue property that is present in real-life solutions, and we show that, for the specific dimensions of the VNL, such solutions always exist. Finally, we model the problem as an integer program, and solve the real-life instances of 2018 and 2019.

The results show that large improvements in fairness are possible, without increasing total travel time.

## References

Alexandros, L., Panagiotis, K., & Miltiades, K., 2012, The existence of home advantage in volleyball, International Journal ofPerformance Analysis in Sport 12, 272–281.

Bonomo, F., Cardemil, A., Duran, G., Marenco, J., & Sab´ an, D.,´ 2012, An application of the traveling tournament problem: The Argentine volleyball league, Interfaces 42, 245–259.

Cocchi, G., Galligari, A., Nicolino, F., Piccialli, V., Schoen, F., & Sciandrone, M., 2018, Scheduling the Italian national volleyball tournament, Interfaces 48, 271–284.

Dotu, I., & van Hentenryck, P., 2005, Scheduling social golfers´ locally, Proceedings ofCPAIOR’05, LNCS 3524, pages 155– 167.

Duran, G., Dur´ an, S., Marenco, J., Mascialino, F., & Rey, P., 2019,´ Scheduling Argentina’s professional basketball leagues: A variation on the travelling tournament problem, European Journal ofOperational Research 275, 1126–1138.

Easton, K., Nemhauser, G., & Trick, M., 2003, Solving the travelling tournament problem: A combined integer programming and constraint programming approach, Lecture Notes in Computer Science 2740, 100–109.

Goerigk, M., & Westphal, S., 2016, A combined local search and integer programming approach to the traveling tournament problem, Annals of Operations Research 239, 343–354.

Harvey, W., & Winterer, T., 2005, Solving the MOLR and social golfers problems, in P. van Beek, ed., Principles and Practice of Constraint Programming – CP 2005, Springer Berlin Heidelberg, Berlin, Heidelberg, pp. 286–300.

Huyghe, T., Scanlan, A., Dalbo, V., & Calleja-Gonzalez, J., 2018,´ The negative inuence of air travel on health and performance in the national basketball association: A narrative review, Sports 6, 89.

Lester, M.M., 2021, Scheduling reach mahjong tournaments using pseudoboolean constraints, Proceedings of the International Conference on Theory andApplications ofSatis´ability Testing (SAT2021), edited by C.-M. Li and F. Many´a, Lecture Notes in Computer Science 12831, 349-358.

Liu, K., Loffler, S., & Hofstedt, P., 2019, Solving the social golfers¨ problems by constraint programming in sequential and parallel, Proceedings of the 11th International Conference on Agents and Artificial Intelligence (ICAART 2019), pages 29– 39.

Lo, M., Aughey, R.J., Stewart, A.M., Gill, N., & McDonald, B., 2020, The road goes ever on and on-a socio-physiological analysis of travel-related issues in super rugby, Journal of Sports Sciences.

Miller, A., Barr, M., Kavanagh, W., Valkov, I., & Purchase, H.C., 2021, Breakout gruop allocation schedules and the socia golfer problem with adjacent group sizes, Symmetry 13.

Raknes, M., & Pettersen, K.H., 2018, Optimizing sports scheduling: Mathematical and constraint programming to minimize traveled distance with benchmark from the norwegian profes-

sional volleyball league, Master Thesis, Norwegian Business School.

Samuels, C., 2012, Jet lag and travel fatigue: A comprehensive management plan for sport medicine physicians and high-performance support teams, Clinical Journal of Sport Medicine 22.

Song, A., Severini, T., & Allada, R., 2017, How jet lag impairs major baseball performance, Proceedings ofNational Academy ofScience 114, 1407–1412.

Stevens, C., Thornton, H., Fowler, P., Esh, C., & Taylor, L., 2018, Longhaul northeast travel disrupts sleep and induces perceived fatigue in endurance athletes, Frontiers in Physiology 20.

Triska, M., & Musliu, N., 2012, An effective greedy heuristic for the social golfer problem,Annals of Operations Research 194, 413–425.

Volkskrant 2021, Aanvoerder Anne Buijs wijst jonkies de weg, see http://www.volkskrant.nl/sport/aanvoerder-anne-buijswijst-jonkies-de-weg-soms-zelfs-naar-het-strand-van-rimini be4c406e/ (in Dutch).

Winter, W.C., Hammond, W.R., Green, N.H., Zhang, Z., & Bliwise, D.L., 2009, Measuring circadian advantage in major league baseball: A 10-year retrospective study, International Journa ofSports Physiology and Performance 4, 394–401.

## Appendix A. Optimal solutions to VNL-instances

Table 9  
A venue assignment for Women’s VNL 2018 with minimum unfairness u(S) = 381

<table><tr><td>Round 1</td><td>Round 2</td><td>Round 3</td><td>Round 4</td><td>Round 5</td></tr><tr><td>Bangkok (THA)</td><td>Eboli (ITA)</td><td>Jiangmen (CHN)</td><td>Apeldoorn (NED)</td><td>Ankara (TUR)</td></tr><tr><td>Barneri (ITA)</td><td>Rotterdam (NED)</td><td>Naklon (THA)</td><td>Bydgozcz (POL)</td><td>Yekaterinburg (RUS)</td></tr><tr><td>Hong Kong</td><td>Stuttgart (GER)</td><td>Suweo (KOR)</td><td>Kraljevo (SRB)</td><td>Lincoln (USA)</td></tr><tr><td>Santa Fe (ARG)</td><td>Walbrzyck (POL)</td><td>Toyota (JPN)</td><td>Ningbo (CHN)</td><td>Macau (CHN)</td></tr></table>

Table 10  
A venue assignment for Men’s VNL 2019 with minimum unfairness u(S) = 347

<table><tr><td>Round 1</td><td>Round 2</td><td>Round 3</td><td>Round 4</td><td>Round 5</td></tr><tr><td>Katowicze (POL)</td><td>Ardabi (IRN)</td><td>Cuiaba (BRA)</td><td>Cannes (FRA)</td><td>Brasilia (BRA)</td></tr><tr><td>Novi Sad (SRB)</td><td>Brisbane (AUS)</td><td>Jiangmen (CHN)</td><td>Gondomas (POR)</td><td>Hofman Est. (USA)</td></tr><tr><td>Plovdiv (BUL)</td><td>Ufa (RUS)</td><td>Mendoza (ARG)</td><td>Leipzig (GER)</td><td>Ningbo (CHN)</td></tr><tr><td>Urmia (IRN)</td><td>Varna (BUL)</td><td>Tokyo (JPN)</td><td>Milan (ITA)</td><td>Ottawa (CAN)</td></tr></table>

Table 11  
A venue assignment for Women’s VNL 2019 with minimum unfairness u(S) = 491

<table><tr><td>Round 1</td><td>Round 2</td><td>Round 3</td><td>Round 4</td><td>Round 5</td></tr><tr><td>Ankara (TUR)</td><td>Boryeong (KOR)</td><td>Bangkok (THA)</td><td>Apeldoorn (NED)</td><td>Ankara (TUR)</td></tr><tr><td>Macau (CHN)</td><td>Yekaterinburg (RUS)</td><td>Brasilia (BRA)</td><td>Conegliano (ITA)</td><td>Belgrade (SRB)</td></tr><tr><td>Opole (POL)</td><td>Ningbo (CHN)</td><td>Jiangmen (CHN)</td><td>Kortrijk (BEL)</td><td>Hong Kong</td></tr><tr><td>Ruse (BUL)</td><td>Tokyo (JPN)</td><td>Lincoln (USA)</td><td>Stuttgart (GER)</td><td>Perugia (ITA)</td></tr></table>