---
raw_title: 02-Ghilas-2016-LNS
subject: 数学建模-策联杯B题
source: "02（重要）.pdf"
status: mineru解析
parser: mineru
priority: 重要
topics:
  - 自适应大邻域搜索
  - 取送货
  - 时间窗
  - 班线
---

# An adaptive large neighborhood search heuristic for the Pickup and Delivery Problem with Time Windows and Scheduled Lines

Veaceslav Ghilas <sup>n</sup>, Emrah Demir, Tom Van Woensel

School of Industrial Engineering, Operations, Planning, Accounting and Control (OPAC), Eindhoven University of Technology, Eindhoven 5600 MB, The Netherlands

## a r t i c l e i n f o

Available online 4 February 2016

Keywords: Freight transportation Pickup and delivery problem Heuristic algorithm Scheduled lines

## a b s t r a c t

The Pickup and Delivery Problem with Time Windows and Scheduled Lines (PDPTW-SL) concerns scheduling a set of vehicles to serve freight requests such that a part of the journey can be carried out on a scheduled public transportation line. Due to the complexity of the problem, which is NP-hard, we propose an Adaptive Large Neighborhood Search (ALNS) heuristic algorithm to solve the PDPTW-SL. Complex aspects such as fixed lines' schedules, synchronization and time-windows constraints are efficiently considered in the proposed algorithm. Results of extensive computational experiments show that the ALNS is highly effective in finding good-quality solutions on the generated PDPTW-SL instances with up to 100 freight requests that reasonably represent real life situations.

& 2016 Elsevier Ltd. All rights reserved

## 1. Introduction

A successful integration of passenger and freight transportation creates a seamless movement of people and freight. This integration achieves socially desirable transport options economically viable in urban areas as it reduces the impact of congestion and air pollution [21]. Actua integration is already being observed in long-haul freight transportation (e.g., passenger aircraft and ferries). Norwegian Hurtigruten carries freigh and people efficiently and seamlessly in the region of Northern Europe [18,16]. However, short-haul passenger and freight (i.e., small packages) transportation is rarely integrated, although these services largely use the same infrastructure.

This paper investigates opportunities and the feasibility of using available public transportation vehicles, which operate according to pre determined routes and schedules, for transporting freight. A successful synchronization of pickup and delivery (PD) vehicles with scheduled lines (SLs) is directly related to coordination and consolidation of transport. Coordination assures the precision and timing of each leg's movement. On the other hand, consolidation implies that the amount of freight transferred to/from SLs fits with capacities of PD and SL vehicles. Considering both coordination and consolidation of such integrated system, we introduce the Pickup and Delivery Problem with Time Windows and Scheduled Line (PDPTW-SL).

There exists a rich literature on PDP-related problems. The interested readers are referred to Berbeglia et al. [3] for a literature survey on the solution methodologies for PDPs. A special case of PDPs where passengers need to be transported from their origin to their destination by considering service level constraints are called dial-a-ride problems (DARP). An overview on the mathematical models and the solution methodologies for single as well as multiple-vehicle DARPs can be found in Cordeau and Laporte [6].

In another extension of the PDP, it is possible to consider transfer opportunity between PD vehicles at predefined transfer nodes (PDP T). Shang and Cuff [29] proposed an insertion heuristic algorithm to solve instances with up to 167 requests for the PDP-T. Cortes et al. [7] proposed an exact decomposition method, namely Branch-and-Cut (B&C), and solved PDP-T instances with up to six requests. Moreover, Masson et al. [22,23] proposed an ALNS to solve PDP-T and DARP-T, respectively. In both cases, the authors solved instances with up to 100 requests. The PDP with cross-docking opportunities has been studied by Petersen and Røpke [25], who proposed a large neighborhood search heuristic to solve instances with up to 982 requests.

To the best our knowledge, Nash [24] is the first author who conceptually introduced the idea of transporting freight using public transportation. One of the first attempts to combine scheduled line services with DARP was done by Liaw et al. [20]. The authors formulated the problem where transfers to public scheduled transportation are allowed for passengers and wheelchaired persons. The authors proposed two types of heuristics $( \mathrm { i . e . , }$ online and offline) and solved instances with up to 120 requests. Later, Aldaihani and Dessouky [1] considered an integrated DARP with public transport and proposed a two-stage heuristic algorithm to solve instances with up to 155 requests. Hall et al. [15] introduced a mixed-integer program to solve an integrated dial-a-ride problem (IDARP). The authors considered transfers to fixed lines without modeling schedules of the public transportation. The authors solved small-sized instances with up to 4 requests. Trentini and Malhene [31] presented a review of solutions for combining freight and passenger transportation used in practice. In a related study, Trentini et al. [32] investigated a two-echelon VRP with transshipment in the context of passenger and freight integrated system. The authors proposed an ALNS to solve instances with 50 customers.

As a real-life application of the integrated transport system, a project, called City Cargo Amsterdam [5], was held as a pilot experiment in the Netherlands in 2007. Two cargo trams were used to transport freight in the city center of Amsterdam. The goods were transferred from cargo trucks onto trams to be delivered to the inner part of the city. In 2009 the project was quit due to lack of funds.

In this paper, we consider two transport scenarios: (i) an integrated transportation system and (ii) the pickup and delivery problem where transfers to scheduled lines are not allowed. These two scenarios are intended to provide plausible and sufficient reasons to implement such system by comparing them in terms of the total operating costs of the PD vehicles. The PDPTW-SL is NP-hard, which means that its computational complexity exponentially increase when the problem size increases. It is shown that only instances with a limited number of requests can be solved to optimality within a reasonable time limit. Therefore, we have designed a metaheuristic algorithm to generate goodquality routing solutions. In particular, we present an ALNS algorithm which is based on the destroy and re-create principle.

The contribution of the paper is three-fold: (i) to adapt the classical ALNS heuristic algorithm to solve PDPTW-SL, (ii) to efficiently handle synchronization constraints within the proposed ALNS framework and finally (iii) to analyze the cost savings due to the use of scheduled lines in freight transportation. The rest of this paper is structured as follows. In Section 2, we present an arc-based mathematical formulation for the PDPTW-SL. Section 3 describes the proposed ALNS heuristic algorithm for the PDPTW-SL. The experimental results are given in Section 4. Finally, conclusions are provided in Section 5.

## 2. The Pickup and Delivery Problem with Time Windows and Scheduled Lines

The PDPTW-SL is an extension of the standard PDPTW that additionally considers the flexibility of using available scheduled lines, such as bus, train, and metro. Due to the fact that public transportation systems have a certain coverage (i.e., rural or urban), some delivery trips of the PD vehicles may overlap with SL services. Thus, using public transportation as a part of freight transportation may lead to cost and environmental benefits for the whole transportation system. For instance, due to less driving time of the PD vehicles, logistics service providers may experience substantial operating cost savings. As a consequence, less traveling time of the vehicles also leads to fewer carbon dioxide-equivalent $( { \mathsf { C O } } _ { 2 } { \mathsf { e } } )$ emissions at the global level for the whole society [9,11]. Furthermore, using scheduled lines for carrying freight gives extra cost benefits for public transport service providers as the utilization of SL services increases. An example application which is based on the current metro system of Amsterdam can be illustrated as in $\mathrm { F i g . ~ } 1$

The system depicted in Fig. 1 contains four scheduled lines and five transfer nodes (end-of-lines stations). Note that $T _ { 1 } ^ { 5 1 } , T _ { 1 } ^ { 5 3 } , T _ { 1 } ^ { 5 4 }$ as well as $T _ { 2 } ^ { 5 0 }$ and $T _ { 2 } ^ { 5 4 }$ can be merged into two transfer nodes as these denote the same locations. Each metro line has one single route with one destination in each direction. To use this metro system as a part of the transportation plan, package(s) can be delivered to one of its endof-line stations and transported to other side of the line considering available capacity and schedules of the metro line.

## 2.1. A formal description of the PDPTW-SL

In this section we give a formal description of the PDPTW-SL. All information $( \mathrm { e . g . } ,$ , requests, demands, travel times, time windows) is considered known beforehand, and a possible transport plan for the whole planning horizon (e.g., one day) should be generated before the execution of the transport activities. A solution to the problem is a routing plan and schedules for both requests and PD vehicles. We now define the PDPTW-SL on a digraph $\mathcal { G } = ( \mathcal { N } , \mathcal { A } )$ , where represents the set of nodes (i.e., depots, pickup, delivery and replicated transfer nodes<sup>1</sup>) and represents the set of arcs. We note that i, j, r, v, w, and t are used as indices in this paper.

\- Request: Each request $r \in \mathcal { P }$ is associated with an origin node r and a destination node $r + n ,$ , where n is the number of requests to be satisfied. Each request is associated with two desired time windows: one for the origin $\left( \left[ l _ { r } , u _ { r } \right] \right)$ , and one for the destination point $( [ l _ { r + n } ,$ $u _ { r + n } ] )$ . Furthermore, demand $d _ { r }$ is known for each request.

\- PD vehicle: A set of PD vehicles is given by . In addition, each vehicle $\nu \in \mathcal V$ is associated with the carrying capacity $Q _ { \nu }$ , the depot (origin and destination) $o _ { \nu } ,$ and time window $[ l _ { o _ { v } } , u _ { o _ { v } } ]$

\- Travel and service time: Travel and service times are known beforehand and remain unchanged during the planning horizon. Each arc ði; $j ) \in \mathcal A$ is associated with travel time $Y _ { i j } .$ The service time at node $i \in \mathcal { N }$ is represented as $s _ { i \cdot }$

\- Scheduled line: A set of all physical transfer nodes is given as and the set of all physical scheduled lines is given as , which is defined by the directed arc between the start and the end of the line $( i , j ) ,$ , such that $i , j \in \mathcal { S } ,$ . For example, between two transfer nodes i and j, there are two scheduled lines considered that are one arc for each direction, (i,j) and $( j , i )$ . Each scheduled line has a set of indices $\mathcal { K } ^ { i j }$ for the departure times from i (the start of fixed line), such that the departure time is given as $p _ { i j } ^ { w } , \forall ( i , j ) \in \mathcal { E } , w \in \mathcal { K } ^ { i j } \left( \mathrm { e . g . } , p _ { T _ { 1 } , T _ { 2 } } ^ { 0 } = 3 0 \right)$ . We note that each scheduled line may have different frequencies than other lines, thus the size of the $\mathcal { K } ^ { i j }$ may differ. Furthermore, it is assumed that SL vehicles are designed to carry a limited number of packages, thus implying a finite carrying capacity $k _ { i j } , \forall ( i , j ) \in \mathcal { E }$

We state the following additional assumptions related to SL services.

\- The package carrying capacity is not influenced by the passenger demand on SL services.

![](02-Ghilas-2016-LNS_images/14e3e6660848f4bde1b09ac5a2fca98c7e292a158c6c40cfbc58aa9085696885.jpg)  
Fig. 1. An illustration of the metro system in Amsterdam (2014).

\- Each transfer node is considered as a coordination and a consolidation point for requests (e.g., [12]). In other words, a storage space for to-be-shipped packages is available at the transfer nodes. The packages can be stored until the vehicle's departure time (i.e., scheduled line or PD). Furthermore, it is considered that multiple PD vehicles can be serviced simultaneously at a transfer node. In other words, we assume that the loading/unloading infrastructure is always available for multiple vehicles at a time.

\- In case of multiple freight carriers using SL services, it is assumed that each carrier has a limited storage space at the transfer node and on the SL vehicle (e.g., contract-based agreement). Hence, it is assured that the considered capacity is not affected by the demand of other actors involved.

\- It is assumed that cost $\eta _ { i j }$ per each unit of parcels shipped on the SL (i, j) includes transportation, handling (transshipment) and storage costs. Handling of the packages during transshipment is assumed to be under the responsibility of the SL service provider (e.g., the driver of the SL vehicle).

\- Since the focus of the present problem is related to the operational-level aspects, we disregard all investments needed, such as the redesign of the SL vehicle and the physical storage space required at the transfer nodes. Obviously this assumption may affect the outcome of the system (i.e., might lead to less benefits)

\- It is assumed that all data is known beforehand. In practice, this might not be the case because of the uncertainty in travel times and demands. Disregarding these aspects in the planning process might eventually lead to infeasible plans and expensive repair (recourse) actions to tackle such violations

Sets.  
![](02-Ghilas-2016-LNS_images/8399756d7a05d5e3f7f2a13896931546263ad9fb286df9456758f5d9ae8c3062.jpg)

![](02-Ghilas-2016-LNS_images/76ce5efda9f8b0d4cba70c1239d97741441d143ce0d67067363b916c514b88f3.jpg)  
Fig. 2. An illustration of a replicated fixed line.

In order to model waiting times of the PD vehicles and multiple visits at the transfer nodes, each physical scheduled line $( \mathrm { i . e . , } ( i , j ) \in \mathcal { E } , \mathrm { e . g . }$ , arcs (1, 2) and (2, 1) in Fig. 2a) is replicated n times as in Hall et al. [15]. In addition, each replication is assigned to one request, and only that specific request can travel on the assigned scheduled line (see Fig. 2b). This is done to reduce the number of decision variables. Therefore, the set of all replicated scheduled lines is given as $\mathcal { F }$ (e.g., (1a, 2a), (1b, 2b), (2a, 1a) and (2b, 1b) in Fig. 2b).

Furthermore, the replication process means that each physical transfer node in (e.g., nodes 1 and 2 in Fig. 2a) is replicated n times $( \mathbf { e . g . , } T \equiv \{ 1 a $ ; 1b; 2a; 2bg in the considered example). For the sake of modeling let $\psi ^ { t }$ ; 8t be the physical transfer node represented by the replicated transfer node $t ~ ( { \bf e . g . } , { \psi } ^ { 1 a } { = } { \psi } ^ { 1 b } { = } 1 )$ . Consequently, set $\boldsymbol { \mathcal { T } ^ { t } }$ can be defined as $\{ i \in T | \psi ^ { i } = \psi ^ { t } , i \neq t \} , \forall t \in T$ (e.g., in Fig. 2b, $\mathcal { T } ^ { 2 a } = \{ 2 b \}$ , as 2a and 2b represent physical transfer node 2).

The proposed model is not limited to only one fixed line (e.g., (1, 2) and (2, 1)). Different topologies may be considered, such as square, triangle, star or any other complex networks. Furthermore, the requests are allowed to be shipped from one scheduled line to the other. The additiona parameters used in our model are given in Table 1.

Table 1 Parameters.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $\delta$ </td><td>Number of depots</td></tr><tr><td> $d_r$ </td><td>Demand of request r</td></tr><tr><td> $Y_{ij}$ </td><td>Traveling time from node i to node j</td></tr><tr><td> $s_i$ </td><td>Service time at node i</td></tr><tr><td> $k_{ij}$ </td><td>Freight carrying capacity on the fixed line (i, j)</td></tr><tr><td> $Q_\nu$ </td><td>Carrying capacity of the vehicle  $\nu$ </td></tr><tr><td> $[l_i, u_i]$ </td><td>Time window of node i</td></tr><tr><td> $p_{ij}^w$ </td><td>Departure time from transfer node i on the scheduled line (i, j), indexed by w</td></tr><tr><td> $\psi^t$ </td><td>Physical transfer node that is represented by replicated transfer node t</td></tr><tr><td> $\tau$ </td><td>Number of replicated transfer nodes (i.e.,  $|T|$ )</td></tr><tr><td> $f_i^r$ </td><td> $\begin{cases} 1 & \text{if node } i \text{ is } r, \\ 0 & \text{if node } i \in \mathcal{N}_2 \setminus \{r; r+n\} (\text{ see Table 2}), \\ -1 & \text{if node } i \text{ is } r+n. \end{cases}$ </td></tr><tr><td> $\theta_\nu$ </td><td>The routing cost per one time unit of vehicle  $\nu$ </td></tr><tr><td> $\eta_{ij}$ </td><td>The cost of shipping one unit of package on the SL (i, j)</td></tr></table>

Using the parameters above, the notation of sets is given in Table 2.

## Table 2

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $\mathcal{V}$ </td><td>Set of PD vehicles</td></tr><tr><td> $\mathcal{O}$ </td><td>Set of depots,  $\mathcal{O} \equiv [1, ..., \delta](i.e. o_v \in \mathcal{O}, \forall v \in \mathcal{V})$ </td></tr><tr><td> $\mathcal{P}$ </td><td>Set of requests or pickup nodes,  $\mathcal{P} \equiv [\delta + 1, ..., \delta + n]$ </td></tr><tr><td> $\mathcal{D}$ </td><td>Set of delivery nodes,  $\mathcal{D} \equiv [\delta + n + 1, ..., \delta + 2n]$ </td></tr><tr><td> $\mathcal{T}$ </td><td>Set of replicated transfer nodes,  $\mathcal{T} \equiv [\delta + 2n + 1, ..., \delta + 2n + \tau](see nodes 1a, 1b, 2a and 2b in Fig. 2b)$ </td></tr><tr><td> $\mathcal{T}^t$ </td><td>Set of replicated transfer nodes associated the same physical transfer node as t (e.g. in Fig. 2b,  $\mathcal{T}^{2a} = \{2b\}, \mathcal{T}^{1a} = \{1b\}, etc.)$ </td></tr><tr><td> $\mathcal{N}$ </td><td>Set of nodes in the graph  $\mathcal{G}; \mathcal{P} \cup \mathcal{D} \cup \mathcal{O} \cup \mathcal{T} \equiv \mathcal{N}$ </td></tr><tr><td> $\mathcal{N}_1$ </td><td>Set of nodes that are related to requests ( $\mathcal{P} \cup \mathcal{D}$ )</td></tr><tr><td> $\mathcal{N}_2$ </td><td>Set of nodes that represent requests and replicated transfer nodes ( $\mathcal{P} \cup \mathcal{D} \cup \mathcal{T}$ )</td></tr><tr><td> $\mathcal{E}$ </td><td>Set of physical SLs which is defined as (i, j), with associated  $\mathcal{K}^{ij}$  and  $k_{ij}$ </td></tr><tr><td> $\mathcal{K}^{ij}$ </td><td>Set of indices for the departure times from the physical transfer node i on SL (i, j) ∈  $\mathcal{E}$ </td></tr><tr><td> $\mathcal{F}$ </td><td>Set of replicated SLs which is defined as (i, j) with associated  $\mathcal{K}^{\psi^j \psi^j}$ </td></tr><tr><td> $\mathcal{F}^r$ </td><td>Set of replicated SLs associated with request r (e.g. in Fig. 2,  $\mathcal{F}^a = \{(1a, 2a), (2a, 1a)\}$ </td></tr><tr><td> $\mathcal{F}^t$ </td><td>Set of replicated SLs connected to the replicated transfer node t (e.g. in Fig. 2,  $\mathcal{F}^{1a} = \{(1a, 2a), (2a, 1a)\}$ </td></tr><tr><td> $\mathcal{F}^{ij}$ </td><td>Set of replicated SLs associated with a physical SL (i, j) ∈  $\mathcal{E}$  (e.g. in Fig. 2,  $\mathcal{F}^{1,2} = \{(1a, 2a), (1b, 2b)\}, \mathcal{F}^{2,1} = \{(2a, 1a), (2b, 1b)\}$ </td></tr><tr><td> $\mathcal{A}$ </td><td>Set of arcs in  $\mathcal{G}$  defined by  $\mathcal{N} \times \mathcal{N}$ , (note that  $\mathcal{A} \backslash \mathcal{A}^1 \equiv \mathcal{F} \cup \{(i,j) | i \in \mathcal{O}, j \in \mathcal{N}_2\} \cup \{(i,j) | i \in \mathcal{N}_2, j \in \mathcal{O}\}$ </td></tr><tr><td> $\mathcal{A}^1$ </td><td>=  $\mathcal{N}_2 \times \mathcal{N}_2 \backslash \mathcal{F}$ </td></tr></table>

The decision variables used to handle routing and scheduling of the PD vehicles, along with the flow and the timing of the requests are given in Table 3.

Table 3 Decision variables.

<table><tr><td>Notation</td><td>Definition</td></tr><tr><td> $x_{ij}^{\nu}$ </td><td>A binary variable equal to 1 if arc (i, j) is used by PD vehicle  $\nu$ , 0 otherwise,  $\forall (i, j) \in \mathcal{A}, \nu \in \mathcal{V}$ </td></tr><tr><td> $\alpha_{\nu}$ </td><td>A continuous variable which shows the time at which vehicle  $\nu$  returns to its depot,  $\forall \nu \in \mathcal{V}$ </td></tr><tr><td> $\beta_{i}$ </td><td>A continuous variable which shows the departure time of a vehicle from node i,  $\forall i \in \mathcal{N}$ </td></tr><tr><td> $y_{ij}^{r}$ </td><td>A binary variable equal to 1 if arc (i, j) is used by request r, 0 otherwise,  $\forall i, j \in \mathcal{N}_{2}, r \in \mathcal{P}$ </td></tr><tr><td> $\gamma_{i}^{r}$ </td><td>A continuous variable which shows the departure time of request r from node i,  $\forall i \in \mathcal{N}_{2}, r \in \mathcal{P}$ </td></tr><tr><td> $q_{ij}^{rw}$ </td><td>A binary variable equal to 1 if replicated fixed line (i, j) is used by request r that departs from i at time  $p_{ij}^{w}$ , 0 otherwise,  $\forall r \in \mathcal{P}, (i, j) \in \mathcal{F}^{r}$ ,  $w \in \mathcal{K}^{\psi^{i}\psi^{j}}$ </td></tr></table>

## 2.2. Mathematical formulation of the PDPTW-SL

The PDPTW-SL can be formalized as the following mixed-integer program:

Minimize θ<sub>v</sub>Υ<sub>ij</sub>x<sup>v</sup><sub>ij</sub> þ η<sub>ij</sub>d<sub>r</sub>q<sup>rw</sup><sub>ij</sub> X<sub>ð</sub>i<sub>;</sub>j<sub>Þ</sub> Xv <sub>A</sub> Xr <sub>A</sub> X<sub>ði;jÞ A</sub> r <sub>w</sub> ψ<sup>i</sup>ψ<sup>j</sup>

ð1Þ

Term (1) minimizes the total travel cost of the PD vehicles and the cost of using SLs for transferred requests: subject to

Routing and flow constraints

$$
\sum_ {i \in \mathcal {N}} \sum_ {v \in \mathcal {V}} x _ {i j} ^ {v} = 1 \quad \forall j \in \mathcal {N} _ {1}\tag{2}
$$

$$
\sum_ {i \in \mathcal {N} _ {2}} x _ {o _ {v}, i} ^ {v} \leq 1 \quad \forall v \in \mathcal {V}\tag{3}
$$

$$
\sum_ {i \in \mathcal {N}} \sum_ {v \in \mathcal {V}} x _ {i t} ^ {v} \leq 1 \quad \forall t \in \mathcal {T}\tag{4}
$$

$$
\sum_ {j \in \mathcal {N}} x _ {i j} ^ {\nu} - \sum_ {j \in \mathcal {N}} x _ {j i} ^ {\nu} = 0 \quad \forall i \in \mathcal {N}, v \in \mathcal {V}\tag{5}
$$

$$
\sum_ {j \in \mathcal {N} _ {2}} y _ {i j} ^ {r} - \sum_ {j \in \mathcal {N} _ {2}} y _ {j i} ^ {r} = f _ {i} ^ {r} \quad \forall r \in \mathcal {P}, i \in \mathcal {N} _ {2}\tag{6}
$$

$$
\sum_ {i \in \mathcal {N}} \sum_ {v \in \mathcal {V}} x _ {i t} ^ {v} \leq \sum_ {r \in \mathcal {P}} \sum_ {(i, j) \in \mathcal {F} ^ {t}} y _ {i j} ^ {r} \quad \forall t \in \mathcal {T}\tag{7}
$$

Constraints (2) assure that all pickup and delivery nodes are visited exactly once. Constraints (3) ensure that each vehicle leaves its depot at most once and Constraints (4) assure that each replicated transfer node is visited at most once. Flow conservation for PD vehicles is considered in Constraints (5). Constraints (6) assure flow conservation for the paths of each request. Constraints (7) ensure that if a request uses a scheduled line, a PD vehicle should pick it up/drop it off at a transfer node related to that specific SL:

Scheduling constraints

$$
y _ {i j} ^ {r} = 1 \Rightarrow \gamma_ {j} ^ {r} \geq \gamma_ {i} ^ {r} + Y _ {i j} + s _ {j} \quad \forall r \in \mathcal {P}, i, j \in \mathcal {N} _ {2}\tag{8}
$$

$$
\sum_ {v \in \mathcal {V}} x _ {i j} ^ {v} = 1 \Rightarrow \beta_ {j} \geq \beta_ {i} + Y _ {i j} + s _ {j} \quad \forall i \in \mathcal {N},   j \in \mathcal {N} _ {2}\tag{9}
$$

$$
x _ {i, o _ {v}} ^ {\nu} = 1 \Rightarrow \alpha_ {v} \geq \beta_ {i} + Y _ {i, o _ {v}} + s _ {o _ {v}} \quad \forall i \in \mathcal {N} _ {2}, v \in \mathcal {V}\tag{10}
$$

$$
\beta_ {r + n} \geq \beta_ {r} + Y _ {r, r + n} + s _ {r + n} \quad \forall r \in \mathcal {P}\tag{11}
$$

$$
l _ {i} \leq \beta_ {i} - s _ {i} \leq u _ {i} \quad \forall i \in \mathcal {N} _ {1}\tag{12}
$$

$$
l _ {g _ {v}} \leq \alpha_ {v} \leq u _ {o _ {v}} \quad \forall v \in \mathcal {V}\tag{13}
$$

$$
\sum_ {w \in \mathcal {K} ^ {\psi^ {i} \psi^ {j}}} q _ {i j} ^ {r w} = y _ {i j} ^ {r} \quad \forall r \in \mathcal {P}, (i, j) \in \mathcal {F} ^ {r}\tag{14}
$$

$$
q _ {i j} ^ {r w} = 1 \quad \text { and } \quad y _ {i j} ^ {r} = 1 \Rightarrow \gamma_ {i} ^ {r} = p _ {i j} ^ {w} \quad \forall r \in \mathcal {P}, (i, j) \in \mathcal {F} ^ {r}, w \in \mathcal {K} ^ {\psi^ {i} \psi^ {j}}\tag{15}
$$

$$
\sum_ {r \in \mathcal {P}} \sum_ {(a, b) \in \mathcal {F} ^ {i j}} d _ {r} q _ {a b} ^ {r w} \leq k _ {i j} \quad \forall (i, j) \in \mathcal {E}, w \in \mathcal {K} ^ {i j}\tag{16}
$$

$$
\sum_ {r \in \mathcal {P}} d _ {r} y _ {i j} ^ {r} \leq \sum_ {v \in \mathcal {V}} Q _ {v} x _ {i j} ^ {v} \quad \forall (i, j) \in \mathcal {A} ^ {1}\tag{17}
$$

Timing for each request is considered in Constraints (8). Similarly for PD vehicles, scheduling is updated in Constraints (9) and (10) Constraints (11) assure precedence relationship of each request. Constraints (12) and (13) force the time windows to be respected. Constraints (14) and (15) assure that if a request uses a scheduled line, it departs at a scheduled departure time. Constraints (16) ensure that package carrying capacity on the scheduled line is not exceeded. Constraints (17) consider the capacity of each PD vehicle:

Synchronization constraints

$$
\sum_ {j \in \mathcal {N} _ {1}} y _ {i j} ^ {r} = 1 \Rightarrow \gamma_ {i} ^ {r} = \beta_ {i} \quad \forall r \in \mathcal {P}, i \in \mathcal {T}\tag{18}
$$

$$
\sum_ {j \in \mathcal {N} _ {2}} y _ {i j} ^ {r} = 1 \Rightarrow \gamma_ {i} ^ {r} = \beta_ {i} \quad \forall r \in \mathcal {P}, i \in \mathcal {N} _ {1}\tag{19}
$$

$$
\sum_ {i \in \mathcal {N} _ {2}} y _ {i, r + n} ^ {r} = 1 \Rightarrow \gamma_ {r + n} ^ {r} = \beta_ {r + n} \quad \forall r \in \mathcal {P}\tag{20}
$$

$$
y _ {t j} ^ {r} = 1 \Rightarrow \gamma_ {t} ^ {r} = \beta_ {t} \quad \forall r \in \mathcal {P}, t \in \mathcal {T}, j \in \mathcal {T} ^ {t}\tag{21}
$$

The set of constraints (18)–(21) ensure the synchronization between requests' and vehicles' schedules. Constraints (18) force departure times of requests and vehicles from a replicated transfer node to be equal if there is a request flow from that node towards a pickup delivery node. Constraints (19) force departure times of requests and vehicles from a pickup/delivery node to be equal if there is a request flow from that node. Constraints (20) force arrival time at the destination node of a request be equal to departure time of a vehicle from that node. Constraints (21) assure time synchronization between vehicles and requests at each transfer node, with regards to flow between replications of the same original transfer node:

Decision variable domains

$$
x _ {i j} ^ {\nu} \in \{0, 1 \} \quad \forall (i, j) \in \mathcal {A}, v \in \mathcal {V}\tag{22}
$$

$$
y _ {i j} ^ {r} \in \{0, 1 \} \quad \forall i, j \in \mathcal {N} _ {2}, r \in \mathcal {P}\tag{23}
$$

$$
\alpha_ {v} \in R ^ {+} \quad \forall v \in \mathcal {V}\tag{24}
$$

$$
\gamma_ {i} ^ {r} \in R ^ {+} \quad \forall i \in \mathcal {N} _ {2}, r \in \mathcal {P}\tag{25}
$$

$$
\beta_ {i} \in R ^ {+} \quad \forall i \in \mathcal {N}\tag{26}
$$

$$
q _ {i j} ^ {r w} \in \{0, 1 \} \quad \forall r \in \mathcal {P}, (i, j) \in \mathcal {F} ^ {r}, w \in \mathcal {K} ^ {\psi^ {i} \psi^ {j}}\tag{27}
$$

Note that Constraints $( 8 ) - ( 1 0 ) , ( 1 5 )$ and (18)–(21) are formulated as implications, and standard linearization techniques can be used to express them using one or two linear inequalities.

## 3. An adaptive large neighborhood search heuristic algorithm for the PDPTW-SL

The proposed metaheuristic (ALNS) is an extension of the Large Neighborhood Search (LNS) heuristic, which is first introduced by Shaw [30]. The ALNS metaheuristic was first used to solve several vehicle routing problems by Røpke and Pisinger [28], Pisinger and Røpke [26]. Unlike LNS, where one large neighborhood is usually used, the ALNS applies several neighborhood operators. The neighborhood of a given set of feasible routes is investigated by removing some requests and reinserting them back to the solution. The operators that performed well in previous iterations, are given higher chances to being chosen than the ones that proved poor performance. Thus, each operator is assigned a probability of being selected. The newly generated solution is accepted if the criteria defined by the master search framework is satisfied.

## 3.1. Initialization stage

A greedy insertion heuristic is used to obtain a feasible initial solution to the PDPTW-SL. All requests are initially stored in a list and inserted one by one in a random order in their best available positions (for more detail on greedy insertion (GI) – see Section 3.4). The feasibility with regard to the capacity of PD and SL. vehicles and time windows is always maintained

## 3.2. Probability adjustment procedure

A roulette-wheel mechanism is used to control the selection of the neighborhood operators. At the beginning, the probability of removal and insertion operators are uniformly assigned. As in the implementation of Røpke and Pisinger [28], every $N _ { w }$ iterations, each operator is given a score π. The probability is updated as $\begin{array} { r } { P _ { d } ^ { t + 1 } = P _ { d } ^ { t } ( 1 - r _ { p } ) + r _ { p } \pi _ { i } / \omega _ { i } , } \end{array}$ where $r _ { p }$ is the adjustment parameter, π is the accumulated score of operator i and ω shows the amount of times the operator was used. The score of the operators is increased by $\sigma _ { 1 }$ if a new best solution is obtained. The score is increased by $\sigma _ { 2 }$ if the newly generated solution outperforms the current solution. Finally, if a deteriorated solution is accepted, the score is increased by $\sigma _ { 3 } .$

## 3.3. Removal stage

Ten removal operators are used in our ALNS heuristic algorithm. All operators are adapted from or inspired by Shaw [30], Røpke and Pisinger [28] and Demir et al. [8]. The removal stage mainly consists of removing $\phi$ requests from the current solution and adding them to the so-called removal list as shown in Algorithm 1. The algorithm starts with a given feasible routing solution X and returns a solution where some requests are disregarded. A chosen operator is used to remove a set of requests (i.e., pickup, delivery and transfer nodes if used) from the solution. The parameter $\phi$ defines the number of requests to be removed. Removed pickup and delivery nodes are then inserted into list .

Algorithm 1. The overall structure of the removal operators.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
input: A feasible solution X and the number of requests to be removed  $\phi$ 
output: A partially destroyed solution  $X_{p}$ 

1 Initialize removal list ( $L \leftarrow \emptyset$ )

2 for  $\phi$  iterations do

3 Apply removal operator to remove a request r (includes two nodes; pickup and delivery)

4  $L \leftarrow L \cup r$
</div>

The removal operators used in our implementation are introduced below:

\- Random removal (RR): This operator randomly removes $\phi$ requests from the solution, and runs for $\phi \in [ \phi , { \overline { { \phi } } } ]$ iterations, where $\phi$ and $\overline { { \phi } }$ are the lower and the upper limits on the number of requests to be removed and $\phi$ is a random integer number within the specified range.

\- Route removal (ROR): This operator removes a complete route from a given solution. The route that is to be removed is randomly selected. The ROR operator then iteratively selects a node j from the selected route until it is emptied. The corresponding node ofj, i.e., its pickup or delivery node, is removed irrespective of which route it is positioned in.

\- Late-arrival removal (LAR): For every request r, this operator calculates the difference between the service start time and $l _ { r } , \ l _ { r + n }$ respectively, and then removes the request with the largest total difference $\begin{array} { r } { ( \mathrm { i . e . , ~ } r ^ { * } = \arg \operatorname* { m a x } _ { r \in \mathcal { P } } \{ | [ \beta _ { r } - s _ { r } - l _ { r } ] + [ \beta _ { r + n } - s _ { r + n } - l _ { r + n } ] | \} } \end{array}$ where $\beta _ { x }$ is the departure time from node x). Similarly to RR, this operator runs for $\phi \in [ \phi , \overline { { \phi } } ]$ iterations.

\- Worst-distance removal (WDR): This operator repeatedly removes costly requests. The cost is considered to be the total distance from the pickup and delivery nodes of a request to the prior and succeeding nodes within given routes, i.e., it removes node $\begin{array} { r } { r ^ { * } = \arg \operatorname* { m a x } _ { r \in \mathcal { P } } \{ | Y _ { i - 1 , r } + Y _ { r , i + 1 } + Y _ { j - 1 , r + n } + Y _ { r + n , j + 1 } | \} } \end{array}$ , where i 1 and $j - 1$ , are predecessors and $i + 1$ and $j + 1$ successors of the pickup and delivery nodes, respectively.

\- Shaw removal (SR): The objective of the SR operator is to remove requests that are similar in terms of certain aspects. The algorithm randomly selects a request $r _ { 1 }$ and adds it $\mathrm { t } 0 \ \mathcal { L } . \ \mathrm { L e t } \ l _ { r _ { 1 } , r _ { 2 } } = - 1$ if two nodes, one related to $r _ { 1 } ( \mathrm { i . e . , } r _ { 1 } \mathrm { o r } r _ { 1 } + n )$ and another to $r _ { 2 } \left( \mathrm { i . e . , } r _ { 2 } \mathrm { o r } r _ { 2 } + n \right)$ are in the same vehicle route, and 1 otherwise. This operator picks the request $\begin{array} { r l } { r ^ { * } = \arg \operatorname* { m i n } _ { r _ { 2 } \in \mathcal { P } } \{ \boldsymbol { { \Pi } } _ { 1 } [ Y _ { r _ { 1 } , r _ { 2 } } + Y _ { r _ { 1 } + } } & { { } n , r _ { 2 } + n ] + \boldsymbol { { \Pi } } _ { 2 } [ | \boldsymbol { { \beta } } _ { r _ { 1 } } - } \end{array}$ $\beta _ { r _ { 2 } } | + | \beta _ { r _ { 1 } + n } - \beta _ { r _ { 2 } + n } | ] + { \cal I } { \cal I } _ { 3 } l _ { r _ { 1 } , r _ { 2 } } + { \cal I } { \cal I } _ { 4 } | d _ { r _ { 1 } } - d _ { r _ { 2 } } | \}$ , where $\varPi _ { 1 } { - } I I _ { 4 }$ are normalized weights. The operator is applied $\phi \in [ \phi , \phi ]$ times by selecting a request, which is not yet added in and which is the most similar to the last added request.

\- Proximity-based removal (PR): This operator removes a set of requests that are similar in terms of distance. In other words, it is a special case of SR operator with $\varPi _ { 1 } = 1$ , and $\begin{array} { r } { { \cal I } / _ { 2 } = { \cal I } / _ { 3 } = { \cal I } / _ { 4 } = 0 . } \end{array}$

\- Demand-based removal (DR): This operator is a special case of SR with $\begin{array} { r } { \varPi _ { 1 } = I I _ { 2 } = I I _ { 3 } = 0 , } \end{array}$ , and $\varPi _ { 4 } = 1$

\- Time-based removal (TR): This operator is a special case of SR with $\Pi _ { 1 } = I I _ { 3 } = I I _ { 4 } = 0 ,$ and $\varPi _ { 2 } = 1$ •. Historical knowledge removal (HR): This operator stores the position cost of every request r. The cost is assumed to be the total distance from the origin and destination nodes of request r to the prior and succeeding nodes within the routes, and determined as $c _ { r } = Y _ { i - 1 , r }$ $+ Y _ { r , i + 1 } + Y _ { j - 1 , r + n } + Y _ { r + n , j + 1 }$ at every iteration of the algorithm. Note that i 1 and j 1 are the preceding nodes of the origin and, respectively, destination nodes of r and i 1 and j 1 are their successors in the corresponding PD-vehicle routes. The best position cost $c _ { r } ^ { * }$ of request r is set to be the minimum of all values found so far. The HR operator then selects the request $r ^ { * }$ with the largest cost difference from its best position cost, i.e., $r ^ { * } = \arg \operatorname* { m a x } _ { r \in \mathcal { P } } \{ c _ { r } - c _ { r } ^ { * } \}$ g. Request $r ^ { * }$ is added to . This operator iterates $\phi \in [ \phi , { \overline { { \phi } } } ]$ .

\- Worst removal (WR): This operator removes $\phi \in [ \phi , { \overline { { \phi } } } ]$ requests with the highest cost. The cost in this case is computed as follows: given a solution, the cost of a request r is the difference in the objective function between the current solution (with r) and the same solution without serving r. Note that the difference between WR and WDR is that WR uses the total cost (including transfer cost) of the requests as obiective, whereas WDR focuses only on the distance, In addition, WR also takes into account the length of the newly introduced arcs $( i - 1 , i + 1 )$ and $( j - 1 , j + 1 )$ when removing nodes i and j from a route.

## 3.4. Insertion stage

We have used 5 insertion operators in the proposed ALNS heuristic algorithm. With the help of insertion operators, the removed requests in $\mathcal { L }$ can be inserted into the existing routes, if possible. The general schematic overview of an insertion procedure is shown in Algorithm 2. It is noteworthy that in Line 5 of the insertion algorithm, we do not consider every possible insertion. In order to avoid redundant computations in repairTransfers(X, r, T<sup>r</sup>) andfeasibleSchedule(X) due to time windows, a preliminary time window check is applied as described in Braekers et al. [4]

Due to the fact that PD-vehicle capacity constraints can be fully verified only after applying repairTransfers(X, r, T<sup>r</sup>) procedure, capacity violations for the routes with no transferable requests can be easily detected. Note that feasibleSchedule(X) and feasibleCapacity(X, c(X), $\eta _ { i j } )$ (see Line 11 in Algorithm 2) methods are described in Section 3.5

## Algorithm 2. The generic structure of an insertion $i ^ { * } \left( X _ { n e w } ^ { * } , \right.$ , X<sub>current</sub>) procedure.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
input: A partially destroyed current solution  $X_{new}^{*}$ , a list of removed requests L, and current solution  $X_{current}$ 

output: A feasible solution obtained after the insertion procedure

1 for (each request r in L) do

2  $X_{new} \leftarrow NULL$ 

3  $c(X_{new}^{*}) \leftarrow +\infty$ 

4 for (each route Q and route M) do

5 for (each position q within a route Q and each position m within a route M) do

6 Insert r and  $r+n$  in positions q and m, respectively, in solution  $X_{new}^{*}$ 

7 if ( $Q \neq M$ ) then

8  $|(X_{t}, t_{r}^{*}, t_{r+n}^{*}) \leftarrow repairTransfers(X_{new}^{*}, r, T^{r})$ 

9 else

10  $|X_{t} \leftarrow X_{new}^{*}$ 

11 if (feasibleCapacity( $X_{t}, c(X_{t}), \eta_{ij}$ ) and feasibleSchedule( $X_{t}$ )) then

12 if (acceptance criteria of  $i^{*}$  is satisfied) then

13  $|X_{new} \leftarrow X_{t}$ 

14

15 if ( $X_{new} \neq NULL$ ) then

16  $|X_{new}^{*} \leftarrow X_{new}$ 

17 else

18 return  $X_{new}^{*}$
</div>

The feasibility with respect to the capacity, SL schedules and time windows is always kept. Note that checking the feasibility is not trivial, since pickup and delivery nodes of the same request can be located in different PD routes, and hence, a tour must include at least one scheduled line. Such partial solutions need to be repaired by adding transfer nodes. Therefore, repairTransfers(X, r, T<sup>r</sup>) procedure is run to insert corresponding replicated transfer nodes in a greedy fashion. As proposed for the MIP formulation, each original transfer node is replicated n (number of requests) times, hence each request gets assigned a list of replicated transfer nodes. The overview of the repair mechanism is shown in Algorithm 3.

Algorithm 3. The generic structure of the repairTransfers(X, r, T<sup>r</sup>) procedure.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
input: A partial solution X, a request r and  $T^{r}$  replicated transfer nodes related to r
output: A feasible solution  $X_{t}$  and a origin and a destination transfer nodes ( $t_{r}^{*}, t_{r+n}^{*}$ ) of r in the current solution  $X_{t}$ 

1 Q ← the route related to r

2 M ← the route related to  $r + n$ 

3  $t_{r}^{*} \leftarrow$  transfer node  $\in T^{r}$  with the cheapest insertion in route Q, sequenced after r

4  $T^{r} = T^{r} \setminus t_{r}^{*}$ 

5  $t_{r+n}^{*} \leftarrow$  transfer node  $\in T^{r}$  with the cheapest insertion in route M, sequenced earlier than  $r + n$ 

6  $X_{t} \leftarrow$  updated X given minimal cost insertions of  $t_{r}^{*}$  and  $t_{r+n}^{*}$ 

7 return ( $X_{t}, t_{r}^{*}, t_{r+n}^{*}$ )
</div>

A transferable request r is assigned two related replicated transfer nodes: t<sup>n</sup> (i.e., origin transfer node), and $t _ { r + n } ^ { * }$ (i.e., destination transfer node).

We now describe the insertion operators. We note that the requests are randomly chosen from the removal list $\mathcal { L } .$

\- Greedy insertion (GI): This operator iteratively inserts a request (both pickup and delivery nodes) in the best possible position of the routes. $\varDelta _ { I _ { i } J _ { i } } ^ { r }$ is the objective function value when the pickup node of r is inserted in route I (position i) and its corresponding delivery node is inserted in route J (position j). Thus, $\varDelta _ { I _ { i } J _ { i } } ^ { r } \ast = \arg \operatorname* { m i n } \{ \varDelta _ { I _ { i } J _ { i } } ^ { r } \}$

•. Second-best insertion (SD): This new operator chooses the second best insertion for randomly selected unassigned request. The main idea of using this operator is to diversify the search.

\- Greedy insertion and noise function (GIN): This operator is similar to the GI and involves certain flexibility in selecting the best insertion of a request. This flexibility is obtained by changing the cost for request $r _ { \ast }$ Updated Cost Actual Cost $+ \overline { { d } } \mu \epsilon$ , where $\overline { d }$ is the largest distance between nodes, $\mu$ is a noise parameter used for diversification and is set equal to 0.1, and ϵ is a random number between [ 1,1]. Updated Cost is computed for each request in $\mathcal { L } .$

\- Second-best insertion and noise function (SIN): This operator is similar to the SI and involves the same noise function that is used in GIN operator.

\- Best out of λ feasible insertions (λFI): This new operator is similar to GI but chooses the best insertion out of the first λ feasible insertions. The parameter λ is a randomly generated integer number between 1 and ψ. For each unassigned request we generate a set of possible insertions associated with corresponding distance-based costs (disregarding distance to the corresponding transfer nodes), while considering precedence constraints. These positions are not necessary feasible in terms of time windows. Additionally, in order to filter out some more of the infeasible insertions, the time windows of the subsequent nodes visited within the considered routes are verified. The generated set is sorted in increasing order based on insertion costs. Hence the operator investigates the cheapest insertions overall routes first.

Moreover, additional five variants of these operators are also used, where the requests are sorted in in terms of their time flexibility (i.e., the least flexible first). The flexibility of request r can be computed as $| u _ { r + n } - l _ { r } |$

## 3.5. Feasibility of the routes and schedules

Scheduling (time windows) constraints bring complexity to the PDPTW-SL since the requests may be picked up by a PD vehicle and delivered by another one. This implies that PD vehicles and SLs must be synchronized. This problem can be handled as shown i Algorithm 4.

Algorithm 4. The generic structure of the feasibleSchedule(X) procedure

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
input: A solution X
output: Boolean value: TRUE if feasible, FALSE if infeasible

1 list ← ∅
2 β$_{t_r^*}$ ← 0, β$_{t_{r+n}^*}$ ← 0, ∀ r ∈ P
3 for (each route I in X) do
4    for (each node i in I) do
5    β$_i$ ← max{β$_{p_i}$ + Y$_{p_i,i}$ + s$_i$; l$_i$ + s$_i$}
6    if (β$_i$ &gt; u$_i$ + s$_i$) then
7    return FALSE
8    if (i = t$_{r+n}^*$, ∀ r ∈ P) then
9    list ← list ∪ i
10    i ← end route
11 while (list ≠ ∅) do
12    for (t$_{r+n}^*$ in list) do
13    if (β$_{t_r^*}$ &gt; 0) then
14    path$_{r}$ ← generatePath(t$_{r}^*$, t$_{r+n}^*$)
15    β$_{t_{r+n}^*}$ ← determineTime(β$_{t_r^*}$, path$_{r}$)
16    for (each successor node i of t$_{r+n}^*$) do
17    β$_i$ ← max{β$_{p_i}$ + Y$_{p_i,i}$ + s$_i$; l$_i$ + s$_i$}
18    if (β$_i$ &gt; u$_i$ + s$_i$) then
19    return FALSE
20    if (i = t$_{r_1+n}^*$, ∀ r$_1$ ∈ P) then
21    list ← list ∪ i
22    i ← end route
23    list ← list\t$_{r+n}^*$
24    if (β$_{t_r^*}$ = 0, ∀ β$_{t_{r+n}^*}$ ∈ list) then
25    return FALSE
26 return TRUE
</div>

All β values for the transfer nodes are reset to 0 in Line 2. The first block of the algorithm (Lines 3–10) sets the time for all nodes at the earliest possible value (depending on the start of the time window and the departure time from the preceding node $p _ { i } )$ . The algorithm switches to the next route whenever a destination transfer node is reached. This node is added to a list that contains all destination transfer nodes which do not have an updated synchronized time. The second part of the algorithm (Lines 11–25) runs until the list of destination transfer nodes is emptied or a cycle (see Fig. 4) is found.

\- For each $t _ { r + n } ^ { * } \in$ list with the corresponding origin transfer node (i.e., t<sup>n</sup>) that has already received a timing, generate a shortest path [13] from $t _ { r } ^ { * }$ to $t _ { r + n } ^ { * }$ (Line 14). Given the shortest path and the departure time from $t _ { r } ^ { * } ,$ , the algorithm computes the time at $t _ { r + n } ^ { * }$ by considering earliest scheduled departure time later than $\beta _ { t _ { r } ^ { * } }$ (i.e., $\lceil \beta _ { t _ { r } ^ { * } } \rceil )$ for every intermediate line used (Line 15). Considered $t _ { r + n } ^ { * }$ with a synchronized timing is removed from the list. Finally, all succeeding nodes of $t _ { r + n } ^ { * }$ get assigned a value until a destination transfe node is reached and added to the list.

![](02-Ghilas-2016-LNS_images/bc755b6c4b15a5ac77c511e92b78c5ddfd3eb10fb37ae12ed52a28ed5b7c0683.jpg)  
Fig. 3. An interdependency relation of the routes.

![](02-Ghilas-2016-LNS_images/a23bcfb9e6868b0cdfcc525caabeb035e31de1add980fea0f48ae5f12a1718bc.jpg)  
Fig. 4. An example of a two-request cycle.

\- Whenever all $\beta _ { t _ { r } ^ { * } }$ is zero $\forall t _ { r + n } ^ { * } \in$ list, the algorithm finds a cycle (see Fig. 4) and stops. Hence, no feasible schedule is possible for a given solution X.

For a better understanding, we refer to the example shown in Fig. 3. Three requests, namely a, b, and $c ,$ are to be delivered to destination nodes $a + n , b + n ,$ and cþn, respectively. All the requests are transferable, thus each request is shipped on a scheduled line. All these transfer nodes are replications of the original transfer nodes and each replication is assigned to only one request. In the present example, $T _ { a }$ represents the origin transfer node of $a ,$ and $T _ { a + n }$ is its destination transfer node. For the sake of simplicity, each arc has one time unit and each node does not require any service time. The numbers on top of the nodes indicate the departure time from that specific node. In this example, three PD vehicles are needed for the transportation of these three requests.

By referring to Fig. 3, the feasibility of the schedule is checked as follows: the process starts in the first route. The algorithm reaches the transfer node $T _ { a + n }$ that is a destination transfer node of request a. The algorithm moves to the second route and reaches $T _ { c + n } ,$ which is a destination transfer node of request $c .$ Finally, it moves to the last route and updates the timing for the whole route as no destination transfer node is encountered. The list contains two destination transfer nodes, i.e., $T _ { a + n }$ and $T _ { c + n \cdot A }$ shortest path is generated from $T _ { c }$ to $T _ { c + n }$ , and the departure time $\beta _ { T _ { c + n } }$ is updated $( \mathrm { i } . \mathsf { e } . , 3 )$ . Afterwards, the subsequent nodes of $T _ { c + n }$ for a given synchronized time $\beta _ { T _ { c + n } }$ get assigned time values until $T _ { b + n }$ is reached. Similarly, the timing of $T _ { a + n }$ is updated and followed by $T _ { b + n }$

Note that a cycle implies that the precedence constraints are violated for at least two transferable requests, since such requests need to be picked up and dropped off twice (see Fig. 4). In addition, cycles may be composed of multiple routes and requests.

The procedure determineTime $( \beta _ { t _ { r } ^ { * } } , p a t h _ { r } )$ (see Algorithm 4, Line 15) computes departure time from $t _ { r + n } ^ { * }$ for a given departure time from $t _ { r } ^ { * } .$

The capacity constraints of both PD and SL vehicles are verified in Algorithm 5. First, the algorithm checks SL capacity by first generating scheduled line paths along with every scheduled departure time from the considered transfer nodes (Line 3). The capacity variables are updated for each SL and each possible scheduled departure. The cost of the solution is updated in Line 6. Whenever the capacity is violated (Line $^ { 7 ) , }$ , the algorithm stops and returns FALSE value. The PD-vehicle capacity constraints can be checked in a standard way with some preprocessing (Line 9). In particular, the destination transfer node of a transferable request $\mathbf { \Omega } ( \mathrm { i } . \mathbf { e } . , t _ { r + n } ^ { * } )$ becomes an origin node on a different route, hence it will have a positive demand $( \mathrm { i } . \mathsf { e } _ { . , } d _ { r } )$ whereas the origin transfer node of $r ( \mathrm { i } . { \mathsf { e } } _ { \cdot } , t _ { r } ^ { * } )$ becomes a destination node and it is assigned a negative demand $( \mathrm { i } . \mathbf { e } . , - d _ { r } )$

Algorithm 5. The generic structure of feasibleCapacity(X, c(X), $\eta _ { i j } )$ procedure.

input: A solution X, routing cost of X, and cost of using SL $\eta _ { i j }$ per unit shipped on (i;j)

output: A boolean value θ

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Initialize $m_{ij}^w$ array for the capacity used on the scheduled line (i,j) at time $p_{ij}^w$ and $\overline{\mathcal{P}}^t \leftarrow$ set of transferable requests in solution X

for (r in $\overline{\mathcal{P}}^t$) do

set $(\overline{\mathcal{K}}^r, \gamma) \leftarrow$ scheduled lines (i,j) used by r and corresponding scheduled departure times $\gamma_{ij}^r$

for $((i,j) \in \overline{\mathcal{K}}^r)$ do

set $m_{ij}^w \leftarrow m_{ij}^w + d_r$

set $c(X) \leftarrow c(X) + d_r\eta_{ij}$

if $(m_{ij}^w &gt; k_{ij})$ then

return FALSE

if (PDvehicleCapacityViolated(X)) then

return FALSE

return TRUE
</div>

## 3.6. Master search framework

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
In the proposed ALNS, we used simulated annealing (SA). The overall pseudo-code of the proposed algorithm is provided in Algorithm 6.
Algorithm 6. The pseudo-code of the ALNS with SA.

input Removal operators D, insertion operators I, initial temperature T, cooling rate κ
output A feasible solution  $X_{best}$ 

1 Generate an initial solution by using the Greedy insertion algorithm
2 Initialize probability  $P_{d}^{t}$  for each destroy operator  $d \in D$  and probability  $P_{i}^{t}$  for each insertion operator  $i \in I$ 
3 Let j be the iteration counter with initial value of  $j \leftarrow 1$ 
4  $X_{current} \leftarrow X_{best} \leftarrow X_{init}$ 
5 repeat

6 Choose a removal operator  $d^{*} \in D$  with probability  $P_{d}^{t}$ 
7 Let  $X_{new}^{*}$  be the solution generated after using operator  $d^{*}$  to  $X_{current}$ 
8 Choose an insertion operator  $i^{*} \in I$  with probability  $P_{i}^{t}$ 
9 Let  $X_{new}$  be the newly–generated solution after applying operator  $i^{*}$  to  $X_{new}^{*}$ 
10 if  $c(X_{new}) &lt; c(X_{current})$  then
11  $X_{current} \leftarrow X_{new}$ 
12 if  $c(X_{current}) &lt; c(X_{best})$  then
13  $|X_{best} \leftarrow X_{current}|$ 
14 Let  $\nu \leftarrow e^{-(c(X_{new}) - c(X_{current}))/T}$ 
15 Generate a random number  $\epsilon \in [0, 1]$ 
16 if  $\epsilon &lt; \nu$  then
17  $|X_{current} \leftarrow X_{new}|$ 
18

19  $T \leftarrow \kappa T$ 
20 Update probabilities using the adaptive probability adjustment procedure
21  $j \leftarrow j + 1$ 
22 until the maximum number of iterations is reached
</div>

The notation $X _ { b e s t }$ shows the best solution obtained, $X _ { c u r r e n t }$ presents the current solution, and $X _ { n e w }$ shows a newly generated solution that can be accepted or rejected at each iteration. Each solution X is associated with a cost $c ( X ) .$ Any solution $X _ { n e w }$ can have three outcomes: (i) if $c ( X _ { n e w } ) < c ( X _ { c u r r e n t } ) ,$ , then it is accepted, $\mathrm { ( i i ) } \operatorname { i f } c ( X _ { n e w } ) > c ( X _ { c u r r e n t } )$ and $e ^ { - ( c ( X _ { n e w } ) - c ( X _ { c u r r e n t } ) ) / T }$ is greater than a random number within [0,1], with $T -$ temperature, then $X _ { n e w }$ is accepted as well, and finally, (iii) it is rejected. The initial temperature is selected as T. The temperature T diminishes at each iteration by a rate κ, where $0 < \kappa < 1$ . The algorithm runs for a given number of iterations (i.e., 10,000 iterations)

## 4. Computational experiments

To analyze the performance of the proposed ALNS, we run a series of experimental tests and present the obtained results in this section

## 4.1. Data generation

Three sets of instances, namely R, C, and RC, with three scheduled lines in a triangular topology and a frequency of one departure of every 30 time units are considered. Each instance contains 100 requests (i.e., 100 pick-up and 100 delivery nodes) over $2 0 0 \times 2 0 0$ time units on an Euclidean space. Instances follow a naming convention of $G _ { - } n _ { - } s l _ { - } \nu ,$ where G is the geographic distribution of the customers, n is the number of requests that needs to be served, sl is the number of SLs. and ν is the number of available PD vehicles, Instances are classified with regard to the location of the requests. For example, C involves clustered nodes around transfer nodes, R considers uniform randomly distributed request nodes, and finally RC involve randomly clustered nodes. More specifically, C and RC have the nodes posi tioned within at most 30, respectively 80 time units to one of its three available transfer nodes. In all cases, two depots with 30 het erogeneous PD vehicles each are considered.

The planning horizon is set to 10 working hours (i.e., 600 time units). The widths of the time windows are randomly generated between 26 and 91 time units. Service times are considered to be up to three time units. Each demand is assigned between one and three units. The capacity of PD vehicle is generated between six and 20 units. The carrying capacity on the considered SLs is assumed to be 15 demand units. Additional instances were also generated such that subsets of requests, PD vehicles, SLs out of R, C, and RC datasets are used. The datasets (i.e., R, C, and RC) can be found on the web page www.smartlogisticslab.nl

## 4.2. Parameter tuning

The proposed algorithm is implemented in NetBeans IDE 7.1.1 using Java. All experiments were conducted on an Intel Core i5 with 2.6 GHz speed and 4 GB RAM. A more detailed tuning was done on the five most sensitive parameters as shown in Table 4. These were identified during some preliminary tests. Three instances of small sizes (i.e., 8, 16 and 25 requests) were solved 10 times each for the given combination of parameters. The rest of the parameters were chosen based on some other experiments and our intuition.

In total, the ALNS algorithm involves 16 parameters which are listed in Table 5.

Table 4  
Results of parameter tuning.

<table><tr><td>Iterations</td><td>Destroy rate %</td><td> $\sigma_1$ </td><td> $\sigma_2$ </td><td> $\sigma_3$ </td><td>Average value €</td><td>Iterations</td><td>Destroy rate %</td><td> $\sigma_1$ </td><td> $\sigma_2$ </td><td> $\sigma_3$ </td><td>Average value €</td></tr><tr><td>10,000</td><td>0.15</td><td>1</td><td>0</td><td>1</td><td>954.09</td><td>15,000</td><td>0.15</td><td>1</td><td>0</td><td>1</td><td>953.72</td></tr><tr><td>10,000</td><td>0.15</td><td>1</td><td>0</td><td>5</td><td>953.08</td><td>15,000</td><td>0.15</td><td>1</td><td>0</td><td>5</td><td>953.61</td></tr><tr><td>10,000</td><td>0.15</td><td>1</td><td>3</td><td>1</td><td>954.18</td><td>15,000</td><td>0.15</td><td>1</td><td>3</td><td>1</td><td>950.98</td></tr><tr><td>10,000</td><td>0.15</td><td>1</td><td>3</td><td>5</td><td>951.86</td><td>15,000</td><td>0.15</td><td>1</td><td>3</td><td>5</td><td>954.02</td></tr><tr><td>10,000</td><td>0.15</td><td>5</td><td>0</td><td>1</td><td>958.49</td><td>15,000</td><td>0.15</td><td>5</td><td>0</td><td>1</td><td>954.03</td></tr><tr><td>10,000</td><td>0.15</td><td>5</td><td>0</td><td>5</td><td>958.52</td><td>15,000</td><td>0.15</td><td>5</td><td>0</td><td>5</td><td>952.59</td></tr><tr><td>10,000</td><td>0.15</td><td>5</td><td>3</td><td>1</td><td>954.66</td><td>15,000</td><td>0.15</td><td>5</td><td>3</td><td>1</td><td>952.94</td></tr><tr><td>10,000</td><td>0.15</td><td>5</td><td>3</td><td>5</td><td>953.00</td><td>15,000</td><td>0.15</td><td>5</td><td>3</td><td>5</td><td>952.57</td></tr><tr><td>10,000</td><td>0.25</td><td>1</td><td>0</td><td>1</td><td>950.04</td><td>15,000</td><td>0.25</td><td>1</td><td>0</td><td>1</td><td>949.80</td></tr><tr><td>10,000</td><td>0.25</td><td>1</td><td>0</td><td>5</td><td>953.80</td><td>15,000</td><td>0.25</td><td>1</td><td>0</td><td>5</td><td>953.82</td></tr><tr><td>10,000</td><td>0.25</td><td>1</td><td>3</td><td>1</td><td>954.87</td><td>15,000</td><td>0.25</td><td>1</td><td>3</td><td>1</td><td>951.89</td></tr><tr><td>10,000</td><td>0.25</td><td>1</td><td>3</td><td>5</td><td>948.25</td><td>15,000</td><td>0.25</td><td>1</td><td>3</td><td>5</td><td>950.64</td></tr><tr><td>10,000</td><td>0.25</td><td>5</td><td>0</td><td>1</td><td>953.16</td><td>15,000</td><td>0.25</td><td>5</td><td>0</td><td>1</td><td>951.42</td></tr><tr><td>10,000</td><td>0.25</td><td>5</td><td>0</td><td>5</td><td>954.14</td><td>15,000</td><td>0.25</td><td>5</td><td>0</td><td>5</td><td>954.47</td></tr><tr><td>10,000</td><td>0.25</td><td>5</td><td>3</td><td>1</td><td>954.10</td><td>15,000</td><td>0.25</td><td>5</td><td>3</td><td>1</td><td>952.34</td></tr><tr><td>10,000</td><td>0.25</td><td>5</td><td>3</td><td>5</td><td>951.46</td><td>15,000</td><td>0.25</td><td>5</td><td>3</td><td>5</td><td>953.02</td></tr><tr><td>10,000</td><td>0.35</td><td>1</td><td>0</td><td>1</td><td>950.63</td><td>15,000</td><td>0.35</td><td>1</td><td>0</td><td>1</td><td>949.67</td></tr><tr><td>10,000</td><td>0.35</td><td>1</td><td>0</td><td>5</td><td>951.08</td><td>15,000</td><td>0.35</td><td>1</td><td>0</td><td>5</td><td>950.36</td></tr><tr><td>10,000</td><td>0.35</td><td>1</td><td>3</td><td>1</td><td>950.53</td><td>15,000</td><td>0.35</td><td>1</td><td>3</td><td>1</td><td>954.97</td></tr><tr><td>10,000</td><td>0.35</td><td>1</td><td>3</td><td>5</td><td>951.65</td><td>15,000</td><td>0.35</td><td>1</td><td>3</td><td>5</td><td>954.01</td></tr><tr><td>10,000</td><td>0.35</td><td>5</td><td>0</td><td>1</td><td>951.77</td><td>15,000</td><td>0.35</td><td>5</td><td>0</td><td>1</td><td>952.77</td></tr><tr><td>10,000</td><td>0.35</td><td>5</td><td>0</td><td>5</td><td>949.89</td><td>15,000</td><td>0.35</td><td>5</td><td>0</td><td>5</td><td>950.59</td></tr><tr><td>10,000</td><td>0.35</td><td>5</td><td>3</td><td>1</td><td>949.72</td><td>15,000</td><td>0.35</td><td>5</td><td>3</td><td>1</td><td>951.11</td></tr><tr><td>10,000</td><td>0.35</td><td>5</td><td>3</td><td>5</td><td>951.88</td><td>15,000</td><td>0.35</td><td>5</td><td>3</td><td>5</td><td>952.34</td></tr></table>

Table 5  
Used parameters in the computational experiments

<table><tr><td>Group</td><td>Parameter</td><td>Value</td></tr><tr><td rowspan="6">I</td><td>The total number of iterations ( $N_i$ )</td><td>10,000</td></tr><tr><td>The number of route-wheel iterations ( $N_w$ )</td><td>200</td></tr><tr><td>The roulette-wheel constant ( $r_p$ )</td><td>0.1</td></tr><tr><td>New best solution ( $\sigma_1$ )</td><td>1</td></tr><tr><td>Improving solution ( $\sigma_2$ )</td><td>3</td></tr><tr><td>Deteriorating solution ( $\sigma_3$ )</td><td>5</td></tr><tr><td rowspan="10">II</td><td>Initial temperature ( $T$ )</td><td>200</td></tr><tr><td>Cooling degree ( $\kappa$ )</td><td>0.9995</td></tr><tr><td>Lower limit of removable requests ( $\underline{\phi}$ )</td><td>2.5% of  $|\mathcal{P}|$ </td></tr><tr><td>Upper limit of removable requests ( $\overline{\phi}$ )</td><td>25% of  $|\mathcal{P}|$ </td></tr><tr><td>First Shaw parameter ( $\Pi_1$ )</td><td>0.5</td></tr><tr><td>Second Shaw parameter ( $\Pi_2$ )</td><td>0.2</td></tr><tr><td>Third Shaw parameter ( $\Pi_3$ )</td><td>0.1</td></tr><tr><td>Fourth Shaw parameter ( $\Pi_4$ )</td><td>0.2</td></tr><tr><td>Noise parameter ( $\mu$ )</td><td>0.1</td></tr><tr><td>Number of feasible insertions ( $\psi$ )</td><td>30</td></tr></table>

It is noted that a driving cost of the PD vehicles is assumed to be 0.5 €per minute. It seems reasonable considering all operational costs, such as fuel consumption, driver wage, insurance, and tax. The cost of each demand unit of package request shipped on a fixed line is set to 1 €, which includes handling, storage and transportation costs. The parameters used in the ALNS algorithm are grouped into two categories below:

\- Group I contains the parameters related to the selection procedure of the operators. The values of $\sigma _ { 1 } , \sigma _ { 2 }$ and $\sigma _ { 3 }$ do not satisfy $\sigma _ { 1 } \geq \sigma _ { 2 } \geq \sigma _ { 3 } ,$ . In our implementation and similar to Demir et al. [8,10], we have chosen (based on parameter tuning) a parameter setting which rewards more acceptance of a worse solutions than discovering of better ones. It turns out to be an effective way for diversifying the search.

\- Group II parameters are used to fine-tune the SA master search and the operators.

Tables 6 and 7 indicate the number of times each operator was used within the ALNS. In addition, these tables show in the parenthesis the total time spent to run each operator. We note that the results are obtained using only one instance of each different size in terms of the number of requests.

The results shown in Table 6 show that operators RR, SR, PR and HR are used almost equally often. In many cases, the most widely used operators are LAR, TR and WR.

As seen in Table 7, most used insertion operators are the ones that have ordered . Since least flexible requests are inserted first, these operators have higher chances to insert all requests within the existing routes. More specifically, oGI, oSI and their variants with noise functions are widely selected. It is noted that randomly ordered insertion operators do not perform well, as many times the algorithm cannot insert all unassigned requests back to the solution due to their order of insertion.

Table 8  
Table 6  
Number of iterations and the computational times needed by each removal operator.

<table><tr><td>Instance</td><td>RR</td><td>ROR</td><td>LAR</td><td>WDR</td><td>SR</td><td>PR</td><td>DR</td><td>TR</td><td>HR</td><td>WR</td></tr><tr><td>R_25_1_8</td><td>986(0.0)</td><td>800(0.0)</td><td>1358(0.1)</td><td>766(0.0)</td><td>979(0.0)</td><td>938(0.0)</td><td>900(0.0)</td><td>1121(0.0)</td><td>904(0.0)</td><td>1248(0.0)</td></tr><tr><td>R_50_1_14</td><td>946(0.0)</td><td>947(0.0)</td><td>900(0.0)</td><td>951(0.0)</td><td>1051(0.0)</td><td>963(0.0)</td><td>826(0.0)</td><td>1241(0.0)</td><td>946(0.0)</td><td>1229(0.0)</td></tr><tr><td>R_75_1_20</td><td>995(0.0)</td><td>893(0.0)</td><td>1104(0.0)</td><td>943(0.1)</td><td>958(0.1)</td><td>933(0.1)</td><td>769(0.0)</td><td>1196(0.1)</td><td>936(0.1)</td><td>1273(0.0)</td></tr><tr><td>R_100_1_24</td><td>1024(0.0)</td><td>640(0.0)</td><td>1323(0.1)</td><td>1294(0.1)</td><td>907(0.1)</td><td>926(0.1)</td><td>743(0.1)</td><td>1205(0.1)</td><td>1096(0.1)</td><td>842(0.1)</td></tr></table>

Table 7  
Number of iterations and the computational times needed by each insertion operator.

<table><tr><td>Instance</td><td>GI</td><td>SI</td><td>GIN</td><td>SIN</td><td> $\lambda$  FI</td><td>oGI</td><td>oSI</td><td>oGIN</td><td>oSIN</td><td>o $\lambda$  FI</td></tr><tr><td>R_25_1_8</td><td>860(0.2)</td><td>855(0.2)</td><td>537(0.1)</td><td>510(0.2)</td><td>451(0.0)</td><td>1843(0.9)</td><td>1945(1.2)</td><td>1024(0.6)</td><td>1045(0.6)</td><td>930(0.3)</td></tr><tr><td>R_50_1_14</td><td>655(0.7)</td><td>631(0.5)</td><td>312(0.1)</td><td>414(0.4)</td><td>453(0.1)</td><td>2359(11.2)</td><td>2332(10.8)</td><td>971(4.5)</td><td>941(4.5)</td><td>932(1.1)</td></tr><tr><td>R_75_1_20</td><td>636(1.4)</td><td>532(0.9)</td><td>404(0.6)</td><td>263(0.5)</td><td>286(0.0)</td><td>2697(44.9)</td><td>2643(42.5)</td><td>1040(13.5)</td><td>832(13.0)</td><td>667(1.5)</td></tr><tr><td>R_100_1_24</td><td>531(4.2)</td><td>485(2.1)</td><td>212(1.3)</td><td>252(1.1)</td><td>273(0.2)</td><td>3315(285.0)</td><td>3095(263.8)</td><td>875(56.7)</td><td>510(42.5)</td><td>452(4.7)</td></tr></table>

Tables 8 and 9 indicate the number of times an operator has found the best and a better solution compared to the current one, respectively. It is noted that the number in parenthesis indicates the number of times a current solution is improved, but not to become a best known.

Number of global best solutions found and number of improving solutions achieved by the removal operators

<table><tr><td>Instance</td><td>RR</td><td>ROR</td><td>LAR</td><td>WDR</td><td>SR</td><td>PR</td><td>DR</td><td>TR</td><td>HR</td><td>WR</td></tr><tr><td>R_25_1_8</td><td>1(61)</td><td>0(47)</td><td>1(29)</td><td>0(4)</td><td>0(77)</td><td>0(43)</td><td>2(48)</td><td>4(97)</td><td>1(60)</td><td>2(152)</td></tr><tr><td>R_50_1_14</td><td>24(179)</td><td>2(111)</td><td>6(205)</td><td>3(68)</td><td>4(188)</td><td>5(137)</td><td>1(72)</td><td>5(257)</td><td>1(56)</td><td>1(154)</td></tr><tr><td>R_75_1_20</td><td>14(195)</td><td>6(94)</td><td>3(208)</td><td>1(154)</td><td>7(235)</td><td>6(178)</td><td>4(42)</td><td>6(290)</td><td>9(189)</td><td>4(168)</td></tr><tr><td>R_100_1_24</td><td>17(226)</td><td>9(73)</td><td>9(292)</td><td>4(107)</td><td>7(228)</td><td>7(196)</td><td>2(32)</td><td>4(306)</td><td>8(163)</td><td>7(256)</td></tr></table>

Table 9  
Number of global best solutions found and number of improving solutions achieved by the insertion operators.

<table><tr><td>Instance</td><td>GI</td><td>SI</td><td>GIN</td><td>SIN</td><td>λ FI</td><td>oGI</td><td>oSI</td><td>oGIN</td><td>oSIN</td><td>oλ FI</td></tr><tr><td>R_25_1_8</td><td>1(7)</td><td>1(7)</td><td>0(3)</td><td>0(2)</td><td>0(0)</td><td>3(253)</td><td>4(210)</td><td>2(73)</td><td>0(63)</td><td>0(0)</td></tr><tr><td>R_50_1_14</td><td>18(36)</td><td>0(10)</td><td>0(3)</td><td>0(1)</td><td>0(0)</td><td>19(755)</td><td>15(575)</td><td>0(25)</td><td>0(22)</td><td>0(0)</td></tr><tr><td>R_75_1_20</td><td>8(21)</td><td>0(5)</td><td>0(0)</td><td>0(2)</td><td>0(0)</td><td>28(1069)</td><td>23(628)</td><td>1(15)</td><td>0(13)</td><td>0(0)</td></tr><tr><td>R_100_1_24</td><td>12(27)</td><td>0(6)</td><td>0(1)</td><td>0(0)</td><td>0(0)</td><td>32(1211)</td><td>30(630)</td><td>0(2)</td><td>0(2)</td><td>0(0)</td></tr></table>

The results indicate that all removal operators, to some extent, contribute to achieving improved solutions. On the other hand, some insertion operators (i.e., λFI and oλFI) do not improve a current solution at any time. However, as it will be shown below, these operators are needed to diversify the search and achieve better overall performance of the algorithm. Furthermore, as expected, greedy operators (i.e., best and second-best) help obtaining improved solutions.

In order to identify the usefulness of the new insertion operators proposed in this paper, we tested four configurations of the ALNS. These are shown in Table 10, along with the average objective function values over 10 runs of the algorithm. We used the same instances as in Table 4.

Table 10  
A tuning of insertion operators.

<table><tr><td>Configuration</td><td>Average value €</td></tr><tr><td>Without SI and SIN</td><td>949.61</td></tr><tr><td>Without λFI and oλFI</td><td>952.15</td></tr><tr><td>Without SI, SIN, λFI and oλFI</td><td>956.13</td></tr><tr><td>With all operators</td><td>948.25</td></tr></table>

According to the obtained results, using SI, SIN and λFI operators leads to the best performance of the algorithm. These operators are mainly destined to diversify the search. As seen in Table 10, it seems imperative to use such operators along with the unconventional scoring setting.

## 4.3. Results of the proposed algorithm on the PDPTWs

In this section, we provide in Tables 11–13 computational results on the PDPTW benchmark instances (i.e., [19]), which come in three sets: R, C and RC classified with respect to the positioning of the customers (i.e., random, clustered and randomly clustered). The reason for choosing these instances is that Røpke and Cordeau [27] and Baldacci et al. [2] provided their results by using the minimization of operating costs as our algorithm does. Tables 11–13 compare published results to the ones obtained by our ALNS heuristic algorithm. The values of the best known (or even optimal) solutions obtained from [27,2,28] are given in under column “Best known value”. Note that the values in bold emphasize that the proposed algorithm found the best known solution. The symbol “n” indicates that the values are not necessary optimal and are obtained by Røpke and Pisinger [28]. Moreover, we note that all figures presented in these tables use a single decimal digit. For the ALNS algorithm, we then present the best solution value obtained in column “ALNS best found”. In addition, we indicate “ALNS average value” after 10 runs with the corresponding average GAP (%) (i.e., let υðALNSÞ be the value of the solution found by the proposed ALNS, then, the GAP (%) 100 (υ(ALNS) υ(Best))/υ(ALNS), where υ(Best) is the value of the best solution known). Finally, we show the average CPU time required to solve the instances using the algorithm.

Results of the proposed algorithm on benchmark PDPTW-C instances.

<table><tr><td>Li and Lim [19] instances</td><td># of requests</td><td>Best known value</td><td>CPU seconds</td><td>ALNS best found</td><td>ALNS average value</td><td>GAP %</td><td>CPU seconds</td></tr><tr><td>LC1_2_1</td><td>106</td><td>2704.6</td><td>3</td><td>2704.6</td><td>2704.6</td><td>0.00</td><td>47</td></tr><tr><td>LC1_2_2</td><td>105</td><td>2764.6</td><td>22</td><td>2764.6</td><td>2764.8</td><td>0.01</td><td>51</td></tr><tr><td>LC1_2_3</td><td>103</td><td>2772.2</td><td>115</td><td>2772.2</td><td>2779.3</td><td>0.26</td><td>121</td></tr><tr><td>LC1_2_4</td><td>105</td><td>2661.4*</td><td>209</td><td>2661.4</td><td>2684.0</td><td>0.84</td><td>123</td></tr><tr><td>LC1_2_5</td><td>107</td><td>2702.0</td><td>5</td><td>2702.0</td><td>2702.0</td><td>0.00</td><td>40</td></tr><tr><td>LC1_2_6</td><td>107</td><td>2701.0</td><td>7</td><td>2701.0</td><td>2701.0</td><td>0.00</td><td>42</td></tr><tr><td>LC1_2_7</td><td>107</td><td>2701.0</td><td>8</td><td>2701.0</td><td>2701.0</td><td>0.00</td><td>38</td></tr><tr><td>LC1_2_8</td><td>105</td><td>2689.8</td><td>16</td><td>2689.8</td><td>2689.9</td><td>0.00</td><td>43</td></tr><tr><td>LC1_2_9</td><td>105</td><td>2724.2</td><td>55</td><td>2724.2</td><td>2758.1</td><td>1.23</td><td>63</td></tr><tr><td>LC1_2_10</td><td>104</td><td>2741.6</td><td>137</td><td>2743.9</td><td>2763.8</td><td>0.80</td><td>67</td></tr><tr><td>Average</td><td></td><td></td><td>58</td><td></td><td></td><td>0.31</td><td>66</td></tr></table>

Table 12  
Results of the ALNS heuristic on benchmark PDPTW-RC instances.

<table><tr><td>Li and Lim [19] instances</td><td># of requests</td><td>Best known value</td><td>CPU seconds</td><td>ALNS best found</td><td>ALNS average value</td><td>GAP %</td><td>CPU seconds</td></tr><tr><td>LRC1_2_1</td><td>106</td><td>3606.1</td><td>3</td><td>3606.1</td><td>3608.9</td><td>0.08</td><td>45</td></tr><tr><td>LRC1_2_2</td><td>103</td><td>3292.4</td><td>322</td><td>3292.4</td><td>3304.3</td><td>0.36</td><td>67</td></tr><tr><td>LRC1_2_3</td><td>105</td><td>3079.5*</td><td>183</td><td>3108.5</td><td>3121.2</td><td>1.34</td><td>107</td></tr><tr><td>LRC1_2_4</td><td>106</td><td>2525.8*</td><td>284</td><td>2552.1</td><td>2583.2</td><td>2.22</td><td>190</td></tr><tr><td>LRC1_2_5</td><td>107</td><td>3715.8</td><td>42</td><td>3766.2</td><td>3788.3</td><td>1.91</td><td>55</td></tr><tr><td>LRC1_2_6</td><td>105</td><td>3360.9</td><td>7</td><td>3382.4</td><td>3401.0</td><td>1.18</td><td>39</td></tr><tr><td>LRC1_2_7</td><td>106</td><td>3317.7</td><td>408</td><td>3344.3</td><td>3377.1</td><td>1.76</td><td>52</td></tr><tr><td>LRC1_2_8</td><td>104</td><td>3086.5</td><td>1563</td><td>3129.5</td><td>3143.7</td><td>1.82</td><td>63</td></tr><tr><td>LRC1_2_9</td><td>104</td><td>3053.8</td><td>1757</td><td>3093.6</td><td>3141.5</td><td>2.79</td><td>54</td></tr><tr><td>LRC1_2_10</td><td>105</td><td>2837.5*</td><td>156</td><td>2857.2</td><td>2881.3</td><td>1.52</td><td>51</td></tr><tr><td>Average</td><td></td><td></td><td>473</td><td></td><td></td><td>1.49</td><td>72</td></tr></table>

Table 13  
Results of the ALNS heuristic on benchmark PDPTW-R instances.

<table><tr><td>Li and Lim [19] instances</td><td># of requests</td><td>Best known value</td><td>CPU seconds</td><td>ALNS best found</td><td>ALNS average value</td><td>GAP %</td><td>CPU seconds</td></tr><tr><td>LR1_2_1</td><td>105</td><td>4819.1</td><td>2</td><td>4819.1</td><td>4819.1</td><td>0.00</td><td>42</td></tr><tr><td>LR1_2_2</td><td>105</td><td>4093.1</td><td>21</td><td>4093.1</td><td>4101.4</td><td>0.20</td><td>96</td></tr><tr><td>LR1_2_3</td><td>104</td><td>3486.8</td><td>3691</td><td>3486.8</td><td>3503.6</td><td>0.48</td><td>162</td></tr><tr><td>LR1_2_4</td><td>105</td><td>2830.7*</td><td>228</td><td>2839.1</td><td>2873.1</td><td>1.48</td><td>201</td></tr><tr><td>LR1_2_5</td><td>106</td><td>4221.6</td><td>3</td><td>4221.6</td><td>4239.2</td><td>0.42</td><td>42</td></tr><tr><td>LR1_2_6</td><td>107</td><td>3763.0</td><td>181</td><td>3763.0</td><td>3769.9</td><td>0.18</td><td>70</td></tr><tr><td>LR1_2_7</td><td>103</td><td>3112.9*</td><td>173</td><td>3112.9</td><td>3124.9</td><td>0.38</td><td>107</td></tr><tr><td>LR1_2_8</td><td>103</td><td>2645.4*</td><td>226</td><td>2652.4</td><td>2664.7</td><td>0.72</td><td>159</td></tr><tr><td>LR1_2_9</td><td>105</td><td>3953.5</td><td>15</td><td>3953.5</td><td>3961.0</td><td>0.19</td><td>52</td></tr><tr><td>LR1_2_10</td><td>104</td><td>3386.3</td><td>1377</td><td>3390.4</td><td>3411.2</td><td>0.73</td><td>62</td></tr><tr><td>Average</td><td></td><td></td><td>592</td><td></td><td></td><td>0.48</td><td>99</td></tr></table>

As shown in Tables 11–13, the ALNS heuristic proved good performance on the PDPTW instances. For 18 out of 30 instances, our heuristic algorithm obtained the best known solutions in at least one out of the 10 runs. For the remaining 12 instances, the GAPs are found to be not greater than 2.79%. The average CPU time needed to solve the instances is found to be 78 s.

## 4.4. Results of the generated instances

In this section, we provide the results on the four generated sets of PDPTW-SL instances. These sets are generated from the three main datasets described in Section 4.1, by considering subsets of request, transfer node and PD vehicle sets. For the first group (with up to 12 requests and one SL), each instance was solved 10 times with the proposed heuristic and once with the PDPTW-SL MIP model by using CPLEX 12.3 (IBM ILOG [17]) with its default settings and the valid inequalities proposed by Ghilas et al. [14]. A time-limit of ten hours was imposed to CPLEX. The following three groups were solved 10 times using the proposed ALNS in the context of PDPTW-SL and PDPTW. The detailed results of these experiments are presented in Tables 14–17.

## Table 14

Computational results for the instances with up to 12 requests.

<table><tr><td rowspan="2">Instance</td><td colspan="4">CPLEX</td><td colspan="3">ALNS</td></tr><tr><td>Upper bound</td><td>Lower bound</td><td>GAP %</td><td>CPU seconds</td><td>Value</td><td>GAP %</td><td>CPU seconds</td></tr><tr><td>C_6_1_4</td><td>369.36</td><td>369.36</td><td>0.00</td><td>5267</td><td>369.36</td><td>0.00</td><td>1</td></tr><tr><td>C_7_1_4</td><td>390.31</td><td>390.31</td><td>0.00</td><td>3762</td><td>390.31</td><td>0.00</td><td>1</td></tr><tr><td>C_8_1_4</td><td>446.35</td><td>384.93</td><td>13.76</td><td>36,000</td><td>446.35</td><td>-</td><td>2</td></tr><tr><td>C_9_1_4</td><td>493.66</td><td>327.43</td><td>33.67</td><td>36,000</td><td>472.68</td><td>-</td><td>2</td></tr><tr><td>C_10_1_4</td><td>-</td><td>335.89</td><td>-</td><td>36,000</td><td>510.01</td><td>-</td><td>2</td></tr><tr><td>C_11_1_4</td><td>-</td><td>347.68</td><td>-</td><td>36,000</td><td>522.84</td><td>-</td><td>2</td></tr><tr><td>C_12_1_4</td><td>-</td><td>366.81</td><td>-</td><td>36,000</td><td>541.60</td><td>-</td><td>2</td></tr><tr><td>RC_6_1_4</td><td>572.76</td><td>572.76</td><td>0.00</td><td>185</td><td>572.76</td><td>0.00</td><td>1</td></tr><tr><td>RC_7_1_4</td><td>575.95</td><td>575.95</td><td>0.00</td><td>368</td><td>575.95</td><td>0.00</td><td>1</td></tr><tr><td>RC_8_1_4</td><td>585.32</td><td>585.32</td><td>0.00</td><td>961</td><td>585.32</td><td>0.00</td><td>1</td></tr><tr><td>RC_9_1_4</td><td>593.70</td><td>593.70</td><td>0.00</td><td>32,204</td><td>593.70</td><td>0.00</td><td>2</td></tr><tr><td>RC_10_1_4</td><td>599.95</td><td>599.95</td><td>0.00</td><td>24,925</td><td>599.95</td><td>0.00</td><td>2</td></tr><tr><td>RC_11_1_4</td><td>624.48</td><td>624.48</td><td>0.00</td><td>18,128</td><td>624.48</td><td>0.00</td><td>2</td></tr><tr><td>RC_12_1_6</td><td>-</td><td>608.89</td><td>-</td><td>36,000</td><td>662.03</td><td>-</td><td>2</td></tr><tr><td>R_6_1_4</td><td>416.16</td><td>416.16</td><td>0.00</td><td>2</td><td>416.16</td><td>0.00</td><td>1</td></tr><tr><td>R_7_1_4</td><td>473.06</td><td>473.06</td><td>0.00</td><td>5</td><td>473.06</td><td>0.00</td><td>1</td></tr><tr><td>R_8_1_4</td><td>558.17</td><td>558.17</td><td>0.00</td><td>16</td><td>558.17</td><td>0.00</td><td>1</td></tr><tr><td>R_9_1_4</td><td>632.42</td><td>632.42</td><td>0.00</td><td>8782</td><td>632.42</td><td>0.00</td><td>1</td></tr><tr><td>R_10_1_4</td><td>636.05</td><td>636.05</td><td>0.00</td><td>3421</td><td>636.05</td><td>0.00</td><td>2</td></tr><tr><td>R_11_1_4</td><td>748.29</td><td>748.29</td><td>0.00</td><td>17,493</td><td>748.29</td><td>0.00</td><td>2</td></tr><tr><td>R_12_1_6</td><td>-</td><td>771.01</td><td>-</td><td>36,000</td><td>934.73</td><td>-</td><td>2</td></tr></table>

## Table 15

Results of C instances.

<table><tr><td>Instance</td><td>Best known value</td><td>Average value</td><td>Average GAP %</td><td>Cost savings %</td><td>Best driving time</td><td>Driving time sav-ings %</td><td>CPU seconds</td><td># of vehicles used</td><td>Units on SLs</td></tr><tr><td>C25_0_8</td><td>1076.70</td><td>1083.40</td><td>0.62</td><td></td><td>2153.40</td><td></td><td>1</td><td>6</td><td></td></tr><tr><td>C25_1_8</td><td>879.94</td><td>882.63</td><td>0.30</td><td>18.27</td><td>1737.88</td><td>19.30</td><td>7</td><td>5</td><td>11</td></tr><tr><td>C25_2_8</td><td>878.86</td><td>881.26</td><td>0.27</td><td>18.37</td><td>1723.72</td><td>19.95</td><td>8</td><td>7</td><td>17</td></tr><tr><td>C25_3_8</td><td>753.03</td><td>754.33</td><td>0.17</td><td>30.06</td><td>1468.06</td><td>31.83</td><td>14</td><td>5</td><td>19</td></tr><tr><td>C_50_0_12</td><td>1529.37</td><td>1541.56</td><td>0.79</td><td></td><td>3058.73</td><td></td><td>4</td><td>8</td><td></td></tr><tr><td>C_50_1_12</td><td>1415.60</td><td>1425.67</td><td>0.71</td><td>7.44</td><td>2793.19</td><td>8.68</td><td>124</td><td>10</td><td>14</td></tr><tr><td>C_50_2_12</td><td>1342.23</td><td>1356.01</td><td>1.02</td><td>12.24</td><td>2634.47</td><td>13.87</td><td>121</td><td>10</td><td>50</td></tr><tr><td>C_50_3_12</td><td>1214.16</td><td>1229.30</td><td>1.23</td><td>20.61</td><td>2354.31</td><td>23.03</td><td>144</td><td>10</td><td>74</td></tr><tr><td>C_75_0_16</td><td>2040.54</td><td>2069.10</td><td>1.38</td><td></td><td>4081.09</td><td></td><td>12</td><td>10</td><td></td></tr><tr><td>C_75_1_16</td><td>1807.33</td><td>1829.14</td><td>1.19</td><td>11.43</td><td>3558.66</td><td>12.80</td><td>411</td><td>12</td><td>56</td></tr><tr><td>C_75_2_16</td><td>1686.85</td><td>1702.30</td><td>0.91</td><td>17.33</td><td>3283.70</td><td>19.54</td><td>528</td><td>12</td><td>90</td></tr><tr><td>C_75_3_16</td><td>1621.18</td><td>1641.60</td><td>1.24</td><td>20.55</td><td>3112.36</td><td>23.74</td><td>650</td><td>13</td><td>130</td></tr><tr><td>C_100_0_20</td><td>2349.46</td><td>2378.79</td><td>1.23</td><td></td><td>4698.91</td><td></td><td>34</td><td>12</td><td></td></tr><tr><td>C_100_1_20</td><td>2112.73</td><td>2126.42</td><td>0.64</td><td>10.08</td><td>4167.47</td><td>11.31</td><td>2378</td><td>13</td><td>58</td></tr><tr><td>C_100_2_20</td><td>2040.36</td><td>2069.71</td><td>1.42</td><td>13.16</td><td>3964.72</td><td>15.62</td><td>2224</td><td>14</td><td>116</td></tr><tr><td>C_100_3_20</td><td>1915.40</td><td>1939.87</td><td>1.26</td><td>18.47</td><td>3662.80</td><td>22.05</td><td>2357</td><td>14</td><td>168</td></tr></table>

Table 16 Results of RC instances.

<table><tr><td>Instance</td><td>Best known value</td><td>Average value</td><td>Average GAP %</td><td>Cost savings %</td><td>Best driving time</td><td>Driving time sav-ings %</td><td>CPU seconds</td><td># of vehicles used</td><td>Units on SLs</td></tr><tr><td>RC_25_0_8</td><td>1572.08</td><td>1572.08</td><td>0.00</td><td></td><td>3144.16</td><td></td><td>1</td><td>7</td><td></td></tr><tr><td>RC_25_1_8</td><td>1530.43</td><td>1530.43</td><td>0.00</td><td>2.65</td><td>3048.86</td><td>3.03</td><td>3</td><td>8</td><td>6</td></tr><tr><td>RC_25_2_8</td><td>1413.06</td><td>1414.44</td><td>0.10</td><td>10.12</td><td>2808.12</td><td>10.69</td><td>4</td><td>7</td><td>9</td></tr><tr><td>RC_25_3_8</td><td>1377.54</td><td>1382.58</td><td>0.36</td><td>12.37</td><td>2727.08</td><td>13.27</td><td>6</td><td>7</td><td>14</td></tr><tr><td>RC50_0_14</td><td>2270.83</td><td>2270.83</td><td>0.00</td><td></td><td>4541.66</td><td></td><td>3</td><td>10</td><td></td></tr><tr><td>RC50_1_14</td><td>2213.06</td><td>2213.54</td><td>0.02</td><td>2.54</td><td>4416.12</td><td>2.76</td><td>11</td><td>10</td><td>5</td></tr><tr><td>RC50_2_14</td><td>2213.06</td><td>2213.85</td><td>0.04</td><td>2.54</td><td>4416.12</td><td>2.76</td><td>12</td><td>10</td><td>5</td></tr><tr><td>RC50_3_14</td><td>2211.89</td><td>2214.13</td><td>0.10</td><td>2.60</td><td>4409.78</td><td>2.90</td><td>15</td><td>10</td><td>7</td></tr><tr><td>RC_75_0_16</td><td>2863.05</td><td>2868.34</td><td>0.18</td><td></td><td>5726.11</td><td></td><td>9</td><td>12</td><td></td></tr><tr><td>RC_75_1_16</td><td>2814.39</td><td>2825.63</td><td>0.40</td><td>1.70</td><td>5616.78</td><td>1.91</td><td>143</td><td>12</td><td>12</td></tr><tr><td>RC_75_2_16</td><td>2814.39</td><td>2836.39</td><td>0.78</td><td>1.70</td><td>5616.78</td><td>1.91</td><td>155</td><td>12</td><td>12</td></tr><tr><td>RC_75_3_16</td><td>2814.39</td><td>2839.05</td><td>0.87</td><td>1.70</td><td>5616.78</td><td>1.91</td><td>181</td><td>12</td><td>12</td></tr><tr><td>RC_100_0_18</td><td>3,114.35</td><td>3,119.10</td><td>0.15</td><td></td><td>6228.70</td><td></td><td>25</td><td>12</td><td></td></tr><tr><td>RC_100_1_18</td><td>3088.07</td><td>3093.66</td><td>0.18</td><td>0.84</td><td>6164.13</td><td>1.04</td><td>794</td><td>12</td><td>12</td></tr><tr><td>RC_100_2_18</td><td>3088.07</td><td>3100.22</td><td>0.39</td><td>0.84</td><td>6164.13</td><td>1.04</td><td>677</td><td>12</td><td>12</td></tr><tr><td>RC_100_3_18</td><td>3088.07</td><td>3134.30</td><td>1.48</td><td>0.84</td><td>6164.13</td><td>1.04</td><td>985</td><td>12</td><td>12</td></tr></table>

Table 17 Results of R instances.

<table><tr><td>Instance</td><td>Best known value</td><td>Average value</td><td>Average GAP %</td><td>Cost savings %</td><td>Best driving time</td><td>Driving time sav-ings %</td><td>CPU seconds</td><td># of vehicles used</td><td>Units on SLs</td></tr><tr><td>R_25_0_8</td><td>1717.39</td><td>1724.71</td><td>0.42</td><td></td><td>3449.42</td><td></td><td>1</td><td>8</td><td></td></tr><tr><td>R_25_1_8</td><td>1636.12</td><td>1637.72</td><td>0.10</td><td>4.73</td><td>3266.24</td><td>5.31</td><td>2</td><td>8</td><td>3</td></tr><tr><td>R_25_2_8</td><td>1597.75</td><td>1601.97</td><td>0.26</td><td>6.97</td><td>3185.50</td><td>7.65</td><td>2</td><td>8</td><td>5</td></tr><tr><td>R_25_3_8</td><td>1540.96</td><td>1545.94</td><td>0.32</td><td>10.27</td><td>3069.92</td><td>11.00</td><td>3</td><td>8</td><td>6</td></tr><tr><td>R_50_0_14</td><td>2620.88</td><td>2649.70</td><td>1.09</td><td></td><td>5241.76</td><td></td><td>2</td><td>13</td><td></td></tr><tr><td>R_50_1_14</td><td>2595.14</td><td>2604.2</td><td>0.35</td><td>0.98</td><td>5186.28</td><td>1.06</td><td>8</td><td>12</td><td>2</td></tr><tr><td>R_50_2_14</td><td>2412.89</td><td>2420.67</td><td>0.32</td><td>7.94</td><td>4803.78</td><td>8.36</td><td>20</td><td>12</td><td>11</td></tr><tr><td>R_50_3_14</td><td>2392.81</td><td>2403.52</td><td>0.45</td><td>8.70</td><td>4759.62</td><td>9.20</td><td>21</td><td>12</td><td>13</td></tr><tr><td>R_75_0_20</td><td>3337.85</td><td>3337.85</td><td>0.00</td><td></td><td>6675.70</td><td></td><td>7</td><td>14</td><td></td></tr><tr><td>R_75_1_20</td><td>3337.85</td><td>3355.41</td><td>0.52</td><td>0.00</td><td>6675.70</td><td>0.00</td><td>69</td><td>14</td><td>0</td></tr><tr><td>R_75_2_20</td><td>3321.14</td><td>3361.77</td><td>1.21</td><td>0.50</td><td>6630.28</td><td>0.68</td><td>98</td><td>15</td><td>12</td></tr><tr><td>R_75_3_20</td><td>3321.14</td><td>3349.07</td><td>0.83</td><td>0.50</td><td>6630.28</td><td>0.68</td><td>110</td><td>15</td><td>12</td></tr><tr><td>R_100_0_24</td><td>3643.07</td><td>3646.89</td><td>0.10</td><td></td><td>7286.14</td><td></td><td>26</td><td>15</td><td></td></tr><tr><td>R_100_1_24</td><td>3643.07</td><td>3665.31</td><td>0.61</td><td>0.00</td><td>7286.14</td><td>0.00</td><td>538</td><td>15</td><td>0</td></tr><tr><td>R_100_2_24</td><td>3628.87</td><td>3646.65</td><td>0.49</td><td>0.39</td><td>7245.74</td><td>0.55</td><td>690</td><td>16</td><td>12</td></tr><tr><td>R_100_3_24</td><td>3628.87</td><td>3637.37</td><td>0.23</td><td>0.39</td><td>7245.74</td><td>0.55</td><td>725</td><td>16</td><td>12</td></tr></table>

Table 14 indicates that in most of the cases, the ALNS algorithm generated the same solutions as CPLEX, but in a significantly shorter CPU times. For the instances solved to optimality, the average CPU time required by CPLEX is approximately 8251 s whereas ALNS needed approximately 2 s. In some cases where CPLEX could not find any solution or could obtain a sub-optimal one, the proposed ALNS was able to find solutions that have a tighter GAP relative to the best lower bound found within the imposed time limit.

Tables 15–17 provide the results obtained for larger instances. The column Instance indicates the instance identification, The Best knowp cost column indicates the best objective value found after 10 runs of the algorithm. In addition, columns Average cost and Average GAP show the average objective values over 10 runs and respectively the average GAP from the best solution found. The Cost savings column indicates the cost savings of the best PDPTW-SL solution compared to the best corresponding PDPTW solution. The Best driving time column shows the total driving time of the best solution found and the Driving time savings indicate the savings with regard to the tota driving time. CPU indicates the average computational time for solving the instances. Vehicles used and Units on SLs provide the number of PD vehicles used and the number of shipments (demand units) on the available SLs in the best solution found.

The proposed algorithm is relatively fast. For example, instances of up to 100 requests are solved in less than 40 min. As it can be noticed from Tables 15–17, the ALNS algorithm for the PDPTW-SL is substantially slower than the same algorithm in case of the PDPTW. The main reason is the extra complexity that is induced by having the flexibility of using available scheduled lines, thus making multiple PD-vehicle routes depend on each other. In particular synchronization constraints (i.e., time windows and capacity) require extra computation time (e.g., 20–30% of the CPU time).

It is noted that the efficiency of the proposed system may be highly dependent on both the spatial pattern of the requests and the configuration of the scheduled lines. Unless the design of the scheduled line services (routes and schedules) is integrated with vehicle routing, it is likely that the gains from an integrated system operation would be very small. Hence, designing such a system involves tactical decisions related to the pattern of the scheduled lines (positioning of the transfer nodes relative to the demand nodes clusters), the storage areas at the transfer nodes, and the re-design of the SL vehicles (e.g., freight compartment), that are not taken into consideration in this paper as the focus was on operational costs of the proposed system.

Overall, the results indicate the potential operating costs due to available scheduled lines. In particular, the savings range from 0 to 30% with regard to operating costs and from 0 to 31% in terms of driving time. Note that in this study the amount of $\mathsf { C O } _ { 2 } \mathsf { e }$ emissions is directly proportional to total driving time as we disregard the extra emissions produced by the SLs due to extra carried weight (i.e., packages)

The most of the savings can be achieved by shipping requests on the available SLs. However, the number of PD vehicles used slightly increases in PDPTW-SL compared to the solutions for PDPTW, especially in C instances. It is explained by the fact that the number of vehicles used depends on the time windows, capacities, and demands. Moreover, we note that savings decrease along with the increase in the number of requests for R and RC instances. This can be explained by the increasing density of the requests over the considered area (200 200 time units). Hence, driving time from one demand node to another becomes shorter. For C instances the savings remain significant for larger instances as well. Hence, we can conclude that the more demand points are clustered around transfer nodes, the better performance of the system is. An obvious point that is supported by the results is that the more SLs are available, more savings can be achieved compared to the classical PDPTW.

## 4.5. The effect of heterogeneous routing costs on the algorithm performance

In this section, we present computational experiments on the instances with heterogeneous vehicle routing costs that are based on the vehicle capacity. The minimum-capacity vehicle is assumed to cost 0.5 €per operating time unit. Larger vehicles are assigned a cost that increases linearly along with the carrying capacity. Each instance is run 10 times and the results are given in Table 18. The columns are self-explanatory, similar to previously presented tables.

Table 18  
An analysis of heterogeneous vehicle routing costs.

<table><tr><td>Instance</td><td>Best known value</td><td>Average value</td><td>Average GAP %</td><td>Cost savings %</td><td>CPU seconds</td><td># of vehicles used</td><td>Units on SLs</td></tr><tr><td>25_C_0_8</td><td>1676.53</td><td>1693.02</td><td>0.97</td><td></td><td>2</td><td>6</td><td></td></tr><tr><td>25_C_1_8</td><td>1333.99</td><td>1354.51</td><td>1.51</td><td>20.43</td><td>6</td><td>6</td><td>13</td></tr><tr><td>25_RC_0_8</td><td>2513.39</td><td>2540.65</td><td>1.07</td><td></td><td>1</td><td>7</td><td></td></tr><tr><td>25_RC_1_8</td><td>2403.87</td><td>2421.96</td><td>0.75</td><td>4.36</td><td>4</td><td>8</td><td>6</td></tr><tr><td>25_R_0_8</td><td>2145.41</td><td>2171.02</td><td>1.18</td><td></td><td>2</td><td>8</td><td></td></tr><tr><td>25_R_1_8</td><td>2019.78</td><td>2035.34</td><td>0.76</td><td>5.86</td><td>2</td><td>8</td><td>1</td></tr><tr><td>50_C_0_12</td><td>1623.09</td><td>1635.45</td><td>0.76</td><td></td><td>3</td><td>8</td><td></td></tr><tr><td>50_C_1_12</td><td>1459.64</td><td>1489.81</td><td>2.03</td><td>10.07</td><td>37</td><td>9</td><td>17</td></tr><tr><td>50_RC_0_14</td><td>3751.17</td><td>3784.39</td><td>0.88</td><td></td><td>5</td><td>10</td><td></td></tr><tr><td>50_RC_1_14</td><td>3570.35</td><td>3611.17</td><td>1.13</td><td>4.82</td><td>12</td><td>10</td><td>5</td></tr><tr><td>50_R_0_14</td><td>3271.88</td><td>3281.55</td><td>0.29</td><td></td><td>4</td><td>12</td><td></td></tr><tr><td>50_R_1_14</td><td>3231.22</td><td>3258.57</td><td>0.84</td><td>1.24</td><td>7</td><td>13</td><td>6</td></tr><tr><td>75_C_0_16</td><td>2278.57</td><td>2309.17</td><td>1.33</td><td></td><td>8</td><td>11</td><td></td></tr><tr><td>75_C_1_16</td><td>1955.53</td><td>1972.39</td><td>0.85</td><td>14.18</td><td>698</td><td>11</td><td>25</td></tr><tr><td>75_RC_0_16</td><td>3164.14</td><td>3183.45</td><td>0.61</td><td></td><td>7</td><td>12</td><td></td></tr><tr><td>75_RC_1_16</td><td>3144.66</td><td>3155.30</td><td>0.34</td><td>0.62</td><td>122</td><td>12</td><td>6</td></tr><tr><td>75_R_0_20</td><td>3583.39</td><td>3603.99</td><td>0.57</td><td></td><td>5</td><td>14</td><td></td></tr><tr><td>75_R_1_20</td><td>3572.31</td><td>3586.76</td><td>0.40</td><td>0.31</td><td>138</td><td>15</td><td>2</td></tr><tr><td>100_C_0_20</td><td>3985.45</td><td>4017.42</td><td>0.80</td><td></td><td>22</td><td>12</td><td></td></tr><tr><td>100_C_1_20</td><td>3557.39</td><td>3576.59</td><td>0.54</td><td>10.74</td><td>2178</td><td>13</td><td>36</td></tr><tr><td>100_RC_0_18</td><td>3420.74</td><td>3461.23</td><td>1.17</td><td></td><td>9</td><td>13</td><td></td></tr><tr><td>100_RC_1_18</td><td>3344.28</td><td>3362.95</td><td>0.56</td><td>2.24</td><td>644</td><td>12</td><td>6</td></tr><tr><td>100_R_0_24</td><td>3758.27</td><td>3792.44</td><td>0.90</td><td></td><td>13</td><td>15</td><td></td></tr><tr><td>100_R_1_24</td><td>3758.27</td><td>3825.33</td><td>1.75</td><td>0.00</td><td>668</td><td>15</td><td>0</td></tr></table>

According to the obtained results, the proposed ALNS seems to perform stable when considering heterogeneous costs, leading to solutions with an average GAP of 0.91% compared to the best known solutions. In addition, the results indicate that objective function values tend to increase due to larger routing costs (heterogeneous costs) for the considered vehicles, compared to homogeneous case (i.e., 0.5 €for all vehicles). In this context, making use of available SLs leads to average cost savings of 6.24% compared to the corresponding best-known PDPTW solutions.

## 4.6. An application study

In this section we investigate the performance of the PDPTW-SL environment on a realistic scheduled lined system. In particular, we solve one instance of 100 randomly generated requests on a 60  60 time-units area, three depots and 20 PD vehicles. The scheduled lines graph is shown in Fig. 5 and it is inspired from the current metro system in Amsterdam (see Fig. 1). The distances are considered Euclidean and time windows are randomly generated.

The results shown in Table 19 are obtained after five runs of the algorithm and indicate the best solutions found for both PDPTW-SL and PDPTW. In particular, the PDPTW-SL integrated transportation system led to 5% savings in terms of operating costs and 9% in shorte total driving time. Even though PDPTW-SL system can lead to operating costs and $\mathsf { C O } _ { 2 } \mathsf { e }$ emissions benefits, the number of vehicles used is increased as compared to PDPTW.

![](02-Ghilas-2016-LNS_images/4df88f49d9bd588e3b9b14ad3f33f18c5f971ee2da33a5826bc5479382713a2c.jpg)  
Fig. 5. An illustrative representation of Amsterdam's metro system.

Table 19  
Results on a realistic real-life scheduled line system.

<table><tr><td rowspan="2">Instance</td><td colspan="5">PDPTW-SL</td><td colspan="4">PDPTW</td></tr><tr><td>Driving time</td><td>Units on SLs</td><td>Cost €</td><td>CPU seconds</td><td># of vehicles</td><td>Driving time</td><td>Cost €</td><td>CPU seconds</td><td># of vehicles</td></tr><tr><td>Amsterdam 100 requests</td><td>1767.22</td><td>36</td><td>919.61</td><td>1258.52</td><td>10</td><td>1945.69</td><td>972.85</td><td>34.62</td><td>7</td></tr></table>

## 5. Conclusions

We proposed a metaheuristic algorithm to solve the PDPTW-SL. To investigate the performance of the algorithm, we have generated several sets of PDPTW-SL instances. Compared to the existing solutions on a set of PDPTW instances, the proposed algorithm performed well in terms of both, solution quality (with a maximum GAP of 2.79%) and CPU time (78 s on average). Furthermore, we have also shown that small PDPTW-SL instances can be solved optimally by the proposed formulation. The solutions obtained from solving larger instances, up to 100 requests, were compared to their corresponding PDPTW solutions and it is concluded that the flexibility of using scheduled line services leads to significant cost savings and fewer CO e emissions. However, note that the performance of the PDPTW-SL system may be highly dependent on the relative positioning of the scheduled lines to the request nodes. In addition, investment costs needed for implementing such system may affect its outcome.

The reliability of such a system may decrease due to extra causes of delays and cargo damages (i.e., transfers to/from SLs, delays in SL schedules). Therefore, shippers may not be willing to use PDPTW-SL system. In order to tackle such issues, more advanced planning tools are needed, which consider stochastic aspects of the problem. The current research state of the considered problem is yet young and further industry collaborations are to be done in order to learn more about practical issues that may or may not prevent the implementation and the execution of such a system.

Overall the numerical experiments indicate that the proposed algorithm leads to high-quality routing solutions for relatively large instances in a reasonable amount of time. Regarding extensions of the investigated problem, additional aspects may be considered such as driver-related constraints, stochastic aspects (demands, travel times) or passenger requests, and the other related constraints (e.g., maximum ride-time). Investigation of exact decomposition algorithms (e.g., Branch and Price) could also be an interesting research direction. In addition, since the results show that the number of PD vehicles used may increase when SLs are introduced, it would be interesting to introduce fixed costs for the PD vehicles as well to make more clear the trade-off between using fewer PD vehicles or using SLs with more PD vehicles.

## Acknowledgments

The authors gratefully acknowledge funds provided by Dinalog, the Dutch Institute for Advanced Logistics, under the Grant titled “Cargo Hitching”, # 2011 4 086R. Thanks are due to the Editor and two anonymous reviewers for their useful comments and for raising interesting points for discussion.

## References

[11 Aldaihani M. Dessouky M. Hybrid scheduling methods for paratransit operations, Comput Ind Eng 2003:45(1):75–96

[2] Baldacci R, Bartolini E, Mingozzi A. An exact algorithm for the pickup and delivery problem with time windows. Oper Res 2011;59(2):414–26.

[3] Berbeglia G, Cordeau J-F, Gribkovskaia I, Laporte G. Static pickup and delivery problems: a classification scheme and survey. TOP: Off J Span Soc Stat Oper Res 2007;15 (1):1–31.

[4] Braekers K, Caris A, Janssens G. Exact and meta-heuristic approach for a general heterogeneous dial-a-ride problem with multiple depots. Transp Res Part B 2014;67:166–86.

[5] Cargo Tram. Official webpage. Available at: 〈www.eltis.org/index.php?id<sub>¼</sub>13&study\_id<sub>¼</sub>1547〉; 2012 [accessed on 21.11.2015].

[6] Cordeau J-F, Laporte G. The dial-a-ride problem: models and algorithms. Ann Oper Res 2007;153(1):29–46.

[7] Cortes E-C, Matamala M, Contardo C. The pickup and delivery problem with transfers: formulation and a branch-and-cut solution method. Eur J Oper Res 2010;200 (3):711–24.

[8] Demir E, Bektaş T, Laporte G. An adaptive large neighborhood search heuristic for the pollution-routing problem. Eur J Oper Res 2012;223(2):346–59

[9] Demir E, Bektaş T, Laporte G. A review of recent research on green road freight transportation. Eur J Oper Res 2014;237(3):775–93.

[10] Demir E, Bektaş T, Laporte G. The bi-objective pollution-routing problem. Eur J Oper Res 2013;232(3):464–78

[11] Demir E, Huang Y, Scholts S, Van Woensel T. A selected review on the negative externalities of the freight transportation: modeling and pricing. Transp Res Part E: Logist Transp Rev 2015;77:95–114.

[12] DHL-Packstation. DHL official webpage. Available at: 〈www.dhl.de/en/paket/pakete-empfangen/packstation.html〉; 2013 [accessed on 21.11.2015].

[13] Dijkstra E-W. A note on two problems in connexion with graphs. Numer Math 1959;1:269–71.

[14] Ghilas V, Demir E, Van Woensel T. Integrating passenger and freight transportation: model formulation and insights. Technical Report, Industrial Engineering & Innovation Sciences Eindhoven University of Technology, BETA No. 441: 2013. p.23

[15] Hall C, Andersson H, Lundgren J, Varbrand P. The integrated dial-a-ride problem. Public Transp 2009;1:39–54.

[16] Hurtigruten. Hurtigruten official webpage. Available at: 〈www.hurtigruten-web.com/index\_en.html〉; 2013 [accessed on 11.11.2015].

[17] IBM ILOG. Copyright international business machines corporation 1987; 2013.

[18] Levin Y, Nediak M, Topaloglu H. Cargo capacity management with allotments and spot market demand. Oper Res 2012;60(2):351–65.

[19] Li H, Lim A. A metaheuristic for the pickup and delivery problem with time windows. Int J Artif Intell Tools 2003;12(2):173–86.

[20] Liaw C-F, White C, Bander J. A decision support system for the bimodal dial-a-ride problem. IEEE Trans Syst Man Cybern Part A 1996;26(5):552–65

[21] Lindholm M, Behrends S. Challenges in urban freight transport planning—a review in the Baltic Sea Region. J Transp Geogr 2012;22:129–36.

[22] Masson R, Lehuede F, Peton O. An adaptive large neighborhood search for the pickup and delivery problem with transfers. Transp Sci 2012;47:1–12

[23] Masson R, Lehuede F, Peton O. The dial-a-ride problem with transfers. Comput Oper Res 2014;41:12–23.

[24] Nash C, editor. Economics of public transport. London, UK: Longman; 1982.

[25] Petersen HL, Røpke S. The pickup and delivery problem with cross-docking opportunity. In: Computational Logistics: Second International Conference, ICCL 2011,

Hamburg, Germany, 19-22 September 2011, Lecture notes in computer science, vol. 6971. Springer, Berlin, Heidelberg; 2011. p. 101–13.

[26] Pisinger D. Røpke S. A general heuristic for vehicle routing problems. Comput Oper Res 2007:34(8):2403–35

[27] Røpke S, Cordeau J-F. Branch and cut and price for the pickup and delivery problem with time windows. Transp Sci 2009;43(3):267–86.

[28] Røpke S, Pisinger D. An adaptive large neighborhood search heuristic for the pickup and delivery problem with time windows. Transp Sci 2006;40(4):455–72.

[29] Shang J, Cuff C. Multicriteria pickup and delivery problem with transfer opportunity. Comput Ind Eng 1996;30(4):631–45.

[30] Shaw P. Using constraint programming and local search methods to solve vehicle routing problems. In: Proceedings of the 4th international conference on principles and practice of constraint programming. New York: Springer; 1998. p. 417–31.

[31] Trentini A, Malhene N. Toward a shared urban transport system ensuring passengers & goods cohabitation. Trimest del Lab Territ Mobilita e Ambient—TeMALab 2010;4:37–44.

[32] Trentini A, Masson R, Lehuede F, Malhene N, Peton O, Tlahig H. A shared “passenger & goods” city logistics system. In: 4th international conference on information systems, logistics and supply chain, Quebec, Canada; 2012.