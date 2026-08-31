---
raw_title: 08-Sundar
subject: 数学建模-策联杯B题
source: "08.pdf"
status: mineru解析
parser: mineru
topics:
  - 混合整数规划
  - 燃油约束
  - 多车辆路径
---

# Analysis of Mixed-Integer Linear Programming Formulations for a Fuel-Constrained Multiple Vehicle Routing Problem

Kaarthik Sundar\*<sup>,§</sup>, Saravanan Venkatachalam<sup>†</sup>, Sivakumar Rathinam<sup>‡</sup>

<sup>\*</sup>Center for Non-Linear Studies, Los Alamos National Laboratory, NM 87544, New Mexico

<sup>†</sup>Department of Industrial and Systems Engineering, Wayne State University, Detroit, MI 48202, Michigan, United States

<sup>‡</sup>Department of Mechanical Engineering, Texas A&M University, College Station, TX 77843, Texas, United States

This paper addresses a fuel-constrained, multiple vehicle routing problem (FCMVRP) in the presence of multiple refueling stations. We are given a set of targets, a set of refueling stations, and a depot where m vehicles are stationed. The vehicles are allowed to refuel at any refueling station, and the objective of the problem is to determine a route for each vehicle starting and terminating at the depot, such that each target is visited by at least one vehicle, the vehicles never run out of fuel while traversing their routes, and the total travel cost of all the routes is a minimum. We present four new mixed-integer linear programming (MILP) formulations for the problem. These formulations are compared both analytically and empirically, and a branch-and-cut algorithm is developed to compute an optimal solution. Extensive computational results on a large class of test instances that corroborate the efectiveness of the algorithm are also presented.

Keywords: Fuel constraints; green vehicle routing; electric vehicles; mixed-integer linear programming; branch-and-cut.

## 1. Introduction

Increasing concerns about climate change and rising green house gas emissions drive the research in sustainable and energy eficient mobility. One such example is the research involving a possible introduction of self driving, electricallypowered vehicles in the future. One of the main operational challenges for autonomous electric vehicles in transport applications is their limited range and the availability of recharging stations [1, 2]. As of November 2015, the number of electric stations in the US was a mere 9,571 with a total of 24,631 charging outlets [3]. Figure 1 shows a map with the locations of electric recharging stations in Texas, USA; observe that the distribution of electric stations is very sparse except in the four major cities of Dallas, Houston, Austin, and San Antonio. Successful adoption of autonomous electric vehicles will strongly depend on methods to alleviate the range and recharging limitations.

![](08-Sundar_images/95d69d4a3c6f9484305eeaa47394884494b43097a5ba45ea1117da953c6051fd.jpg)

Another example of sustainable and energy eficient mobility deals with vehicle routing applications involving green vehicles. Green vehicle routing problem is a variant of the vehicle routing problem (VRP) and was introduced by authors in [4] to account for the challenges associated with operating a fleet of alternate-fuel vehicles (AFVs). The US transportation sector accounts for 28% of national green house gas emissions [5]. Several eforts over many decades focusing towards the introduction of cleaner fuels (e.g. ultra-low sulfur diesel) and eficient engine technologies have led to reduced emissions and greater mileage per gallon of fuel used. Many government organizations, municipalities, and private companies are converting their fleet of vehicles to AFVs voluntarily either to alleviate the environmental impact of fossil-based fuels or to meet environmental regulations. For instance, FedEx, in its overseas operations, employs AFVs that run on bio-diesel, liquid natural gas or compressed natural gas.

![](08-Sundar_images/84cb9f57dc12d1b936feb6a159c5c97ba3b93cceabdc83b5ac51ccb51723c2f5.jpg)  
Fig. 1. Electric station locations in Texas, USA [3].

In both the aforementioned applications, the following fuel-constrained, multiple vehicle routing problem (FCMVRP) naturally arises in order to eficiently manage a team of autonomous vehicles: Given a set of targets, a set of refueling stations, and a set of vehicles (AFVs or electric vehicles) stationed at a depot, find a route for each vehicle starting and ending at the depot such that (i) each target is visited at least once by some vehicle, (ii) no vehicle runs out of fuel as it traverses its path, and (iii) the total cost of the routes for the vehicles is minimized. We assume that whenever a vehicle visits a refueling station, it refuels to its capacity.

In this paper, we formulate the FCMVRP as a combinatorial optimization problem. In particular, we introduce and compare four diferent mixed-integer linear programming (MILP) formulations for the FCMVRP. There are multiple formulations available for an NP-Hard problem such as the FCMVRP. In general, the efectiveness of a formulation in terms of computation time depends on multiple factors such as the number of variables involved, the tightness of the relaxations, the type of constraints used in the formulation, etc. Several studies have shown that it is dificult to a-priori know the efectiveness of a formulation without implementing it for the desired class of instances [6]. For instance, a formulation whose relaxations provide tight bounds on the optimal cost may be dificult to solve; on the other hand, a formulation with a large number of variables with weak bounds may lead to faster algorithms [7]. Therefore, computational experimentation on the multiple formulations is the only way to ascertain which formulation is the best for the desired class of instances. Furthermore, developing and analyzing diferent formulations for routing and path planning problem in the presence of fuel constraints is new and has not been addressed previously in the literature. We use a well-known idea in combinatorial optimization called \lifting" [8] to compare the formulations analytically. The first two formulations are arc-based, and the rest are node-based formulations that use the Miller-Tucker-Zemlin (MTZ) constraints [9]. The arc-based and edge-based formulations have additional decision variables for each edge and vertex, respectively, to impose fuel constraints on the vehicles. We then develop a branch and-cut algorithm to compute an optimal solution to the FCMVRP based on the formulations. The importance of developing such formulations is two-fold: tight formula tions provide lower bounds to the optimal objective value in the case of a minimization problem, and this can in turn lead to an eficient way of benchmarking various heuristics to compute feasible solutions to the problem. Secondly, tight formulations tend to result in a faster convergence behavior of the branch-and-cut algorithm (typically in the order of a few minutes) when a heuristic solution that are close to the optimal objective value are provided to the algorithm as an initial feasible solution [10]. In summary, the major contributions of this paper are as follows: (1) present four new MILP formulations for the FCMVRP, (2) compare the formulations both analytically and empirically, and (3) show through extensive computational experiments that instan ces with maximum of 40 targets are within the computational reach of a branch-and-cut algorithm based on the best of the four formulations.

## 2. Related Work

The FCMVRP is NP-hard because it is a generalization of the Traveling Salesman Problem (TSP). The existing literature on the FCMVRP is quite scarce. The single vehicle variant of the FCMVRP was first introduced by authors in [11]. When the travel costs are symmetric and satisfy the triangle inequality, the authors provide an approximation algorithm for this variant. They assume that the minimum fuel required to travel from any target to its nearest depot is at most equal to $F \alpha / 2$ units, where  is a constant in the interval ½0; 1Þ and F is the fuel capacity of the vehicle. This is a reasonable assumption as, in any case, one cannot have a feasible tour if there is a target that cannot be visited from any of the depots. Using these assumptions, Khuller et al. [11] present a $( 3 ( 1 + \alpha ) ) / ( 2 ( 1 - \alpha ) )$ approximation algorithm for the problem [10, 12–15]. Address variants of the FCMVRP in the context of path planning for unmanned aerial vehicles. In particular, the authors formulate in [12] the single vehicle variant as a MILP and present k-opt based exchange heuristics to obtain feasible solutions within 7% of the optimal, on an average. The MILP formulations are solved using of-the-shelf commercial sol vers to obtain an optimal solution to the single vehicle variant; they also observe that the solvers are not able to handle their formulation for instances with more than 25 targets. Sundar et al. [10] extend the approximation algorithm in [11] to the asymmetric case and also present heuristics to solve the asymmetric version of this variant. Furthermore, variable neighborhood search heuristics for the FCMVRP with heterogeneous vehicles, i.e. vehicles with diferent fuel capacities, are presented by Levy et al. [13]. More recently, an approximation algorithm and heuristics are developed for FCMVRP [14]. The authors in [14] extend the MILP proposed in [12] to the multiple vehicle setting. Similar to [12] they also observed that of-the-shelf mixed-integer solvers had dificulty computing an optimal solution for reasonable size test instances. To the best of our knowledge, there is no work in the literature that focuses on developing eficient formulations to obtain an optimal solution to even the single vehicle variant of the FCMVRP, let alone the FCMVRP.

Variants of the classic VRP that are closely related to FCMVRP include the distance constrained VRP [16–20], the orienteering problem [21, 22], and the capacitated version of the arc routing problem [23, 24]. The distance constrained VRP is a special case of FCMVRP with a single vehicle and single depot that can be considered as a fuel station. The FCMVRP is also quite diferent and more general compared to the orienteering problem where one is interested in maximizing the number of targets visited by the vehicle subject to its fuel constraints. Lastly, the arc routing problem is a single depot VRP given a set of intermediate facilities, and the vehicle has to cover a subset of edges along which targets are present. The vehicle is required to collect goods from the targets as it traverses the given set of edges and unloads the goods at the intermediate facilities. The goal of this problem is to find a tour of minimum length that starts and ends at the depot such that the vehicle visits the given subset of edges, and the total amount of goods carried by the vehicle does not exceed the capacity of the vehicle along the tour. One of the key differences between the arc routing problem and FCMVRP is that there is no requirement that any subset of edges must be visited in FCMVRP.

The remainder of the paper is organized as follows. Section 3 states the formal definition of the problem and introduces the notations. Section 4 introduces the mathematical preliminaries on lifting for MILPs that is used in parts of this paper for strengthening a given MILP formulation. In Sec. 5, we develop the four MILP formulations. The first two formulations are arc-based and the rest are nodebased formulations i.e. decision variables for enforcing the fuel constraints are introduced for each edge and each target, respectively. The LP relaxations of the formulations are analytically compared in this section. Then, in Sec. 6 we detail the main steps involved in developing a branch-andcut algorithm to solve the four formulations. Finally, in Sec. 8, we present the computational results followed by conclusions and possible extensions.

## 3. Problem Definition

Let T denote the set of targets $\{ t _ { 1 } , \ldots , t _ { n } \}$ and let $d _ { 0 }$ denote the depot where the m vehicles are initially stationed with each vehicle fueled to its capacity. Let D<sup>^</sup> denote the set of refueling stations $\{ d _ { 1 } , \ldots , d _ { k } \}$ . Let $D = \hat { D } \cup \{ d _ { 0 } \}$ . We assume that the vehicles cannot refuel at the depot. The FCMVRP is defined on a directed graph $G = \left( V , E \right)$ where $V = T \cup D ,$ and E is the set of edges joining any two vertices in $V ;$ E does not contain any self-loops. We assume that G does not contain any self-loops. Each edge $( i , j ) \in E$ is associated with a nonnegative cost $c _ { i j }$ required to travel from vertex i to vertex j, and $f _ { i j }$ is the fuel spent by traveling from i to $j .$ It is assumed that the cost of traveling from vertex i to vertex j is directly proportional to the fuel spent in traversing the edge $( i , j )$ i.e. $c _ { i j } = K \cdot f _ { i j } \ ( c _ { i j }$ and $c _ { j i }$ may be different, but for the purpose of this paper, we assume $c _ { i j } = c _ { j i } )$ . It is also assumed that travel costs satisfy the triangle inequality i.e. for every $i , j , k \in V , c _ { i j } + c _ { j k } \geq c _ { i k } .$ . Furthermore, let F denote the fuel capacity of all vehicles. The FCMVRP consists of finding a route for each vehicle such that each vehicle $\nu _ { i }$ starts and ends its route at $d _ { 0 } ,$ , each target is visited at least once by some vehicle, the vehicles never run out of fuel while they traverse their respective routes, and the sum of the cost of all the edges present in the routes is a minimum. Figure 2 shows a feasible solution to the FCMVRP for an instance with four vehicles and five refueling stations. In the next section, we will briefly present a few mathematical preliminaries regarding \lifting for $\mathrm { M L P } s ^ { \prime \prime }$ that will be used in Sec. 5.2 to develop tighter formulations.

T<sub>arge</sub>t Refueling station D<sub>epo</sub>t  
![](08-Sundar_images/84138af8f9fecabe8f888a319002c4171f20c683dcb3b0da29b1e5f7cc5463fa.jpg)  
Fig. 2. A feasible solution to the FCMVRP. The solution is for a 4-vehicle problem. $d _ { 0 }$ denotes the depot where all the vehicles are stationed initially. Note that a refueling station can be visited any number of times for refueling while some refueling stations may not be visited at all.

## 4. Lifting for MILPs

Before we present the idea of lifting for MILPs, we will review two useful definitions. A polyhedron is defined as the solution set of a finite number of linear equalities and inequalities, and a polytope is defined as a bounded polyhedron. A valid inequality for a polyhedron is an inequality that does not remove any feasible points of the polyhedron. Now, lifting is the process of constructing a valid inequality for a high dimensional polyhedron using a valid inequality for a low dimensional polyhedron. The idea of lifting was introduced by Gomory in 1969 [8]. The computational aspects of lifting were investigated by Padberg [25]. Since then, lifting has been studied extensively [26–29] and has been used for a variety of problems including vehicle routing, knapsack problem, supply chain, orienteering problems, to name a few. Lifting is usually applied sequentially; variables in a set are lifted one after another, and a separate optimization problem is solved to determine each lifting coeficient. The resulting inequality depends on the order in which the variables are lifted.

Proposition 4.1. A lifted inequality is guaranteed to have a dimension at least one greater than the original inequality, and the higher dimensional inequality is stronger than its corresponding lower dimensional counterpart.

Proof. See [7, Chap. 11.2, Propositions 1.1 and 2.2].

Now, we illustrate the process of lifting using a numerical example. We will formulate an optimization problem to compute the lifting coeficient and observe that the lifted inequality is stronger than the original inequality. Consider the polytope P defined by

$$
P := \left\{\left(x _ {1}, x _ {2}\right) \in \mathbb {Z} _ {+} ^ {2}: x _ {1} + 3 x _ {2} \leq 3, 3 x _ {1} + x _ {2} \leq 3 \right\},\tag{1}
$$

where, $\mathbb { Z } _ { + } ^ { 2 }$ is the set of nonnegative integer points. P contains the points $( 0 , 0 ) , ( 1 , 0 )$ , and ð0; 1Þ. The inequality $x _ { 1 } \leq$ 1 is a valid inequality for the polytope P i.e. it does not remove any points in P. We will now lift this valid inequality to obtain a stronger valid inequality. The variable to be lifted is $x _ { 2 } ,$ and we are interested in finding the best value of  (the lifting coeficient) such that the inequality $x _ { 1 } + \alpha x _ { 2 } \leq$ 1 does not remove any feasible points in P. This can be formulated as the following optimization problem:

$$
\alpha = \max \left\{1 - x _ {1}: \left(x _ {1}, x _ {2}\right) \in P, x _ {2} = 1 \right\}.\tag{2}
$$

Solving the above optimization problem, we obtain $\alpha = 1$ , which is the best value for the lifting coeficient. The resulting inequality $x _ { 1 } + x _ { 2 } \leq 1 .$ , a lifted version of $x _ { 1 } \leq 1$ , is a better inequality for the polytope P. This simple procedure is used throughout the rest of the paper to strengthen various constraints for the FCMVRP and obtain tighter formulations.

## 5. Mathematical Formulations

This section presents four formulations for the FCMVRP. The first two formulations are arc-based, and the remaining formulations are node-based. The arc-based and node based formulations have additional decision variables for each edge and vertex, respectively, to impose the fuel constraints. For any given formulation ${ \mathcal { F } } ,$ , let $\mathcal { F } ^ { L }$ denote its LP relaxation obtained by allowing the integer variables to take continuous values within the lower and upper integer bounds, and optðFÞ denote the cost of its optimal solution. Additional notations that will be used in the formulation are as follows: for any set $S \subset V , \delta ^ { + } ( S ) = \{ ( i , j ) \in E : i \in S , j \notin$ Sg and for any $\begin{array} { r } { A \subseteq E , x ( A ) = \sum _ { ( i , j ) \in A } x _ { i j } . } \end{array}$

## 5.1. Arc-based formulations

We first present an arc-based formulation ${ \mathcal { F } } _ { 1 }$ for the FCMVRP, inspired by the models for standard routing problems [6,19,30,31]. The decision variables used in the arcbased formulations are as follows: each edge $( i , j ) \in E$ is associated with a variable $x _ { i j } ,$ , which equals 1 if the edge $( i , j )$ is traversed by some vehicle, and 0 otherwise. Also, associated with each edge $( i , j )$ is a flow variable $z _ { i j }$ denoting the total fuel consumed by any vehicle as it starts from a depot and reaches the vertex $j ,$ when the predecessor of j is i. Finally, associated with each refueling station $d \in D \backslash \{ d _ { 0 } \}$ is a binary variable $y _ { d }$ that takes a value 1 if it is used at least once by some vehicle and 0 otherwise. Using the above variables, the first arc-based formulation $\mathcal { F } _ { 1 }$ is given as follows:

$$
\left(\mathcal {F} _ {1}\right) \quad \text { Minimize } \quad \sum_ {(i, j) \in E} c _ {i j} x _ {i j}
$$

subject to:

$$
\sum_ {i \in V} x _ {d i} = \sum_ {i \in V} x _ {i d}, \quad \forall d \in D \backslash \{d _ {0} \},\tag{3}
$$

$$
\sum_ {i \in V} x _ {d i} \leq y _ {d}, \quad \forall d \in D \backslash \{d _ {0} \},\tag{4}
$$

$$
\sum_ {i \in V} x _ {i d _ {0}} = m \quad \text { and } \quad \sum_ {i \in V} x _ {d _ {0} i} = m,\tag{5}
$$

$$
\sum_ {i \in V} x _ {i j} = 1 \quad \text { and } \quad \sum_ {i \in V} x _ {j i} = 1 \quad \forall j \in T,\tag{6}
$$

$$
x \left(\delta^ {+} (S)\right) \geq y _ {d}, \quad \forall d \in S \cap D, S \subset V \backslash \left\{d _ {0} \right\},\tag{7}
$$

$$
\sum_ {j \in V} z _ {i j} - \sum_ {j \in V} z _ {j i} = \sum_ {j \in V} f _ {i j} x _ {i j}, \quad \forall i \in T,\tag{8}
$$

$$
0 \leq z _ {i j} \leq F x _ {i j}, \quad \forall (i, j) \in E,\tag{9}
$$

$$
z _ {d i} = f _ {d i} x _ {d i}, \quad \forall   i \in T,   d \in D,\tag{10}
$$

$$
x _ {i j} \in \{0, 1 \}, \quad \forall (i, j) \in E, \quad \text { and }\tag{11}
$$

$$
y _ {d} \in \{0, 1 \}, \quad \forall d \in D \backslash \left\{d _ {0} \right\}.\tag{12}
$$

In the above formulation, the constraints (3) and (4) state that the in-degree of each refueling station is equal to its out-degree. Constraints (4) also force $y _ { d }$ for the refueling station $d \in D \backslash \{ d _ { 0 } \}$ to be 1 if it is used by any vehicle. The constraints (5) ensure that all the vehicles leave and return to the depot. Constraints (6) state that the in-degree and out-degree of each target must take a value 1. Constraints (7) ensure that a feasible solution to FCMVRP is connected. The constraints (8) eliminate sub-tours of the targets and also defines the flow variables $z _ { i j }$ for each edge $( i , j ) \in E$ The constraints (9) and (10) together impose $0 \leq z _ { i j } \leq F$ and they ensure that the fuel consumed by any vehicle to travel up to a depot does not exceed the fuel capacity of the vehicle, F. Finally, the constraints (11) and (12) impose the binary restrictions on the decision variables $x _ { i j }$ and $y _ { d } .$

Proposition 5.1. The constraints (12) can be replaced by

$$
x _ {d i} \leq y _ {d}, \quad \forall   i \in T \cup \{d _ {0} \}, \quad d \in D \backslash \{d _ {0} \}, \quad \text { and }\tag{13}
$$

$$
0 \leq y _ {d} \leq 1, \quad \forall d \in D \backslash \{d _ {0} \}.\tag{14}
$$

Proof. We first note that the constraints (13) are valid inequalities for the FCMVRP. They state that the vehicles can use a refueling station d only if $y _ { d } = 1$ . This constraint also ensures that the value of $y _ { d }$ will either be 0 or 1 as $x _ { d i } \in \{ 0 , 1 \}$ for any $i \in T \cup \{ d _ { 0 } \}$ . Hence, the binary restrictions on the variables $y _ { d }$ are relaxed in (14). □

Next, we present another arc-based formulation $\mathcal { F } _ { 2 }$ which is a strengthened version of ${ \mathcal { F } } _ { 1 }$ . The following proposition is a modified version of Ref. [19, Proposition 1] for the distance-constrained VRP; it strengthens the bounds given by the constraints (9).

Proposition 5.2. The inequalities in (9) can be strengthened as follows:

$$
z _ {i j} \leq (F - t _ {j}) x _ {i j}, \quad \forall j \in T, (i, j) \in E,\tag{15}
$$

$$
z _ {i d} \leq F x _ {i d}, \quad \forall i \in V \quad \text { and } \quad d \in D,\tag{16}
$$

$$
z _ {i j} \geq (s _ {i} + f _ {i j}) x _ {i j}, \quad \forall i \in T, (i, j) \in E,\tag{17}
$$

where $t _ { i } = \operatorname* { m i n } _ { d \in D } f _ { i d }$ and $s _ { i } = \operatorname* { m i n } _ { d \in D } f _ { d i }$

Proof. When $j \in D$ or $i \in D ,$ the constraints (16) and (10) specify the values of $z _ { i d }$ and $z _ { d i }$ , respectively. When both $i , j \in D ,$ the constraint (9) bounds the value of $z _ { i j } .$ . Hence, we need only to discuss the case when $i , j \in T ,$ . When $x _ { i j } = 1 _ { \cdot }$ the total fuel consumed by any vehicle that traverses the edge ði;jÞ cannot be greater that $\left( F - t _ { j } \right)$ , where $t _ { j }$ is the minimum amount of fuel required by any vehicle to reach a refueling station or the depot from target j. Therefore, the constraint in (15) strengthens the upper bound of $z _ { i j }$ in (9). Similarly, any vehicle that traverses the edge ði;jÞ consumes at least $( s _ { i } + f _ { i j } )$ amount of fuel. As a result, the constraint in (17) strengthens the lower bound of $z _ { i j }$ in (9). □

Hence, the second arc-based formulation is as follows:

$$
\left(\mathcal {F} _ {2}\right) \quad \text { Minimize } \quad \sum_ {(i, j) \in E} c _ {i j} x _ {i j}
$$

subject to: (3)–(8), (10), (11), and (13)–(17).

Corollary 5.3. $\mathrm { o p t } ( \mathcal { F } _ { 2 } ^ { L } ) \geq \mathrm { o p t } ( \mathcal { F } _ { 1 } ^ { L } )$

## 5.2. Node-based formulations

In this section, we present a node-based formulation for the FCMVRP based on the models for the distance-constrained VRP [18, 32]. For the node-based formulation, apart from the binary variable $x _ { i j }$ for each edge $( i , j ) \in E$ , we have an auxiliary variable $u _ { i }$ for each target i to eliminate sub-tours of the targets disconnected from the vertices in set D and to enforce the fuel constraints. In addition, we will also use the following two parameters: $t _ { i } = \operatorname* { m i n } _ { d \in D } f _ { i d }$ and $s _ { i } = \operatorname* { m i n } _ { d \in D }$ $f _ { d i }$ for every vertex $i \in V .$ . For any $d \in D , t _ { d } = 0$ and $s _ { d } = 0 ,$ Using the above notations, the formulation $\mathcal { F } _ { 3 }$ is given as follows:

$$
\left(\mathcal {F} _ {3}\right) \quad \text { Minimize } \quad \sum_ {(i, j) \in E} c _ {i j} x _ {i j}
$$

subject to: (3)–(7), (11), (13)–(14),

$$
u _ {i} - u _ {j} + M _ {i j} x _ {i j} \leq M _ {i j} - f _ {i j}, \quad \forall i, j \in T,\tag{18}
$$

$$
u _ {i} \geq s _ {i} + \sum_ {d \in D} (f _ {d i} - s _ {i}) x _ {d i}, \quad \forall i \in T, \quad \text { and }\tag{19}
$$

$$
u _ {i} \leq F - t _ {i} - \sum_ {d \in D} (f _ {i d} - t _ {i}) x _ {i d}, \quad \forall i \in T.\tag{20}
$$

The constraints (18) serve two purposes: they eliminate sub-tours of targets that are disconnected from any vertex in the set D and any path connecting two vertices in the set D that consume greater than F amount of fuel (see Proposition 5.4). These constraints are a modified version of the MTZ [9] constraints. The value of $M _ { i j }$ in (18) is given by $M _ { i j } = F - s _ { j } - t _ { i } + f _ { i j }$ . The constraints (19) and (20) specify the upper and lower bounds on $u _ { i } ,$ for every target i. The next proposition proves the validity of the constraint (18) for the FCMVRP; it is similar to a proposition presented for the distance-constrained VRP [32].

Proposition 5.4. The constraint (18) eliminates sub-tours ofthe targets disconnected from any vertex in the D and any path connecting two vertices in D that requires more than F amount offuel for any vehicle.

Proof. Suppose $( t _ { 1 } , t _ { 2 } , \ldots , t _ { k } , t _ { k + 1 } \equiv t _ { 1 } )$ is a sub-tour of the targets disconnected from any vertex in the set $D .$ Aggregating the constraints (18) corresponding to each edge in the sub-tour, we obtain

$$
\sum_ {i = 1} ^ {k} \left(u _ {t _ {i}} - u _ {t _ {i + 1}} + f _ {t _ {i} t _ {i + 1}}\right) \leq 0 \Rightarrow \sum_ {i = 1} ^ {k} f _ {t _ {i} t _ {i + 1}} \leq 0,
$$

a contradiction. Hence, the constraint (18) eliminates subtours of the targets disconnected from any vertex in the set D. Now, let $\left( \nu _ { 1 } , \nu _ { 2 } , \ldots , \nu _ { k - 1 } , \nu _ { k } \right)$ denote a path such that $\nu _ { 1 } ,$ $\boldsymbol { v } _ { k } \in D$ and $\boldsymbol { v } _ { i } \in T$ for $i \in \left\{ 2 , \ldots , k - 1 \right\}$ . Again, aggregating the constraints (18) for the edges $( v _ { j } , v _ { j + 1 } ) , j = 2 , \ldots , k - 2 ,$ we obtain

$$
u _ {v _ {2}} - u _ {v _ {k - 1}} + \sum_ {j = 2} ^ {k - 2} f _ {v _ {j} v _ {j + 1}} \leq 0.
$$

But, by constraints (19) and (20), we have $u _ { v _ { 2 } } \geq f _ { v _ { 1 } v _ { 2 } }$ and $u _ { \nu _ { k - 1 } } \leq F - f _ { \nu _ { k - 1 } \nu _ { k } } ,$ respectively. Combining all the three inequalities, we obtain

$$
\sum_ {i = 1} ^ {k - 1} f _ {v _ {i}, v _ {i + 1}} \leq F.
$$

Hence, any vehicle that traverses a path starting and terminating at vertices in $D ,$ consumes less than F amount of fuel. □

The following proposition strengthens the constraints (18)–(20). It uses the idea of lifting (see Sec. 4) to tighten these constraints.

Proposition 5.5. The inequalities in (18), (19), and (20) can be strengthened as follows:

$$
u _ {i} - u _ {j} + M _ {i j} x _ {i j} + \left(M _ {i j} - f _ {i j} - f _ {j i}\right) x _ {j i} \leq M _ {i j} - f _ {i j}, \quad \forall i, j \in T,\tag{21}
$$

$$
u _ {i} \geq \sum_ {j \in V} (s _ {j} + f _ {j i}) x _ {j i}, \quad \forall i \in T, \quad a n d\tag{22}
$$

$$
u _ {i} \leq F - \sum_ {j \in V} (t _ {j} + f _ {i j}) x _ {i j}, \quad \forall i \in T\tag{23}
$$

where $x _ { i i } = 0$ and $x _ { i j } = 0$ whenever $s _ { i } + f _ { i j } + t _ { j } > F .$

Proof. The constraints (21) are obtained by lifting each variable $x _ { j i } , j \in T$ in (18), in any order. Let j be an arbitrary target in T. We compute its lifting coeficient as the maximum value of  such that the following constraint is valid to the FCMVRP:

$$
u _ {i} - u _ {j} + M _ {i j} x _ {i j} + \alpha x _ {j i} \leq M _ {i j} - f _ {i j}.\tag{24}
$$

The above inequality is valid when $x _ { j i } = 0 .$ , as it reduces to (18). So, we suppose $x _ { j i } = 1 ;$ then, we have $x _ { i j } = 0$ and $u _ { j } + f _ { j i } \le u _ { i }$ . The constraint (24) simplifies to

$$
\alpha \leq M _ {i j} - f _ {i j} + u _ {j} - u _ {i} \Rightarrow \alpha \leq M _ {i j} - f _ {i j} - f _ {j i}.
$$

Hence, the lifting coeficient for the variable $x _ { j i }$ is given by $M _ { i j } - f _ { i j } - f _ { j i } .$

Similarly, (22) can be obtained by lifting each $x _ { j i }$ variable for $j \in T$ in constraint (19), in any order. To that end, let $j \in T$ . We compute the maximum value that  can take so that the following constraint is valid to the FCMVRP:

$$
u _ {i} \geq s _ {i} + \sum_ {d \in D} (f _ {d i} - s _ {i}) x _ {d i} + \alpha x _ {j i}.\tag{25}
$$

The above inequality is valid for $x _ { j i } = 0 .$ When $x _ { j i } = 1$ , we have $x _ { d i } = 0$ and $u _ { j } + f _ { j i } \le u _ { i }$ . Hence, we have

$$
\alpha \leq u _ {i} - s _ {i} \leq u _ {j} + f _ {j i} - s _ {i}.
$$

The minimum value of $u _ { j }$ is equal to $s _ { j } .$ . Hence, the lifting coeficient for $x _ { j i }$ is equal to $s _ { j } + f _ { j i } - s _ { i } .$ Similarly, the coefficients of the other $x _ { j i }$ variables can be computed. Using these extra terms, the constraint (25) can be simplified as follows:

$$
\begin{array}{l} u _ {i} \geq s _ {i} + \sum_ {j \in V} (s _ {j} + f _ {j i} - s _ {i}) x _ {j i}, \quad \forall i \in T \\ \Rightarrow u _ {i} \geq s _ {i} + \sum_ {j \in V} (s _ {j} + f _ {j i}) x _ {j i} - s _ {i} \cdot \sum_ {j \in V} x _ {j i}, \quad \forall i \in T \\ \Rightarrow u _ {i} \geq \sum_ {j \in V} (s _ {j} + f _ {j i}) x _ {j i}, \quad \forall i \in T. \end{array}
$$

The last implication follows from the constraints (6).

Finally, the constraints (23) are obtained from (20) by lifting each $x _ { i j }$ variable for every $j \in T$ in any order. Since, the procedure for computing the lifting coeficients is similar, we list the coeficients without proof. The lifting coef ficient for the variable $x _ { i j }$ where $j \in T$ is equal to $f _ { i j } + t _ { j } - t _ { i } .$ Further simplification using the degree constraint (6) yields:

$$
u _ {i} \leq F - \sum_ {j \in V} (t _ {j} + f _ {i j}) x _ {i j}.
$$

Now, we will replace the constraints (18)–(20) in the node-based formulation $\mathcal { F } _ { 3 }$ using its strengthened counterparts, (21)–(23). Then, we observe that for the first target r that any vehicle visits either from the depot or a refueling station $d \in D ,$ the constraints (22) and (23) imply

$$
\begin{array}{l} f _ {d r} \leq u _ {r} \leq F - \sum_ {j \in V} (f _ {r j} + t _ {j}) x _ {r j} \\ \Rightarrow f _ {d r} \leq u _ {r} \leq F - \max _ {j \in V} (f _ {r j} + t _ {j}). \end{array}
$$

This indicates that the value of each auxiliary variable $u _ { i } , \ i \in T$ in a solution to the FCMVRP obtained using the new formulation may not provide any meaningful information [18]. This can be easily rectified by using the following valid inequality:

$$
u _ {i} \leq F - t _ {i} - \sum_ {d \in D} (F - t _ {i} - f _ {d i}) x _ {d i}.\tag{26}
$$

The above valid inequality tightens the upper bound on the auxiliary variable $u _ { i } ,$ whenever i is the first target visited by any vehicle as it leaves the depot or a refueling station. Hence, in lieu of the constraints (21)–(26), the u s can be redefined as the total fuel consumed by any vehicle as it reaches the target i. The redefined $u _ { i } s$ are a more natural choice of decision variables to impose the fuel restrictions of the vehicles. These are the variables that authors in [12, 14] use to formulate the single vehicle and multiple vehicle fuel-constrained VRP. But, we will observe in Sec. 8 that this choice is not well suited for obtaining an optimal solution to the FCMVRP.

Now, we present the second node-based formulation as follows:

$$
\left(\mathcal {F} _ {4}\right) \quad \text { Minimize } \quad \sum_ {(i, j) \in E} c _ {i j} x _ {i j}.
$$

subject to: (3)–(7), (11), (13)–(14), and (21)–(26).

The following result follows from Proposition 5.5.

Corollary 5.6. opt ${ \bf \Phi } ( \mathcal { F } _ { 4 } ^ { L } ) \ge \tt o p t ( \mathcal { F } _ { 3 } ^ { L } )$

## 6. Branch-and-Cut Algorithm

In this section, we briefly present the main ingredients of a branch-and-cut algorithm that are used to solve the four diferent formulations presented in the previous section to optimality. The branch-and-cut algorithm is an implicit enumeration algorithm and it has an exponential worse case running time. This is the case for any algorithm that aims to compute an optimal solution for every instance of an NP-hard problem, which is also the case for the FCMVRP. One technique which is used often in the literature [10] to speed up the convergence of the branch-and-cut algorithm is to provide a feasible solution obtained using a good heuristic as an initial solution to the algorithm. Developing such a heuristic for the FCMVRP is a separate research problem and is not the focus of this paper and hence, is delegated to future work. The formulations developed in the Sec. 5 can be provided to of-the-shelf commercial branch-and-cut solvers to obtain an optimal solution to the FCMVRP. But, observe that all the formulations contain constraint (7) to ensure any feasible solution to FCMVRP is connected. The number of such constraints is exponential and it may not be computationally eficient to enumerate all these constraints and provide them to these solvers. To address this issue, we use the following approach: we relax the constraints (7) from the formulation, and whenever the solver obtains an integer feasible solution to this relaxed problem, we check if any of the constraints (7) are violated by the integer feasible solution. If so, we add the infeasible constraint and continue solving the original problem. This process of adding constraints to the problem sequentially has been observed to be computationally eficient for the TSP, VRP and a huge number of their variants [6, 33, 34].

Now, we will detail the algorithm used to find a constraint (7) that is violated for a given integer feasible solution to the relaxed problem. We will use formulation $\mathcal { F } _ { 1 }$ to present the algorithm. The same algorithm can be used for the remaining formulations, without any modifications, to find violated constraint (7). A violated constraint (7) can be described by a subset of vertices $S \subset V \backslash \{ d _ { 0 } \}$ such that $S \cap D \neq \emptyset$ and $x ( \delta ^ { + } ( S ) ) < y _ { d }$ for every $d \in S \cap D .$ Given an integer feasible solution to the relaxed problem, we construct a support graph $G ^ { * }$ defined as follows: $G ^ { * } = ( V ^ { * } , E ^ { * } )$ where $V ^ { * } \bar { = } T \cup \bar { \{ d _ { 0 } \} } \cup \{ d \in D \backslash \{ d _ { 0 } \} : y _ { d } = 1 \}$ and $E ^ { * } =$ $\{ ( i , j ) \in E : x _ { i j } = 1 \}$ . We then find the strongly connected components of $G ^ { * }$ . Every strongly connected component that does not contain the depot is a subset S of $V \backslash \{ d _ { 0 } \}$ which violates the constraint (7). We add all these infeasible constraints and continue solving the original problem. Many of-the-shelf commercial solvers [35] provide a feature called \solver callbacks" to implement such an algorithm into its branch-and-cut framework.

## 7. A Qualitative Comparison of the Node-Based and the Edge-Based Formulations

The performance of the branch-and-cut algorithm on the edge-based and arc-based MILP formulations of the FCMVRP depends upon various factors like tightness of the formulation, geometry of a polyhedron, number of decision variables, etc. Furthermore, a-priori qualitative guarantees that can be made, if any, are problem specific and, in majority of the cases, can only be ascertained with the help of computational experiments.

Nevertheless, for general path planning problems, it has been observed in the literature [36] that formulations using big-M values (as in Eqs. (18) and (21) for the node-based formulations) are not desirable. An interested reader is referred to [37] for demonstrations of the adverse sideefects of using constraints with big-M values. Hence, based on the work in the literature [36], we expect, the branchand-cut algorithm on the edge-based formulation, $\mathcal { F } _ { 2 } ,$ to outperform the node-based formulation ${ \mathcal { F } } _ { 4 }$ even though, the node-based formulation is an intuitively natural way to formulate fuel constraints [10, 12, 15, 14].

## 8. Computational Results

In this section, we discuss the computational performance of the branch-and-cut algorithm for all the four formulations presented in Sec. 5. The mixed-integer linear programs were implemented in Java, using the traditional branch-and-cut framework and the solver callback functionality of CPLEX version 12.6.2. All the simulations were performed on a Dell Precision T5500 workstation (Intel Xeon E5630 processor @2.53 GHz, 12 GB RAM). The computation times reported are expressed in seconds, and we imposed a time limit of 3,600 s for each run of the algorithm. The performance of the algorithm was tested with randomly generated test instances.

## Instance generation

The problem instances were randomly generated in a square grid of size [100,100]. The number of refueling stations was set to 4 and the locations of the depot and all the refueling stations were fixed a priori for all the test instances. The number of targets varies from 10 to 40 in steps of five, while their locations were uniformly distributed in the square grid; for each jTj 2 f10; 15; 20; 25; 30; 25; 40g, we generated five random instances. For each of the above generated instances, the number of vehicles in the depot was varied from 3 to 5, and the fuel capacity of the vehicles, F, was varied linearly with a parameter .  is defined as the maximum distance between the depot and any target. The fuel capacity F was assigned a value from the set f2:25; 2:5; 2:75; 3g. The travel costs and the fuel consumed to travel between any pair of vertices were assumed to be directly proportional to the Euclidean distances between the pair and rounded down to the nearest integer. In total, our test bed consisted of 420 instances. Two sets of computational experiments were performed on these instances. The first experiment was aimed at comparing the LP relaxations of the four formulations and ensuring that the computational behavior of the formulations conforms with the corollaries 5.3 and 5.6. The second set of test runs was aimed at finding the most useful formulation to compute an optimal solution to any instance of the problem using the branch-and-cut algorithm proposed in Sec. 6.

Table 1. Cost of the LP relaxation for the instances with 40 targets and five vehicles.

<table><tr><td>#</td><td> $\text{opt}(\mathcal{F}_1^L)$ </td><td> $\text{opt}(\mathcal{F}_2^L)$ </td><td> $\text{opt}(\mathcal{F}_3^L)$ </td><td> $\text{opt}(\mathcal{F}_4^L)$ </td></tr><tr><td>1</td><td>572.051</td><td>587.347</td><td>551.014</td><td>620.000</td></tr><tr><td>2</td><td>567.454</td><td>578.639</td><td>551.014</td><td>620.000</td></tr><tr><td>3</td><td>564.260</td><td>572.561</td><td>551.014</td><td>620.000</td></tr><tr><td>4</td><td>561.937</td><td>568.191</td><td>551.014</td><td>620.000</td></tr><tr><td>5</td><td>561.001</td><td>574.636</td><td>535.011</td><td>590.500</td></tr><tr><td>6</td><td>558.195</td><td>568.381</td><td>535.011</td><td>590.500</td></tr><tr><td>7</td><td>556.121</td><td>563.924</td><td>535.011</td><td>590.500</td></tr><tr><td>8</td><td>554.441</td><td>560.568</td><td>535.011</td><td>590.500</td></tr><tr><td>9</td><td>493.041</td><td>497.721</td><td>477.507</td><td>544.000</td></tr><tr><td>10</td><td>489.625</td><td>493.075</td><td>477.507</td><td>544.000</td></tr><tr><td>11</td><td>486.908</td><td>489.610</td><td>477.507</td><td>544.000</td></tr><tr><td>12</td><td>484.697</td><td>486.902</td><td>477.507</td><td>544.000</td></tr><tr><td>13</td><td>604.135</td><td>617.703</td><td>574.005</td><td>611.500</td></tr><tr><td>14</td><td>599.296</td><td>607.671</td><td>574.005</td><td>611.500</td></tr><tr><td>15</td><td>595.086</td><td>600.576</td><td>574.005</td><td>611.500</td></tr><tr><td>16</td><td>591.773</td><td>596.955</td><td>574.005</td><td>611.500</td></tr><tr><td>17</td><td>593.720</td><td>607.825</td><td>563.007</td><td>616.000</td></tr><tr><td>18</td><td>588.627</td><td>599.340</td><td>563.007</td><td>616.000</td></tr><tr><td>19</td><td>584.692</td><td>592.348</td><td>563.007</td><td>616.000</td></tr><tr><td>20</td><td>581.550</td><td>587.525</td><td>563.007</td><td>616.000</td></tr></table>

Tables 1 and 2, and Figs. 4–6 summarize the computational behavior of the algorithms. The following nomenclature is used throughout the rest of the paper:

#: instance number;

opt $( \mathcal { F } _ { i } ^ { L } )$ : LP relaxation solution for formulation i; n: instance size i.e. number of targets in the instance; # cuts: number of constraints (7) violated during a branch and-cut solve. These violated constraints are computed using the algorithm detailed in Sec. 6; total: total number of test instances of a given size (the number of targets and the number of vehicles are given);

Table 2. Comparison of formulations $\mathcal { F } _ { 2 }$ and $\mathcal { F } _ { 4 } .$

<table><tr><td rowspan="2">n</td><td rowspan="2">total</td><td colspan="2">m=3</td><td colspan="2">m=4</td><td colspan="2">m=5</td></tr><tr><td> $\mathcal{F}_2$ succ</td><td> $\mathcal{F}_4$ succ</td><td> $\mathcal{F}_2$ succ</td><td> $\mathcal{F}_4$ succ</td><td> $\mathcal{F}_2$ succ</td><td> $\mathcal{F}_4$ succ</td></tr><tr><td>10</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>15</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>25</td><td>20</td><td>19</td><td>18</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>30</td><td>20</td><td>20</td><td>12</td><td>20</td><td>18</td><td>20</td><td>20</td></tr><tr><td>35</td><td>20</td><td>16</td><td>7</td><td>18</td><td>10</td><td>18</td><td>10</td></tr><tr><td>40</td><td>20</td><td>16</td><td>3</td><td>16</td><td>5</td><td>16</td><td>8</td></tr></table>

![](08-Sundar_images/530d2e69c374bc7a004ff3b471778e69cec8d9a3f7d51108b7d096474d7df233.jpg)  
Fig. 3. Optimal solution for a 25-target, 2-vehicle instance.

succ: number of instances for which optimal solutions were computed within a time limit of 3,600 s.

Table 1 compares the cost of the LP relaxations of the four formulations presented in Sec. 5 for the instances with 40 targets and five vehicles. The results in Table 1 provide an empirical comparison of the formulations presented in $5 ;$ the observed behavior is expected because the formulations $\mathcal { F } _ { 2 }$ and ${ \mathcal { F } } _ { 4 }$ are strengthened versions of ${ \mathcal { F } } _ { 1 }$ and ${ \mathcal { F } } _ { 3 } ,$ , respectively (see corollaries 5.3 and 5.6). As for the LP relaxations of formulations $\mathcal { F } _ { 2 }$ and ${ \mathcal { F } } _ { 4 } ,$ the formulation ${ \mathcal { F } } _ { 4 }$ is observed to have a better LP relaxation value for 95% of the instances. Also, the formulation $\mathcal { F } _ { 2 }$ is consistently better than the formulation $\mathcal { F } _ { 3 }$ with respect to the strength of the LP relaxation. Hence, the rest of the computational experiments is devoted to comparing the formulations $\mathcal { F } _ { 2 }$ and ${ \mathcal { F } } _ { 4 }$ with regards to computing an optimal solution to any instance of the FCMVRP.

![](08-Sundar_images/342efdd851dd9ad72c697055f72872d982a64ca9f8e8277d6945907c5730a9f4.jpg)  
Fig. 4. Average time taken to compute an optimal solution for $\mathcal { F } _ { 2 }$ and ${ \mathcal { F } } _ { 4 } .$

![](08-Sundar_images/003609884693abc9bcdc6186dc7d4cc58a6675c90dab5ad549290d680bc5c710.jpg)  
0 |T| = 20 0 0 |T| = 25  0 |T| = 30  0 |T| = 35 I |T| = 40  
Fig. 5. Average time taken to compute the optimal solution for the formulation $\mathcal { F } _ { 2 }$

Table 2 shows the number of instances of diferent sizes solved to optimality by the formulations $\mathcal { F } _ { 2 }$ and ${ \mathcal { F } } _ { 4 }$ within the time limit of 3,600 s. For a fixed number of targets n, and number of vehicles $m ,$ the branch-and-cut algorithm for formulations $\mathcal { F } _ { 2 }$ and ${ \mathcal { F } } _ { 4 }$ was run on a set of 20 instances. The column titled \succ" indicates the number of instances, out of 20, that were solved to optimality. We observe that the formulation $\mathcal { F } _ { 2 }$ is more successful in computing an optimal solution for the instances with 35 and 40 targets. In total, the formulation $\mathcal { F } _ { 2 }$ provided an optimal solution to 399 out of 420 test instances within 3,600 s. In contrast, the formulation ${ \mathcal { F } } _ { 4 }$ provided an optimal solution only to 331 test instances within the stipulated time. We also note that the formulation $\mathcal { F } _ { 2 }$ , for the 21 instances that were not solved to optimality, provided feasible solutions that were within 2.5% of the optimal value, on an average. Initial computational experiments indicate that the branch-and-cut algorithm using formulation $\mathcal { F } _ { 2 }$ scales well up to 50 targets and is capable of computing an optimal solution within 3; 600 s. Beyond 50 targets, the algorithm can take more than 2 h to compute the optimal solution.

Figure 3 shows an optimal solution that is obtained for a 25-target, 2-vehicle instance. The formulation $\mathcal { F } _ { 2 }$ is used to compute the optimal solution and the computation time for the instance of 78.05 s.

Figure 4 shows the average time taken by the two formulations to compute an optimal solution. The computation time reported in Fig. 4 is averaged over all the instances for a given value of $n ,$ the number of targets. Both Table 2 and Fig. 4 indicate that the arc-based formulation $\mathcal { F } _ { 2 }$ outperforms the node-based formulation ${ \mathcal { F } } _ { 4 }$ for around 95% of the instances. The remaining 5% of the instances on which the two formulations were indistinguishable contained less than 15 targets.

![](08-Sundar_images/330ff4895a84ae181ee18508cf891bc2b5399f972b8005715ec86578d11e10eb.jpg)  
0 |T| = 20  0 |T| = 25  0 |T| = 30  0 |T| = 35 I ☑ |T| = 40  
Fig. 6. Average number of violated constraints (7) identified by the branch-and-cut algorithm for the formulation $\mathcal { F } _ { 2 } .$

Figures 5 and 6 analyze the behavior of the branch-andcut algorithm using the arc-based formulation $\mathcal { F } _ { 2 }$ . Figure 5 compares the average time taken to compute an optimal solution to the FCMVRP as the number of vehicles is varied from 3 to 5. The plot indicates that the computation time decreases with the increase in the number of vehicles. This is not surprising because the combinatorial dificulty of the problem arises due to the fuel constraints of the vehicles. Since all the vehicles are forced to leave the depot, the fuel constraints tend to be irrelevant with the increase in the number of vehicles. Finally, Fig. 6 shows the average number of connectivity constraints (7), as the number of vehicles and the number of targets is varied from 3 to 5 and 20 to 40, respectively, that were actually violated and added back to the relaxed formulation by the branch-and-cut algorithm. The plot corroborates the proposed approach of relaxing the exponential number of connectivity constraints (7) and adding back the formulation when a violation occurs. We observe that the number of violated constraints (7) is much less when compared to the original number of constraints in the formulation.

## 9. Conclusions and Future Work

In this paper, we presented four diferent MILP formulations for the FCMVRP problem. The problem arises frequently in the context of green vehicle routing, routing electric vehicles, and path planning for UAVs. The first two formulations ${ \mathcal { F } } _ { 1 }$ and $\mathcal { F } _ { 2 }$ are arc-based, and the rest i.e. $\mathcal { F } _ { 3 }$ and ${ \mathcal { F } } _ { 4 }$ are node-based formulations. The arc-based formulations use decision variables on the edges to impose the fuel constraints and the node-based formulations use extra decision variables on the targets to enforce the fuel constraints. Though the node-based formulations are a more natural way of formulating the FCMVRP, the arc-based formulations outperform the node-based formulations with respect to computing an optimal solution to any instance of the problem. Computational experiments on a large number of test instances corroborate this observation. Among the two proposed arc-based formulations, the second formulation $\mathcal { F } _ { 2 }$ is shown to be the most efective, both analytically and empirically. Hence, $\mathcal { F } _ { 2 }$ can be used as a template for enforcing fuel constraints on any problem that includes similar fuel restrictions on the vehicle. Future work can be directed towards developing similar MILP formulations, fast heuristics, and branch-and-cut algorithms to solve a heterogeneous variant of the problem i.e. with vehicles having diferent fuel capacities.

## References

[1] M. Schneider, A. Stenger and D. Goeke, The electric vehicle-routing problem with time windows and recharging stations, Transp. Sci. 48(4) (2014) 500–520.

[2] G. Hiermann, J. Puchinger, S. Ropke and R. F. Hartl, The electric fleet size and mix vehicle routing problem with time windows and recharging stations, European J. Oper. Res. 252(3) (2016) 995–1018.

[3] US DOE, Alternate Fuels Data Center.

[4] S. Erdoğan and E. Miller-Hooks, A green vehicle routing problem Transp. Res. E Logis. Transp. Rev. 48(1) (2012) 100–114.

[5] US EPA, Environment Protection Agency, Inventory of US Greenhouse Gas Emissions and Sinks: 1990-2007, EPA 430-R-09-004 (2009).

[6] P. Toth and D. Vigo, The Vehicle Routing Problem (Siam, 2001).

[7] L. A. Wolsey and G. L. Nemhauser, Integer and Combinatorial Opti mization (John Wiley & Sons, 2014).

[8] R. E. Gomory, Some polyhedra related to combinatorial problems Linear Algebra Appl. 2(4) (1969) 451–558.

[9] C. E. Miller, A. W. Tucker and R. A. Zemlin, Integer programming formulation of traveling salesman problems, J. Assoc. Comput. Mach 7(4) (1960) 326–329.

[10] K. Sundar and S. Rathinam, Algorithms for routing an unmanned aerial vehicle in the presence of refueling depots, IEEE Trans. Autom Sci. Eng. 11(1) (2014) 287–294.

[11] S. Khuller, A. Malekian and J. Mestre, To fill or not to fill: The gas station problem in Proc. 15th Annual European Conf. Algorithm (ESA 2007), (Springer, 2007), pp. 534–545

[12] K. Sundar and S. Rathinam, Route planning algorithms for unmanned aerial vehicles with refueling constraints, in Proc. American Control Conference (ACC), 2012, (IEEE, 2012), pp. 3266–3271.

[13] D. Levy, K. Sundar and S. Rathinam, Heuristics for routing heterogeneous unmanned vehicles with fuel constraints, Mathematical Problems in Engineering 2014 (2014) Article ID 131450, 12 pages, doi:10.1155/2014/131450.

[14] D. Mitchell, M. Corah, N. Chakraborty, K. Sycara and N. Michael, Multirobot long-term persistent coverage with fuel constrained robots 2015 IEEE Int. Conf. Robotics and Automation (ICRA), (IEEE, 2015), pp. 1093–1099.

[15] K. Sundar, S. Venkatachalam and S. Rathinam, Formulations and algorithms for the multiple depot, fuel-constrained, multiple vehicle routing problem, in Proc. American Control Conf. (ACC, 2016) (IEEE 2016), pp. 6489–6494.

[16] G. Laporte, M. Desrochers and Y. Nobert, Two exact algorithms for the distance-constrained vehicle routing problem, Networks 14(1) (1984) 161–172.

[17] C.-L. Li, D. Simchi-Levi and M. Desrochers, On the distance constrained vehicle routing problem, Oper. Res. 40(4) (1992) 790–799.

[18] I. Kara, On the Miller-Tucker-Zemlin based formulations for the distance constrained vehicle routing problems, in ICMS Int. Conf. Mathematical Science, (AIP Publishing, 2010), pp. 551–561.

[19] I. Kara, Arc based integer programming formulations for the distance constrained vehicle routing problem, 2011 3rd IEEE Int. Symp. Logistics and Industrial Informatics (LINDI) (IEEE, 2011), pp. 33–38.

[20] V. Nagarajan and R. Ravi, Approximation algorithms for distance constrained vehicle routing problems, Networks 59(2) (2012) 209–214.

[21] M. Fischetti, J. J. S. Gonzalez and P. Toth, Solving the orienteering problem through branch-and-cut, INFORMS J. Comput. 10(2) (1998) 133–148.

[22] P. Vansteenwegen, W. Soufriau and D. Van Oudheusden, The orienteering problem: A survey, Eur. J. Oper. Res. 209(1) (2011) 1–10.

[23] G. Ghiani, F. Guerriero, G. Laporte and R. Musmanno, Tabu search heuristics for the arc routing problem with intermediate facilities under capacity and length restrictions, J. Math. Model. Algorithms 3 (3) (2004) 209–223.

[24] M. Polacek, K. F. Doerner, R. F. Hartl and V. Maniezzo, A variable neighborhood search for the capacitated arc routing problem with intermediate facilities, J. Heuristics 14(5) (2008) 405–423.

[25] M. W. Padberg, On the facial structure of set packing polyhedra, Math. program. 5(1) (1973) 199–215.

[26] Z. Gu, G. L. Nemhauser and M. W. Savelsbergh, Sequence independent lifting in mixed integer programming, J. Comb. Optim. 4(1) (2000) 109–129.

[27] A. Atamtürk, Sequence independent lifting for mixed-integer programming, Oper. Res. 52(3) (2004) 487–490.

[28] E. Balas and E. Zemel, Facets of the knapsack polytope from minima covers, SIAM J. Appl. Math. 34(1) (1978) 119–148.

[29] L. A. Wolsey, Technical note: Facets and strong valid inequalities for integer programs, Oper. Res. 24(2) (1976) 367–372.

[30] K. Sundar and S. Rathinam, An exact algorithm for a heterogeneous, multiple depot, multiple traveling salesman problem, 2015 Int. Conf. Unmanned Aircraft Systems (ICUAS) (IEEE, 2015), pp. 366–371.

[31] K. Sundar and S. Rathinam, Algorithms for heterogeneous, multiple depot, multiple unmanned vehicle path planning problems, J Intell. Robot. Syst. (2016) 1–14.

[32] M. Desrochers and G. Laporte, Improvements and extensions to the miller-tucker-zemlin subtour elimination constraints, Oper. Res. Lett. 10(1) (1991) 27–36.

[33] K. Sundar and S. Rathinam, Multiple depot ring star problem: A polyhedral study and an exact algorithm, J. Global Optim. (2016) 1–25.

[34] K. Sundar and S. Rathinam, Generalized multiple depot traveling salesmen problem-polyhedral study and exact algorithm, Comput. Oper. Res. 70 (2016) 39–55.

[35] IBM ILOG CPLEX Optimizer (2015).

[36] S. Melkote and M. S. Daskin, An integrated model of facility location and transportation network design, Transp. Res. A Policy Pract. 35(6) (2001) 515–538.

[37] J. Desrosiers and M. E. Lübbecke, A primer in column generation, in Column generation (Springer, 2005), pp. 1–32.

![](08-Sundar_images/adc45dac7b429a52fc589c45c50fc3844b15c689f5c7035f50edc4e807da9f2c.jpg)  
Kaarthik Sundar is a post-doctoral researcher at the Center for Nonlinear Studies (CNLS), Los Alamos National Laboratory. He received his Ph.D. degree in Mechanical Engineering and M.S. degree in Electrical Engineering from the Texas A&M University, College Station in 2012 and 2016, respectively. He is mainly interested in problems pertaining to vehicle routing, path planning, and control for unmanned/autonomous systems; optimal control, estimation, and large-scale optimization problems in power and gas networks; combinatorial optimization; and global optimiza tion for mixed-integer nonlinear programs.

![](08-Sundar_images/675c7d5441b31aa5e1af2a54cd05afa8a2868a2ac20b221066786f38201dd162.jpg)

Saravanan Venkatachalam is currently an assistant professor in Industrial and Systems Engineering at Wayne State University, Detroit. His research interests are in stochastic programming, large scale optimization, and discrete event modeling and simulation. Applications of interest include supply chain management, healthcare, pricing and revenue management, and energy management. Before joining the Ph.D. program at the Texas A&M University, he worked in industry for nine years for companies like JDA Software,

Hewlett Packard where he had opportunities to develop and implement decision support systems (mathematical and statistical models) in the domains of consumer support, supply chain management, transportation, and pricing and revenue management.

![](08-Sundar_images/2daaa628eb9d060dd3563cfde2a5c4e6fd02a754b74c742cfabcb0577aa138b3.jpg)  
Sivakumar Rathinam is currently an associate professor in mechanical engineering at the Texas A&M University, College Station. Prior to joining A&M. he was an associate research scientist at the University of California-NASA Ames Research Center. He received his Ph.D. degree in civil-systems engineering and M.S. in electrical engineering and computer science from the University of California in 2007 and 2006, respectively. His research interests include autonomous vehicles, motion planning, combinatorial optimization, air trafic control, and vision-based control.