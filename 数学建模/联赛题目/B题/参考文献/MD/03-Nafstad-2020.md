---
raw_title: 03-Nafstad-2020
subject: 数学建模-策联杯B题
source: "03（最重要）.pdf"
status: mineru解析
parser: mineru
priority: 最重要
topics:
  - 直升机航班调度
  - 海上油气物流
  - 精确求解
  - 航班调度
---

# An exact solution method for a rich helicopter flight scheduling problem arising in offshore oil and gas logistics

![](03-Nafstad-2020_images/1f7caaea0155faa279fd0adca1282184f38f02838a8cd373ab161f171515636d.jpg)

Gaute Messel Nafstad <sup>a</sup>, Amund Haugseth <sup>a</sup>, Vebjørn Høyland <sup>a</sup>, Magnus Stålhane <sup>a,</sup>⇑

<sup>a</sup> Norwegian University of Science and Technology, Department of Industrial Economics and Technology Management, Trondheim, Norway

## a r t i c l e i n f o

Article history: Received 2 January 2020 Revised 31 July 2020 Accepted 19 November 2020 Available online 29 November 2020

Keywords: Offshore logistics Helicopter routing Multi-trip VRP Multi-depot VRP Temporal synchronization

## a b s t r a c t

This paper studies the problem of creating an optimal flight schedule for a heterogeneous fleet of helicopters tasked with transporting personnel to, from, and between offshore installations. The problem can be modelled as a rich vehicle routing problem and combines the following properties from the vehicle routing literature: pickup and delivery structure, heterogeneous fleet operating out of multiple depots, multi-trip, and temporal synchronization of transportation tasks. We present compact and extended mathematical models of the problem, where the extended model is based on generating all trips apriori. When solving the extended model we apply delayed constraint generation (DCG) to parts of the model to speed up the solution process. Computational results are presented that show that the extended formulation and solution method can solve realistic instances of the problem within one hour. The results further show that the DCG method works significantly better than using lazy constraints from a commercial solver, especially when the number of transportation tasks requiring temporal synchro nization becomes large.

 2020 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

## 1. Introduction

Since the discovery of the Ekofisk field in 1969, the Norwegian oil and gas sector has developed into the country’s largest industry (Norwegian Petroleum, 2020a). Today, Norway is the seventh largest producer of natural gas, and the 15th largest producer of oil worldwide (British Petroleum Company, 2020). The yearly accumulated export value for crude oil, natural gas, and condensate is almost 435 billion NOK ( 44 billion USD) (Statistics Norway, 2019), and approximately 140,000 people are, directly or indirectly, employed in the petroleum industry (Statistics Norway, 2019). At the end of 2019, there were 87 fields in production on the Norwegian continental shelf (NCS), while another 95 oil and gas discoveries are candidates for development (Norwegian Petroleum, 2020b). The total petroleum resources on the NCS are estimated to be 15,6 billion standard cubic meter, of which only 7.5 billion has been produced, sold and delivered thus far (Norwegian Petroleum, 2020b).

These petroleum resources are extracted by offshore installations that are either fixed oil platforms or floating production vessels. These installations are operated by personnel who needs to be transported to and from shore. This transportation was earlier conducted by sea vessels, but for the last decades it has almost exclusively been handled by helicopters. In 2018, over 350,000 unique deployments of personnel were conducted on the NCS according to the number of bookings made in the Dawinci Industry Hub (TietoEVRY, 2020). This equals approximately 1000 persons transported every day, which corresponds to over 50 fully loaded Sikorsky S-92 helicopters, with a capacity of 19 passengers (Aerospace Technology, 2018). Helicopter transportation is expensive, and one operator on the NCS estimates annual total costs of chartering and operating helicopters to be around two billion NOK. Today, chartering of helicopters, and planning their flights, is done manually by each company operating installations on the NCS. However, because of the complexity of the planning problem, it is likely that significant savings can be achieved by applying operational research methods to solve the problem.

In this paper we study the problem of operating a heterogeneous fleet of helicopters to transport personnel between offshore installations and/or heliports onshore. Personnel is available at his/ her pickup location at a given time, and has a latest time for when he/she is to arrive at the destination. The transportation of personnel is mainly done from a heliport onshore to an installation offshore or vice versa, but transportation between offshore installations also occur. The latter is typically transportation of personnel between floating hotel facilities (flotels) and production platforms, or when moving expert personnel between installations.

Further, there exist temporal dependencies that affect the allowed pickup and/or delivery time of certain personnel. For key personnel it is required that the replacement must arrive at the installation at least a minimum amount of time before he/she can depart to allow time for a debriefing. It also happens that certain personnel travel back and forth between a heliport and an installation on a single day to perform some key task, in which case they must be given sufficient time at the installation to perform their intended task.

To transport their personnel, each operator has a fleet of helicopters at its disposal. The helicopters are stationed at different heliports along the coast, and each helicopter operates to and from their assigned heliport. The fleet of helicopters is heterogeneous with respect to the number of seats available for passengers, the fixed cost of operating each day, the fuel consumption per hour, and the capacity of their fuel tanks. Flight time and fuel consumption between locations are assumed to be based the distance between them and the cruising speed of each helicopter, and not affected by wind conditions or the number of personnel on board. It is further assumed that the time spent at each offshore installation is constant, regardless of the number of personnel (dis)embarking, and that helicopters leave the offshore installation immediately afterwards.

A trip is defined as a flight sequence starting at a heliport, visiting installations in a given order and returning to the initial heliport. In addition to the limitations of the helicopter stated above, each trip is limited by safety regulations stipulating a maximum number of landings any personnel transported can partake in. Helicopters may perform several trips each day, and the sequence of trips conducted by a given helicopter on a given day is defined as a route. Between trips the helicopter must wait a given amount of time to allow for refueling, which can only be done at heliports, and required rest for the pilots. Due to the limited number of helipads (usually just one) at an offshore installation, it is also necessary to ensure that no two helicopter routes are scheduled to visit the same installation at the same time.

The objective in this problem is to design a set of routes for the helicopters to fly, minimizing costs associated with operating a helicopter and the distance flown, while transporting all personnel from(to) their intended origin(destination), and adhering to all the limitations described above.

The purpose of this paper is to present an exact solution method for the problem of planning helicopter flights that transport personnel to, from, and between offshore installations. The problem statement is based on the operations on the NCS, however, the same (or similar) problems are faced by operators of offshore installations all over the world. A new mathematical formulation is presented, that take into account several aspects of the problem that has previously not been addressed in the literature. Further, we develop a second mathematical model where all possible trips are generated apriori, and the concatenation of trips into routes for each helicopter is handled by the model. We further develop a customized labeling algorithm to generate trips and apply delayed constraint generation when solving this model using branch-andbound. To make the solution method even more effective, we preprocess both arcs and time windows, and add customized branching strategies. A computational study shows the effectiveness of the solution methodology.

The remainder of the paper is organized as follows: In Section 2 we give an overview of the literature on helicopter planning, and a brief overview of the literature on relevant variants of the vehicle routing problem. Then, in Section 3 we present both a compact and an extended mathematical model of the problem, before discussing in detail the different parts of our solution methodology in Section 4. Finally, we test the computational performance of the proposed solution method in Section 5, before giving some concluding remarks in Section 6.

## 2. Related literature

Optimal transportation of personnel to and from offshore oil installations have been studied since the late 1980s when Galvão and Guimarães (1987, 1990) presented a heuristic solution method, and a decision support system utilizing this heuristic, to optimally transport crew to and from oil platforms off the coast of Brazil. The first paper presenting a mathematical model of the operational planning of personnel transport by helicopters between heliports onshore and offshore platforms is that of Sierksma et al. (1998), who present both exact and heuristic approaches for solving the problem. The objective is to route each helicopter such that a given number of personnel are replaced at each location, and the total transportation costs are minimized. The problem is modelled as a split delivery vehicle routing problem, where more than one helicopter may meet the demand at a given offshore installation.

Since then, similar problems have been studied by Moreno et al. (2005), Moreno et al. (2006) and Menezes et al. (2010), who all consider transportation of personnel from heliports to offshore oil platforms off the Brazilian coast. Moreno et al. (2005) study the problem of planning trips for each helicopter for a single day, where the trips are limited by the number of intermediate landings for both orders and trips, and the objective is to minimize costs related to takeoff and landing, distance and hours travelled, and personnel not transported. To solve this problem they propose a heuristic that constructs a set of trips and aggregates the trips into routes for each helicopter. Moreno et al. (2006) extend the work of Moreno et al. (2005) by adding column generation procedures to the heuristic, utilizing information from the LP relaxation to construct helicopter routes. The problem also involves the element of an imposed waiting time between trips. The work is further extended by Menezes et al. (2010) who use a column generationbased solution approach for the same problem.

Another aspect of operational offshore helicopter planning is safety and risk. This has been studied by Qian et al. (2011) and Qian et al. (2014) who both analyze and propose approaches to minimize takeoff and landing risk, and suggest new operational procedures intended to create safer flight schedules for pickups and deliveries of personnel.

Hermeto et al. (2014) and Fernández-Cuesta et al. (2017) solve strategic problems where the goal is to minimize the long-term costs related to opening and operating airfields, and transporting workers to and from offshore installations. Hermeto et al. (2014) apply a simple routing system which assume that each helicopter only visits one platform on each trip, whereas Fernández-Cuesta et al. (2017) establish a more complex routing component where a route may visit several offshore installations. In addition, Fernández-Cuesta et al. (2017) incorporate the possibility of leasing hubs for refueling off the coast.

What separates the problem studied in this paper from earlier works, is that we consider transportation of personnel between offshore installations, in addition to between the installations and the heliport. Further, we consider time dependencies between transportation of key personnel and enforce that no two helicopters can be present at an installation at the same time. We thus have a richer problem, incorporating more of the real-life constraints and dependencies.

The problem studied in this paper can be seen as a rich variant of the vehicle routing problem (VRP) with time windows. It combines several variants and extensions of the VRP where each aspect has a rich body of research literature thoroughly reviewed in dedicated surveys. The problem is a pickup and delivery problem (PDP) (Berbeglia et al., 2007), with multiple depots (Montoya-Torres et al., 2015), heterogeneous fleet (Koç et al., 2016), multiple trips (Cattaruzza et al., 2016) and temporal synchronization of operations (Drexl, 2012). In the following we will classify our prob lem within the classification schemes presented by the surveys cited above, and present the most recent papers on exact solution methods for each variant and extension.

According to the classification scheme of PDPs presented by Berbeglia et al. (2007), a PDP is categorized as a one-to-one-PDP (1-1-PDP) if it has exactly one pickup node and one delivery node for all orders and categorized as a one-to-many-to-one-PDP (1-M-1-PDP) if orders consist of either pickups at the depot and delivery to customers, or vice versa. If each customer has both positive pickup and delivery demands it is categorized as a problem with combined demands. According to this classification, the problem studied in this paper is a combination of the 1-M-1-PDP and the 1-1-PDP, however, as seen in Section 3, we model it as a strictly 1-1-PDP. State of the art exact solution methods for the 1-1-PDP are presented by Ropke and Cordeau (2009) and Baldacci et al. (2011). The former present a solution method based on branch-priceand-cut, while the latter is based on dual bounding techniques combined with enumeration of all routes with reduced cost in the interval between the best known primal and dual solutions. Both solution methods use a set partitioning model where each variable represents a feasible route for each vehicle.

In the survey on VRP with heterogeneous fleet given by Koç et al. (2016), they divide the literature into categories based on whether fleet composition is fixed (HF) or a decision variable (FSM), whether the objective includes fixed costs, variable costs, or both, and whether the problem includes time windows. Accord ing to their classification the problem studied here is a HFTW(D), where the problem has a fixed fleet, includes time windows and the variable part of the costs are related to the distance travelled. Exact solution methods for this problem are presented by Baldacci et al. (2010) who apply a dual bounding algorithm and route enumeration, and Pessoa et al. (2018) who combine a route enumeration scheme for small vehicles with a tailored branch price-and-cut algorithm. Both methods rely on set partitioning models.

A literature review on the multi depot vehicle routing problem is given by Montoya-Torres et al. (2015), which categorizes the multi depot VRP into two categories with single or multiple objectives. The problem studied in this paper belongs to the former category, for which recent exact algorithms are presented by Baldacci and Mingozzi (2009) and Contardo and Martinelli (2014). As with the problem variants described above, dual bounding and branch-and-price solution methods are used in this paper, both based on set partitioning models. It is also worth mentioning that an extension of this problem, known as the location routing problem, where the location of the depots must also be decided, has gotten significant attention in the literature (Drexl and Schneider, 2015).

In the survey on multi-trip VRPs given by Cattaruzza et al. (2016), they identify four main academic extensions of the problem: time windows, service dependent loading times, limited trip duration, and profits. The problem in this paper include time windows and limited trip durations, but not the other two. An exact solution method to the multi-trip VRP is proposed by Mingozzi et al. (2013), while an exact method for an extension of the problem which include both time windows and limited trip durations is given by Hernandez et al. (2016). Both papers base their solution algorithm on first generating trips for the vehicles and then concatenating these trips into feasible routes for each vehicle.

A survey on VRPs with synchronization is presented by Drexl (2012). According to his classification scheme, the problem studied in this paper includes temporal operation synchronization with precedence, both with respect to when personnel is picked up/de livered and when the offshore installations are visited. Dohn et al. (2011) present four different formulations for handling temporal synchronization, including handling the synchronization through branching on the time windows. All the models are based on a branch-and-price approach. For the case of synchronized VRP with pickup and deliveries, a comparison of branch-and-price based solution methods, is conducted by Gschwind (2015).

Common for all the extensions and variants of the VRP surveyed, is that the solution methodology is based on a (generalized) set partitioning formulation, where each variable represents a path through the problem defining network. For the PDP, MDVRP, and HFTW, the problem can be formulated as a standard set partitioning model where each variable represents a feasible path through the problem defining network, and there is one constraint per customer, and one per vehicle. For the synchronization aspect, additional constraints have to be added to the model to ensure that the different vehicles interact in accordance with the synchronization requirements. For the multi-trip VRP, the complexity of the model depends on whether the variables in the model represent single trips, or a complete route for each vehicle. In the former case, one needs to coordinate the sequence and start times of the trips for each vehicle, leading to additional constraints in the model.

## 3. Mathematical models

When modelling this problem it is natural to aggregate all personnel going from the same heliport to the same installation (or vice versa) and that has the same time restrictions and dependencies, into one order. In this section we present two mathematical models for the transportation of a set of orders using helicopters. In Section 3.1 we present a compact mathematical formulation of the problem based on commodity flows along the arcs of the problem defining graph. Then in Section 3.2 we present a model based on pregeneration of all possible trips for each helicopter from its heliport to a set of installations and back to its heliport.

## 3.1. Compact mathematical formulation

The problem of serving n orders may be modelled on a graph where the pickup and delivery location of orders are represented by nodes. Let $N ^ { P } = \{ 1 , 2 , \dots n \}$ be the set of pickup nodes, and $N ^ { D } = \{ n + 1 , n + 2 , \dots , 2 n \}$ be the set of delivery nodes, where $( i + n )$ is the delivery node of the order picked up at node i. Denote the number of personnel picked up or delivered at node i as $P _ { i } ,$ , and let $\underline { { T } } _ { i }$ and $\overline { { T } } _ { i }$ denote the earliest and latest time a node may be serviced, respectively. Let $\boldsymbol { N } ^ { C } \subset \boldsymbol { N } ^ { D } \times \boldsymbol { N } ^ { P }$ , indexed by ð Þi;j , be the set of connected nodes, i.e a pair of nodes where node i must be visited at least $T _ { i j } ^ { C }$ time units beforej. Let $N _ { i } ^ { l }$ represent the set of nodes located at the same installation/heliport as node i. Further, we have a set of refueling nodes $N ^ { F }$ located at heliports where the helicopters may refuel between trips during the day, and a set $N ^ { S } \subset N ^ { P } \bigcup N ^ { D }$ con-Staining all nodes that are not located at a heliport. Fig. 1 shows an example of how nodes are distributed across two heliports and three offshore installations.

Let H be the set of helicopters, indexed by h, where each helicopter has a given seat capacity $K _ { h }$ and a fixed cost $C _ { h } ^ { H }$ that occurs if the helicopter is being used. Let s hð Þ and $e ( h )$ be the start node and end node, respectively, representing the heliport where helicopter h starts and ends its day. With each helicopter we associate a graph $G _ { h } = ( N _ { h } , A _ { h } )$ where ${ \cal N } _ { h } = { \cal N } ^ { P } \bigcup { \cal N } ^ { D } \bigcup { \cal N } _ { h } ^ { F } \bigcup \{ e ( h ) , s ( h ) \}$ g, and $N _ { h } ^ { F } \subset N ^ { F }$ S S S<sub>is the set of refueling nodes located at the same heliport</sub> as nodes e hð Þ and s hð Þ. Let $\overline { { F } } _ { h i }$ and $\underline { F } _ { h i }$ denote the maximum and minimum level of fuel on board helicopter h when arriving at node i, respectively.

![](03-Nafstad-2020_images/18c34fba0a383242681cec6ebe9cbda5dcfcedd72c94752da57ab28a691d993e.jpg)

![](03-Nafstad-2020_images/0b497982d841035150dd6614930662a4cb6305cf3cf7b6e4c88eed58a778d9e6.jpg)

![](03-Nafstad-2020_images/2a6920225996237e4d291c48cf8ded5231863e923a59509c879068ff8b3fc27f.jpg)

![](03-Nafstad-2020_images/2a75f9effd1d662d4b8e02932e1be250312070993593e5f2ade1fa013cecd5d4.jpg)  
Fig. 1. Example of nodes on installations and heliports. The white nodes represent pickup nodes, the grey represent delivery nodes and the black nodes, S; F, and E, represent start, refueling and end nodes for helicopters stationed at heliport number 1 and 2, respectively.

The set $A _ { h } \subset N _ { h } \times N _ { h }$ define the arcs that are feasible for the helicopter to traverse. First, to avoid sub-tours at an installation, and ensuring that we deliver before picking up, we remove all arcs $( i , j )$ from $A _ { h } \mathrm { ~ i f ~ } j \in N _ { i } ^ { I }$ and $i < j .$ Second, to enforce refueling every time the helicopter returns to the heliport, we remove all arcs between a pickup and a delivery node at a heliport, and ensure that no arc from a node at another installation can go directly to a pickup node at a heliport. Thus all helicopters arriving at heliports must visit (a subset of) the delivery nodes, then the refueling node, and finally (a subset of) the pickup nodes.

With each arc $( i , j ) \in A _ { h }$ we associate a cost $C _ { h i j } ,$ fuel consumption $F _ { h i j }$ , and a time $T _ { h i j }$ for traversing it. Let $T ^ { L }$ be the landing time at any installation, and let $T _ { i j } ^ { L }$ be the landing time at node i when travelling to node j specifically. Note that both $T _ { h i j }$ and $T _ { i j } ^ { L }$ are 0 if $j \in N _ { i } ^ { I } ,$ , i.e. node i and j are at the same offshore installation. Due to safety regulations there is a maximum number of legs travelled between the pickup and delivery of an order, given by L. Let $K = \left\{ 1 , \ldots , { \overline { { K } } } \right\}$ be the set of possible leg numbers, indexed by k, - <sub>where K is an upper bound on the number of legs a helicopter</sub> can fly on a given day.

Let the binary variable $x _ { h i j k }$ be equal to one if helicopter h travels from node i to j on leg $k ,$ and zero otherwise. Variable $p _ { h i }$ is the number of passengers when leaving node i, and $f _ { h i }$ is the fuel level and $t _ { h i }$ is the time when helicopter h is arriving at node i. The binary variable $z _ { h }$ equals one if helicopter h is used, and zero otherwise. Further, we introduce the binary variable $\gamma _ { h i j }$ which is equal to one if helicopter h service both nodes $i \in N$ and $j \in N _ { i } ^ { I }$ and zero otherwise, while $\delta _ { i j }$ is equal to zero if two different helicopters service nodes i and j and i is serviced at least $T ^ { L }$ time units before j.

![](03-Nafstad-2020_images/628f30b9cf4995cda02eea53286fe2895f6607f9bb4bf0f370b93323849f8ddd.jpg)

For ease of exposition, the constraints in the model below are defined using sets of nodes and may therefore contain combinations of the indices $h , i ,$ and j for which the corresponding arc $( i , j ) \in A _ { h }$ does not exist (e.g. when $i = j )$ . In these cases the corresponding variable $x _ { h i j k }$ can be assumed to take the value zero. Using this notation, the problem can be formulated as follows:

$$
\min \sum_ {h \in H} \sum_ {i \in N _ {h}} \sum_ {j \in N _ {h}} \sum_ {k \in K} C _ {h i j} x _ {h i j k} + \sum_ {h \in H} C _ {h} ^ {H} z _ {h},\tag{1}
$$

subject to:

$$
\sum_ {h \in H} \sum_ {j \in N _ {h}} \sum_ {k \in K} x _ {h i j k} = 1, \quad i \in N ^ {P},\tag{2}
$$

$$
\sum_ {j \in N _ {h}} \sum_ {k \in K} x _ {h i j k} - \sum_ {j \in N _ {h}} \sum_ {k \in K} x _ {h (n + i) j k} = 0, \quad h \in H, i \in N ^ {P},\tag{3}
$$

$$
\sum_ {j \in N _ {h}} \sum_ {k \in K} x _ {h i j k} - \sum_ {j \in N _ {h}} \sum_ {k \in K} x _ {h j i k} = 0, \quad h \in H,   i \in N _ {h} \setminus \{s (h), e (h) \},\tag{4}
$$

$$
\sum_ {j \in N ^ {p}} x _ {h s (h) j 1} = z _ {h}, \quad h \in H,\tag{5}
$$

$$
\sum_ {i \in N ^ {D}} \sum_ {k \in K} x _ {h i e (h) k} = z _ {h}, \quad h \in H,\tag{6}
$$

$$
\sum_ {j \in N _ {h}} x _ {h j i k} = \sum_ {j \in N _ {i} ^ {I}} x _ {h i j k} + \sum_ {j \in N _ {h} \backslash N _ {i} ^ {I}} x _ {h i j (k + 1)},
$$

$$
h \in H, i \in N _ {h} \setminus \{s (h), e (h) \}, k \in K \setminus \{| K | \},\tag{7}
$$

$$
\sum_ {j \in N _ {h}} \sum_ {k \in K} k x _ {h j (i + n) k} - \sum_ {j \in N _ {h}} \sum_ {k \in K} k x _ {h j i k} \leqslant \bar {L}, \quad h \in H, i \in N ^ {P},\tag{8}
$$

$$
f _ {h i} - F _ {h i j} - f _ {h j} + M _ {h i j} ^ {F} \left(1 - \sum_ {k \in K} x _ {h i j k}\right) \geqslant 0,
$$

$$
h \in H, i \in N _ {h}, j \in N _ {h} \setminus N _ {h} ^ {F},\tag{9}
$$

$$
\underline {{{F}}} _ {h i} \leqslant f _ {h i}, \leqslant \overline {{{F}}} _ {h i}, \quad h \in H, i \in N _ {h},\tag{10}
$$

$$
p _ {h i} + P _ {j} - p _ {h j} - K _ {h} \left(1 - \sum_ {k \in K} x _ {h i j k}\right) \leqslant 0, \quad h \in H, i \in N _ {h}, j \in N ^ {P},\tag{11}
$$

$$
p _ {h i} - P _ {j} - p _ {h j} - K _ {h} \left(1 - \sum_ {k \in K} x _ {h i j k}\right) \leqslant 0, \quad h \in H, i \in N _ {h}, j \in N ^ {D},\tag{12}
$$

$$
p _ {h i} - p _ {h j} - K _ {h} \left(1 - \sum_ {k \in K} x _ {h i j k}\right) \leqslant 0, \quad h \in H, i \in N _ {h}, j \in N _ {h} ^ {F},\tag{13}
$$

$$
p _ {h i} = 0, \quad h \in H, i \in N _ {h} ^ {F},
$$

$$
P _ {i} \sum_ {k \in K} \sum_ {j \in N _ {h}} x _ {h i j k} \leqslant p _ {h i} \leqslant K _ {h} z _ {h}, \quad h \in H, i \in N ^ {p},\tag{14}
$$

ð15Þ

$$
0 \leqslant p _ {h (i + n)} \leqslant \left(K _ {h} - P _ {i + n}\right) \sum_ {k \in K} \sum_ {j \in N _ {h}} x _ {h (i + n) j k}, \quad h \in H, i \in N ^ {P},\tag{16}
$$

$$
t _ {h i} + T _ {i j} ^ {L} + T _ {h i j} - t _ {h j} + M _ {h i j} ^ {\prime} \left(1 - \sum_ {k \in K} x _ {h i j k}\right) \geqslant 0,
$$

$$
h \in H, i \in N _ {h}, j \in N _ {h} \setminus N _ {h} ^ {F},\tag{17}
$$

$$
t _ {h i} + T _ {i j} ^ {L} + T _ {h i j} - t _ {h j} + M _ {h i j} ^ {\prime \prime} \left(1 - \sum_ {k \in K} x _ {h i j k}\right) \leqslant 0,
$$

$$
h \in H, i \in N _ {h}, j \in N _ {h},\tag{18}
$$

$$
t _ {h i} + \sum_ {j \in N _ {h}} \sum_ {k \in K} x _ {h i j k} \left(T _ {h i (i + n)} + T _ {i (i + n)} ^ {L}\right) \leqslant t _ {h (i + n)}, \quad h \in H, i \in N ^ {P},\tag{19}
$$

$$
\sum_ {h \in H} t _ {h i} + T _ {i j} ^ {C} \leqslant \sum_ {h \in H} t _ {h j}, \quad (i, j) \in N ^ {C},\tag{20}
$$

$$
\sum_ {h \in H} t _ {h i} - \sum_ {h \in H} t _ {h j} - T ^ {L} + \left(T ^ {L} + \bar {T} _ {j}\right) \delta_ {i j} \geqslant 0, \quad i \in N ^ {S}, j \in N _ {i} ^ {l},\tag{21}
$$

$$
\sum_ {i \in N} \sum_ {k \in K} x _ {h i i \prime k} + \sum_ {j \in N} \sum_ {k \in K} x _ {h j j \prime k} \leqslant 2 \gamma_ {h i j}, \quad h, \in H, i \in N ^ {\mathcal {S}}, j \in N _ {i} ^ {I} | i <   j,\tag{22}
$$

$$
\delta_ {i j} + \delta_ {j i} \leqslant 1 + \sum_ {h \in H} \gamma_ {h i j}, \quad i \in N ^ {S}, j \in N _ {i} ^ {I} | i <   j,\tag{23}
$$

$$
\sum_ {j \in N _ {h}} \sum_ {k \in K} T _ {i} x _ {h i j k} \leqslant t _ {h i} \leqslant \sum_ {j \in N _ {h}} \sum_ {k \in K} \overline {{T}} _ {i} x _ {h i j k}, \quad h \in H, i \in N _ {h},\tag{24}
$$

$$
x _ {h i j k} \in \{0, 1 \}, \quad h \in H, (i, j) \in A _ {h}, k \in K,\tag{25}
$$

$$
z _ {h} \in \{0, 1 \}, \quad h \in H,\tag{26}
$$

$$
\gamma_ {h i j} \in \{0, 1 \}, \quad h \in H, i \in N _ {h}, j \in N _ {i} ^ {I},
$$

$$
\delta_ {i j} \in \{0, 1 \}, \quad i \in N, j \in N _ {i} ^ {I}.\tag{27}
$$

ð28Þ

The objective function (1) minimizes the cost related to traversing arcs and utilizing helicopters. The constraints (2) and (3) make sure that all orders are handled and that the same helicopter visits both the pickup node and the corresponding delivery node. Constraints (4)-(6) ensure continuous flight sequences, while beginning and ending in the correct nodes. The arcs are given the correct leg index with constraints (7), while constraints (8) limit the number of legs between a pickup node and the corresponding delivery node. Constraints (9) and (10) handle fuel consumption and limit the fuel levels. The big M is given by $M _ { h i j } ^ { F } =$ $F _ { h i } + F _ { h i j } - F _ { h j } .$ . Embarking and disembarking of personnel at pickup and delivery nodes are enforced with constraints (11) and (12), respectively, while constraints (13) and (14) ensure that no personnel is on board the helicopter when refueling. Constraints (15) and (16) limit the number of passengers on board a helicopter when leaving a pickup and delivery node, respectively. Updating the departure times from each node visited is handled by constraints (17) and (18). Note that the refueling nodes are not part of constraints (17) because, unlike at installation nodes, you are allowed to wait at the heliports before refueling. The big Ms are given as $M _ { h i j } ^ { \prime } = \overline { { T } } _ { j } + T _ { i j } ^ { L } + T _ { h i j }$ and $M _ { h i j } ^ { \prime \prime } = \overline { { T } } _ { i } + T _ { i j } ^ { L } + T _ { h i j }$ , respectively. Constraints (19) ensure that the pickup node is visited earlier than the corresponding delivery node. The minimum time difference between handling the connected orders is enforced through constraints (20). Constraints (21)-(23) ensure that no two helicopters are present at an installation simultaneously. The upper and lower limit of the departure time are stated with constraints (24). Finally, constraints (25)-(28) give the domain of each variable.

## 3.2. Trip-based mathematical formulation

An alternative to the model presented above, is a formulation where each variable represents a trip beginning and ending at a heliport. Let $R _ { h }$ be the set of all possible trips for helicopter h, indexed by r, and $\operatorname { l e t } S = \{ 1 , \dots , | S | \}$ be the set of trip numbers that a helicopter may perform during a day, indexed by s, indicating which trip number it is currently performing. The parameter $C _ { h r } ^ { T }$ is the cost related to travelling trip r with helicopter $h ,$ and the binary parameter $A _ { i h r }$ indicates whether a node i is visited on trip r with helicopter h or not. The time helicopter h uses on trip r is denoted $T _ { h r }$ , while the time from the start of a trip to a specific node i is denoted $T _ { i h r }$ . Let $\underline { { T } } _ { h r }$ be the earliest and $\overline { { T } } _ { h r }$ be the latest possible time that trip r can be initiated with helicopter h. The parameter $T ^ { H }$ is the minimum time consumption at a heliport between trips. The binary variable $\lambda _ { h r s }$ equals one if helicopter h travels trip r on trip number s, and zero otherwise. Variable $t _ { h s }$ represents the point in time when helicopter h starts trip number s from the heliport, while variable $t _ { i }$ is the point in time when node i is visited. With this notation, the the trip-based model is formulated as follows:

$$
\min \sum_ {h \in H} \sum_ {r \in R _ {h}} \sum_ {s \in S} C _ {h r} ^ {T} \lambda_ {h r s} + \sum_ {h \in H} \sum_ {r \in R _ {h}} C _ {h} ^ {H} \lambda_ {h r 1},\tag{29}
$$

subject to:

$$
\sum_ {h \in H} \sum_ {r \in R _ {h}} \sum_ {s \in S} A _ {i h r} \lambda_ {h r s} = 1, \quad i \in N ^ {P},\tag{30}
$$

$$
\sum \lambda_ {h r s} \leqslant 1, \quad h \in H, s \in S,\tag{31}
$$

$$
\sum_ {r \in R _ {h}} ^ {n} \lambda_ {h r s} \geqslant \sum_ {r \in R _ {h}} \lambda_ {h r (s + 1)}, \quad h \in H, s \in S \setminus \{| S | \},\tag{32}
$$

$$
\sum_ {r \in R _ {h}} T _ {h r} \lambda_ {h r s} \leqslant t _ {h s} \leqslant \sum_ {r \in R _ {h}} \overline {{T}} _ {h r} \lambda_ {h r s}, \quad h \in H, s \in S,\tag{33}
$$

$$
t _ {h s} + \sum_ {r \in R _ {h}} \left(T ^ {H} + T _ {h r}\right) \lambda_ {h r s} \leqslant t _ {h (s + 1)} + M _ {h} \left(1 - \sum_ {r \in R _ {h}} \lambda_ {h r (s + 1)}\right),
$$

$$
h \in H, s \in S \setminus \{| S | \},
$$

$$
t _ {j} - t _ {i} \geqslant T _ {i j} ^ {C}, \quad (i, j) \in N ^ {C},\tag{34}
$$

$$
t _ {i} \geqslant t _ {h s} + \sum_ {r \in R _ {h}} T _ {i h r} \lambda_ {h r s} - M _ {i h} \left(1 - \sum_ {r \in R _ {h}} A _ {i h r} \lambda_ {h r s}\right),\tag{35}
$$

$$
i \in N, h \in H, s \in S,\tag{36}
$$

$$
t _ {i} \leqslant t _ {h s} + \sum_ {r \in R _ {h}} T _ {i h r} \lambda_ {h r s} + \overline {{T}} _ {i} ^ {p} \left(1 - \sum_ {r \in R _ {h}} A _ {i h r} \lambda_ {h r s}\right),
$$

$$
i \in N, h \in H, s \in S,
$$

$$
t _ {i} - t _ {j} \geqslant T ^ {L} - \left(\overline {{T}} _ {j} + T ^ {L} - \underline {{T}} _ {i}\right) \delta_ {i j}, \quad i \in N ^ {S}, j \in N _ {i} ^ {I},\tag{37}
$$

$$
\sum_ {r \in R _ {h}} \sum_ {s \in S} A _ {i h r} \lambda_ {h r s} + \sum_ {r \in R _ {h}} \sum_ {s \in S} A _ {j h r} \lambda_ {h r s} \geqslant 2 \gamma_ {h i j},\tag{38}
$$

$$
h \in H, i \in N ^ {S}, j \in N _ {i} ^ {I} | i <   j,
$$

$$
\underline {{{T}}} _ {i} \leqslant t _ {i} \leqslant \overline {{{T}}} _ {i}, \quad i \in N,\tag{39}
$$

ð40Þ

$$
\overline {{\delta_ {i j}}} + \delta_ {j i} \leqslant 1 + \sum_ {h \in H} \gamma_ {h i j}, \quad i \in N ^ {S}, j \in N _ {i} ^ {I} | i <   j,\tag{41}
$$

$$
\gamma_ {h i j} \in \{0, 1 \}, \quad h \in H, i \in N ^ {S}, j \in N _ {i} ^ {I},
$$

$$
\delta_ {i j} \in \{0, 1 \}, \quad i \in N, j \in N _ {i} ^ {I},\tag{42}
$$

$$
\lambda_ {h r s} \in \{0, 1 \}, \quad h \in H, r \in R _ {h}, s \in S. (4 4)\tag{43}
$$

The objective function (29) minimizes the cost of the selected trips and the fixed cost of using helicopters. Constraints (30) ensure that all orders are handled. Constraints (31) and (32) make sure that a helicopter can maximum do one trip for each trip number, and that a trip can be assigned to a trip number, only if the previous trip number has already been used. In constraints (33) the time windows for when a helicopter can initiate a trip are bounded by which trip the helicopter is using. If a helicopter does not use trip number s, the starting time of that trip number is set to 0. Constraints (34) state the earliest point in time a helicopter can initiate a trip, with the big M given as: $M _ { h } = \operatorname* { m a x } _ { r \in R _ { h } } \left\{ \overline { { T } } _ { h r } + T _ { h r } \right\} + T ^ { H }$ . Con-- <sub>straints (35) ensure that there is sufficient time between the ser-</sub> vice of two connected orders. Constraints (36) and (37) ensure that the service time of each order is calculated correctly. The big

M is set to $M _ { i h } = \operatorname* { m a x } _ { r \in R _ { h } } \left\{ \overline { { T } } _ { h r } \right\} - \underline { { T } } _ { i } .$ . Constraints (38)–(41) ensure - <sub>that no two helicopters are present at any installation simultane</sub> ously. Finally, constraints (42)-(44) state the variable domains.

## 4. Solution method

Mixed integer programming models such as those presented in Section 3 may be solved by commercial solvers using the branchand-bound (B&B) algorithm. However, a prerequisite for solving the trip-based model formulated in Section 3.2 is that all possible trips for all helicopters can be generated apriori.In the following we describe such a trip generation algorithm in Section 4.1, before proposing an alternative formulation of parts of the trip-based model requiring delayed constraint generation in Section 4.2. In Section 4.3 we describe how the number of arcs in the problem defining graph may be reduced, and how the width of the time windows may be decreased, before finally introducing some aggregated branching rules used when solving the trip-based mathematical model in Section 4.4.

## 4.1. Apriori trip generation

The trips in the trip based model are generated apriori using a labeling algorithm. Labeling algorithms are commonly used to solve shortest path problem with resource constraints (SPPRC) (Irnich and Desaulniers, 2005). For the trip generation algorithm presented here, a labeling algorithm is run for each helicopter $h \in I$ H and its corresponding graph $G _ { h }$ presented in Section 3. We do, however, make one minor modification to $G _ { h } \colon$ since we are generating trips, and refueling is done between trips, the set of refueling nodes $N _ { h } ^ { F }$ is removed from the graph. A pseudo code for the trip generation is provided in Algorithm 1.

A label is used to store a partial path through the network, and the resources accumulated along that path. A label $L ( i , \mathcal { R } , L ^ { * } )$ , contains the last node on the path, i, a set of resources, R, and a pointer to the parent label, L<sup></sup>. The parent label pointer is necessary in order to retrace the path represented by the label. The labeling algorithm starts by initiating a set of unprocessed labels, U, only consisting of the start label ${ \cal L } ( s ( h ) , \mathcal { R } _ { 0 } , N U L L )$ . The initial set of resources are referred to as $\mathcal { R } _ { 0 } ,$ and the parent label pointer is a zero pointer, NULL. In the algorithm, a selected label ${ \cal L } = ( i , \mathcal { R } , \ast )$ , representing a partial path from node s to i with accumulated resources R, is removed from U. This partial path is extended along all arcs $( i , j ) \in A _ { h }$ to create new partial paths, each one represented by a label L0. The resource consumption of label L0 is calculated according to so-called resource extension functions, given by $f _ { i j } ( \mathcal { R } )$ , where R is the resource consumption of label L. The resource consumption of each extended label is then checked to see if it is within the resource window $[ a _ { j } , b _ { j } ]$ . If it is, then the new label is added to U unless $j = e ( h )$  	<sub>, in which case the label has been extended to</sub> the sink node. The algorithm terminates when there are no unprocessed labels left in U. In the following we describe which

## Table 1

Label attributes and initial values.

<table><tr><td>Resource</td><td>Description</td><td>Initial value</td></tr><tr><td> $\mathcal{O}$ </td><td>Open orders (started, but not yet completed)</td><td> $\emptyset$ </td></tr><tr><td> $\mathcal{U}$ </td><td>Unreachable orders</td><td> $\emptyset$ </td></tr><tr><td> $\mathcal{L}_{o}$ </td><td>Legs travelled for order  $o$ </td><td>0</td></tr><tr><td> $f$ </td><td>Remaining fuel</td><td> $\overline{F}_{hs(h)}$ </td></tr><tr><td> $\underline{t}$ </td><td>Earliest possible arrival at the current node</td><td> $\underline{T}_{hs(h)}$ </td></tr><tr><td> $\bar{t}$ </td><td>Latest possible arrival at the current node</td><td> $\overline{T}_{hs(h)}$ </td></tr><tr><td> $t_{i}^{C}$ </td><td>Time counter for node  $i$ </td><td>0</td></tr></table>

resources are stored in R, what the resource extension functions look like, and what the resource window is for each resource.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1. Label algorithm for trip generation for helicopter h.

1:  $R_{h} = \varnothing$ 
2:  $U = \{L(s, \mathcal{R}_{0}, NULL)\}$ 
3: while  $U \neq \varnothing$ 
4:  $L = (i, \mathcal{R}, *) = RemoveFirst(U)$ 
5: for  $(i, j) \in A$ 
6:  $L' = (j, f_{ij}(\mathcal{R}), L)$ 
7: if  $a_{j} \leqslant f_{ij}(\mathcal{R}) \leqslant b_{j}$ 
8: if  $j = e(h)$ 
9:  $R_{h} = R_{h} \cup \{L'\}$ 
10: else
11:  $U = U \cup \{L'\}$ 
12: end if
13: end if
14: end for
15: end while
</div>

## 4.1.1. Resources

The resources are used to model constraints (3)-(12), (15)–(19) and (24)–(25) in the mathematical model. The set of resources kept in a label is described in Table 1, as well as their value in the initial label. The resource set, R, is defined as $\mathcal { R } = \left\{ \mathcal { O } , \mathcal { U } , \mathcal { L } _ { o } , f , t , \bar { t } , t _ { i } ^ { C } \right\}$ and $\mathcal { R } _ { 0 }$ is the set of initial resource values.

The resources $f , \underline { { t } } ,$ and t keep track of the fuel left on board the helicopter and the earliest and latest feasible arrival time at node i. Further, the resource O keeps track of the orders on board the helicopter when reaching node i, while the resource $\scriptstyle { \mathcal { L } } _ { o }$ keep track of the number of legs travelled for each order $o \in { \mathcal { O } } .$ . The set U keeps track of orders which can no longer be serviced on the partial path. This may be because the order has already been served on the (partial) path, or because the time windows of the pickup and/or delivery node makes it impossible to service the order on any feasible extension of the path. Finally, the resource $t _ { i } ^ { C }$ keeps track of the amount of time that has elapsed since the visit at node i. The cost of travelling a trip can be calculated after a label has reached the end node, and is therefore not tracked.

## 4.1.2. Resource extension functions

This subsection presents the resource extension functions used when extending labels in the labeling algorithm.

$$
f _ {i j} ^ {\mathcal {O}} (\mathcal {O} (L)) = \left\{ \begin{array}{l l} \mathcal {O} (L) \cup \{j \} & j \in N ^ {P} \\ \mathcal {O} (L) \setminus \{j - n \} & j \in N ^ {D} \\ \mathcal {O} (L) & j = e (h) \end{array} \right.\tag{45}
$$

$$
f _ {i j} ^ {\mathcal {U}} (\mathcal {U} (L)) = \left\{ \begin{array}{l l} \mathcal {U} (L) \cup \{j \} & j \in N ^ {p} \\ \mathcal {U} (L) & \text { otherwise } \end{array} \right.\tag{46}
$$

$$
f _ {i j} ^ {\mathcal {L} _ {o}} (\mathcal {L} _ {o} (L)) = \left\{ \begin{array}{c c} \mathcal {L} _ {o} (L) + 1 & j \notin N _ {i} ^ {I} \wedge o \in \mathcal {O} (L) \\ L _ {o} (L) & \text {otherwise} \end{array} \right.\tag{47}
$$

$$
f _ {i j} ^ {f} (f (L)) = f (L) - F _ {h i j}
$$

$$
f _ {i j} ^ {\underline {{t}}} (\underline {{t}} (L)) = \max \left\{\underline {{T}} _ {h j}, \underline {{t}} (L) + T _ {i j} ^ {L} + T _ {h i j} \right\}\tag{48}
$$

ð49Þ

$$
f _ {i j} ^ {\bar {t}} (\bar {t} (L)) = \min \left\{\overline {{T}} _ {h j}, \bar {t} (L) + T _ {i j} ^ {L} + T _ {h i j} \right\}\tag{50}
$$

$$
f _ {i j} ^ {t _ {k} ^ {C}} \big (t _ {k} ^ {C} (L) \big) = \left\{ \begin{array}{l l} \max \Big \{T _ {j k} ^ {C},   t _ {k} ^ {C} (L) - T _ {h i j} - T _ {i j} ^ {L} \Big \} & (j, k) \in N ^ {C} \\ \max \Big \{0,   t _ {k} ^ {C} (L) - T _ {h i j} - T _ {i j} ^ {L} \Big \} & \text {otherwise} \end{array} \right.\tag{51}
$$

The sets of open and unreachable orders are extended using Eqs. (45) and (46), respectively. In addition, the set of unreachable orders can be updated by considering the possible extensions. If an extension to a pickup node is found to be infeasible due to lack of fuel, or because the earliest possible arrival time is outside the time window, the pickup node is added to the set of unreachable orders. These resource windows cannot become feasible. Thus, it is impos sible for any extension to the end node to handle the order. For a pair of time connected orders, the order related to the service that must be conducted first is added to the set U, when the service related to the other order has been conducted. Eqs. (47) update the number of intermediate landings for each open order, and Eq. (48) update the fuel level. Eqs. (49) and (50) extend the lower and upper limits for the arrival at the current node, while Eqs. (51) update the time counter for all nodes.

## 4.1.3. Resource windows

An extension to node j is feasible for a label L if criteria (52)– (58) are met. Criterion (52) states that the extension cannot be a part of the set of unreachable orders if the evaluated extension is a pickup node. This criterion ensures that the related order has to be open in order to extend to a delivery node, and that a label cannot be extended to the end node if it has any open orders. Cri terion (53) states that the maximum leg counters cannot exceeded their limits. Sufficient fuel level for the helicopter to return to the heliport is stated in criterion (54). Criterion (55) enforces that the number of personnel on board the helicopter does not violate its capacity. Criteria (56) and (57) ensure that the time window at the last node of the path is not violated. Finally, criterion (58) enforces that the time counter resource must be zero or negative, if node j is part of a connected pair of orders.

$$
\mathcal {L} _ {k} \leqslant \overline {{L}}, k \in \mathcal {O}\tag{52}
$$

$$
f (L) \geqslant \underline {{F}} _ {h j}\tag{53}
$$

ð54Þ

$$
\sum_ {i \in \mathcal {O} (L)} P _ {i} \leqslant K _ {h}\tag{55}
$$

$$
\bar {t} (L) \geqslant \underline {{T}} _ {h j}\tag{56}
$$

$$
\underline {{t}} (L) \leqslant \overline {{T}} _ {h j}\tag{57}
$$

$$
t _ {j} ^ {C} \leqslant 0\tag{58}
$$

## 4.2. Delayed constraint generation

A drawback of the model presented in Section 3.2 is that there is a large number of constraints ((36)–(43)), and a large number of binary variables (d and c) that are needed only to ensure that no two helicopters visit the same installation at the same time. One way to handle this, would be to categorize these constraints as lazy constraints, a concept available in most commercial solvers that removes the constraints from the model, and re-inserts them as they are needed throughout the B&B tree. However, these constraints are potentially quite weak because of the big-M formulations used in constraints (36)–(38), and constraints (36) and (37) are quite dense as they sum over the set of trips R .

Instead, we can reformulate the part of the mathematical model covering constraints (37)–(43). First, we re-define constraints (36) and (37) to only be active for nodes i that are part of a pairing $N ^ { C }$ by re-writing them as:

$$
t _ {i} \geqslant t _ {h s} + \sum_ {r \in R _ {h}} T _ {i h r} \lambda_ {h r s} - M _ {i h} \left(1 - \sum_ {r \in R _ {h}} A _ {i h r} \lambda_ {h r s}\right), (i, *), (*, i) \in N ^ {C}, h \in H, s \in S,\tag{59}
$$

$$
t _ {i} \leqslant t _ {h s} + \sum_ {r \in R _ {h}} T _ {i h r} \lambda_ {h r s} + \overline {{T}} _ {i} ^ {p} \left(1 - \sum_ {r \in R _ {h}} A _ {i h r} \lambda_ {h r s}\right), (i, *), (*, i) \in N ^ {C}, h \in H, s \in S.\tag{60}
$$

This is done in order to handle constraints (35). Note that the number of connected orders is usually quite small in practice, leading to few constraints of this type.

Second, to enforce that at most one helicopter is present at each offshore installation at any given time we introduce an alternative formulation, using an exponential number of constraints. Let

$$
\Theta_ {i} = \{(h, r, s) | h \in H, r \in R _ {h} s \in S, A _ {i h r} = 1 \}
$$

and for ease of exposition we define $\theta _ { k } = \left( h _ { k } , r _ { k } , s _ { k } \right)$ . Using this nota tion we can re-formulate the model as:

$$
t _ {h _ {1} s _ {1}} + T _ {h _ {1} r _ {1} i} \lambda_ {h _ {1} r _ {1} s _ {1}} - \left(t _ {h _ {2} s _ {2}} + T _ {h _ {2} r _ {2} j} \lambda_ {h _ {2} r _ {2} s _ {2}}\right) - T ^ {L} \geqslant - M _ {h _ {2}} ^ {2} \left(1 - \delta_ {\theta_ {1} \theta_ {2}}\right),
$$

$$
i \in N ^ {S}, j \in N _ {i} ^ {I}, \theta_ {1} \in \Theta_ {i}, \theta_ {2} \in \Theta_ {j} | h _ {1} \neq h _ {2}
$$

$$
\delta_ {\theta_ {1} \theta_ {2}} + \delta_ {\theta_ {2} \theta_ {1}} \geqslant \lambda_ {h _ {1} r _ {1} s _ {1}} + \lambda_ {h _ {2} r _ {2} s _ {2}} - 1\tag{61}
$$

$$
\boldsymbol {i} \in N ^ {S}, \boldsymbol {j} \in N _ {i} ^ {I}, \theta_ {1} \in \Theta_ {i}, \theta_ {2} \in \Theta_ {j} | \boldsymbol {i} <   \boldsymbol {j}, h _ {1} \neq h _ {2},
$$

$$
\delta_ {\theta_ {1} \theta_ {2}} \in \{0, 1 \}, \quad i \in N ^ {S}, j \in N _ {i} ^ {I}, \theta_ {1} \in \Theta_ {i}, \theta_ {2} \in \Theta_ {j} | h _ {1} \neq h _ {2}.\tag{62}
$$

ð63Þ

Constraints (61) correspond to constraints (36)–(38), with $M _ { h } ^ { 2 } = \operatorname* { m a x } _ { r \in { \cal R } _ { h } } \left\{ \bar { T } _ { h r } \right\} - \bar { T } _ { i } - T ^ { L }$ . Note that each of these constraints - <sub>contains exactly five variables, making them very sparse. Con-</sub> straints (62) correspond to constraints (39), and constraints (63) put binary restrictions on the d-variables.

Since there is an exponential number of these constraints, it would be impractical, and in many cases impossible to add all of them to the model apriori. To avoid this we instead use delayed constraint generation, where constraints (37)-(43) are initially removed from the model, and the B&B algorithm is applied to the relaxed model. Whenever a potential best integer solution is found, we check whether it violates any of the constraints (61)– (63). If it does not, then the solution provides a primal bound, otherwise the violated constraints are added to make the solution infeasible, and the B&B node is re-solved.

## 4.3. Preprocessing

Both the set of arcs for a given helicopter $A _ { h }$ and time windows of some of the orders can be preprocessed in order to reduce the number of variables in the arc-flow model, the number of label extensions in Algorithm 1, and the size of the solution space. This section proposes a number of conditions that imply that an arc can be removed from the graph or that a time window can be narrowed.

## 4.3.1. Preprocessing of arcs

Consider a helicopter h and the arc $( i , j ) \in A _ { h }$ . Under the following circumstances may the arc be removed from the problem:

1. Arc is going from a start node or refueling node to a delivery node. $i \in \mathcal { N } ^ { F } \bigcup \{ s ( h ) \} \wedge j \in \mathcal { N } ^ { D }$

S2. Arc from a pickup node to an end node or refueling node. $i \in \mathcal { N } ^ { P } \land j \in \mathcal { N } ^ { F } \bigcup \{ e ( h ) \}$

S3. Node i or j, or their corresponding pickup/delivery node, is located at a another heliport than the one used by helicopter h.

4. The nodes i and j are at the same installation, and $j \in N _ { i } ^ { I } \land i < j$ . This also breaks symmetry.

5. Arrival at node j is too late. $\underline { { T } } _ { h i } + T _ { i j } ^ { L } + T _ { h i j } > \overline { { T } } _ { h j }$

6. Arrival at node j is too early. T $+ T _ { i j } ^ { L } + T _ { h i j } < \underline { { { T } } } _ { h j }$

7. The nodes are connected in the opposite order. $( j , i ) \in N ^ { C }$

8. It is impossible to get the required time difference if the arc is used.

$$
T _ {h i j} + T _ {i j} ^ {L} <   T _ {i j} ^ {C} \text {   and   } (i, j) \in N ^ {C}
$$

9. Given the maximum amount of fuel it is possible to have when arriving at node i, it must be possible to fulfill the orders related to nodes i and j, and travel back to the helicopter’s heliport.

$$
F _ {h i j} + F _ {h (i + n) (j + n)} + \min \left\{ \begin{array}{l} F _ {h j (i + n)} + F _ {h (j + n) e (h)} \\ F _ {h i (j + n)} + F _ {h (i + n) e (h)} \end{array} \right\} > \overline {{F}} _ {h i} \quad i, j \in N ^ {P}\tag{64}
$$

$$
F _ {h i j} + F _ {h j (i + n)} + F _ {h (i + n) e (h)} > \overline {{{F}}} _ {h i} \quad i \in N ^ {P}, j \in N ^ {D}\tag{65}
$$

$$
F _ {h i j} + F _ {h j (j + n)} + F _ {h (j + n) e (h)} > \overline {{F}} _ {h i} \quad i \in N ^ {D}, j \in N ^ {P}\tag{66}
$$

$$
F _ {h i j} + F _ {h j e (h)} > \overline {{F}} _ {h i} \quad i, j \in N ^ {D}\tag{67}
$$

10. Node i is a pickup node at an installation with a related delivery node located at another installation, while j is a node located on a heliport.

11. Node i is a delivery node located at a heliport and j is a pickup node.

12. The helicopter does not have enough capacity to handle the orders related to nodes i, and j simultaneously. $\big ( P _ { i } + P _ { j } > K _ { h } \big ) \wedge \neg \Big ( i \in N ^ { D } \wedge j \in N ^ { P } \big ) .$

13. The helicopter does not have enough capacity to handle the order size of node i or j. max $\left( P _ { i } , P _ { j } \right) > K _ { h }$

Applying all of these rules, we can greatly reduce the solution space of the compact formulation, and the number of extensions made in the labeling algorithm.

## 4.3.2. Preprocessing of time window

The time dependent orders create the possibility of reducing their respective time windows. This method is based on the time window reduction presented by Dohn et al. (2011). The reduction of the time windows for a given pairing $( i , j ) \in N ^ { C }$ is formulated in Table 2.

## 4.4. Aggregated branching variables

The choice of what variables to branch on in each node in the B&B tree, affects the effectiveness of the algorithm (Gamrath et al., 2015). Dumas et al. (1991) and Andersson et al. (2011) include variables in their PDPs for the sole purpose of branching on them. Dumas et al. (1991) branch on variables related to each order in a PDP, while Andersson et al. (2011) use aggregated branching variables, also referred to as constraint branching, in the maritime pickup and delivery problem with split loads.

Aggregated branching variables have been utilized in the the trip based model. Here, variables with the highest branching priority are a set of variables $\mu _ { h s } ,$ , which equals 1 if helicopter h travels any trip on trip number $s ,$ and 0 otherwise. Eq. (68) provides the connection between these variables and the original variables in the model.

Table 2  
Preprocessing of time windows for connected orders.

<table><tr><td>Node</td><td>Pre-reduction</td><td>Post-reduction</td></tr><tr><td>i</td><td> $\left[\underline{T}_{i},\overline{T}_{i}\right]$ </td><td> $\left[\underline{T}_{i},\min\left\{\overline{T}_{i},\overline{T}_{j}-T^{C}\right\}\right]$ </td></tr><tr><td>j</td><td> $\left[\underline{T}_{j},\overline{T}_{j}\right]$ </td><td> $\left[\max\left\{\underline{T}_{j},\underline{T}_{i}+T^{C}\right\},\overline{T}_{j}\right]$ </td></tr></table>

$$
\mu_ {h s} = \sum_ {r \in R _ {h}} \lambda_ {h r s}, \quad h \in H, s \in S\tag{68}
$$

The set of aggregated branching variables with the second highest priority, are similar to the binary variables applied by Andersson et al. (2011). The binary variable $\kappa _ { i h } ,$ , equals 1 if helicopter h conducts a pickup at node i, and 0 otherwise. The variables are connected with the original variables through Eq. (69).

$$
\kappa_ {i h} = \sum_ {r \in R _ {h}} \sum_ {s \in S} A _ {i h r} \lambda_ {h r s}, \quad i \in N ^ {P}, h \in H\tag{69}
$$

## 5. Computational study

In this section we perform a study of the computational performance of the two mathematical models presented in Section 3, when solved using Gurobi 9.0.0. All tests were conducted on a Lenovo NextScale nx360 M5 computer, with an Intel E5-2643v3 six core 23.40GHz processor and 512.0 GB installed memory, running on a Linux operating system. The test instance generation and labeling algorithm were implemented in C++.

In Section 5.1 we explain how the test instances used in this computational study were generated, before we compare the computational performance of the compact and trip-based model formulations in Section 5.2. Further, we test the effect the number of connected orders in the set $N ^ { C }$ has on the computational time in Section 5.3, before finally comparing the computational effect of solving instances with a single, rather than multiple, heliport (s) in Section 5.4.

## 5.1. Test instance generation

The input for the test instance generation was extracted from flight records for helicopters on the Norwegian continental shelf in 2018. Selected heliports were Bergen Airport Flesland and Stavanger Airport Sola, which are the two most used heliports on the NCS. In addition we selected ten installations, which have frequent flights to or from these heliports, and are reachable from both heliports. This created a network where all locations can be reached from an arbitrary location in the network. A map showing the location of the heliports and the offshore installations can be seen in Fig. 2.

Each instance is characterized by the following features:

 Number of orders, i.e. the instance size.

 Number of personnel in each order.

 Pickup and delivery location of each order.

 Time windows for each order.

 What orders that are time connected orders, and required time differences.

Three instances were generated per instance size. The number of personnel per order, was drawn randomly in the interval between 6 and 10, and the time windows were given widths of one hour. The number of orders between installations were set to be 25 % of the total orders in an instance, although flight records suggest that the actual percentage is closer to 5 %. This relatively high percentage imposes a stronger need for coordination and synchronization between helicopters, as helicopters must conduct more visits at installations. We thus get test instances where this aspect is prominent.

The helicopters used in the test instances were the Super Puma and Sikorsky S-92, which are the most used helicopter types on the

![](03-Nafstad-2020_images/1f31673f328572e2daf3456e89cea660c9d6afbe4250ad39f050ce7d61519e85.jpg)  
Fig. 2. Overview of the two airports (squares) and the location of the 10 offshore installations (crosses) used to generate the test instances

NCS. The number of helicopters included in each instance depends on the number of orders. For a given number of orders, n, the number of helicopters included, jHj, was given by $\begin{array} { r } { | H | = 2 \cdot \left\lceil \frac { n } { 5 } \right\rceil + 2 } \end{array}$ . This number just needs to be large enough to make the instance feasible, since a part of the objective is to minimize the number of helicopters used. The helicopters were evenly distributed among the two heliports.

The testing of the solution methods is divided into three parts. For the first part, presented in Section 5.2, one pair of time connected orders was included in each instance. In the second part of the testing, presented in Section 5.3 we increased the number of pairs of connected orders in each instance from 0 and up to 8. In both these parts, the time connected orders were determined by randomly choosing the pickup and the delivery of two different orders. Finally, in the third part of the testing, presented in Section 5.4, we removed the heliport Flesland from each instance and moved all pickup and delivery nodes, and helicopters, to Sola Airport.

## 5.2. Comparison of models

A comparison of the computational effort needed to solve the compact and trip based models, respectively, using a commercial solver for instances between 8 and 16 orders is presented in Table 3. For the compact model we give the optimality gap at the termination of the B&B search (Opt. gap) and the computing time in seconds (Comp. time). For the trip-based model we give the optimality gap, the time spent generating trips (Trip gen. time), the time spent solving the mathematical model using a commercial solver (B&B time), and the total computing time (Comp. time) which is the sum of the two. Maximum computing time for both solution methods was set to 3600 seconds.

As can be seen from the table, the compact model struggles to solve instances with 10 orders, and once the number of orders is increased to 12 or more, none of the instances may be solved within one hour. Most of the instances also have an optimality gap of 100%, indicating that not even a feasible solution was found to the problem within the time limit. However, the trip based model can solve all instances from 8 to 16 orders within two seconds.

It is clear from the results presented in Table 3 that the tripbased model outperforms the compact model in terms of solution quality within a limited computing time when applying standard commercial solvers to both model formulations. To see how the trip-based model handles larger test instances, we compare three solution methods based on this model formulation. The first is to use standard branch-and bound (B&B) to solve the model presented in Section 3, while the second one is to define constraints (37)–(43) as lazy constraints during the execution of the B&B algorithm (Lazy). The third is to use delayed constraint generation (DCG), as described in Section 4.2.

Common for all the solution methods, is that all trips have to be generated apriori. In Table 4 we report the time used for generating trips, and the number of trips generated, for instances with 17 to 52 orders. Each row is an aggregation of 9 instances, with 3 instances of each order size. For each of these sets of 9 instances, we give the minimum, average, and maximum time, and number of trips, respectively. Unsurprisingly, the general trend is that both the time and number of trips increase with an increasing number of orders, however, there are some exceptions. E.g. the maximum time spent on the instances with an order size in the 44–46 interval is larger than the maximum time spent on instances with an order size in the 50–52 interval. In general we see that the total time spent is less than one minute for all the instances up to 40 orders, and even for some of the instances up to 52 orders. In the worst case over all instances tested, it takes less than 12 min (720 s) to generate all trips. We further observe that the number of trips generated varies a lot within each order interval, with e.g. the instances in the 44–46 interval ranging from 100,000 to 10,000,000 trips. This indicates that the distribution of orders across heliports and offshore installations, and the possibilities to remove arcs and reduce time windows, have a large impact on the number of feasible trips for each helicopter.

The results of running the three solution methods for larger instances are presented in Table 5. For each of the solution methods, and each order size interval, we give the number of instances solved to optimality (# Opt.), the average optimality gap (Opt. gap), and the total computing time in seconds (Comp. time). The last line of the table (Tot./Avg.) gives the total number of instances solved, and the average optimality gap and computing time, respectively, over all tested instances. For each instance, the maximal time of the B&B search is adjusted to account for the time spent generating the trips so that the maximal total computing time is one hour (3600 s).

Table 3  
Table comparing the computational performance of the compact model presented in Section 3.1 and the trip-based model presented in Section 3.2. For the compact model we present the optimality gap (Opt. gap) and the computing time (Comp. time), while for the trip-based model we present the optimality gap (Opt. gap) the time spent generating trips (Trip gen. time), the time spent in the B&B search (B&B time) and the total computing time (Comp. time).

<table><tr><td colspan="4">compact model</td><td colspan="3">trip-based model</td></tr><tr><td># Orders</td><td>Opt. gap</td><td>Comp. time [s]</td><td>Opt. gap</td><td>Trip gen. time [s]</td><td>TtB&amp;B time [s]</td><td>Comp. time [s]</td></tr><tr><td>8</td><td>0.00 %</td><td>37</td><td>0.00 %</td><td>0.01</td><td>0.03</td><td>0.04</td></tr><tr><td>8</td><td>0.00 %</td><td>11</td><td>0.00 %</td><td>0.00</td><td>0.03</td><td>0.03</td></tr><tr><td>8</td><td>0.00 %</td><td>298</td><td>0.00 %</td><td>0.01</td><td>0.12</td><td>0.13</td></tr><tr><td>10</td><td>100.00 %</td><td>3600</td><td>0.00 %</td><td>0.01</td><td>0.32</td><td>0.33</td></tr><tr><td>10</td><td>0.00 %</td><td>619</td><td>0.00 %</td><td>0.01</td><td>0.09</td><td>0.10</td></tr><tr><td>10</td><td>25.20 %</td><td>3600</td><td>0.00 %</td><td>0.01</td><td>0.31</td><td>0.32</td></tr><tr><td>12</td><td>100.00 %</td><td>3600</td><td>0.00 %</td><td>0.01</td><td>0.33</td><td>0.35</td></tr><tr><td>12</td><td>100.00 %</td><td>3600</td><td>0.00 %</td><td>0.01</td><td>0.04</td><td>0.05</td></tr><tr><td>12</td><td>53.65 %</td><td>3600</td><td>0.00 %</td><td>0.01</td><td>0.44</td><td>0.45</td></tr><tr><td>14</td><td>100.00 %</td><td>3600</td><td>0.00 %</td><td>0.03</td><td>1.12</td><td>1.15</td></tr><tr><td>14</td><td>100.00 %</td><td>3600</td><td>0.00 %</td><td>0.01</td><td>0.28</td><td>0.29</td></tr><tr><td>14</td><td>100.00 %</td><td>3600</td><td>0.00 %</td><td>0.02</td><td>0.52</td><td>0.54</td></tr><tr><td>16</td><td>100.00 %</td><td>3600</td><td>0.00 %</td><td>0.04</td><td>1.48</td><td>1.52</td></tr><tr><td>16</td><td>100.00 %</td><td>3600</td><td>0.00 %</td><td>0.02</td><td>0.86</td><td>0.88</td></tr><tr><td>16</td><td>100.00 %</td><td>3600</td><td>0.00 %</td><td>0.05</td><td>1.73</td><td>1.77</td></tr></table>

This table gives an overview of the minimum, average, and maximum time spent generating trips using Algorithm 1, and the minimum, average, and maximum number of trips produced for subsets of 9 test instances with an increasing number of orders.

<table><tr><td colspan="4">Time generating trips</td><td colspan="3">Number of trips</td></tr><tr><td>Orders</td><td>Min</td><td>Average</td><td>Max</td><td>Min</td><td>Average</td><td>Max</td></tr><tr><td>17–19</td><td>0.01</td><td>0.05</td><td>0.20</td><td>845</td><td>4 231</td><td>18 115</td></tr><tr><td>20–22</td><td>0.01</td><td>0.11</td><td>0.39</td><td>1 390</td><td>8 427</td><td>25 902</td></tr><tr><td>23–25</td><td>0.03</td><td>0.11</td><td>0.32</td><td>2 868</td><td>8 616</td><td>22 230</td></tr><tr><td>26–28</td><td>0.08</td><td>0.40</td><td>1.97</td><td>6 720</td><td>21 087</td><td>75 117</td></tr><tr><td>29–31</td><td>0.09</td><td>0.74</td><td>2.23</td><td>6 790</td><td>34 368</td><td>87 416</td></tr><tr><td>32–34</td><td>0.19</td><td>5.51</td><td>18.50</td><td>13 472</td><td>172 859</td><td>535 536</td></tr><tr><td>35–37</td><td>1.30</td><td>7.18</td><td>16.14</td><td>50 616</td><td>198 262</td><td>441 960</td></tr><tr><td>38–40</td><td>1.56</td><td>11.56</td><td>42.35</td><td>53 442</td><td>278 478</td><td>871 101</td></tr><tr><td>41–43</td><td>3.66</td><td>35.85</td><td>82.94</td><td>103 800</td><td>780 779</td><td>1 697 120</td></tr><tr><td>44–46</td><td>4.36</td><td>123.47</td><td>696.44</td><td>132 187</td><td>2 137 780</td><td>10 902 628</td></tr><tr><td>47–49</td><td>16.13</td><td>92.33</td><td>274.94</td><td>762 245</td><td>2 021 542</td><td>4 945 039</td></tr><tr><td>50–52</td><td>15.51</td><td>218.86</td><td>621.90</td><td>942 007</td><td>3 793 540</td><td>9 411 108</td></tr></table>

Table comparing solving the trip-based model with standard B&B, with B&B using lazy constraints (Lazy), and delayed constraint generation (DCG), respectively. For each method we give the number of instances solved to optimality (# Opt.), the average optimality gap (Opt. gap), and the average computing time (comp. time).

<table><tr><td></td><td colspan="3">B&amp;B</td><td colspan="3">Lazy</td><td colspan="3">DCG</td></tr><tr><td>Orders</td><td># Opt.</td><td>Opt. gap</td><td>Comp. time [s]</td><td># Opt.</td><td>Opt. gap</td><td>Comp. time [s]</td><td># Opt.</td><td>Opt. gap</td><td>Comp. time [s]</td></tr><tr><td>17-19</td><td>9</td><td>0.00 %</td><td>16.36</td><td>9</td><td>0.00 %</td><td>5.49</td><td>9</td><td>0.00 %</td><td>4.73</td></tr><tr><td>20-22</td><td>9</td><td>0.00 %</td><td>190.40</td><td>9</td><td>0.00 %</td><td>54.31</td><td>9</td><td>0.00 %</td><td>10.39</td></tr><tr><td>23-25</td><td>9</td><td>0.00 %</td><td>275.82</td><td>9</td><td>0.00 %</td><td>33.98</td><td>9</td><td>0.00 %</td><td>44.76</td></tr><tr><td>26-28</td><td>8</td><td>1.58 %</td><td>928.97</td><td>9</td><td>0.00 %</td><td>395.29</td><td>9</td><td>0.00 %</td><td>63.68</td></tr><tr><td>29-31</td><td>7</td><td>2.57 %</td><td>1541.25</td><td>9</td><td>0.00 %</td><td>969.34</td><td>8</td><td>0.62 %</td><td>772.64</td></tr><tr><td>32-34</td><td>1</td><td>20.61 %</td><td>3233.70</td><td>3</td><td>35.80 %</td><td>2540.17</td><td>3</td><td>16.18 %</td><td>2579.32</td></tr><tr><td>35-37</td><td>1</td><td>28.76 %</td><td>3413.04</td><td>3</td><td>28.07 %</td><td>2935.91</td><td>3</td><td>14.84 %</td><td>2585.45</td></tr><tr><td>38-40</td><td>0</td><td>23.51 %</td><td>3600.00</td><td>2</td><td>67.07 %</td><td>3365.38</td><td>2</td><td>41.16 %</td><td>3151.38</td></tr><tr><td>41-43</td><td>0</td><td>53.18 %</td><td>3600.00</td><td>0</td><td>68.79 %</td><td>3600.00</td><td>0</td><td>39.12 %</td><td>3600.00</td></tr><tr><td>44-46</td><td>0</td><td>64.36 %</td><td>3600.00</td><td>0</td><td>48.61 %</td><td>3600.00</td><td>0</td><td>71.34 %</td><td>3600.00</td></tr><tr><td>47-49</td><td>0</td><td>90.69 %</td><td>3600.00</td><td>0</td><td>100.00 %</td><td>3600.00</td><td>0</td><td>100.00 %</td><td>3600.00</td></tr><tr><td>50-52</td><td>0</td><td>91.34 %</td><td>3600.00</td><td>0</td><td>100.00 %</td><td>3600.00</td><td>0</td><td>100.00 %</td><td>3600.00</td></tr><tr><td>Tot/Avg</td><td>44</td><td>31.38 %</td><td>2300.0</td><td>53</td><td>37.36 %</td><td>2058.3</td><td>52</td><td>31.94 %</td><td>1967.7</td></tr></table>

As can be seen from the table, all methods solve all instances with up to 25 orders, though the standard B&B method is significantly slower than the other two. For the instances with between 26 and 31 orders, the three methods can solve 15, 18, and 17 out of 18 instances, respectively. Once the number of orders becomes greater than 31, less than half of the instances within each order size interval can be solved, and once the number of orders passes 40, none of the methods can solve any instance to optimality within one hour, though feasible solutions can be found for many of the instances. Overall, we see that both delayed constraint generation and applying lazy constraints outperforms standard B&B, both when it comes to the number of instances solved, and the average computing time. It is, however, notable that B&B finds feasible solutions to some of the largest instances, which neither of the other solution methods do. Comparing DCG with Lazy shows that neither outperforms the other. Using lazy constraints we are able to solve one more instance to optimality than when using DCG, while the latter has a lower average optimality gap and computing time. Thus, for instances with one pair of connected orders, both of these methods seem to be equally good at solving the problem.

## 5.3. Testing the effect of connected orders

In the tests presented above, the instances contained only one pair of connected orders. In order to test the effect of the number of connected orders on the computational performance of the proposed methods, we have generated 5 additional instances with 30 orders each. Each of these instances has been solved 9 times, with an increasing number of connected orders, from 0 to 8 pairs. The computational performance of these tests can be seen in Table 6. Here we have aggregated the results according to the number of connected orders, and give the number of instances solved to opti mality within one hour (# Opt.), the average optimality gap (Opt. gap), and the computing time (Comp. time). For the DCG method we also list the average number of times constraints (61)–(63) were added during the B&B search (# Cons.).

The table shows that the trend from the previous tests, where the standard B&B performed inferior to the other two methods, is present in these tests as well. It solves the least number of instances, and has a higher average computing time than the other two. What is interesting in Table 6 is that the delayed constraint generation seems to significantly outperform the B&B with lazy constraints, which spends, on average, about 50 % longer, and solves 4 instances less within one hour, compared with the DCG method. The general trend for all three methods is also that increasing the number of connected orders, increases the computing time, however, there are some outliers. E.g. when using lazy constraints, the instances without any connected orders take, on average, longer to solve than 1–6 pairs of connected orders, and it is unable to solve one of the instances.

In Table 7 we give the average number of trips generated (# Trips), and the average number of B&B nodes generated (# B&B nodes), when using the three different methods proposed in the paper. First, we notice that the number of trips is reduced signifi cantly, when the number of connected orders increase. This is due to the preprocessing techniques described in Section 4.3, where we both remove arcs and narrow time windows for the nodes representing these orders. There thus exists fewer feasible paths through the problem defining network, reducing the number of trips generated by the labeling algorithm described in Section 4.1. When the number of connected orders reaches 8, we see an almost 30 % reduction in the the average number of trips, compared with when there are no connected orders.

When comparing the number of nodes in the B&B tree, there is also a trend that the delayed constraint generation creates a larger B&B tree than the other two. In some cases, this may be explained by the fact that the other two methods did not terminate their search. However, e.g. for 2 connected orders we can see that using lazy constraints gives roughly 53; 000 B&B nodes on average, while delayed constraint generation gives 145; 000 nodes when all instances are solved to optimality. Despite generating much larger B&B trees, we still get significantly shorter computing times, when using DCG, indicating that less time is used in each node. This is likely due to the fact that fewer constraints are added to the formulation at a time, and the added constraints are less dense. Both these factors are known to influence the time it takes to solve a linear program.

## 5.4. Testing the effect of one vs two heliports

To show that the presented methodology is also viable in the single heliport case, and to compare the computational performance, we have altered the instances presented in Section 5.1 by moving all pickup and delivery nodes located at the heliport in Bergen, to Stavanger. The results of using the DCG solution method on the test instances from 17 to 37 orders are presented in Table 8. Each row is an aggregation of nine instances, while the first three columns presents the number ofinstances solved to optimality (# Opt), the average optimality gap (Opt. gap), and the average total computing time (Comp time). The last two columns show the percentage deviation in objective value (D obj.) and the deviation in the number of trips generated (D trips), respectively, when comparing the results with the original test instances with two heliports. When calculating these deviations, we have only considered the subset of instances where both versions have been solved to optimality.

As seen in Table 8 we can solve all instances up to 31 order to optimality, and further 8 of the instances from 32 to 37 orders. Comparing these results to those presented in Table 3 we can see that the DCG solution method can solve 3 more instances, and has, on average, both smaller optimality gaps and shorter computing times. We also see that the number of trips generated is not effected much by the reduction from two to one heliports. Thus, we may conclude that the methodology works equally well for instances with a single heliport.

Studying the results presented in Table 8, we further see that the objective values, on average, increase slightly when going from two to one heliports. This is not surprising, as the helicopters have to fly a longer distances to service those installations closest to Bergen. Comparing the optimal solutions of the test instances with one and two heliports, the number of helicopters used are mostly the same in both cases, however, there are both instances where it increases and decreases by one.

Table comparing solving the trip-based model with B&B, Lazy, and DCG, respectively, when the number of connected orders is increased. For each method we give the number of instances solved to optimality (# Opt.), the average optimality gap (Opt. gap), and the average computing time (Comp. time). For the DCG method, the number of times constraints were added is also listed (# Cons).

<table><tr><td></td><td colspan="3">B&amp;B</td><td colspan="3">Lazy</td><td colspan="4">DCG</td></tr><tr><td> $|\mathcal{W}^c|$ </td><td># Opt.</td><td>Opt. gap</td><td>Comp. time</td><td># Opt.</td><td>Opt. gap</td><td>Comp. time</td><td># Opt.</td><td>Opt. gap</td><td>Comp. time</td><td># Cons.</td></tr><tr><td>0</td><td>5</td><td>0.00 %</td><td>2595.24</td><td>4</td><td>0.33 %</td><td>1668.36</td><td>5</td><td>0.00 %</td><td>471.59</td><td>73.6</td></tr><tr><td>1</td><td>3</td><td>0.95 %</td><td>2804.86</td><td>5</td><td>0.00 %</td><td>1095.65</td><td>5</td><td>0.00 %</td><td>359.72</td><td>76.0</td></tr><tr><td>2</td><td>3</td><td>0.95 %</td><td>2501.21</td><td>5</td><td>0.00 %</td><td>1089.97</td><td>5</td><td>0.00 %</td><td>737.95</td><td>94.6</td></tr><tr><td>3</td><td>3</td><td>1.44 %</td><td>2368.23</td><td>5</td><td>0.00 %</td><td>1001.42</td><td>5</td><td>0.00 %</td><td>816.27</td><td>151.8</td></tr><tr><td>4</td><td>3</td><td>3.15 %</td><td>3067.16</td><td>5</td><td>0.00 %</td><td>1034.59</td><td>5</td><td>0.00 %</td><td>1177.73</td><td>99.6</td></tr><tr><td>5</td><td>3</td><td>4.03 %</td><td>2469.74</td><td>4</td><td>0.72 %</td><td>1545.19</td><td>5</td><td>0.00 %</td><td>909.73</td><td>137.0</td></tr><tr><td>6</td><td>4</td><td>1.58 %</td><td>2223.34</td><td>4</td><td>0.33 %</td><td>1583.26</td><td>4</td><td>1.34 %</td><td>1194.56</td><td>144.0</td></tr><tr><td>7</td><td>3</td><td>3.27 %</td><td>2222.25</td><td>4</td><td>0.20 %</td><td>1722.28</td><td>5</td><td>0.00 %</td><td>737.87</td><td>145.2</td></tr><tr><td>8</td><td>3</td><td>4.19 %</td><td>2215.46</td><td>3</td><td>3.47 %</td><td>2058.27</td><td>4</td><td>0.94 %</td><td>1829.65</td><td>161.8</td></tr><tr><td>Tot/Avg</td><td>30</td><td>2.17 %</td><td>2496.39</td><td>39</td><td>0.56 %</td><td>1422.11</td><td>43</td><td>0.25 %</td><td>915.01</td><td>120.4</td></tr></table>

Table 7  
Table listing the average number of trips generated (# Trips) and the average number of B&B nodes (# B&B nodes) generated when solving the trip-based model with B&B, Lazy, and DCG, respectively, when the number of connected orders is increased.

<table><tr><td> $|\mathcal{N}^c|$ </td><td colspan="2"># Trips</td><td colspan="2"># B&amp;B nodes</td></tr><tr><td></td><td></td><td>B&amp;B</td><td>Lazy</td><td>DCG</td></tr><tr><td>0</td><td>47695.2</td><td>57440.8</td><td>77568.0</td><td>69721.2</td></tr><tr><td>1</td><td>45564.4</td><td>33261.0</td><td>53397.0</td><td>55336.6</td></tr><tr><td>2</td><td>45151.4</td><td>29664.0</td><td>53671.8</td><td>144530.4</td></tr><tr><td>3</td><td>42890.4</td><td>21094.4</td><td>59297.4</td><td>132799.2</td></tr><tr><td>4</td><td>41573.0</td><td>47016.0</td><td>88488.6</td><td>345396.4</td></tr><tr><td>5</td><td>38420.2</td><td>30898.8</td><td>93327.4</td><td>271439.8</td></tr><tr><td>6</td><td>36524.6</td><td>38656.6</td><td>207333.6</td><td>327316.6</td></tr><tr><td>7</td><td>33749.8</td><td>34993.0</td><td>194810.0</td><td>147105.4</td></tr><tr><td>8</td><td>30298.8</td><td>35063.6</td><td>171104.2</td><td>635135.6</td></tr></table>

Table 8

Table comparing solving the test instances with one and two heliports using the DCG solution method. The table lists the number of instances solved to optimality (# Opt), the average optimality gap (Opt. gap) and total computing time (Comp time), as well as the average difference in objective value objective value (D obj.) and number of trips (D trips) when using one instead of two heliports.

<table><tr><td>Orders</td><td># Opt.</td><td>Opt. gap</td><td>Comp time [s]</td><td>Δ obj.</td><td>Δ trips</td></tr><tr><td>17–19</td><td>9</td><td>0.00 %</td><td>3.90</td><td>1.21 %</td><td>-5.56</td></tr><tr><td>20–22</td><td>9</td><td>0.00 %</td><td>8.51</td><td>0.41 %</td><td>-196.22</td></tr><tr><td>23–25</td><td>9</td><td>0.00 %</td><td>59.13</td><td>1.38 %</td><td>-98.00</td></tr><tr><td>26–28</td><td>9</td><td>0.00 %</td><td>95.60</td><td>1.99 %</td><td>-597.33</td></tr><tr><td>29–31</td><td>9</td><td>0.00 %</td><td>376.69</td><td>0.34 %</td><td>175.33</td></tr><tr><td>32–34</td><td>4</td><td>14.14 %</td><td>2273.47</td><td>0.15 %</td><td>2199.11</td></tr><tr><td>35–37</td><td>4</td><td>6.20 %</td><td>2378.85</td><td>1.13 %</td><td>-4214.44</td></tr></table>

## 6. Concluding remarks

In this paper we have studied a rich helicopter flight scheduling problem from the offshore oil and gas industry. The problem consists of designing routes for helicopters to transport personnel either between heliports onshore and offshore installations or between offshore installations. The problem can be modelled as a rich vehicle routing problem, which includes a pickup and delivery structure, heterogeneous fleet of vehicles, multiple trips, multiple depots, and temporal synchronization of transportation tasks.

To solve this problem, we have presented a trip-based model, where all trips are generated apriori, and a mathematical model that puts these trips together to form feasible routes. To further improve the solution time when solving these models using branch-and-bound (B&B), we have re-formulated the model using an exponential number of constraints which is added to the model using delayed constraint generation (DCG) during the B&B search. The computational experiments indicate that when the number of temporal dependencies in the model become large, the delayed constraint generation method outperforms both standard B&B, and using the lazy constraints option built into (most) commercial solvers. Further investigation of the computational results indicate that the using DCG generates larger B&B trees than the other two methods, and thus the explanation for its improved performance is likely to stem from the fact that it adds fewer and sparser constraints to the model, thus affecting the time needed to solve each node in the B&B tree less than when adding lazy constraints. Finally, testing of the DCG indicates that there is little difference in the computational effort needed to solve instances with one and two heliports.

## Declaration of Competing Interest

The authors declare that they have no known competing finan cial interests or personal relationships that could have appeared to influence the work reported in this paper.

## CRediT authorship contribution statement

Gaute Messel Nafstad: Conceptualization, Methodolody, Software, Investigation, Writing - review & editing, Visualization. Amund Haugseth: Conceptualization, Methodolody, Software. Vebjørn Høyland: Conceptualization, Methodolody, Software. Magnus Stålhane: Conceptualization, Methodolody, Supervision, Writing - original draft, Writing - review & editing.

## Acknowledgements

We would like to thank the two referees for their valuable comments and suggestions. We would further like to thank TietoEVRY for their cooperation and for providing us with industry data.

## References

Andersson, H., Christiansen, M., Fagerholt, K., 2011. The maritime pickup and delivery problem with time windows and split loads. INFOR 49 (2), 79–91.

Baldacci, R., Bartolini, E., Mingozzi, A., 2011. An exact algorithm for the pickup and delivery problem with time windows, Oper, Res, 59 (2), 414–426.

Baldacci, R., Bartolini, E., Mingozzi, A., Roberti, R., 2010. An exact solution framework for a broad class of vehicle routing problems. Comput. Manage. Sci. 7 (3), 229–268.

Baldacci, R., Mingozzi, A., 2009. A unified exact method for solving different classe of vehicle routing problems. Math. Program. 120 (2), 347.

Berbeglia, G., Cordeau, J.-F., Gribkovskaia, I., Laporte, G., 2007. Static pickup and delivery problems: a classification scheme and survey. TOP 15 (1), 1–31.

Aerospace Technology, 2018. Norway’s largest industries. URL:https://www. aerospace-technology.com/projects/s92/..

British Petroleum Company, 2020. bp Statistical Review of World Energy 2020. URL: https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs energy-economics/statistical-review/bp-stats-review-2020-full-report.pdf..

Cattaruzza, D., Absi, N., Feillet, D., 2016. Vehicle routing problems with multiple trips. 4OR 14 (3), 223–259.

Contardo, C., Martinelli, R., 2014. A new exact algorithm for the multi-depot vehicle routing problem under capacity and route length constraints. Discr. Optim. 12 129-146

Dohn, A., Rasmussen, M.S., Larsen, J., 2011. The vehicle routing problem with time windows and temporal dependencies. Networks 58 (4), 273–289..

Drexl, M., 2012. Synchronization in vehicle routing–a survey of VRPs with multiple synchronization constraints. Transp. Sci. 46 (3), 297–316.

Drexl, M., Schneider, M., 2015. A survey of variants and extensions of the location routing problem. Eur. J. Oper. Res. 241 (2), 283–308.

Dumas, Y., Desrosiers, J., Soumis, F., 1991. The pickup and delivery problem with time windows. Eur. I. Oper. Res. 54. 7-22.

Fernández-Cuesta, E., Norddal, I.K., Andersson, H., Fagerholt, K., 2017. Base location and helicopter fleet composition in the oil industry. In: INFOR: Information Systems and Operational Research, pp. 71–92. URL:https://doi.org/10.1080 03155986.2016.1262583.

Galvão, R., Guimarães, J., 1987. An algorithm for helicopter routing in the support of offshore oil exploration. In: Proceedings of the XX Brazilian OR Symposium, pp. 96–108.

Galvão, R.D., Guimarães, J., 1990. The control of helicopter operations in the Brazilian oil industry: Issues in the design and implementation of a computerized system. Eur. J. Oper. Res. 49 (2), 266–270.

Gamrath, G., Melchiori, A., Berthold, T., Gleixner, A.M., Salvagnin, D., 2015. Branching on multi-aggregated variables. In: Michel, L. (Ed.), Integration of AI and OR Techniques in Constraint Programming. Springer International Publishing, Cham, pp. 141–156.

Gschwind, T., 2015. A comparison of column-generation approaches to the synchronized pickup and delivery problem. Eur. J. Oper. Res. 247 (1), 60–71.

Hermeto, N. d. S.S., Filho, V.J.M.F., Bahiense, L., 2014. Logistics network planning for offshore air transport of oil rig crews. Computers & Industrial Engineering 75, 41 – 54..

Hernandez, F., Feillet, D., Giroudeau, R., Naud, O., 2016. Branch-and-price algorithms for the solution of the multi-trip vehicle routing problem with time windows. Eur. J. Oper. Res. 249 (2), 551–559.

Irnich, S., Desaulniers, G., 2005. Shortest path problems with resource constraints. In: Desaulniers, G., Desrosiers, J., Solomon, M.M. (Eds.), Column Generation GERAD 25th Anniversary Series. Springer, pp. 33–65.

Koç, Ç., Bektas, T., Jabali, O., Laporte, G., 2016. Thirty years of heterogeneous vehicle routing. Eur. J. Oper. Res. 249 (1), 1–21.

Menezes, F., Porto, O., Reis, M.L., Moreno, L., Aragão, M.P. d., Uchoa, E., Abeledo, H. Nascimento, N.C. d., 2010. Optimizing helicopter transport of oil rig crews at Petrobras. Interfaces 40 (5), 408–416..

Mingozzi, A., Roberti, R., Toth, P., 2013. An exact algorithm for the multitrip vehicle routing problem. INFORMS J. Comput. 25 (2), 193–207.

Montoya-Torres, J.R., Franco, J.L., Isaza, S.N., Jiménez, H.F., Herazo-Padilla, N., 2015. A literature review on the vehicle routing problem with multiple depots. Comput. Ind. Eng. 79, 115–129.

Moreno, L., de Aragão, M.P., Uchoa, E., 2006. Column generation based heuristic for a helicopter routing problem. In: Àlvarez, C., Serna, M. (Eds.), Experimental Algorithms. Springer Berlin Heidelberg, Berlin, Heidelberg, pp. 219–230.

Moreno, L., Poggi de Aragao, M., Porto, O., Reis, M., 2005. Planning offshore helicopter flights on the Campos Basin. XXXVII Simpósio Brasileiro de Pesquisa Operacional (SBPO), Gramado, Brazil, pp. 967–976..

Norwegian Petroleum, 2020a. ECONOMY. URL: https://www.norskpetroleum.no/ en/economy/..

Norwegian Petroleum, 2020b. Everything you need to know about norwegian petroleum activities. URL: https://www.norskpetroleum.no/en/.

Pessoa, A., Sadykov, R., Uchoa, E., 2018. Enhanced branch-cut-and-price algorithm for heterogeneous fleet vehicle routing problems. Eur. J. Oper. Res. 270 (2), 530– 543.

Qian, F., Gribkovskaia, I., Sr, Øyvind Halskau, 2011. Helicopter routing in the norwegian oil industry: Including safety concerns for passenger transport. Int. J. Phys. Distrib. Logist. Manage. 41 (4), 401–415. URL:https://doi.org/10.1108 09600031111131959.

Qian, F., Strusevich, V., Gribkovskaia, I., Halskau, Ø., 2014. Minimization of passenger takeoff and landing risk in offshore helicopter transportation: models, approaches and analysis. Omega 51, 93–106.

Ropke, S., Cordeau, J.-F., 2009. Branch and cut and price for the pickup and delivery problem with time windows. Transp. Sci. 43 (3), 267–286.

Sierksma, G., Tijssen, G.A., Jan 1998. Routing helicopters for crew exchanges on offshore locations. Ann. Oper, Res. 261-286

Statistics Norway, 2019. External trade in goods. URL:https://www.ssb.no/en utenriksokonomi/statistikker/muh/aar..

Statistics Norway, 2019. Spillover-effects from the offshore petroleum to the mainland economy. URL:https://www.ssb.no/nasjonalregnskap-og konjunkturer/artikler-og-publikasjoner/\_attachment/405655? \_ts=16ecb1da138..

TietoEVRY, 2020. Dawinci industry hub - changing perspectives on oil & gas logistics. URL:https://www.tietoevry.com/en/industries/oil-and-gas/ Integrated-logistics-management/..