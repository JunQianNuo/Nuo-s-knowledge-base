---
raw_title: 07-Ghilas-2016-Scenario
subject: 数学建模-策联杯B题
source: "07.pdf"
status: mineru解析
parser: mineru
topics:
  - 情景规划
  - 货运调度
  - 班线
  - 运输规划
---

# A scenario-based planning for the pickup and delivery problem with time windows, scheduled lines and stochastic demands

![](07-Ghilas-2016-Scenario_images/09352020bdb79188947e97798b5563e2d9e4b2852890ffd4c08e05848f9d3ae8.jpg)

Veaceslav Ghilas<sup>∗</sup>, Emrah Demir, Tom Van Woensel

School of Industrial Engineering, Operations, Planning, Accounting and Control (OPAC), Eindhoven University of Technology, Eindhoven 5600 MB, The Netherland

## a r t i c l e i n f o

Article history: Received 9 September 2015 Revised 22 April 2016 Accepted 23 April 2016 Available online 13 May 2016

Keywords: Freight transportation Pickup and delivery problem Scheduled lines Stochastic demands Heuristic algorithm

## a b s t r a c t

The Pickup and Delivery Problem with Time Windows, Scheduled Lines and Stochastic Demands (PDPTW-SLSD) concerns scheduling a set of vehicles to serve a set of requests, whose expected demands are known in distribution when planning, but are only revealed with certainty upon the vehicles’ arrival. In addition, a part of the transportation plan can be carried out on limited-capacity scheduled public transportation line services. This paper proposes a scenario-based sample average approximation approach for the PDPTW-SLSD. An adaptive large neighborhood search heuristic embedded into sample average approximation method is used to generate good-quality solutions. Computational results on instances with up to 40 requests (i.e., 80 locations) reveal that the integrated transportation networks can lead to operational cost savings of up to 16% compared with classical pickup and delivery systems.

© 2016 Elsevier Ltd. All rights reserved.

## 1. Introduction

Integrated public and freight transportation flows have been successfully achieved in long-haul transportation. Apart from the passengers, cruise ships carry freight between ports (Hurtigruten, 2013). Passenger aircraft are used to transport freight without affecting the service level for passengers (Levin et al., 2012). On the other hand, freight and passenger transportation are rarely integrated in short-haul transportation operations. There are only a few initiatives to investigate the potential benefits of integrated system. MULI was a demonstration project in the west of Germany between 1996 and 1999 (Trentini and Malhene, 2010). Special-design buses were used for both passengers and small-sized packages to reduce emissions. City Cargo Amsterdam was set up as a pilot experiment in 2007 (CargoTram, 2007). Two cargo trams were redesigned to transport packages in the city center of Amsterdam. In 2009, the project was abandoned due to lack of public funds. Later, Masson et al. (2015) investigated a freight distribution system in the French city La Rochelle. The results demonstrated that integrated short-haul transportation systems could lead to improved vehicle utilization and reduced operational costs. In our view, aforementioned projects did not succeed due to a number of practical challenges, such as decision support, information sharing between involved parties and insuficient funding for (re-)designing existing transportation systems.

As a result of economic development and increased populations, urban areas are densely covered by public transportation lines (i.e., bus, metro, tram), which typically operate according to predefined routes and schedules. In this paper, such public transportation services are referred as scheduled line services (SLs). A possible integration of freight transportation with SLs might provide eficiency gains for all transport stakeholders. The integrated system can potentially reduce operational costs of logistic service providers (LSPs) and can lead to extra revenue for public transport companies. As a side effect, fewer emissions can be achieved with shorter vehicle routes (Demir et al., 2014; 2015b, see, e.g.,). Integrated transport systems may also be beneficial to low-density areas, where vehicles usually make fewer stops over longer distances (Santos et al., 2010).

This paper investigates the Pickup and Delivery Problem with Time Windows, Scheduled Lines and Stochastic Demands (PDPTW-SLSD), in which a set of geographically-spread freight requests need to be transported to their destinations using a fleet of heterogeneous pickup and delivery (PD) vehicles (i.e., a priori optimization). Moreover, capacitated SL services can be used as a part of requests’ journey without affecting passenger service level. This characteristic of the PDPTW-SLSD implies that a request can be served in two ways, direct delivery or transferred through SLs. Furthermore, the exact quantities demanded by each customer are only learned upon vehicles’ arrival at the corresponding pickup locations. Depending on the demand realizations, there are two possible violation outcomes: (i) PD vehicle may arrive at a pickup location without enough carrying capacity, and (ii) SL service capacity might not be suficient for the realized demand. In such cases, called route failures, corrective (or recourse) actions need to be applied in order to recover feasibility. These actions obviously lead to extra costs which can be charged by LSPs or freight carriers.

In order to consider demand uncertainty, a Sample Average Approximation (SAA) method along with an adaptive large neighborhood search (ALNS) algorithm is proposed. The SAA is a scenario-based framework to deal with stochastic discrete optimization problems (Kleywegt et al., 2001). The basic steps of the SAA are as follows: (i) solving the SAA problem for a given restricted set of scenarios (i.e., a subset of a larger set of scenarios), (ii) evaluating the found solution on a larger set of scenarios and approximating the expected value function by the sample average function, and (iii) iterating (step (i)–(ii)) until the defined stopping criterion is reached. We note that exact as well as heuristic algorithms (i.e., ALNS) can be used to solve the SAA problem in step (i).

The scientific contribution of this study is two-fold: (i) we propose a solution approach for the integrated short-haul transportation problem in a stochastic environment, and (ii) we quantify the benefits of the integrated system in stochastic setting. The remainder of this paper is organized as follows. Section 2 provides a brief literature review on related topics. The problem description and the mathematical formulation are discussed in Section 3. The solution approach is given in Section 4. Section 5 presents the results of extensive computational experiments. Conclusions are stated in Section 6.

## 2. Literature review

In this section, we present a brief review on the existing literature related to the PDPs with transfers, as these are the most closely related to the PDPTW-SLSD. We then present recent works on stochastic PDPs

## 2.1. PDPs with transfers

To the best of our knowledge, there are only a few studies on PDPs with transfers to public transportation services. One of the first attempts to combine the deterministic dial-a-ride problem (DARP) with SLs was done by Liaw et al. (1996). The authors proposed heuristic algorithms to tackle static and dynamic aspects of the problem and solved instances with up to 120 requests. In another study, Aldaihani and Dessouky (2003) investigated an integrated DARP with public transportation. A two-stage heuristic algorithm was proposed to solve instances with up to 155 requests. They concluded that shifting some requests to available SLs reduces the overall trip times of the requests and total traveled distance by all PD vehicles. Häll et al. (2009) formalized the integrated DARP as an arc-based mixed-integer program (MIP) and used an all-purpose solver to tackle instances with up to four requests. The authors disregarded the schedules of the public transportation services.

In another study, Ghilas et al. (2016c) provided an arc-based MIP formulation for the deterministic PDPTW-SL. The authors optimally solved instances with up to 11 requests and showed that significant operating-cost savings of up to 20% can be achieved due to the use of available SLs. As a follow-up study, Ghilas et al. (2016b) proposed an ALNS to solve large-size PDPTW-SL instances. The authors concluded that the benefits of the integrated system remain significant for large instances as well. Later, Ghilas et al. (2016a) developed an exact branch-and-price algorithm to solve small- to medium-size instances of the PDPTW-SL. The authors reformulated the problem in terms of paths (routes), and the latter were generated by solving a variant of the elementary shortest path with resource constraints using a tailored labeling algorithm. Instances with up to 50 requests were optimally solved.

The interested readers are referred to Drexl (2012) for an extensive literature review on Vehicle Routing Problems (VRPs) with synchronization constraints. In addition, a related survey on planning semi-flexible transit systems can be found in Errico et al (2013)

## 2.2. Stochastic PDPs

Over the years, there has been an increasing interest for the VRP with stochastic demands (VRPSD) (see, e.g., Laporte et al., 2002; Verweij et al., 2003; Secomandi and Margot, 2009). The most advanced solution approaches can be categorized into two groups according to the use of stochastic techniques. The most commonly used approach is stochastic programming with recourse, which is a well-known framework for modeling optimization problems that involve uncertainty. Since some data is unknown at the moment of planning, one decision is made and expected (or recourse) costs of the consequences of the plan are minimized. The second most-used approach and the one related to this paper is the multi-scenario approach (or Monte Carlo simulation). This method is a common way to estimate expected costs when a closed-form expression is not available. Therefore, an approximation is made by evaluating a solution on a set of generated scenarios. In order to implement a multi-scenario stochastic optimization approach, metaheuristic algorithms can be eficiently engaged with sampling approaches. The interested readers are referred to Bianchi et al. (2009) and Gutjahr (2011) for metaheuristic algorithms proposed in the domain of stochastic combinatorial optimization.

To the best of our knowledge, limited literature exists on PD-related problems (e.g., one-to-one PDP, DARP) with stochastic demands. One of the first works was studied by Powell et al. (1988), who considered the dynamic PDP with stochastic demands in the context of long haul freight transportation. The computational results indicated that substantial profits can be achieved by considering uncertainty in the planning process while increasing the service level compared with the previous deterministic planning approach. Other examples are the single vehicle PDP (or 1-TSP) with stochastic demands by Louveaux and Gonzalez (2009), the DARP with stochastic customers’ delays by Heilporn et al. (2011), and the stochastic DARP with expected return transports by Schilde et al. (2011).

## 3. Problem description and mathematical formulation

The PDPTW-SLSD is an extension of the classical PDPTW (see, e.g., Dumas et al., 1991; Nanry and Barnes, 2000; Lu and Dessouky, 2006). The PDPTW-SLSD consists of routing and scheduling a set of vehicles to transport a set of geographicallyspread requests from corresponding origins to their destinations. In addition, a set of limited-capacity scheduled line vehicles operates according to pre-defined routes and schedules. Each request may use any of the available SL services as a part of its journey. In other words, a request may be collected by one PD vehicle, transferred to a scheduled line and afterwards delivered to its final destination after being re-collected by another PD vehicle. Furthermore, each request has to be served within its corresponding time windows.

It is assumed that demand of each request is unknown by the time of planning. The exact quantities demanded by each request are only learned upon the vehicle’s arrival at the corresponding pickup locations. However, the demand of each request is assumed to follow a known probability distribution.

Due to aforementioned source of uncertainty, capacity constraints might be violated at any time for a given a priori route. More specifically, two types of capacity violations might occur. In case $( i ) ,$ at an origin or a transfer node, there might be an insuficient capacity on a PD vehicle to perform the pickup operation. In this case, it is assumed that the to-be-picked-up request will be served by an outsourced service at a certain cost, which is dependent on the direct distance from the point of failure to its destination. In case (ii), there might be an insuficient capacity on a SL service. In this case, the excessive demand can be transported by using the subsequent service of the SL. If time windows are violated or the capacity of the subsequent SL service is exceeded, the service is outsourced similarly to case (i). Below we introduce the notations and assumptions used throughout the paper.

• Request: Every request is associated with an origin node $r \in \mathcal { P }$ and a destination node $r + n \in { \mathcal { D } }$ , where $n = | \mathcal { P } |$ (the number of requests to be served). Each request has one time window for the pickup node $\left( \left[ l _ { r } , u _ { r } \right] \right)$ , and one time window for the delivery node $( [ l _ { r + n } , \ u _ { r + n } ] )$ . Furthermore, each freight request has demand quantity $d _ { r }$ that is defined with a probability distribution function. We assume that each demand unit corresponds to a package of a standardized small size (disregarding the nature of its content, e.g., dry or frozen, and its weight). In addition, we refer to a request by its corresponding pickup node

Vehicle: The set of PD vehicles is denoted by . In addition, each vehicle $\nu \in \mathcal { V }$ is associated with a capacity $Q _ { v }$ (i.e., maximum number of packages), the depot $o _ { v } \in \mathcal { O }$ , where is the set of depots, and its corresponding time window $[ l _ { o _ { \nu } } , u _ { o _ { \nu } } ]$ . Finally, each vehicle is assigned a routing cost per one time unit $\theta _ { v }$

Travel and service time: Travel and service times are known beforehand and remain unchanged during the planning hori zon. Each arc $( i , j )$ is associated with travel time $\Upsilon _ { i j } .$ The service time at node i is represented by $s _ { i } .$

Scheduled line: The set of all physical transfer nodes is given as $s .$ The set of all physical scheduled lines is denoted by $\mathcal { E } ,$ which is defined by a directed arc between the start and the end of the line $( i , j )$ , where $i , j \in { \mathcal { S } } .$ . For example, between two transfer nodes i and $j ,$ two scheduled lines with opposite directions are considered as (i, j) and $( j , i ) . \kappa ^ { i j }$ represents a set of indices for the departure times from origin node i of SL (i, j), such that the departure time is denoted by $p _ { i j } ^ { w }$ (e.g., $p _ { T _ { 1 } , T _ { 2 } } ^ { 0 } = 3 0$ units). Furthermore, the capacity of the SLs is denoted by $Q _ { i j } , \forall ( i , j ) \in \mathcal { E }$ . Note that scheduled lines are considered to be heterogeneous in terms of frequency and capacity. Shipping one unit of package on $\mathrm { S L } \left( i , j \right)$ costs $\eta _ { i j }$

Additional practical assumptions related to SLs are given as follows.

Every SL vehicle is assumed to have a separate compartment for carrying packages, thus the passenger capacity is not influenced.

A storage space (DHL-Packstation, 2016) for to-be-shipped packages is always available at transfer nodes. We also assume that transfers are only allowed only at the end-of-line stations in order to avoid long delays (i.e., loading/unloading) at the intermediate stops. Furthermore, we assume that multiple PD vehicles can be serviced at a time at every transfer node.

![](07-Ghilas-2016-Scenario_images/a2ce1b11a9f3af4cde4b31c5f74ba077a0564655917525b7a060770aa482662c.jpg)  
Fig. 1. An illustration of a replicated scheduled line (Ghilas et al., 2016c).

In case of multiple freight carriers using SLs, it is assumed that each carrier has a limited storage space at a transfer node and on SLs (e.g., contract-based agreement).

Cost $\eta _ { i j }$ includes transportation, handling (transshipment) and storage costs.

Since the focus of the present problem is on operational decisions, investment costs, such as the re-design of the SL vehicles and the storage capacities at the transfer nodes are disregarded.

For modeling purposes, every physical SL is assigned n copies as in Häll et al. (2009). Fig. 1a illustrates an example with one physical SL (i.e., arcs (1, 2) and (2, 1)) and two requests. Each replication is assigned to one request, and only that specific request can travel on the assigned SL (see Fig. 1b). This is done to reduce the number of decision variables in the formulation. Therefore, a set of all replicated scheduled lines is denoted by (e.g., (1a, 2a), (1b, 2b), (2a, 1a) and (2b, 1b) in Fig. 1b). The set of replicated SLs associated with request r is given as ${ \mathcal { F } } ^ { r }$ (e.g., in Fig. 1, <sup>a</sup> = {(1a, 2a), (2a, 1a)}). In addition, the set of replicated SLs related to the replicated transfer node t is given as $\mathcal { F } ^ { t } ( \mathrm { e . g . } , \mathcal { F } ^ { 1 a } = \{ ( 1 \mathrm { a } , 2 \mathrm { a } ) , ( 2 \mathrm { a } , 1 \mathrm { a } ) \}$ in Fig. 1). Finally, <sup>ij</sup> includes all replicated SLs associated with a physical SL $( i , j ) \in \mathcal { E } \ ( \mathrm { e . g . } , \mathcal { F } ^ { 1 , 2 } = \{ ( 1 \mathrm { a } , 2 \mathrm { a } ) , ( 1 \mathrm { b } , 2 \mathrm { b } ) \} , \mathcal { F } ^ { 2 , 1 } =$ {(2a, 1a), (2b, 1b)}).

Furthermore, each transfer node in (e.g., nodes 1 and 2 in Fig. 1a) is copied n times. Hence, represents the set of all replicated transfer nodes (e.g., ≡ {1a, 1b, 2a, 2b} in Fig. 1b). For the sake of modeling eficiency, we use ψ<sup>t</sup>, ∀ t ∈ as the physical transfer node represented by the replicated transfer node t (e.g., $\psi ^ { 1 a } = \psi ^ { 1 b } = 1 )$ . Therefore, set $\tau ^ { t }$ is $\{ i \in \mathcal { T } | \ \psi ^ { i } = \psi ^ { t }$ and $i \neq t \} , \forall t \in \mathcal { T } \ ( \mathrm { e . g . } , \mathcal { T } ^ { 2 a } = \{ 2 b \}$ in Fig. 1b). Finally, let $f _ { i } ^ { r }$ be a constant taking value 1 if node i is the pickup node of request r, value –1 if it is the delivery node of r, or value 0 if it is none of them (pickup nor delivery node of r).

The proposed formulation is not limited to use of only one scheduled line. Any complex network topology (i.e., square, triangle, star, etc.) might be considered, and the requests are allowed to be transferred from one SL to another.

Finally, the PDPTW-SLSD can be defined on a digraph $\mathcal { G } = ( \mathcal { N } , \mathcal { A } )$ , where $\mathcal { N }$ is the set of nodes $( \mathrm { i . e } , \mathcal { O } \cup \mathcal { P } \cup \mathcal { D } \cup \mathcal { T } )$ and the set of arcs $\mathcal { A } \equiv \mathcal { A } _ { 1 } \cup \mathcal { A } _ { 2 } \cup \mathcal { A } _ { 3 } \cup \mathcal { A } _ { 4 }$ defined as follows:

$$
\begin{array}{l} \mathcal {A} _ {1} = ((\mathcal {P} \cup \mathcal {D})) \times (\mathcal {P} \cup \mathcal {D})) \setminus \{(r + n, r): r \in \mathcal {P} \} \\ \mathcal {A} _ {2} = \{(i, j): i \in \mathcal {O}, j \in \mathcal {P} \} \cup \{(i, j): i \in \mathcal {D}, j \in \mathcal {O} \} \cup (\mathcal {O} \times \mathcal {T}) \\ \mathcal {A} _ {3} = ((\mathcal {P} \cup \mathcal {D})) \times \mathcal {T}) \setminus (\{(j, r): r \in \mathcal {P}, j \in \mathcal {T} ^ {r} \} \cup \{(r + n, j): r \in \mathcal {P}, j \in \mathcal {T} ^ {r} \}) \\ \mathcal {A} _ {4} = \{(i, j): i, j \in \mathcal {T}, (\psi^ {i}, \psi^ {j}) \notin \mathcal {E} \}. \end{array}
$$

These sets of arcs consider all feasible connections in terms of precedence constraints. Fig. 2 presents a small example of a network with one depot, two requests and one SL service along with all possible arcs. Sets $\mathcal { A } _ { 1 }$ and $\mathbf { \mathcal { A } } _ { 2 }$ are shown in Fig. 2a and sets $\mathbf { \mathcal { A } } _ { 3 }$ and $\mathcal { A } _ { 4 }$ are presented in Fig. 2b.

The binary variable $x _ { i j } ^ { \nu }$ equals to 1 if arc (i, j) is used by PD vehicle v, 0 otherwise, $\forall ( i , j ) \in \mathcal { A } , \nu \in \mathcal { V } .$ . Variable $y _ { i j } ^ { r }$ takes value 1 if arc (i, j) is used by request $r , 0$ otherwise, $\forall ~ i , j \in \mathcal { P } ~ \cup ~ \mathcal { D } ~ \cup ~ \mathcal { T } , ~ r \in \mathcal { P }$ . In addition, $q _ { i j } ^ { r w }$ takes value 1 if replicated SL (i, j) is used by request r that departs from i at time $p _ { i j } ^ { w } , \ : 0$ otherwise, $\forall \ r \in \mathcal { P } , ( i , j ) \in \mathcal { F } ^ { r } , \ w \in \mathcal { K } ^ { \psi ^ { i } \psi ^ { j } }$ . Timing decisions are assured by: $\alpha _ { v }$ that indicates the time at which vehicle v arrived back to the depot, $\forall \ \nu \in \mathcal { V } ,$ , by $\beta _ { i }$ that shows the time of departure of a PD vehicle from node $i , \forall i \in \mathcal { N }$ , and finally, $\gamma _ { i } ^ { r }$ that indicates the time at which request r departed from node $i , \forall \ i \in \mathcal { P } \ \cup \ \mathcal { D } \ \cup \ \mathcal { T } , \ r \in \mathcal { P }$

The two-stage stochastic PDPTW-SLSD formulation is shown in the following two subsections.

![](07-Ghilas-2016-Scenario_images/ab012d76c455b41f106ce107b309a505961f4709482c5e3d47c2e3acbd485b56.jpg)  
Fig. 2. An example network with two requests and one SL service (Ghilas et al., 2016a)

3.1. The first-stage model

$$
\begin{array}{l l} \text { Minimize } & \sum_ {(i, j) \in \mathcal {A}} \sum_ {\nu \in \mathcal {V}} \theta_ {\nu} \Upsilon_ {i j} x _ {i j} ^ {\nu} \\ & + E [ Q (\boldsymbol {x}, \xi , \eta) ] \end{array}\tag{1}
$$

(2)

The objective function minimizes the total operating costs incurred by PD vehicles (1) and the recourse costs (2). In the recourse function, x is the given routing vector, $\xi$ is the set of scenarios, and $\eta$ is the cost vector for using SLs per unit shipped.

subject to

Routing and flow constraints

$$
\sum_ {i \in \mathcal {N}} \sum_ {\nu \in \mathcal {V}} x _ {i j} ^ {\nu} = 1 \quad \forall j \in \mathcal {P} \cup \mathcal {D}\tag{3}
$$

$$
\sum_ {i \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}} x _ {o _ {\nu}, i} ^ {\nu} \leq 1 \quad \forall \nu \in \mathcal {V}\tag{4}
$$

$$
\sum_ {i \in \mathcal {N}} \sum_ {\nu \in \mathcal {V}} x _ {i t} ^ {\nu} \leq 1 \quad \forall t \in \mathcal {T}\tag{5}
$$

$$
\sum_ {j \in \mathcal {N}} x _ {i j} ^ {\nu} - \sum_ {j \in \mathcal {N}} x _ {j i} ^ {\nu} = 0 \quad \forall i \in \mathcal {N}, \nu \in \mathcal {V}\tag{6}
$$

$$
\sum_ {j \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}} y _ {i j} ^ {r} - \sum_ {j \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}} y _ {j i} ^ {r} = f _ {i} ^ {r} \quad \forall r \in \mathcal {P}, i \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}\tag{7}
$$

$$
\sum_ {i \in \mathcal {N}} \sum_ {\nu \in \mathcal {V}} x _ {i t} ^ {\nu} \leq \sum_ {r \in \mathcal {P}} \sum_ {(i, j) \in \mathcal {F} ^ {t}} y _ {i j} ^ {r} \quad \forall t \in \mathcal {T}\tag{8}
$$

Constraints (3) state that all pickup and delivery nodes are visited exactly once. Constraints (4) ensure that each vehicle leaves its depot at most once and constraints (5) state that each replicated transfer node is visited at most once. Flow conservations for PD vehicles and requests are considered in constraints (6) and (7), respectively. Constraints (8) ensure that if a request uses a scheduled line, a PD vehicle should pick up or drop off the request at the corresponding transfer node.

Scheduling constraints

$$
y _ {i j} ^ {r} = 1 \Rightarrow \gamma_ {j} ^ {r} \geq \gamma_ {i} ^ {r} + \Upsilon_ {i j} + s _ {j} \quad \forall r \in \mathcal {P}, i, j \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}\tag{9}
$$

$$
\sum_ {v \in \mathcal {V}} x _ {i j} ^ {v} = 1 \Rightarrow \beta_ {j} \geq \beta_ {i} + \Upsilon_ {i j} + s _ {j} \quad \forall i \in \mathcal {N}, j \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}\tag{10}
$$

$$
x _ {i, o _ {\nu}} ^ {\nu} = 1 \Rightarrow \alpha_ {\nu} \geq \beta_ {i} + \Upsilon_ {i, o _ {\nu}} + s _ {o _ {\nu}} \quad \forall i \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}, \nu \in \mathcal {V}\tag{11}
$$

$$
\beta_ {r + n} \geq \beta_ {r} + \Upsilon_ {r, r + n} + s _ {r + n} \quad \forall r \in \mathcal {P}\tag{12}
$$

$$
l _ {i} \leq \beta_ {i} - s _ {i} \leq u _ {i} \quad \forall i \in \mathcal {P} \cup \mathcal {D}\tag{13}
$$

$$
l _ {g _ {\nu}} \leq \alpha_ {\nu} \leq u _ {o _ {\nu}} \quad \forall \nu \in \mathcal {V}\tag{14}
$$

$$
\sum_ {w \in \mathcal {K} ^ {\psi^ {i} \psi^ {j}}} q _ {i j} ^ {r w} = y _ {i j} ^ {r} \quad \forall r \in \mathcal {P}, (i, j) \in \mathcal {F} ^ {r}\tag{15}
$$

$$
q _ {i j} ^ {r w} = 1 \quad a n d \quad y _ {i j} ^ {r} = 1 \Rightarrow \gamma_ {i} ^ {r} = p _ {i j} ^ {w} \quad \forall r \in \mathcal {P}, (i, j) \in \mathcal {F} ^ {r}, w \in \mathcal {K} ^ {\psi^ {i} \psi^ {j}}\tag{16}
$$

Timing variables of each request are considered in constraints (9). Similarly, schedules for PD vehicles are considered in constraints (10) and (11). Constraints (12) define the precedence relations for each request. Constraints (13) and (14) enforce time windows restrictions. Constraints (15)–(16) state that if a request uses a scheduled line, SL vehicle must only depart at its scheduled departure time.

Synchronization constraints

$$
\sum_ {j \in \mathcal {P} \cup \mathcal {D}} y _ {i j} ^ {r} = 1 \Rightarrow \gamma_ {i} ^ {r} = \beta_ {i} \quad \forall r \in \mathcal {P}, i \in \mathcal {T}\tag{17}
$$

$$
\sum_ {j \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}} y _ {i j} ^ {r} = 1 \Rightarrow \gamma_ {i} ^ {r} = \beta_ {i} \quad \forall r \in \mathcal {P}, i \in \mathcal {P} \cup \mathcal {D}\tag{18}
$$

$$
\sum_ {i \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}} y _ {i, r + n} ^ {r} = 1 \Rightarrow \gamma_ {r + n} ^ {r} = \beta_ {r + n} \quad \forall r \in \mathcal {P}\tag{19}
$$

$$
y _ {t j} ^ {r} = 1 \Rightarrow \gamma_ {t} ^ {r} = \beta_ {t} \quad \forall r \in \mathcal {P}, t \in \mathcal {T}, j \in \mathcal {T} ^ {t}\tag{20}
$$

The set of constraints (17)–(20) ensure the synchronization between requests’ and vehicles’ schedules.

$$
\text { Decision   variable   domains }
$$

$$
x _ {i j} ^ {\nu} \in \{0, 1 \} \quad \forall (i, j) \in \mathcal {A}, \nu \in \mathcal {V}\tag{21}
$$

$$
y _ {i j} ^ {r} \in \{0, 1 \} \quad \forall i, j \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}, r \in \mathcal {P}\tag{22}
$$

$$
\alpha_ {\nu} \in R ^ {+} \quad \forall \nu \in \mathcal {V}\tag{23}
$$

$$
\gamma_ {i} ^ {r} \in R ^ {+} \quad \forall i \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}, r \in \mathcal {P}\tag{24}
$$

$$
\beta_ {i} \in R ^ {+} \quad \forall i \in \mathcal {N}\tag{25}
$$

$$
q _ {i j} ^ {r w} \in \{0, 1 \} \quad \forall r \in \mathcal {P}, (i, j) \in \mathcal {F} ^ {r}, w \in \mathcal {K} ^ {\psi^ {i} \psi^ {j}}.\tag{26}
$$

We note that constraints (9)–(11), (16) and (17)–(20) are formulated as implications. Standard linearization techniques can be easily used to express them using one or two linear inequalities, as follows:

$$
\gamma_ {j} ^ {r} \geq \gamma_ {i} ^ {r} + \Upsilon_ {i j} + s _ {j} - M _ {i j} \left(1 - y _ {i j} ^ {r}\right) \quad \forall r \in \mathcal {P}, i, j \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}\tag{27}
$$

$$
\beta_ {j} \geq \beta_ {i} + \Upsilon_ {i j} + s _ {j} - M _ {i j} \left(1 - \sum_ {\nu \in \mathcal {V}} x _ {i j} ^ {\nu}\right) \quad \forall i \in \mathcal {N}, j \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}\tag{28}
$$

$$
\alpha_ {\nu} \geq \beta_ {i} + \Upsilon_ {i, o _ {\nu}} + s _ {o _ {\nu}} - M _ {i, o _ {\nu}} \left(1 - x _ {i, o _ {\nu}} ^ {\nu}\right) \quad \forall i \in \mathcal {P} \cup \mathcal {D} \cup \mathcal {T}, \nu \in \mathcal {V}\tag{29}
$$

$$
\gamma_ {i} ^ {r} \leq p _ {i j} ^ {w} + M _ {i} \left(2 - q _ {i j} ^ {r w} - y _ {i j} ^ {r}\right) \quad \forall r \in \mathcal {P}, (i, j) \in \mathcal {F} ^ {r}, w \in \mathcal {K} ^ {i j}\tag{30}
$$

$$
\gamma_ {i} ^ {r} \geq p _ {i j} ^ {w} - M _ {i} \left(2 - q _ {i j} ^ {r w} - y _ {i j} ^ {r}\right) \quad \forall r \in \mathcal {P}, (i, j) \in \mathcal {F} ^ {r}, w \in \mathcal {K} ^ {i j}\tag{31}
$$

$$
\gamma_ {i} ^ {r} \leq \beta_ {i} + M _ {i} \left(1 - \sum_ {j \in \mathcal {P} \cup \mathcal {D}} y _ {i j} ^ {r}\right) \quad \forall r \in \mathcal {P}, i \in \mathcal {T}\tag{32}
$$

$$
\gamma_ {i} ^ {r} \geq \beta_ {i} - M _ {i} \left(1 - \sum_ {j \in \mathcal {P} \cup \mathcal {D}} y _ {i j} ^ {r}\right) \quad \forall r \in \mathcal {P}, i \in \mathcal {T}.\tag{33}
$$

Constraints (18)–(20) can be linearized in the same way as constraints (17) (i.e., (32) and (33)).

## 3.2. The second-stage decisions

Given an a priori routing solution vector x, the expected costs $\operatorname { E } [ \mathbf { Q } ( \pmb { x } , \ \pmb { \xi } , \ \eta ) ]$ can be computed in two steps. In Step 1, capacity violations of the PD vehicles are evaluated. As a consequence, some requests (including transferable ones) may not be served by the available PD vehicles due to given demand realizations and capacity restrictions. Hence, extra costs are required for outsourcing. Further in Step 2, for remaining set of requests that are supposed to be transferred, SLs’ capacity violations are verified. Each step is explained in detail below.

![](07-Ghilas-2016-Scenario_images/88544c1d1ee215f98127d1d2e029972471e53a486337fce6f332ae99fcfa6e0a.jpg)  
Fig. 3. An illustrative routing example of the PDPTW-SLSD.

Step 1: For PD vehicles, capacity violations might happen either (i) at the pickup node of a request r $( \mathsf { e } . \mathsf { g } . , \mathsf { p } _ { 1 }$ in Fig. 3), or (ii) at the transfer node of a request $t ^ { d } ,$ , which is a destination transfer node $( \mathbf { e . g . } , \ T _ { 1 } ^ { d }$ in Fig. 3). In either way, it is assumed that an outsourced vehicle (e.g., taxi) could deliver the request to its destination from the point of failure at a cost of $P _ { 1 } \Upsilon _ { l , r + n } , \forall l \in \{ p _ { 1 } , T _ { 1 } ^ { d } \}$ . Moreover, the destination node of r does not need to be visited and the shortened route leads to reduced operational costs.

Example. We now consider four possible situations: (i) let PD vehicle’s capacity be violated at node $p _ { 2 }$ (see Fig. 3). In this case, node $d _ { 2 }$ will not be visited as the demand from the origin $p _ { 2 }$ cannot be picked up by a PD vehicle. Hence, the transport service has to be outsourced. (ii) It is assumed that the vehicle’s capacity is violated at node $p _ { 1 }$ . Hence, no related nodes to request 1 are visited: $T _ { 1 } ^ { p } , \ T _ { 1 } ^ { d }$ , and $d _ { 1 } . ~ ( i i i )$ Let the capacity be violated at node $T _ { 1 } ^ { d } .$ . In this case, node $d _ { 1 }$ cannot be visited. (iv) Let the demand of request 1 be zero. Similarly to aforementioned cases, $T _ { 1 } ^ { p ^ { - } } , T _ { 1 } ^ { d } , d _ { 1 }$ cannot be visited. It is noted that, in cases (i)–(iii) the considered routes are shortened while incurring additional outsourcing costs, whereas case (iv) only leads to reduction in operational costs, due to lack of demand, thus no other related nodes need to be visited.

Step 2: As a result of the previous step, a restricted set of transferable requests $\overline { { \mathcal { P } } } ^ { t }$ is obtained. The capacity of SL service is only violated when the total demand of a set of transferable requests exceeds the capacity at a given scheduled departure time, i.e. $\begin{array} { r } { \sum _ { r \in \overline { { \mathcal { P } } } ^ { t } } \sum _ { ( a , b ) \in { \mathcal { F } } ^ { i j } } d _ { r } q _ { a b } ^ { r w } > k _ { i j } ~ \forall ~ ( i , ~ j ) \in \mathcal { E } , ~ w \in { \mathcal { K } } ^ { i j } } \end{array}$ . In such case, the excessive demand can be stored at the origin of the SL until the next scheduled departure. If waiting leads to violation of the time window constraints, or if the SL capacity on the next trip is exceeded, then the service is outsourced as in Step 1 (from the origin of the SL to the demand’s destination). The recourse cost of a given routing solution can be calculated as shown in Algorithm 1.

The recourse cost variable is initialized in Line 1. For each considered scenario (Line 3), a set of routes is also stored (Line 4) and a set of transferable requests from the given routing solution is selected (Line 6). Three cases of capacity violation of a PD vehicle may exist as explained earlier. The penalty cost for not serving a request is updated in Lines 13 and 16. Once the routes are shortened, routing cost savings are updated in Line 21, where c(X) is the routing cost of the shortened set of routes.

The extra costs incurred by exceeding SLs capacities is updated in get $S L C o s t ( \mathcal { P } ^ { t } )$ (Line 22). More specifically, for each SL (i, $j ) \in \mathcal { E } , w \in \mathcal { K } ^ { i j }$ with violated SL capacity, the requests with the latest end time window of the corresponding delivery nodes (i.e., excess demand) are re-scheduled for the next trip on the same SL service. If time windows or SL capacity constraints are violated, the service is outsourced at an extra cost dependent on the distance to destination of the exceeded demand. As a result, the vehicle routes are shortened, i.e., the end-of-the-line station and the corresponding delivery node are not visited. Finally, line 23 updates the sample average approximation function and line 24 returns the expected recourse costs for a given routing solution x and a set of scenarios $\xi .$

## 3.3. An illustrative example

We now provide an example to show the necessity of using recourse actions during the transport planning. Assume an instance with two vehicles, six requests and two transfer nodes $( \mathrm { i } . \mathsf { e } . , T _ { 1 }$ and $T _ { 2 } )$ . Nodes $p _ { 1 } , \ldots , p _ { 6 }$ represent pickup locations and nodes $d _ { 1 } , \ldots , d _ { 6 }$ represent the corresponding delivery locations. For simplicity reasons, assume the traveling time on each arc (including SLs) to be one time unit. Two different solutions with the same routing costs are shown in Fig, 4 These solutions differ in terms of recourse costs. The numbers on top (or bottom) of each node, which are shown in italic, represent the departure times from the corresponding nodes and the numbers on top of dotted arrows indicate the request flows on the SLs.

We note that throughout the paper we refer to stochastic solutions as the ones that are generated using the proposed methodology in this paper, whose objective function is to minimize the routing and the recourse expected costs. On the other hand, deterministic solutions are generated using the methodology proposed in Ghilas et al. (2016b) (using average demands), which disregards the cost of recourse actions, thus minimizing routing and SL costs only.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 1: The generic structure of Recourse(x, ξ, η) procedure

input : A routing solution x, a set of scenarios ξ
output: The average recourse cost E[Q(x, ξ, η)]

1 Initialize E[Q(x, ξ, η)] ← 0
2 Let c(x) be the routing costs of solution x
3 for scenario s in ξ do
4    X ← x
5    cost ← 0
6    $\overline{P}^t$ ← set of transferable requests in x
7    for each node i in X do
8    r ← getRelatedRequest(i)
9    if i ∈ P and capacity violated then
10    X ← X \ i + n
11    X ← X \ ($T_i^o \cup T_i^d$)
12    $\overline{P}^t$ ← $\overline{P}^t$ \ i
13    cost ← cost + $P_1 \Upsilon_{i,i+n}$
14    else if i is a destination transfer node and related request r is picked up and capacity violated then
15    X ← X \ r + n
16    cost ← cost + $P_1 \Upsilon_{i,r+n}$
17    else if i ∈ P and $d_i$ = 0 then
18    X ← X \ i + n
19    X ← X \ ($T_i^o \cup T_i^d$)
20    $\overline{P}^t$ ← $\overline{P}^t$ \ i
21    cost ← cost - c(x) + c(X)
22    cost ← cost + getSLCost($\overline{P}^t$, η)
23    set E[Q(x, ξ, η)] ← E[Q(x, ξ, η)] + $\frac{cost}{|\xi|}$
24 return E[Q(x, ξ, η)]
</div>

![](07-Ghilas-2016-Scenario_images/99d010c1b2543a3a8ac8bb5c7ee0e53429dbe57568abb58094fcf5b1d5bdff1c.jpg)  
Fig. 4. Two illustrative solutions with the same routing cost.

In both cases, five requests, i.e., 1, 3, 4, 5 and 6, are being transported through SLs. However, the expected costs of these solutions differ. More specifically, the solution shown in Fig. 4a has a lower recourse cost as Vehicle 1 first picks up requests 1, 3, and 4 and ships them on the SL service $( \mathrm { i } . { \mathsf { e } } . , T _ { 1 } - T _ { 2 }$ , see dashed arrows in Fig. 4a). Then, Vehicle 1 picks up request 6 (which was picked up by Vehicle 2 and shipped from $T _ { 2 } )$ from $T _ { 1 }$ , and finally requests 5 and 2 from their pickup locations. Request 5 is shipped on the SL from $T _ { 1 }$ . In this case, the total expected cost of this solution is found to be 385.40 units for a given set of scenarios.

On the other hand, in the deterministic solution (Fig. 4b), Vehicle 1 first picks up requests 1, 3, 4 from their pickup locations and request 6 from station $T _ { 1 }$ . Then the vehicle delivers request 6 to its destination node 13 and picks up requests 5 and 2 from their pickup locations to transfer them on the SL by visiting the transfer node $T _ { 1 }$ . This solution has a total expected cost of 462.48 units and the difference from the stochastic solution is triggered by the lack of available capacity at the pickup location of request 5. Therefore, one can observe that in addition to the routing decisions, a sequence of actions (i.e., departure times on the SLs) is also important when considering the expected cost of a transport plan.

## 4. The ALNS-based solution methodology for the PDPTW-SLSD

In this section, we provide a solution methodology for the PDPTW-SLSD. As aforementioned, our approach consists of a scenario-based SAA framework combined with an ALNS algorithm.

## 4.1. The sample average approximation method

The SAA is an iterative sampling approach proposed by Kleywegt et al. (2001) to solve stochastic discrete optimization problems, where the number of scenarios is very large. Given a large scenario set $\Omega ^ { ' }$ , which is intractable, the SAA consists of solving a set of smaller and tractable problems (referred to as SAA problems) with samples of size $| \Omega | \ll | \Omega ^ { \prime } |$ . For the PDPTW-SLSD, a sample (or a scenario) contains a demand vector for the considered requests, given probability distributions. The SAA procedure used to calculate the approximate optimality gap (or SAA gap) for the PDPTW-SLSD is as follows:

1. The algorithm takes the following input: (i) a sample size | | to generate the SAA solution, (ii) a larger set of scenarios $\Omega ^ { ' }$ to approximate the value of the optimal solution of the SAA problem, and (iii) the number of iterations M.

2. For $m = 1  M ,$ , do the following:

2.1 Generate a sample set and solve the corresponding SAA problem to obtain the objective value $\nu _ { \Omega } ^ { m }$ and the solution $x ^ { m }$ by using the proposed ALNS algorithm (see Section 4.2)

2.2 Using Algorithm 1, determine the upper bound on the SAA solution for the generated sample $\Omega ^ { \prime }$ , which is denoted by $\nu _ { \mathrm { { O } ^ { \prime } } } ( x ^ { m } )$ . Let xˆ be the solution that has the best value of the upper bound $\nu _ { \Omega ^ { \prime } } ( \hat { x } )$ found after a number of iterations The variance of this estimated upper bound can be computed as follows:

$$
\sigma_ {\Omega^ {\prime}} ^ {2} (\hat {x}) = \frac {1}{| \Omega^ {\prime} | (| \Omega^ {\prime} - 1 |)} \sum_ {i \in \Omega^ {\prime}} \left(\nu_ {i} (\hat {x}) - \nu_ {\Omega^ {\prime}} (\hat {x})\right) ^ {2},\tag{34}
$$

where $\nu _ { i } ( \hat { x } )$ is the objective function value of the solution xˆ for scenario i.

2.3 Calculate the average of the objective function values obtained in previous iterations, denoted by $\hat { \nu } _ { \Omega } ^ { m }$ , and their corresponding variance as shown below.

$$
\hat {v} _ {\Omega} ^ {m} = \frac {1}{m} \sum_ {i = 1} ^ {m} v _ {\Omega} ^ {i},\tag{35}
$$

$$
\sigma_ {\hat {v} _ {\Omega} ^ {m}} ^ {2} = \frac {1}{m (m - 1)} \sum_ {i = 1} ^ {m} \left(v _ {\Omega} ^ {i} - \hat {v} _ {\Omega} ^ {m}\right) ^ {2}.\tag{36}
$$

The value $\hat { \nu } _ { \Omega } ^ { m }$ is a statistical lower bound for the optimal solution value of the sample $\Omega ^ { \prime }$ as given in Kleywegt et al. (2001). To the best of our knowledge, this is the only way that was used in the literature of approximating the statistical lower bound (see, e.g., Verweij et al., (2003); Adulyasak et al., (2015); Demir et al., (2015a)) in SAA.

2.4 Calculate the SAA gap $\epsilon ^ { S A A } ( \Omega , \Omega ^ { \prime } )$ and the variance of the gap as follows:

$$
\epsilon^ {S A A} (\Omega , \Omega^ {'}) = \nu_ {\Omega^ {'}} (\hat {x}) - \hat {\nu} _ {\Omega} ^ {m}\tag{37}
$$

$$
\sigma_ {\epsilon^ {S A A} (\Omega , \Omega^ {\prime})} ^ {2} = \sigma_ {\Omega^ {\prime}} ^ {2} (\hat {x}) + \sigma_ {\hat {v} _ {\Omega} ^ {m}} ^ {2}.\tag{38}
$$

The best value of $\epsilon ^ { S A A } ( \Omega , \Omega ^ { \prime } )$ and its corresponding $\sigma _ { \epsilon ^ { S A A } ( \Omega , \Omega ^ { \prime } ) } ^ { 2 }$ are stored during the process.

3. Return the best solution xˆ.

In the next subsection, we provide details of the ALNS heuristic algorithm, which is used to generate routing solutions of minimum total expected cost. Note that Algorithm 1 is used within ALNS to compute the recourse cost of a considered solution.

## 4.2. The ALNS heuristic

The ALNS heuristic was first used in Røpke and Pisinger (2006); Pisinger and Røpke (2007) to solve several variants of the VRPs. The ALNS iteratively applies a set of removal and insertion operators to modify the solution. The operators are dynamically selected according to their past and current performances. The general framework of the ALNS is given in Algorithm 2.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Algorithm 2: The ALNS framework with simulated annealing.

input : Removal operators D, insertion operators I, temperature T
output:  $X_{best}$ 

1 Generate an initial solution  $X_{current}$ , initialize  $X_{best} \leftarrow X_{current}$ 

2 for a number of iterations do

3 Select a removal operator  $d^{*} \in D$  with probability  $P_{d}^{t}$  and apply it to  $X_{current}$  to get the partially destroyed solution  $X^{d}$ 

4 Select an insertion operator  $i^{*} \in I$  with probability  $P_{i}^{t}$  and apply it to  $X^{d}$  to get a new solution  $X_{new}$ 

5 if  $c(X_{new}) &lt; c(X_{current})$  then

6  $X_{current} \leftarrow X_{new}$ 

7 if  $c(X_{current}) &lt; c(X_{best})$  then

8  $X_{best} \leftarrow X_{current}$ 

9 else

10 if a random number  $\epsilon \in [0, 1] &lt; e^{-(c(X_{new}) - c(X_{current})) / T}$  then

11  $X_{current} \leftarrow X_{new}$ 

12 Update operator probabilities and temperature T
</div>

Given an initial solution $X _ { c u r r e n t } ,$ , a number of requests are removed from the solution. Afterwards, these requests are re-inserted back to the partially-destroyed solution using a chosen insertion operator. A new solution $X _ { n e w }$ is obtained and evaluated. Three possibilities exist: (i) if the new solution is better than $X _ { c u r r e n t }$ , then it is accepted; (ii) if the new solution is worse than $X _ { n e w } ,$ but the simulated annealing criterion is satisfied, then it is accepted; finally, (iii) the solution is rejected At every iteration, the best solution $X _ { b e s t }$ found so far is updated. The probabilities of the operators and the temperature T are updated.

The ALNS algorithm for the deterministic PDPTW-SL is first proposed by Ghilas et al. (2016b). The authors proposed effective neighborhood operators to investigate the solution space and an eficient feasibility-check mechanism. In this paper, we extend the ALNS proposed by Ghilas et al. (2016b) to solve the SAA problems of the PDPTW-SLSD as discussed in Section 4.1. The performance of the algorithm is enhanced by adapting several operators in stochastic setting. The details of the algorithm used are given in the following subsections.

## 4.2.1. Initial solution

To obtain an initial solution to the problem, a greedy insertion heuristic is used. For every vehicle an empty route is constructed with the appropriate capacity level and depot. The requests are stored in a list and are greedily inserted one by one in a random order (greedy insertion). The objective is to minimize (1) and (2), namely routing and recourse costs (see Algorithm 1) simultaneously. At this stage, we assure the feasibility in terms of SL schedule and time windows.

## 4.2.2. Removal operators

We use ten removal operators in the proposed ALNS algorithm. As aforementioned, the aim of the removal stage is to partially destroy a given solution X, by removing $\phi$ requests and adding them to a removal list . All ten operators were inspired or adapted from Røpke and Pisinger (2006); Demir et al. (2012) and Ghilas et al. (2016b). We first present the so-called stochastic removal operators.

Shaw removal (SR): The SR operator removes a number of requests that are related in a predefined way and therefore are easy to change. The procedure first randomly selects one request $r _ { 1 }$ and then adds it to the removal list $\mathcal { L } .$ Let $l _ { r _ { 1 } , r _ { 2 } } = - 1$ if two nodes, one related to $r _ { 1 } ~ ( \mathrm { i . e . , } ~ r _ { 1 } ~ \mathrm { o r } ~ r _ { 1 } + n )$ and another to $r _ { 2 } ( \mathrm { i } . \mathrm { e } . , r _ { 2 }$ or $r _ { 2 } + n )$ are in the same route, and 1 otherwise. SR selects the request $r ^ { * } = a r g m i n _ { r _ { 2 } \in \mathcal { P } } \{ \Pi _ { 1 } [ \Upsilon _ { r _ { 1 } , r _ { 2 } } + \Upsilon _ { r _ { 1 } + n , r _ { 2 } + n } ] + \Pi _ { 2 } [ | \beta _ { r _ { 1 } } - \beta _ { r _ { 2 } } | + | \beta _ { r _ { 1 } + n } - \beta _ { r _ { 2 } + n } | ] + \Pi _ { 3 } l _ { r _ { 1 } , r _ { 2 } } + \Pi _ { 4 } [ | \beta _ { r _ { 2 } + n } - \beta _ { r _ { 2 } + n } | ] + a \tan ^ { 2 } \beta _ { r _ { 1 } + n } - \beta _ { r _ { 2 } + n } \} ,$ $\Pi _ { 4 } ( | \overline { { { d } } } _ { r _ { 1 } } - \overline { { { d } } } _ { r _ { 2 } } | + | \sigma _ { r _ { 1 } } ^ { 2 } - \sigma _ { r _ { 2 } } ^ { 2 } | ) \}$ , where $\Pi _ { 1 } { - } \Pi _ { 4 }$ are the normalize weights, $\overline { { d } } _ { r _ { 1 } }$ and $\sigma _ { r _ { 1 } } ^ { 2 }$ are the mean of the demand of request $r _ { 1 }$ given the probability distribution and its variance, respectively.

Demand-based removal (DR): DR is a special case of SR with $\Pi _ { 4 } = 1$ , and $\Pi _ { 1 } = \Pi _ { 2 } = \Pi _ { 3 } = 0 .$

Worst expected removal (WER): This operator removes a number of requests with the highest total expected costs. The cost is determined as follows: for a given routing solution, the cost of request r is the difference in the objective function between two solutions, namely one where request r is served and the solution were request r is not served.

We now briefly present so-called deterministic removal operators. For more details, the reader is referred to Ghilas et al. (2016b).

Random removal (RR): This operator randomly removes a number of requests from the solution. Random selection helps diversifying the search.

• <sup>Route removal (ROR): This operator removes a randomly selected route from the solution. The ROR sequentially removes</sup> a node j from the selected route until all nodes are removed. The related nodes of j, i.e., its pickup, delivery node, or transfer nodes are also removed.

• <sup>Worst-distance removal (WDR): This operator removes a number of requests, that require long detours to visit their cor-</sup> responding pickup and delivery nodes in the given routes. In other words, this operator iteratively removes request $r ^ { * } = a r g m a x _ { r \in \mathcal { P } } \{ | \Upsilon _ { i - 1 , r } + \Upsilon _ { r , i + 1 } + \Upsilon _ { j - 1 , r + n } + \Upsilon _ { r + n , j + 1 } | \}$ , where i − 1 and j − 1, are predecessors and i + 1 and $j + 1$ successors of the pickup and delivery nodes, respectively.

• <sup>Late-arrival removal (LAR): Operator LAR removes a number of requests with the largest deviation of the service start</sup> time from l and $l _ { r + n } .$ , respectively. In other words, the procedure iteratively removes a request $r ^ { * } = a r g m a x _ { r \in \mathcal { P } } \{ | [ \beta _ { r } -$ $s _ { r } - l _ { r } ] + [ \beta _ { r + n } - s _ { r + n } - l _ { r + n } ] | \}$ , where $\beta _ { i }$ is the departure time from node i. The idea is to avoid delayed service start times or long waiting times.

• <sup>Proximity-based removal (PR): This operator is a special case of SR operator with</sup> $\Pi _ { 1 } = 1$ , and $\Pi _ { 2 } = \Pi _ { 3 } = \Pi _ { 4 } = 0 .$

Time-based removal (TR): The operator is a special case of the SR with $\Pi _ { 2 } = 1$ , and $\Pi _ { 1 } = \Pi _ { 3 } = \Pi _ { 4 } = 0 .$

Historical knowledge node removal (HR): This neighborhood operator stores the position cost of every request r. This cost is calculated as $c _ { r } = \Upsilon _ { i - 1 , r } + \Upsilon _ { r , i + 1 } + \Upsilon _ { j - 1 , r + n } + \Upsilon _ { r + n , j + 1 }$ at every iteration. The best position cost $c _ { r } ^ { * }$ of request r is updated to be the minimum of all $c _ { r }$ values calculated. The HR operator then selects the request $r ^ { \ast }$ with the maximum deviation from its best position cost, i.e., $r ^ { * } = a r g m a x _ { r \in \mathcal { P } } \{ c _ { r } - c _ { r } ^ { * } \}$ and adds it to .

## 4.2.3. Insertion operators

The insertion operators repair a partially-destroyed solution by re-inserting the requests from the removal list back into the routes. Five construction heuristics are used as insertion operators and these are described as follows:

Greedy insertion (GI): The GI repeatedly inserts a request (both pickup and delivery nodes) in the cheapest possible way. The requests are chosen randomly from . Let $\Delta _ { I _ { i } J _ { i } } ^ { r }$ be the objective function value when the pickup node of r is inserted in route I (position i) and its corresponding delivery node is inserted in route J (position j). Thus, $\Delta _ { I _ { i } J _ { i } } ^ { r } * = a r g m i n \{ \Delta _ { I _ { i } J _ { i } } ^ { r } \}$

Greedy insertion with noise function (GIN): GIN is an extension of GI with a modified cost function NewCost = Actual Cost $+ ~ \bar { d } \mu \epsilon$ , where d<sup>¯</sup> is the longest distance between nodes, μ is a noise parameter used to diversify the cost function and is set equal to 0.1, and  is a random number between [−1, 1].

• <sup>Second-best insertion (SI): This operator selects the second best insertion for all considered requests. The SI helps diversify</sup> the search.

Second-best insertion with noise function (SIN): This operator is an extension of SI and uses the same cost function as the GIN operator.

Best out of λ feasible insertions (λFI): For each selected request, this operator selects the best option found after first λ feasible insertions. The constant λ is a random number ∈ [1, ψ]. For each request $r \in { \mathcal { L } } .$ this operator generates a set of possible insertions by assuring the precedence constraints. This set is then sorted in increasing order based on the insertion cost (distance-based) and the search starts following the first cheapest insertion criterion.

Furthermore, five variants of the aforementioned operators are used, where is a sorted list, in terms of time flexibility $( { \mathrm { i . e . } }$ . the least flexible first) of requests. The flexibility of request r is calculated as $| u _ { r + n } - l _ { r } |$ , We note that unlike classical pickup and delivery problem, the PDPTW-SLSD may have the pickup and delivery nodes of certain requests positioned in different routes. This requires a solution to include at least one SL. To handle this, the procedure introduced in Ghilas et al. (2016b) is used to insert transfer nodes by considering the precedence constraints. In addition to aforementioned, checking the feasibility with respect to time windows is not straightforward and therefore we use the procedure introduced in Ghilas et al. (2016b) to do that. Finally, in order to avoid redundant calculations, time windows are used to check for feasible positions as described in Braekers et al. (2014).

## 4.2.4. Adaptive score adjustment procedure

A roulette-wheel mechanism controls the selection of the removal and insertion operators. Initially, each removal and insertion operators are assigned a probability (i.e., the probability of each is set to 0.1). After $N _ { w }$ iterations, the probabilities are updated using the following formula: $P _ { d } ^ { t + 1 } = P _ { d } ^ { t } \left( 1 - r _ { p } \right) + r _ { p } \pi _ { i } / \omega _ { i }$ , where $r _ { p }$ is the roulette-wheel constant, $\pi _ { i }$ and $\omega _ { i }$ are the score and the number of times operator i was used during the last $N _ { w }$ iterations, respectively. The score of operators measures their effect on the search progress. If a new best solution is found, the score of the removal and insertion operators is increased by $\sigma _ { 1 }$ . If the new solution outperforms the current solution, the score is increased by $\sigma _ { 2 } .$ . If the solution quality deteriorates but the solution is accepted, the score is increased by $\sigma _ { 3 }$

## 5. Computational experiments

This section presents the results of computational experiments performed to assess the performance of the proposed methodology. We first describe the instance characteristics and the parameters used.

## 5.1. Data and experimental setting

Three sets of instances R, C, and RC were adapted from Ghilas et al. (2016a) to consider stochastic demands. Each instance contains up to three SLs in a triangular topology. The SLs have a frequency of one departure every 30 time units. Each instance contains up to 40 requests (i.e., up to 40 pick-up and 40 delivery nodes) over 200 × 200 Euclidean space. Instances are named as $G _ { - } n _ { - } s l _ { - } \nu ,$ where G is the geographic distribution of the customers, n is the number of to-be-served requests, sl is the number of available SLs, and v is the number of available PD vehicles. By geographic distribution G we mean the following: C – clustered request nodes around transfer nodes, R – uniform-randomly distributed request nodes, and finally RC – randomly clustered nodes. More specifically, C has nodes positioned within at most 30 time units to one of the three available transfer nodes whereas RC has nodes within 80 time units respectively. In all cases, two depots with up to six PD vehicles each are considered.

The planning horizon is set to 600 time units. The time windows are randomly generated with an average width of 40 units. Service times are set to at most three time units. The request demands are assumed to follow a discrete triangular distribution for a given minimum value a, mean b and maximum value c. The capacity of each PD vehicle is generated between six and nine units. The carrying capacity on the considered SLs is assumed to be five demand units. The instances can be found on the web page of SmartLogisticsLab (2016).

The parameters used in the computational experiments are shown in Table 1. Heuristic-specific parameters have been assigned the same values as in Ghilas et al. (2016b), which were used to solve the deterministic PDPTW-SL. The settings used generally worked well on the test problems with uncertain demands. We assume a driving time unit cost for PD vehicles to be 0.5 units. It seems quite reasonable when considering the driver’s wage, fuel consumption, insurance, taxes, and etc. Furthermore, the cost of using SL service is set to 1 unit and it includes transportation, handling and storage costs The recourse cost for outsourcing the service, which is considered per driving time unit, is assumed to be 3 units.

## 5.2. The performance of the operators

To show the number of times each removal and insertion operator was called within the ALNS, we give relevant information in Tables 2 and 3. These tables indicate the usage frequency as a percentage of the total number of iterations, and the total time spent (shown in parenthesis) of each operator, respectively. We note that the results are obtained using only three instances of different sizes

Table 1  
Parameters used in the methodology.

<table><tr><td>Notation</td><td>Definition</td><td>Value</td><td>Notation</td><td>Definition</td><td>Value</td></tr><tr><td> $\theta_v$ </td><td>Cost of vehicle v</td><td>0.5</td><td> $|\Omega'|$ </td><td>The size of the large set of scenarios</td><td>10,000</td></tr><tr><td> $\eta_{ij}$ </td><td>Cost of SL (i, j)</td><td>1</td><td> $|\Omega|$ </td><td>The size of the small set of scenarios</td><td>60</td></tr><tr><td> $P_1$ </td><td>Cost for outsourcing</td><td>3</td><td>M</td><td>Number of SAA iterations</td><td>10</td></tr><tr><td> $k_{ij}$ </td><td>Capacity of SL (i, j)</td><td>5</td><td> $\sigma_1$ </td><td>Score for new best solution</td><td>1</td></tr><tr><td></td><td>Number of ALNS iterations</td><td>10,000</td><td> $\sigma_2$ </td><td>Score for improving the current solution</td><td>3</td></tr><tr><td>λ</td><td>Number of feasible insertions (λFI)</td><td>30</td><td> $\sigma_3$ </td><td>Score for accepting a worse solution</td><td>5</td></tr></table>

Table 2  
Number of iterations as a percentage of the total number iterations and the CPU times required by the removal operators

<table><tr><td>Instance</td><td>RR</td><td>ROR</td><td>LAR</td><td>WDR</td><td>SR</td><td>PR</td><td>DR</td><td>TR</td><td>HR</td><td>WER</td></tr><tr><td>C10_1_4</td><td>7.89 (0.00)</td><td>10.52 (0.00)</td><td>21.05 (0.01)</td><td>5.26 (0.00)</td><td>5.26 (0.00)</td><td>5.26 (0.00)</td><td>7.89 (0.00)</td><td>5.26 (0.00)</td><td>10.52 (0.00)</td><td>21.05 (0.01)</td></tr><tr><td>RC15_1_6</td><td>3.44 (0.00)</td><td>6.89 (0.00)</td><td>1.72 (0.00)</td><td>22.41 (0.01)</td><td>8.62 (0.01)</td><td>6.89 (0.00)</td><td>5.17 (0.00)</td><td>8.62 (0.01)</td><td>24.16 (0.01)</td><td>12.08 (0.01)</td></tr><tr><td>R20_1_8</td><td>1.72 (0.00)</td><td>3.12 (0.00)</td><td>10.93 (0.01)</td><td>12.49 (0.01)</td><td>1.56 (0.00)</td><td>7.81 (0.01)</td><td>12.49 (0.01)</td><td>4.68 (0.00)</td><td>14.06 (0.01)</td><td>31.14 (0.02)</td></tr></table>

Table 3  
Number of iterations as a percentage of the total number iterations and the CPU times required by the insertion operators.

<table><tr><td>Instance</td><td>GI</td><td>SI</td><td>GIN</td><td>SIN</td><td> $\lambda$ FI</td><td>oGI</td><td>oSI</td><td>oGIN</td><td>oSIN</td><td>o $\lambda$ FI</td></tr><tr><td>C10_1_4</td><td>5.89 (0.89)</td><td>7.62 (1.15)</td><td>8.22 (1.24)</td><td>3.64 (0.92)</td><td>3.64 (0.55)</td><td>22.07 (3.33)</td><td>17.25 (2.30)</td><td>17.11 (3.68)</td><td>3.66 (0.90)</td><td>10.90 (1.94)</td></tr><tr><td>RC15_1_6</td><td>2.86 (0.36)</td><td>6.13 (0.78)</td><td>6.26 (0.80)</td><td>1.64 (0.58)</td><td>1.85 (0.23)</td><td>26.29 (3.37)</td><td>22.24 (2.85)</td><td>19.04 (2.54)</td><td>1.18 (0.57)</td><td>12.51 (1.86)</td></tr><tr><td>R20_1_8</td><td>7.89 (2.83)</td><td>7.29 (2.51)</td><td>9.38 (2.99)</td><td>1.34 (0.51)</td><td>3.03 (0.97)</td><td>23.26 (7.43)</td><td>24.06 (7.68)</td><td>16.94 (5.41)</td><td>1.27 (0.59)</td><td>5.54 (2.09)</td></tr></table>

Table 4  
Comparison between the PDPTW-SD and the PDPTW-SLSD with different number of SLs

<table><tr><td rowspan="2">Instance</td><td colspan="2">PDPTW-SD</td><td colspan="3">SL = 1</td><td colspan="3">SL = 2</td><td colspan="3">SL = 3</td><td rowspan="2">CPU (s)</td></tr><tr><td>E(x)</td><td>#vehs</td><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td><td>#SLs</td></tr><tr><td>C10_SL_4</td><td>966.98</td><td>3</td><td>931.65</td><td>4</td><td>4</td><td>924.55</td><td>4</td><td>8</td><td>860.94</td><td>4</td><td>12</td><td>378</td></tr><tr><td>C15_SL_6</td><td>1440.96</td><td>4</td><td>1363.13</td><td>5</td><td>9</td><td>1336.68</td><td>4</td><td>19</td><td>1290.08</td><td>6</td><td>23</td><td>863</td></tr><tr><td>C20_SL_8</td><td>1291.81</td><td>5</td><td>1229.41</td><td>6</td><td>6</td><td>1223.27</td><td>7</td><td>12</td><td>1163.13</td><td>7</td><td>18</td><td>1582</td></tr><tr><td>C25_SL_8</td><td>1742.78</td><td>6</td><td>1538.03</td><td>7</td><td>13</td><td>1536.38</td><td>7</td><td>13</td><td>1449.71</td><td>7</td><td>22</td><td>2111</td></tr><tr><td>C40_SL_8</td><td>1978.31</td><td>8</td><td>1930.53</td><td>8</td><td>9</td><td>1906.94</td><td>7</td><td>21</td><td>1851.45</td><td>8</td><td>20</td><td>2532</td></tr><tr><td>RC10_SL_4</td><td>1105.20</td><td>4</td><td>988.49</td><td>3</td><td>3</td><td>987.90</td><td>3</td><td>3</td><td>954.52</td><td>4</td><td>5</td><td>403</td></tr><tr><td>RC15_SL_6</td><td>1614.19</td><td>6</td><td>1614.42</td><td>6</td><td>0</td><td>1605.58</td><td>6</td><td>1</td><td>1580.85</td><td>6</td><td>2</td><td>418</td></tr><tr><td>RC20_SL_8</td><td>2038.22</td><td>7</td><td>1815.02</td><td>7</td><td>6</td><td>1779.64</td><td>6</td><td>12</td><td>1746.79</td><td>7</td><td>10</td><td>1144</td></tr><tr><td>RC25_SL_8</td><td>2196.56</td><td>8</td><td>2179.62</td><td>8</td><td>5</td><td>2057.69</td><td>8</td><td>14</td><td>2000.96</td><td>8</td><td>14</td><td>1823</td></tr><tr><td>RC40_SL_12</td><td>2940.16</td><td>11</td><td>2898.77</td><td>10</td><td>2</td><td>2892.61</td><td>11</td><td>7</td><td>2796.76</td><td>11</td><td>8</td><td>2753</td></tr><tr><td>R10_SL_4</td><td>874.60</td><td>4</td><td>873.01</td><td>4</td><td>2</td><td>871.18</td><td>4</td><td>2</td><td>870.54</td><td>4</td><td>4</td><td>209</td></tr><tr><td>R15_SL_6</td><td>1535.15</td><td>6</td><td>1530.84</td><td>6</td><td>0</td><td>1513.99</td><td>6</td><td>1</td><td>1494.42</td><td>6</td><td>6</td><td>475</td></tr><tr><td>R20_SL_8</td><td>2179.94</td><td>8</td><td>2179.58</td><td>8</td><td>0</td><td>2119.65</td><td>8</td><td>3</td><td>2087.96</td><td>8</td><td>3</td><td>939</td></tr><tr><td>R25_SL_8</td><td>2656.76</td><td>8</td><td>2583.78</td><td>8</td><td>4</td><td>2549.66</td><td>8</td><td>6</td><td>2549.51</td><td>8</td><td>6</td><td>1878</td></tr><tr><td>R40_SL_12</td><td>3651.34</td><td>10</td><td>3633.18</td><td>11</td><td>3</td><td>3568.82</td><td>10</td><td>7</td><td>3555.55</td><td>11</td><td>6</td><td>2579</td></tr><tr><td>Average</td><td>1880.86</td><td>7</td><td>1819.30</td><td>7</td><td>4</td><td>1791.64</td><td>7</td><td>9</td><td>1750.21</td><td>7</td><td>11</td><td>1339</td></tr></table>

Table 2 shows that WDR, HR and WER are the most frequently used operators. The first operator is used to consider traveling distance aspect of the problem whereas the HR and WER operators consider the objective function value (including uncertainty aspect) of the PDPTW-SLSD.

Table 3 shows that the most frequently used insertion operators are oGI, oSI and oGIN. Ordered insertion operators tend to perform better than randomly-ordered ones. Furthermore, insertion operators with noise functions are used less than the operators without noise function.

## 5.3. Comparison between the PDPTW-SD and the PDPTW-SLSD

In this section, we identify the effects of using SLs on the total operational costs (including expected recourse costs). Table 4 shows the obtained results for four different scenarios: (i) the classical PDPTW with stochastic demands, where no transfers are allowed, (ii)–(iv) the PDPTW-SLSD with one, two and three available SLs. The results indicate the average value over the 10 runs of the algorithm. Column E(x) indicates the total expected cost, #vehs shows the number of vehicles used, and finally #SLs indicates the number of demand units (i.e., mean value of the given probability distribution of each request) that used SL services. Finally, the average CPU time needed to solve the PDPTW-SLSD is shown in the last column.

According to the obtained results, the flexibility of using SLs as a part of transport plan leads to reasonable amount of operational cost savings. More specifically, on average, the total expected costs can be decreased by 7%. In some cases (e.g., RC20\_3\_8) using SLs may even lead to 14% cost savings. However, in some cases (e.g., RC15\_1\_8), the integrated networks do not lead to any benefits as SLs are not used. There may be several reasons for not using the available SLs. For example: time windows of the requests may not have suficient slack time for using SLs, or the pickup and delivery nodes are close to the same transfer node. Fig. 5 illustrates the average cost savings by considering all three scenarios (i.e., 1-, 2-, and 3-SLs) on three instance sets (C, RC, and R).

As can be observed from Table 4 and Fig. 5, if more request nodes are clustered around the transfer nodes, larger operational cost savings can be achieved. More specifically, integrated networks yield larger benefits in C and RC instances (i.e., up to 16% and 14%, respectively), compared to R instances (i.e., up to 4%). In addition, the more SLs are available, the larger integration between the transportation networks is, hence larger cost savings can be achieved. In other words, all instance sets with one available SL lead to more costly solutions, compared to the 2-SLs and 3-SLs cases. It can be observed in Table 4 that the more SLs are available, the more freight units are served using public transportation services, thus decreasing the expected costs.

## 5.4. The relationship between SL capacity and total expected costs

In this section, we investigate the effect of SLs capacity on the total expected costs. We test three scenarios with different SLs capacity: five, 10, 15 demand units. The average results out of ten runs of the algorithm are shown in Table 5.

On average, one can observe a trend (Fig. 6), which indicates that larger SL service capacity lead to fewer violations, hence fewer recourse actions needed to tackle SL service capacity violations. With an extra capacity, the PDPTW-SLSD solutions become cheaper (up to 0.44%) and slightly more freight units are shipped via SLs.

It is important to note that, in some cases (e.g., RC15\_1\_6), statistically insignificant difference in terms of total expected cost can be observed. This is explained by the fact that each solution is evaluated on different sets of independently generated scenarios for a given demand distribution.

![](07-Ghilas-2016-Scenario_images/de3553d1c68b611498ccd71b1c39cf3f415b0b849e4e6bc96772949286b93d2d.jpg)  
Fig. 5. Average savings by using different number of SLs

Table 5  
The effect of SLs capacity on the total expected operational costs

<table><tr><td rowspan="2">Instance</td><td colspan="3"> $k_{ij}=5$ </td><td colspan="3"> $k_{ij}=10$ </td><td colspan="3"> $k_{ij}=15$ </td></tr><tr><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td><td>#SLs</td></tr><tr><td>C10_1_4</td><td>931.65</td><td>4</td><td>4</td><td>926.23</td><td>4</td><td>5</td><td>926.23</td><td>4</td><td>5</td></tr><tr><td>C15_1_6</td><td>1363.13</td><td>5</td><td>9</td><td>1361.08</td><td>5</td><td>9</td><td>1361.89</td><td>5</td><td>9</td></tr><tr><td>C20_1_8</td><td>1229.41</td><td>6</td><td>6</td><td>1218.96</td><td>6</td><td>6</td><td>1218.98</td><td>6</td><td>6</td></tr><tr><td>C25_1_8</td><td>1538.03</td><td>7</td><td>13</td><td>1522.38</td><td>7</td><td>13</td><td>1522.39</td><td>7</td><td>13</td></tr><tr><td>C40_1_8</td><td>1930.53</td><td>8</td><td>9</td><td>1894.53</td><td>8</td><td>10</td><td>1868.89</td><td>8</td><td>10</td></tr><tr><td>RC10_1_4</td><td>988.49</td><td>3</td><td>3</td><td>986.35</td><td>3</td><td>3</td><td>986.80</td><td>3</td><td>3</td></tr><tr><td>RC15_1_6</td><td>1614.42</td><td>6</td><td>0</td><td>1615.27</td><td>6</td><td>0</td><td>1615.45</td><td>6</td><td>0</td></tr><tr><td>RC20_1_8</td><td>1815.02</td><td>7</td><td>6</td><td>1809.18</td><td>7</td><td>6</td><td>1809.95</td><td>7</td><td>6</td></tr><tr><td>RC25_1_8</td><td>2179.62</td><td>8</td><td>5</td><td>2177.85</td><td>8</td><td>6</td><td>2177.95</td><td>8</td><td>6</td></tr><tr><td>RC40_1_12</td><td>2898.77</td><td>10</td><td>2</td><td>2898.70</td><td>11</td><td>2</td><td>2898.41</td><td>10</td><td>3</td></tr><tr><td>R10_1_4</td><td>873.01</td><td>4</td><td>2</td><td>862.91</td><td>4</td><td>7</td><td>862.71</td><td>4</td><td>7</td></tr><tr><td>R15_1_6</td><td>1530.84</td><td>6</td><td>0</td><td>1530.60</td><td>6</td><td>0</td><td>1530.63</td><td>6</td><td>0</td></tr><tr><td>R20_1_8</td><td>2179.58</td><td>8</td><td>0</td><td>2179.27</td><td>8</td><td>0</td><td>2177.93</td><td>8</td><td>0</td></tr><tr><td>R25_1_8</td><td>2583.78</td><td>8</td><td>4</td><td>2582.18</td><td>8</td><td>4</td><td>2582.44</td><td>8</td><td>4</td></tr><tr><td>R40_1_12</td><td>3633.18</td><td>11</td><td>3</td><td>3628.10</td><td>10</td><td>4</td><td>3628.72</td><td>11</td><td>5</td></tr><tr><td>Average</td><td>1819.30</td><td>7</td><td>4</td><td>1812.91</td><td>7</td><td>5</td><td>1811.29</td><td>7</td><td>5</td></tr></table>

![](07-Ghilas-2016-Scenario_images/d6e8ecc67706e8b1eae82151325c47e71126c2195735d68a53d94496f71607ab.jpg)  
Fig. 6. The effect of SLs capacity.

Table 6  
The effect of the SLs frequency on the total expected costs.

<table><tr><td rowspan="2">Instance</td><td colspan="3">7 units</td><td colspan="3">30 units</td><td colspan="3">180 units</td><td colspan="2">PDPTW-SD</td></tr><tr><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td></tr><tr><td>C10_1_4</td><td>905.53</td><td>4</td><td>8</td><td>931.65</td><td>4</td><td>4</td><td>932.30</td><td>4</td><td>4</td><td>966.98</td><td>3</td></tr><tr><td>C15_1_6</td><td>1361.64</td><td>5</td><td>9</td><td>1363.13</td><td>5</td><td>9</td><td>1374.10</td><td>4</td><td>9</td><td>1440.96</td><td>4</td></tr><tr><td>C20_1_8</td><td>1218.82</td><td>6</td><td>6</td><td>1229.41</td><td>6</td><td>6</td><td>1291.88</td><td>5</td><td>0</td><td>1291.81</td><td>5</td></tr><tr><td>C25_1_8</td><td>1527.91</td><td>7</td><td>13</td><td>1538.03</td><td>7</td><td>13</td><td>1665.44</td><td>7</td><td>5</td><td>1742.78</td><td>6</td></tr><tr><td>C40_1_8</td><td>1882.80</td><td>8</td><td>9</td><td>1930.53</td><td>8</td><td>9</td><td>1973.03</td><td>8</td><td>3</td><td>1978.31</td><td>8</td></tr><tr><td>RC10_1_4</td><td>987.22</td><td>3</td><td>3</td><td>988.49</td><td>3</td><td>3</td><td>1103.76</td><td>4</td><td>0</td><td>1105.20</td><td>4</td></tr><tr><td>RC15_1_6</td><td>1614.42</td><td>6</td><td>0</td><td>1614.42</td><td>6</td><td>0</td><td>1614.50</td><td>6</td><td>0</td><td>1614.19</td><td>6</td></tr><tr><td>RC20_1_8</td><td>1812.13</td><td>7</td><td>6</td><td>1815.02</td><td>7</td><td>6</td><td>2038.35</td><td>7</td><td>0</td><td>2038.22</td><td>7</td></tr><tr><td>RC25_1_8</td><td>2179.77</td><td>8</td><td>6</td><td>2179.62</td><td>8</td><td>5</td><td>2193.69</td><td>8</td><td>0</td><td>2196.56</td><td>8</td></tr><tr><td>RC40_1_12</td><td>2898.78</td><td>11</td><td>2</td><td>2898.77</td><td>10</td><td>2</td><td>2918.31</td><td>11</td><td>1</td><td>2940.16</td><td>11</td></tr><tr><td>R10_1_4</td><td>873.45</td><td>4</td><td>0</td><td>873.01</td><td>4</td><td>2</td><td>874.62</td><td>4</td><td>1</td><td>874.60</td><td>4</td></tr><tr><td>R15_1_6</td><td>1530.47</td><td>6</td><td>0</td><td>1530.84</td><td>6</td><td>0</td><td>1534.37</td><td>6</td><td>0</td><td>1535.15</td><td>6</td></tr><tr><td>R20_1_8</td><td>2176.10</td><td>8</td><td>0</td><td>2179.58</td><td>8</td><td>0</td><td>2179.13</td><td>8</td><td>0</td><td>2179.94</td><td>8</td></tr><tr><td>R25_1_8</td><td>2583.16</td><td>8</td><td>4</td><td>2583.78</td><td>8</td><td>4</td><td>2588.67</td><td>8</td><td>4</td><td>2656.76</td><td>8</td></tr><tr><td>R40_1_12</td><td>3624.64</td><td>10</td><td>3</td><td>3633.18</td><td>11</td><td>3</td><td>3635.61</td><td>10</td><td>3</td><td>3651.34</td><td>10</td></tr><tr><td>Average</td><td>1811.79</td><td>7</td><td>5</td><td>1819.30</td><td>7</td><td>4</td><td>1861.18</td><td>7</td><td>2</td><td>1880.86</td><td>7</td></tr></table>

Table 7  
Heterogeneous PD vehicle routing costs.

<table><tr><td rowspan="2">Instance</td><td colspan="3">PDPTW-SLSD</td><td colspan="3">PDPTW-SD</td></tr><tr><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td><td>Savings %</td></tr><tr><td>C10_1_4</td><td>1061.22</td><td>4</td><td>2</td><td>1067.11</td><td>4</td><td>0.55</td></tr><tr><td>C15_1_6</td><td>1473.20</td><td>5</td><td>9</td><td>1630.01</td><td>4</td><td>9.62</td></tr><tr><td>C20_1_8</td><td>1430.77</td><td>6</td><td>6</td><td>1521.17</td><td>6</td><td>5.94</td></tr><tr><td>C25_1_8</td><td>1827.49</td><td>7</td><td>13</td><td>2117.86</td><td>6</td><td>13.71</td></tr><tr><td>C40_1_8</td><td>2423.78</td><td>8</td><td>6</td><td>2525.79</td><td>8</td><td>4.04</td></tr><tr><td>RC10_1_4</td><td>1050.29</td><td>3</td><td>3</td><td>1187.57</td><td>4</td><td>11.56</td></tr><tr><td>RC15_1_6</td><td>1975.01</td><td>6</td><td>0</td><td>1975.80</td><td>6</td><td>0.04</td></tr><tr><td>RC20_1_8</td><td>2222.48</td><td>7</td><td>6</td><td>2458.30</td><td>7</td><td>9.59</td></tr><tr><td>RC25_1_8</td><td>2750.97</td><td>8</td><td>2</td><td>2762.94</td><td>8</td><td>0.43</td></tr><tr><td>RC40_1_12</td><td>3671.89</td><td>10</td><td>2</td><td>3678.82</td><td>11</td><td>0.19</td></tr><tr><td>R10_1_4</td><td>940.25</td><td>4</td><td>4</td><td>954.99</td><td>4</td><td>1.54</td></tr><tr><td>R15_1_6</td><td>1648.02</td><td>6</td><td>0</td><td>1649.34</td><td>6</td><td>0.08</td></tr><tr><td>R20_1_8</td><td>2666.05</td><td>8</td><td>1</td><td>2689.03</td><td>8</td><td>0.85</td></tr><tr><td>R25_1_8</td><td>3169.48</td><td>8</td><td>4</td><td>3233.18</td><td>8</td><td>1.97</td></tr><tr><td>R40_1_12</td><td>3986.54</td><td>11</td><td>4</td><td>4015.53</td><td>10</td><td>0.72</td></tr><tr><td>Average</td><td>2153.16</td><td>7</td><td>4</td><td>2231.16</td><td>7</td><td>4.06</td></tr></table>

## 5.5. The SLs frequency analysis

In this section, we quantify the effect of the SLs frequency on the total expected costs of the PDPTW-SLSD. We test three situations, namely one departure every seven time units, the original case (i.e., every 30 time units) and, finally, one departure every 180 time units. The average over 10 runs of the algorithm is shown for each instance in Table 6.

According to the obtained results, lower operational costs can be achieved with higher frequency of the SLs. The cost savings increase due to the fact that more requests are shipped via SLs. On the other hand, higher frequency implies more SLs capacity, hence higher integration between the two transportation networks that leads to fewer SLs capacity violations.

## 5.6. An analysis on heterogeneous PD vehicle routing costs

In this section, we investigate the benefits of the integrated networks considering heterogeneous routing costs of the PD vehicles and one SL. More specifically, the minimum-capacity vehicle is assumed to cost 0.5 per operating time unit. Larger vehicles are assigned a cost that linearly increases with the carrying capacity. The average results over the 10 runs of the algorithm are presented in Table 7. The columns are self-explanatory.

The results indicate that operating cost savings of up to 13% can be achieved compared to the corresponding PDPTW-SD solutions. On average, using the same amount of vehicles as in classical pickup and delivery system, and the available SLs may lead to average cost savings of 4%.

Sensitivity analysis on the ratio of costs.

<table><tr><td rowspan="2"> $\theta\backslash\eta$ </td><td colspan="3">1</td><td colspan="3">10</td><td colspan="3">30</td><td colspan="2">PDPTW-SD</td></tr><tr><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td><td>#SLs</td><td>E(x)</td><td>#vehs</td></tr><tr><td>0.5</td><td>406.72</td><td>6</td><td>37</td><td>419.42</td><td>4</td><td>0</td><td>419.58</td><td>4</td><td>0</td><td>419.84</td><td>4</td></tr><tr><td>1</td><td>790.40</td><td>5</td><td>35</td><td>823.77</td><td>6</td><td>11</td><td>829.54</td><td>4</td><td>0</td><td>829.87</td><td>4</td></tr><tr><td>5</td><td>3757.50</td><td>6</td><td>36</td><td>3851.50</td><td>6</td><td>32</td><td>3878.86</td><td>6</td><td>30</td><td>4199.47</td><td>4</td></tr></table>

![](07-Ghilas-2016-Scenario_images/48eb2db38c75ca6924cb024c7860a7e7c60d7bc9af0456b60f857416340629a8.jpg)  
Fig. 7. Relationship between the operating cost savings and $\theta \backslash \eta .$

## 5.7. Case study of Amsterdam metro system

In this section, we investigate the performance of the PDPTW-SLSD on a realistic scheduled-line network. More specifically, we replicate the Amsterdam metro system as a case study. In addition, one instance with 25 requests and two depots with three vehicles each is considered. We evaluate the systems’ performance on different cost (i.e., routing and SL) settings. Note that outsourcing cost $P _ { 1 }$ is set to $6 \times \theta$ , where θ is considered to be the same for all PD vehicles. Table 8 indicates the obtained results.

Fig. 7 illustrates the relationship between operational cost savings and the ratio θ\η. As can be seen, the larger routing cost is, the more savings can be achieved from the integrated transportation networks (see 5\1, 5\10, etc. in Fig. 7).

For a given SL cost η, the larger θ is, the more requests will be shipped via available SLs to perform the deliveries, and thus more cost savings can be achieved. On the other hand, smaller θ leads to insignificant incentives to make use of SLs, unless their cost is very small. Otherwise, the cost of using SLs will trade-off the routing cost savings, thus reducing the benefits of integrating system to none.

It is important to note that the challenges for integrating freight movement with public transport services include complex issues of public transportation (e.g., tight timetables), differences between customer-focused companies versus operations-focused companies (e.g., time and cost), obligations of the parties involved in each business (e.g., labor unions), availability of reliable and consistent data (e.g., lack of real-time data), and limited responses to the technological advances (e.g., design of new stations). All above cited attempts to augment public transport services with urban freight transport in real-life proved to be unsuccessful. In our view, the main reason is the lack of decision support tools that help generate reliable delivery plans. Secondly, lack of coordination and information sharing between actors involved played a crucial role. Finally, lack of suficient financial resources needed for constructing storage facilities and re-designing the public transport vehicles had an impact on the outcome of the projects. These challenges could be reduced by increasing the communication between the parties involved and proposing new algorithms and methodologies to tackle the uncertainty of the transportation systems.

## 6. Conclusions

We proposed a scenario-based solution methodology to solve the considered short-haul transportation problem, where demand uncertainty is also taken into consideration. ALNS heuristic algorithm is used within the SAA framework to solve the PDPTW-SLSD. The computational results on instances with up to 40 requests (i.e., 80 locations) indicate significant reduction in expected operational costs, compared to the corresponding PDPTW stochastic routing solutions (i.e., up to

16%). In addition, using more SLs leads to shorter vehicle routes and fewer capacity violations. As a consequence of using extra capacity, lower operational costs can be achieved. Intuitively, larger SL capacity or higher SL frequency benefits the transportation system since fewer recourse actions need to be taken. Furthermore, the results indicate that the relationship between routing and SL costs drives the cost savings.

There are a number of challenges that remain to be tackled before implementing such an integrated transportation system. In particular, other sources of uncertainty (e.g., travel times) need to be taken into consideration in the decision support tools. Re-designing the public transportation (e.g., schedules, routes, storage facilities) for transporting freight is also needed to be done in a cost-eficient way. In terms of future research, investigating exact algorithms for the PDPTW-SLSD may be an interesting topic. Therefore, eficient mathematical formulation for the recourse problem is needed to apply exact algorithms based on stochastic programming techniques. Last, but no least, focusing on environmental aspects, i.e., minimizing the emissions instead of operating costs, may be an interesting research area.

## Acknowledgments

The authors gratefully acknowledge funds provided by the Dutch Institute for Advanced Logistics (DINALOG), under the grant titled “Cargo Hitching”, # 2011 4 086R. Thanks are due to the Editor-in-chief, Area Editor, and three anonymous reviewers for their useful comments and for raising interesting points for discussion.

## References

Adulyasak, Y., Cordeau, J-F., Jans, R., 2015. Benders decomposition for production routing under demand uncertainty. Operations Research 63 (4), 851–867.

Aldaihani, M., Dessouky, M., 2003. Hybrid scheduling methods for paratransit operations. Computers and Industrial Engineering 45 (1), 75–96.

Bianchi, L., Dorigo, M., Gambardella, L., Gutjahr, W., 2009. A survey on metaheuristics for stochastic combinatorial optimization. Natural Computing 8 (2), 239–287.

Braekers. K., Caris. A., Janssens, G., 2014. Exact and meta-heuristic approach for a general heterogeneous dial-a-ride problem with multiple depots, Transportation Research Part B: Methodological 67. 166-186.

CargoTram, 2007. Oficial webpage (accessed on 11.01.2016) http://www.eltis.org/discover/case-studies/delivering-goods-cargo-tram-amsterdam-netherlands.

Demir, E., Bektas¸ , T., Laporte, G., 2012. An adaptive large neighborhood search heuristic for the pollution-routing problem. European Journal of Operationa Research 223 (2), 346–359.

Demir, E., Bektas¸ , T., Laporte, G., 2014. A review of recent research on green road freight transportation. European Journal of Operational Research 237 (3), 775-793.

Demir, E., Burgholzer, W., Hrušovsky,\` M., Arıkan, E., Jammernegg, W., Woensel, T.V., 2015a. A green intermodal service network design problem with trave time uncertainty. Transportation Research Part B: Methodological. (in press)

Demir, E., Huang, Y., Scholts, S., Van Woensel, T., 2015b. A selected review on the negative externalities of the freight transportation: modeling and pricing. Transportation Research Part E: Logistics and Transportation Review 77, 95–114.

DHL-Packstation, 2016. DHL oficial webpage (accessed on 11.01.2016). URL www.dhl.de/en/paket/pakete-empfangen/packstation.html.

Drexl, M., 2012. Synchronization in vehicle routing - a survey of vrps with multiple synchronization constraints. Transportation Science 46, 297–316.

Dumas, Y., Desrosiers, J., Soumis, F., 1991. The pickup and delivery problem with time windows. European Journal of Operational Research 54 (1), 7–22.

Errico, F., Crainic, T., Malucelli, F., Nonato, M., 2013. A survey on planning semi-flexible transit systems: Methodological issues and a unifying framework. Transportation Research Part C: Emerging Technologies 36, 324–338.

Ghilas, V., Cordeau, J-F., Demir, E., Van Woensel, T., 2016a. Branch-and-Price for the Pickup and Delivery Problem with Time Windows and Scheduled Lines. Technical Report. Industrial Engineering & Innovation Sciences, Operations, Planning, Accounting, and Control, Eindhoven University of Technology.

Ghilas, V., Demir, E., Van Woensel, T., 2016b. An adaptive large neighborhood search heuristic for the pickup and delivery problem with scheduled lines. Computers & Operations Research 72, 12–30.

Ghilas, V., Demir, E., Van Woensel, T., 2016c. The pickup and delivery problem with time windows and scheduled lines. INFOR: Information Systems and Operational Research. (in press)

Gutjahr, W., 2011. Recent trends in metaheuristics for stochastic combinatorial optimization. Central European Journal of Computer Science 1, 58–66.

Häll, CH., Andersson, H., Lundgren, J., Varbrand, P., 2009. The integrated dial-a-ride problem. Public Transportation 1, 39–54.

Heilporn, G., Cordeau, J-F., Laporte, G., 2011. An integer L-shaped algorithm for the dial-a-ride problem with stochastic customer delays. Discrete Applied Mathematics.159(9).883-895

Hurtigruten, 2013. Hurtigruten oficial webpage (accessed on 11.01.2016) URL www.hurtigruten-web.com/index\_en.html.

Kleywegt, A., Shapiro, A., Homem-De-Mello, T., 2001. The sample average approximation method for stochastic discrete optimization. SIAM Journal of Optimization 2, 898–913.

Laporte, G., Louveaux, F., van Hamme, L., 2002. An integer L-shaped algorithm for the capacitated vehicle routing problem with stochastic demands. Operations Research 50 (3), 415–423.

Levin. Y.. Nediak, M., Topalôglu. H., 2012, Cargo capacity management with allotments and spot market demand. Operations Research 60 (2). 351–365.

Liaw, C., White, C., Bander, J., 1996. A decision support system for the bimodal dial-a-ride problem. IEEE Transactions on Systems, Man, and Cybernetics, Part A 26 (5), 552–565.

Louveaux, F., Gonzalez, J., 2009. On the one-commodity pickup-and-delivery traveling salesman problem with stochastic demands. Mathematical Programming 119 (1). 169–194.

Lu. O., Dessouky, M., 2006, A new insertion-based construction heuristic for solving the pickup and delivery problem with time windows. European Journal of Operational Research 175 (2), 672–687.

Masson, R., Trentini, A., Lehuede, F., Malhene, N., Peton, O., Tlahig, H., 2015. Optimization of a city logistics transportation system with mixed passengers and goods. EURO Journal on Transportation and Logistics 1–29.

Nanry, W, Barnes. I., 2000, Solving the pickup and delivery problem with time windows using reactive tabu search, Transportation Research Part B: Methodological 34 (2), 107–121.

Pisinger, D., Røpke, S., 2007. A general heuristic for vehicle routing problems. Computers & Operations Research 34 (8), 2403–2435

Powell, W., Shefi, Y., Nickerson, K., Butterbaugh, K., Atherton, S., 1988. Maximizing profits for north american van lines’ truckload division: A new fremwork for pricing and operation. Interfaces 1 (18), 21–41.

Røpke. S., Pisinger, D.. 2006. An adaptive large neighborhood search heuristic for the pickup and delivery problem with time windows. Transportation Science 40 (4), 455–472.

Santos, G., Behrends, H., Teytelboym, A., 2010. Part II: Policy instruments for sustainable road transport. Research in Transportation Economics 28, 46–91.

Schilde, M., Doerner, KF., Hartl, RF., 2011. Metaheuristics for the dynamic stochastic dial-a-ride problem with expected return transports. Computers & Operations Research 38 (12), 1719–1730.

Secomandi, N., Margot, F., 2009. Reoptimization approaches for the vehicle-routing problem with stochastic demands. Operations Research 57 (1), 214–230. SmartLogisticsLab, 2016. Oficial webpage (accessed on 11.01.2016) URL http://www.smartlogisticslab.nl.

Trentini, A., Malhene, N., 2010. Toward a Shared Urban Transport System Ensuring Passengers & Goods Cohabitation. Trimestrale del Laboratorio Territorio Mobilita e Ambiente - TeMALab, pp. 37–44.

Verweij, B., Ahmed, S., Kleywegt, A., Nemhauser, G., Shapiro, A., 2003. The sample average approximation method applied to stochastic routing problems: a computational study. Computational Optimization and Applications 24, 289–333.