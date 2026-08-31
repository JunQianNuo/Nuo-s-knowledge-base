---
raw_title: 12-Sethanan
subject: 数学建模-策联杯B题
source: "12.pdf"
status: mineru解析
parser: mineru
topics:
  - 差分进化
  - 遗传算子
  - 多程车辆路径
---

# Hybrid diferential evolution algorithm and genetic operator for multi-trip vehicle routing problem with backhauls and heterogeneous fleet in the beverage logistics industry

![](12-Sethanan_images/0571f951d77f65c580ad76ecfc0bde8e8d3f90200497ab7ce1a605c8d464a3a3.jpg)

Kanchana Sethanan, Thitipong Jamrus

Research Unit on System Modeling for Industry, Department of Industrial Engineering, Faculty of Engineering, Khon Kaen University, Khon Kaen 40002, Thailand

## A R T I C L E I N F O

Keywords: Vehicle routing problem Backhauls Multiple trips Diferential evolution algorithm Genetic operator

## A B S T R A C T

Logistics is increasingly challenging because of increased competition and the uncertainty introduced by glo balization. The drinks distribution system considered here uses glass bottles for soft drinks to deliver to all customers who need soft drinks in glass bottles, before making any pickups of empty glass bottles from clients to return to the company. This study aims at both an integer linear programming formulation and a novel hybrid diferential evolution algorithm involving a genetic operator with fuzzy logic controller, for solving the multitrip vehicle routing problem with backhauls and a heterogeneous fleet. The objective function is to minimize total cost, which is related to distance travelled. For validation, we designed numerical experiments to compare the proposed approaches with LINGO computational software, using the conventional diferential evolution algorithm and diferential evolution with selected genetic operator and fuzzy logic controller in real settings. The experimental results demonstrate the practical viability of the proposed approaches

## 1. Introduction

In the current business environment, factories are encountering pressure not only to make their operations more eficient and reduce production costs, but also to provide good service quality to clients. This pressure also occurs significantly in logistic companies, which need to improve their related logistics and planning under changing client needs. Logistics is increasingly challenging because of changes in cli ents’ demand, rapid technological change, increasing competition and uncertainty introduced by globalization (Jamrus, Wang, & Chien, 2020). The recent advances in transport systems have motivated logistics companies to better manage the planning in their companies. Because of evolving client demand, logistic companies require an efi cient delivery service with good service quality, while maintaining business profitability.

Food and beverages industries are increasing in importance from day to day. In particular, the beverage industry is one of the major contributors to the growth of global economics. The global beverages industry is expected to reach an estimated \$1.9 trillion by 2021, and is forecast to grow at a compound annual growth rate of 3.0% from 2016 to 2021 (Reportlinker, 2019). However, distribution costs are important and can account for up to 70% of the value added costs of products in the food and beverages industry (De Backer, Furnon, Kilby, Prosser &

Shaw, 1997). Also, the transportation cost is one elemental cost in the logistics business that has dominated the total cost. The beverage logistics company in this case study provides logistics services for alcoholic and non-alcoholic beverages. This company provides warehousing, transportation and distribution services. In particular, transportation and distribution services are the main total value-added costs of products for the company. The company transports soft drinks to customers, who are agents, distributors and restaurants. It likes to distribute soft drinks in glass bottles to all clients who need soft drinks in glass bottles, before making any empty glass bottle pickups back from clients to the company. There are two truck sizes for delivery and pickup of the soft drink glass bottles, and each truck may perform several routes within a single planning period. Therefore, each client has a known demand for delivery or pick up and is serviced by a vehicle of a heterogeneous fleet of capacitated trucks within a given time period. There are many transportation costs that are vital to logistic management. They can be reduced while maintaining a competitive pricing advantage and retaining profitability.

The vehicle routing problem (VRP) is one of the optimization problems faced most regularly in logistics; it determines the optimal sequence for clients to be visited by each vehicle. It aims to minimize the cost of transportation operations by a fleet of vehicles delivering to clients. The VRP with multiple trips (MTVRP) is characterized by an optimized set of vehicles and drivers working multiple routes or trips within a given time period (Brandão & Mercer, 1997). In addition, the vehicle routing problem with backhauls (VRPB) is one in which a vehicle may pick up products to carry them back to the depot after deliveries have been made. The client set of the VRPB can be classified into linehaul and backhaul customers. Each linehaul customer requires a given quantity of goods from a central depot, and a given quantity of goods is collected from each backhaul customer and returned to the depot. The backhauls must be visited after the linehauls in each route (Koç & Laporte, 2018). In this paper, the case study is the multi-trip vehicle routing problem with backhauls (MTVRPB), which can be described as a VRP problem with backhauling and multiple trips in a single planning period with a heterogeneous fleet, such that the total travel distance is minimized as shown in Fig. 1. The challenge for the backhaul beverage industry is how to deliver the soft drinks in glass bottles to all customers that need them, before making any empty glass bottle pickups from clients to return them to the company. In order to do so, the appropriate route for sequencing clients to be visited is determined for each vehicle, so that all delivery clients are served before any pickup ones, while optimizing the set of vehicles and drivers working multiple routes or trips within a given time period and with a heterogeneous fleet. The objective function is to minimize total cost, which is related to the distance travelled.

![](12-Sethanan_images/cb41c7e7c0887b305dbb27ebbca4e8672144729527c4a4b7610a5bc21d7b3896.jpg)  
Fig. 1. An example of the MTVRPB.

Many studies have addressed the single trip vehicle routing problem with backhaul and homogeneous fleet. Also, these problems have been solved using the simplicity of traditional metaheuristics. To fill the gap, this study proposes an integer linear programming formulation (ILP) and a hybrid diferential evolution algorithm and genetic operator with fuzzy logic controller (FLC), called HDEGO, to identify an appropriate route for sequencing of clients to be visited by each vehicle, so that all delivery clients are served before any pickup ones. In order to improve the solution quality in terms of travelling cost, through enhancing the diversity of vectors for exploring the solution space, selection of the vector representation can obviously be improved using a genetic operator. The genetic algorithm selection for the next generation is significant to the problem, because of the derived optimized solution. The elitism method is applied, which is the best of all selection methods. It is a selection strategy where a limited number of individuals with the best fitness values are chosen to pass to the next iteration. The limited number is the selected lowest number in an elitist way. Thus, this study will have the advantage of genetic operators applied with the elitism method to replace the traditional selection operator of DE, which is similar to a tournament selection feature. Moreover, an adaptive autotuning of the DE algorithm can adaptively regulate F and CR values during mutation and recombination operators. To illustrate the proposed method’s efectiveness, numerical experimental results were compared with the mathematical model and with the traditional DE. The next section provides a review of the relevant literature. The problem formulation is described in Section 3, and the HDEGO is presented in Section 4. Section 5 outlines computational experiments and results. Finally, a summary is given in Section 6.

## 2. Literature review

The VRP was first proposed by Dantzig and Ramser (1959). It has been extensively studied in the literature for several and varied applications. All the clients correspond to deliveries and the demands are known in advance and probably are not split (Liu, Li, & Liu, 2017). Many researchers have given state of the art reviews of VRP and approaches developed in the past (Eksioglu, Vural, & Reisman, 2009; Braekers, Ramaekers, & Van Nieuwenhuyse, 2016). For example, Shimizu and Sakaguchi (2013) proposed a hierarchical procedure that designed an economically eficient VRP for reverse logistics networks, and revealed some ways to reduce carbon dioxide emissions from the VRP in the same framework. Then, they extended the complexity to multi-depot VRPs that gave a more general framework for various real world applications, including those in green logistics (Shimizu & Sakaguchi, 2014).

The MTVRP is similar to the VRP but has a larger number of constraints. It has a set of vehicles and drivers working multiple routes or trips within a given time period. Brandão and Mercer (1997) first proposed certain assumptions: during each day a vehicle can make more than one trip and drivers' schedules must respect the maximum legal driving time per day and the legal time breaks. Cattaruzza, Absi, Feillet, and Vidal (2014) proposed a hybrid genetic algorithm for the MTVRP that allows for a diversified exploration over the search space, due to the management of several solutions at the same time. Also, François, Arda, Crama, and Laporte (2016) presented the problem in which each vehicle can deliver several routes during the same working shift to customers. They compared approaches between a heuristic that makes use of specific operators designed to tackle the routing and large neighborhood search (LNS) to perform the MTVRP. Their approach improved the results obtained with a given LNS algorithm.

The VRPB is also an extension of the classical VRP. Further con straints include: vehicles have to deliver to all the linehaul customers before visiting any backhaul customers; while routes with only backhauls are disallowed, routes with only linehauls can be delivered. Koç and Laporte (2018) comprehensively reviewed the existing up-to-date literature on the VRPB, including models, heuristic and metaheuristic approaches for solving the VRPB applications. There are many constraints considered, such as heterogeneous fleet, time windows, multidepot and mixed backhauls. For example, Ong & Suprayogi (2011) considered VRPB with time windows and homogeneity that was solved by the ant colony optimization, minimizing the number of vehicles, the total duration time and the range of duration times. Salhi, Wassan, and Hajarat (2013) proposed a heuristic algorithm for solving the VRPB with an unlimited number of vehicles and a heterogeneous fleet. They showed that the mathematical model can solve for small-size instances, but large-size instances were solved using upper and lower bounds. García-Nájera, Bullinaria, and Gutiérrez-Andrade (2015) studied multi objective VRPB that used a similarity-based selection multi-objective evolutionary algorithm, minimizing travel cost, number of routes and uncollected backhauls.

However, little literature is available on the MTVRPB. Yu and Qi (2014) presented the MTVRPB for the homogenous fleet of an express delivery company, with multiple-delivery and pickup customer visits each day and multiple trips per vehicle. They proposed modeling as a mixed ILP and developed the tabu search algorithm. The tabu search algorithm outperformed others, getting better solutions in a much shorter time than other heuristics, which also resulted in significant cost saving for the company. In addition, Wassan, Wassan, Nagy, and Salhi (2017) presented the MTVRPB with a homogenous fleet, with the ob jective to minimize the total cost by reducing the total distance travelled and the suitable number of vehicles used. They proposed an ILP for small and medium instances. For large instances of the MTVRPB, a two-level variable neighborhood search algorithm was developed and used, which produced eficient results for the VRPB. Thus, many metaheuristic approaches have been published with novel approaches and practical efectiveness.

The metaheuristic approach is mainly used owing to its ability to be more intensive and use robust methodologies to solve problems. Potvin, Duhamel, and Guertin (1996) determined the VRPB by a greedy route construction heuristic and a genetic algorithm, so that it ordered good routes. The objective is to minimize the total distance traveled, while satisfying backhauls and time window constraints. Both approaches were outperformed when these were combined. Zhong and Cole (2005) proposed a guided local search heuristic to solve a vehicle routing problem with backhauls and time windows. With this problem, the mathematical models or optimal methods are not appropriate, since the VRPB is an NP-hard problem and includes several constraints, and doe not simplify the problem. Xiao, Zhao, Kaku, and Mladenovic (2014) also proposed a metaheuristic approach that is a variant of the variable neighbourhood search, combined with simulated annealing for solving the VRP. The results show that the metaheuristic approach out performed most general algorithms in terms of computational efec tiveness and eficiency. Küçükoğlu and Öztürk (2014) presented a dif ferential evolution algorithm (DE) to solve a vehicle routing problem with backhauls and time windows and applied it to a catering firm. Also, Wisittipanich and Hengmeechai (2015) used a multi-objective DE for truck scheduling and door assignment in a multi-inbound and out bound doors cross docking problem with the Just-In-Time concept. The DE is a population-based search technique that uses simple operation on a generated vector set. There are operations that consist of initia vector, mutation, crossover and selection to create new vectors and competitive solutions. The highlighted diference from diferential evolution is combining several solutions with the candidate solution (Kachitvichyanukul, 2012). Even though diferential evolution has been used efectively in a variety of fields, it has been very limited when applying it to solve the VRP, especially the MTVRPB, because the en coding and decoding form of DE cannot be directly applied for the MTVRPB. Hence, the complexity of the MTVRPB with a heterogeneou fleet needs an eficient solution for minimizing the total distance travelled. We propose the HDEGO, not only applied with the elitism method to replace the traditional selection operator of the DE, but in cluding adaptive auto-tuning of the DE algorithm, which can also reg ulate parameters during mutation and recombination operators. We aim to solve the beverage logistic transportation problem by improving the solution quality in terms of travelling cost.

## 3. Mathematical model for MTVRPB

The MTVRP characteristics are explained as follows: (i) A set of clients is divided into two types, linehaul and backhaul customers; (ii) The fleet of trucks is heterogeneous; (iii) A truck may deliver more than one trip in a single planning period; (iv) All delivery clients are delivered before any pickup from backhaul customers; (v) Trucks are not allowed to pick up only backhauls on routes, but linehaul deliveries alone are allowed; (vi) Truck capacities are of two types. The notations used in this paper are summarized as follows.

<table><tr><td colspan="2">Index</td></tr><tr><td>i, j</td><td>index of customers (i, j = 1,2,..., N)</td></tr><tr><td>k</td><td>index of trucks (k = 1,2,..., K)</td></tr><tr><td colspan="2">Parameters</td></tr><tr><td>θ</td><td>depot or company (i, j = 1)</td></tr><tr><td>L</td><td>set of linehaul customers</td></tr><tr><td>B</td><td>set of backhaul customers</td></tr><tr><td>N</td><td>number of customers, N ∈ {θ, L, B}</td></tr><tr><td>K</td><td>number of trucks</td></tr><tr><td>m</td><td>maximum working period</td></tr><tr><td>ck</td><td>capacity of truck k</td></tr><tr><td>dij</td><td>distance between location of customers i and j</td></tr><tr><td>qi</td><td>demand of customer i</td></tr><tr><td colspan="2">Decision variables</td></tr><tr><td>bik</td><td>decision variable for sub-tour</td></tr><tr><td>sij</td><td>amount of deliveries or pickups in arcs i and j</td></tr><tr><td>xijk</td><td>=1, if truck k runs from customer i to j = 0, otherwise</td></tr></table>

The proposed model was formulated based on an ILP for MTVRPB. The objective is to minimize cost, which relates to the total distance travelled, as follows.

min $\sum _ { i = 1 } ^ { N } \sum _ { j = 1 } ^ { N } \sum _ { k = 1 } ^ { K } d _ { i j } \times x _ { i j k }$

subject to

$$
\sum_ {j = 1} ^ {N} \sum_ {k = 1} ^ {K} x _ {j i k} = 1 i \in \{L, B \}\tag{1}
$$

$$
\sum_ {j = 1} ^ {N} \sum_ {k = 1} ^ {K} x _ {i j k} = 1 i \in \{L, B \}\tag{2}
$$

$$
\sum_ {j = 1} ^ {N} x _ {j i k} - \sum_ {j = 1} ^ {N} x _ {i j k} = 0 \forall k, i \in \{L, B \}\tag{3}
$$

$$
\sum_ {i \in L} s _ {i j} - q _ {i} = \sum_ {i = 1} ^ {N} s _ {j i} j \in \{L \}\tag{4}
$$

$$
\sum_ {i \in \{L, B \}} s _ {i j} + q _ {i} = \sum_ {i = \{\theta , B \}} s _ {j i} j \in \{B \}\tag{5}
$$

$$
s _ {i j} \leq c _ {k} \times x _ {i j k} \forall k, i \in \{L, B \}, j \in \{L, B \}\tag{6}
$$

$$
\sum_ {i = 1} ^ {N} \sum_ {j = 1} ^ {N} d _ {i j} \times x _ {i j k} \leq m \forall k\tag{7}
$$

$$
b _ {i k} \geq b _ {j k} + q _ {i} - c _ {k} + c _ {k} (x _ {i j k} + x _ {j i k}) - (q _ {i} + q _ {j}) \times x _ {i j k} \forall i, j, k\tag{8}
$$

$$
, i \neq j, j \neq \theta \forall \mathrm{i}, \mathrm{j}, \mathrm{k}, \mathrm{i} \neq \mathrm{j}, \mathrm{j} \neq \theta\tag{9}
$$

$$
b _ {i k} \leq c _ {k} - (c _ {k} - q _ {i}) \times x _ {1 i k} \forall i, k\tag{10}
$$

$$
b _ {i k} \geq q _ {i} + \sum_ {j \in \{L, B \}} q _ {j} \times x _ {j i k} \forall i, k
$$

$$
s _ {i j} = 0 i \in \{L \}, j \in \{\theta , B \}\tag{11}
$$

$$
x _ {i j k} = 0 \forall k, i \in \{B \}, j \in \{L \}\tag{12}
$$

(13)

$$
x _ {i j k} = 0 \forall k, i \in \{\theta \}, j \in \{B \}\tag{14}
$$

$$
s _ {i j} \geq 0 \forall i, j \in \{L, B \}\tag{15}
$$

$$
x _ {i j k} = \{0, 1 \} \forall i, j, k\tag{16}
$$

The objective function (1) is to minimize total cost, which is the distance travelled. Constraints (2) and (3) ensure that every customer is delivered to or picked up from exactly once. Constraint (4) imposes that the number of times truck k visits customer i is the same as the number of times it departs from customer i. Constraints (5) and (6) impose the truck load change on a route for linehaul and backhaul customers, re spectively. Inequality (7) limits the maximum truck capacity constraint (heterogeneous fleet) that can serve the routes. The maximum working period constraint depends on distance, which is ensured by Inequality (8). Inequalities (9), (10) and (11) ensure sub-tour conditions. Constraint (12) disallows any load carried from a linehaul customer to be either a backhaul trip or to the depot. Constraints (13) and (14) ensure all delivery customers are delivered to before any pickup is made from backhaul customers. Also, trucks are not allowed to pick up only backhauls on routes, but only linehaul deliveries are allowed. In equality (12) sets $s _ { i j }$ as a non-negative variable. Constraint (13) is the binary variable constraint.

## 4. The HDEGO for MTVRPB

The hybrid diferential evolution algorithm and genetic operator with fuzzy logic controller, called HDEGO, has the following steps.

## 4.1. Initial solution

The DE is an indirect approach for solving some VRPBs used by Küçükoğlu and Öztürk (2014). They used two blocks in each vector to denote the customer and the vehicle number. However, the vectors of MTVRPB are designed to support both linehaul and backhaul customers, and truck types under a single planning period. The number of the po pulation is the population size or the number of vectors, where each vector consists of a customer vector and a truck type vector. Firstly, each customer vector will be randomly generated, equal to the number of linehaul and backhaul customers. The decryption sorts the rank order value of each vector, in ascending order, so that it obtains the sequence of customers to be visited. An additional vector is the truck type vector, which will also be randomly generated and equal to the number of customers. However, the decoding will design size numbers to be the same as the truck types, and there are two truck types in this study. Afte the encoding section, the sequences of customers are sorted in ac cordance with customer specifications, so that each linehaul custome must be placed before a backhaul customer. Fig. 2 shows an illustrative example of vector construction. There are five linehaul customers and three backhaul customers. For example, customer vector: $0 . 7 8 \substack { - 0 . 5 2 - 0 . 3 1 - 0 . 9 3 - 0 . 1 2 - 0 . 8 1 - 0 . 3 3 - 0 . 5 6 }$ . The customer ID is 1–2 − 3–4 − 5–6 − 7–8. After it is sorted in ascending order, it is obtained the customer vector: $0 . 1 2 \mathrm { - } 0 . 3 1 \mathrm { - } 0 . 3 3 \mathrm { - } 0 . 5 2 \mathrm { - } 0 . 5 6 \mathrm { - } 0 . 7 8 \mathrm { - } 0 . 8 1 \mathrm { - } 0 . 9 3 .$ . So, the customer ID is 5–3 − 7–2 − 8–1 − 6–4. The initial solution was pro cessed and sorted to obtain sequences of truck routes by prioritized linehaul customers and backhaul customers: truck type 1 is 0–5–2–7–6–0 and truck type 2 is 0–3–1–4–8–0, where 0 is the depot. In addition, these vectors consider the maximum working period constraints. If the tota working period of a route is more than the maximum working period, then the route will use more trucks to serve this route to meet the de mand fully within the maximum working period. The route is split so that the maximum working period is not exceeded. The accumulated working time starts from the depot until it reaches the maximum working period. For example, the truck type 1 route is 0–5–2–7–6–0 in Fig. 2 and there is the maximum working period. If the truck type 1 drives to node 2, then the accumulated working time is more than the maximum working period when it will drive to node 7. Thus, the truck type 1 will drive back to depot (0–5–2–0) and the split route (0–7–6–0) will be given to another truck.

In the multi-trip case, the accumulated working time of any truck is less than the maximum working period when the truck arrives at the depot. If there is working time remaining for one more trip, customers will be delivered to. For example, the truck type 1 route is 0–5–2–7–6–0 in Fig. 2. If the accumulated working time is still less than the maximum working period (0–5–2–0), then the truck could deliver more trips until the maximum working period is achieved (0–5–2–0 and 0–7–6–0). The objective is to minimize cost, which relates to the total distance travelled. Thus, the total distance of travelled truck type 1 is calculated two times, for the routes 0–5–2–0 and 0–7–6–0.

## 4.2. Diferential evolution algorithm (DE)

The DE algorithm was first introduced by Storn and Price (1997). The original DE has four methods consisting of the generations of initial solution, mutation, recombination and selection. In this study, a solution could not be found using an optimization program with large scale problems, because the number of variables is excessive, and the problem is NP-hard and highly complex, so we use the DE algorithm that finds optimal solutions from initial solutions (Section 4.1).

## 4.2.1. Mutation operation

Vector number (NP) is the number of vectors that is used for DE iterations. NP vectors will be randomly generated to an initial solution as in Section 4.1. Then, the mutation operation is the second process of the DE mechanism. Eq. (17) is used to randomly combine three selected vectors into a mutant vector. The scaling factor F is a constant from [0, 2]. $V _ { i , G + I }$ is called the mutant vector and $X _ { r 1 , G } , X _ { r 2 , G } , X _ { r 3 , G }$ are random vectors.

$$
V _ {i, G + 1} = X _ {r 1, G} + F (X _ {r 2, G} - X _ {r 3, G})\tag{17}
$$

## 4.2.2. Recombination operation

The recombination or crossover operator incorporates successful solutions from the previous iteration. The trial vector $( U _ { j i , G + I } )$ is obtained from Eq. (18). Each position value in a vector can be the position value of a target or trial vector, depending on a random number (Rand) that is generated for that position, and compared with the crossover rate (CR). The value of an indicated position will be replaced from the position value of that position in the target vector $( X _ { j i , G } ) ,$ , if the random number for that position is greater than the CR value. On the other hand, if the random number generated for that position is lower than or equal to the CR value, the value of the indicated position will be replaced from the position value of that position in the mutant vector $( V _ { j i , G + I } ) ;$ , as represented in Eq. (18).

$$
U _ {j i, G + 1} = \left\{ \begin{array}{l l} V _ {j i, G + 1} i f & (R a n d (j) \leq C R) \\ X _ {j i, G} i f & (R a n d (j) > C R) \end{array} \right.\tag{18}
$$

## 4.2.3. Selection operation

The traditional selection operation of DE is like tournament selection, which is a method of selecting an individual from a population of individuals in a genetic algorithm. The target vector $( X _ { j i , G } ) ,$ , is compared with the trial vector $\left( U _ { j i , G + 1 } \right)$ , and the one with the lowest objective value is selected to be the target vector for the next iteration $( X _ { j i , G + I } ) .$ Equation (19) represents the selection formula.

$$
X _ {j i, G + 1} = \left\{ \begin{array}{c} U _ {j i, G + 1}   \text {if}    (U _ {j i, G + 1} <   f (X _ {j i, G})) \\ X _ {j i, G}    \text {otherwise} \end{array} \right.\tag{19}
$$

## 4.3. Genetic operator

Genetic algorithm (GA) is an influential technique that has been applied in various research fields. GA has been widely employed for solving optimization problems. In GA, the fitness of every individual in a population is evaluated. GA searches from a population of points; therefore it can avoid being trapped in a local optimal solution. GA can solve all optimization problems that can be described through chromosome encoding; moreover, they provide multiple solutions and use fitness functions, which are obtained from objective functions, without the need for other derivative or auxiliary information. Moreover, they can be easily transferred to existing simulations and models (Jamrus & Chien, 2016). Although the GA has been used in a variety of research areas, it has limitations when applied for solving a problem, as the solution process may not be complex enough to find the optimal solution. In order to improve the diversity of DE, the hybridization of the DE with GA has been used to enhance the performance of the traditional DE and GA.

![](12-Sethanan_images/a8cba5ac0471d623e15a1509e3e78a6a4140dab9be0ec074c1a5157528fc2206.jpg)  
Fig. 2. An illustrative example of vector construction.

The GA selection for the next generation is significant to the problem because of the derived optimized solution. Panchal, Chudasama & Shah (2011) presented a comparison of selection operators: roulette wheel, elitism and tournament selection methods for the travelling salesman problem. They found that the elitism method is the best of all these methods. The elitist selection is a selection strategy where a limited number of individuals with the best fitness values are chosen to pass on to the next iteration. Thus, in this study the elitism method is applied to replace the traditional selection operator of DE, which is similar to the tournament selection feature. The target vectors are compared with the trial vector elitist selection that are selected to be the target vectors of the next iteration, as shown in Fig. 3. All target vectors and trial vectors were sorted by fitness value, and the best fit ness values selected to pass on to the next iteration.

## 4.4. Adaptive auto-tuning by fuzzy logic controller (FLC)

The conventional DE algorithm may not guarantee an optimal so lution in all cases, because the DE uses an unknown scaling factor (F) and crossover rate (CR). Adaptive auto tuning of the DE algorithm can adaptively regulate F and CR values during mutation and recombination operations. Yun and Gen (2003) and Jamrus, Chien, Gen, and Sethanan (2015) proposed a heuristic updating strategy for crossover and mutation rates of the genetic algorithm, to consider changes of average fitness in the population of two continuous generations. Therefore, this study uses the applied adaptive auto tuning for the DE algorithm that will control F and CR values during mutation and recombination processes. For the minimization problem, the change of the average fitness at iteration t, Δfavg(t), is as shown in Eq. (20). The vecsize is the vector size that satisfies constraints, and trisize is the trial vector size that satisfies constraints.

![](12-Sethanan_images/5966c12b901bb8f1833431d7f3dd0928eea8dab2e2265bd04a78bfcab8fe0668.jpg)  
Fig. 3. An illustrative example of elitist selection.

$$
\Delta f _ {a v g} (t) = \stackrel {-} {f _ {v e c s i z e}} (t) - \stackrel {-} {f _ {t r i s i z e}} (t) = \frac {1}{v e c s i z e} \sum_ {k = 1} ^ {v e c s i z e} f _ {k} (t) - \frac {1}{t r i s i z e} \sum_ {k = 1} ^ {t r i s i z e} f _ {k} (t).\tag{20}
$$

## 4.5. The HDEGO algorithm

The algorithm first defines the initial solution sectns such as encoding and decoding vectors for MTVRPB. Each vector consists of a customer vector, linehaul or backhaul customer, and a truck type vector, type 1 or type 2. The objective is to minimize cost, which is the total distance travelled (Section 4.1). Then, DE is used with four methods consisting of generation of initial solution, mutation, recombination, and selection. This study uses the elitism method to re place the traditional selection operator of DE (Sections 4.2–4.4). Finally, the adaptive auto-tuning of the DE algorithm can adaptively regulate F and CR values during mutation and recombination operators (Section 4.4). The HDEGO algorithm procedure is shown in Fig. 4.

Table 3  
Example of distance matrix [km]  
Table 1  
```vhdl
Procedure: Hybrid differential evolution with genetic operator algorithms (HDEGO)
Input :MTVRPB data, DE parameters (CR, F, NP)
Output :Optimal solution
Begin :
Encoding step: randomly generate a set of target vectors n (n = 1...NP); //n is the index of the vector representation; NP is a predefined number of population
while termination condition is not satisfied do
for n = 1 to NP //NP is the predefined number of population
Solution Initialization (section 4.1)
Decoding and Evaluation (section 4.1)
Mutation Operation (section 4.2)
Recombination Operation (section 4.2)
Elitist Selection Operation (section 4.3)
Tune Parameters by Adaptive Auto Tuning (section 4.4)
end
end
end;
```  
Fig. 4. Overall HDEGO algorithm procedure.

## 5. Computational experiments

To demonstrate the eficiency and efectiveness of the HDEGO in MTVRPB, the DE parameters are designed as tuning parameters according to the adaptive auto-tuning routine for F and CR. The numerical experiments are 10 sets with vecsize = 50 and maxiter = 500. The proposed algorithms were run using MatLab on a 2.10 GHz PC, with 8 GBytes of RAM, for testing and evaluation. For illustration, we generated 10 problems (Table 1) involving various numbers of maximum working periods and linehaul and backhaul customers. Each demand for customers was generated in the value interval for pallets [2, 10] for each problem. There are two truck sizes, 40 and 50 pallets. For instance 1, the number of linehaul and backhaul customers are set at three and two, respectively. The distance between linehaul and backhaul customers is shown in Table 2. In addition, linehaul customer demand is 6, 5 and 7 pallets and backhaul customer demand is 7 and 2 pallets. Table 3 presents the solution for instance 1 in which two large trucks are used with maximum working period by optimal solution. The problems were formulated as an integer programming model for the multiple trip vehicle routing problem with backhauls and heterogeneous fleet, as shown in Table 4.

The results of the test problems for deriving an optimal solution follow, made by generating seven problems and presenting total travel distance and computational time for each problem. For instances 1 to 4, the computational time increases dramatically depending on the problem size, since the problem is an NP-hard problem. Instances 5 to 7 yielded a high number of variables, in which the MTVRPB problem was NP-hard and highly complex. Also, the freight forwarder accepts computational time which is less than 360 min (6 h), so that limits the sequence of customers to be visited by each vehicle. Instances 5 to 10 cannot be accepted by the mathematical model. Therefore, this paper proposes that the HDEGO can determine the sequence of customers to be visited by each vehicle for satisfying customer demands and solving both small and large problems.

Test problem sizes.

<table><tr><td>Instance</td><td>No. of Linehauls</td><td>No. of Backhauls</td><td>Max. working period</td></tr><tr><td>1</td><td>3</td><td>2</td><td>14</td></tr><tr><td>2</td><td>6</td><td>3</td><td>14</td></tr><tr><td>3</td><td>9</td><td>3</td><td>14</td></tr><tr><td>4</td><td>11</td><td>4</td><td>14</td></tr><tr><td>5</td><td>15</td><td>5</td><td>16</td></tr><tr><td>6</td><td>18</td><td>5</td><td>16</td></tr><tr><td>7</td><td>25</td><td>6</td><td>16</td></tr><tr><td>8</td><td>25</td><td>8</td><td>18</td></tr><tr><td>9</td><td>32</td><td>10</td><td>18</td></tr><tr><td>10</td><td>40</td><td>12</td><td>18</td></tr></table>

Table 2

<table><tr><td>Customer</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>-</td><td>2</td><td>4</td><td>3</td><td>5</td><td>8</td></tr><tr><td>2</td><td>2</td><td>-</td><td>3</td><td>6</td><td>4</td><td>7</td></tr><tr><td>3</td><td>4</td><td>3</td><td>-</td><td>5</td><td>3</td><td>1</td></tr><tr><td>4</td><td>3</td><td>6</td><td>5</td><td>-</td><td>7</td><td>3</td></tr><tr><td>5</td><td>5</td><td>4</td><td>3</td><td>7</td><td>-</td><td>4</td></tr><tr><td>6</td><td>8</td><td>7</td><td>1</td><td>3</td><td>4</td><td>-</td></tr></table>

Results for instance 1 [km].

<table><tr><td>Instance 1</td><td colspan="2">Results</td></tr><tr><td>Total travel distance (km)</td><td>24</td><td></td></tr><tr><td>Computational time (minutes)</td><td>0.05</td><td></td></tr><tr><td>Trucks used</td><td>Two large trucks</td><td></td></tr><tr><td rowspan="2">Sequences of customers</td><td rowspan="2">Truck 1</td><td>Trip 1: 0-1-0</td></tr><tr><td>Trip 2: 0-3-0</td></tr><tr><td></td><td>Truck 2</td><td>Trip 1: 0-2-5-4-0</td></tr></table>

The best total cost from solving by ILP.

<table><tr><td>Instance</td><td>Total travel distance [km]</td><td>Computational time [min]</td></tr><tr><td>1</td><td>24</td><td>0.05</td></tr><tr><td>2</td><td>34</td><td>2.3</td></tr><tr><td>3</td><td>39</td><td>20.6</td></tr><tr><td>4</td><td>36</td><td>814</td></tr></table>

We tested the traditional DE, GA and HDEGO performance using seven test problem instances, the same as the ILP test. The computational tests compared the best and average total cost of each solution for solving each problem by 10 runs, and the results of the optimal solution, DE GA and HDEGO for MTVRPB are shown in Table 5. The DE, GA and HDEGO determined that the best total distance equals the optimal solution for instances 1 to 3; nevertheless, the HDEGO gave the same result as the optimal solution compared with the DE and GA for instance 4. Moreover, the HDEGO obtained best and average solutions better than the DE and GA for instances 5 to 10. The proposed HDEGO outperformed the DE and GA, particularly for medium and large problem sizes. The time here is the CPU time in seconds for every run, and in the example of the HDEGO experiment, determining the solution used slightly more CPU time than DE and GA for instances 1 to 10. The large problem used CPU time of about three minutes. On the other hand, the optimal solution is 814 min (about 13.5 h) and the freight forwarder cannot accept this computational time. Moreover, the HDEGO determined that the total distance equals the optimal solution and has enhanced results compared with the traditional DE and GA, whereas in the comparison results between the DE, GA and HDEGO for each problem, the HDEGO spends fewer iterations than the number of generations in the DE for finding the best solution for large problems (Instances 5–10). The proposed HDEGO outperforms the traditional DE for large problems. Time is the CPU time in seconds for every run, and the example of the HDEGO experiment facilitated determining the best solution at 11.9 s at the 18th iteration in instance 5. However, the CPU time of EP-DPSO found a solution that is less than the nEP-HGA, in which the best solution is at 24.3 s at the 26th iteration. In addition, the CPU time and times for HDEGO and DE runs are 167.3 s (74th iteration) and 174.8 s (115th iteration), respectively for instance 10. However, in small problems such as instances 1 to 4, the results of HDEGO and DE are similar. However, they can determine which real world demands must be optimized for long-term eficient operation of the entire transportation system. Thus, the HDEGO can determine which beverage logistic must be optimized for eficient operation of the backhaul transportation.

Table 6  
Table 5  
Comparison of the best and average total distances of each solution from solving each problem.

<table><tr><td rowspan="2">No.</td><td colspan="2">Optimal solution by LINGO</td><td colspan="4">Solution by DE</td><td colspan="4">Solution by GA</td><td colspan="4">Solution by HDEGO</td></tr><tr><td>Best solution [km]</td><td>CPU time [min]</td><td>Avg. [km]</td><td>Std.</td><td>Best solution [km]</td><td>CPU time [sec]</td><td>Avg. [km]</td><td>Std.</td><td>Best solution [km]</td><td>CPU time [sec]</td><td>Avg. [km]</td><td>Std.</td><td>Best solution [km]</td><td>CPU time [sec]</td></tr><tr><td>1</td><td>24</td><td>0.05</td><td>24.0</td><td>0</td><td>24</td><td>6.4</td><td>24.0</td><td>0</td><td>24</td><td>6.4</td><td>24.0</td><td>0</td><td>24</td><td>6.6</td></tr><tr><td>2</td><td>34</td><td>2.3</td><td>35.0</td><td>0.3</td><td>34</td><td>8.7</td><td>34.9</td><td>0.2</td><td>34</td><td>8.8</td><td>34.5</td><td>0.2</td><td>34</td><td>9.1</td></tr><tr><td>3</td><td>39</td><td>20.6</td><td>41.2</td><td>0.3</td><td>39</td><td>11.3</td><td>40.9</td><td>0.3</td><td>39</td><td>11.5</td><td>40.1</td><td>0.2</td><td>39</td><td>11.3</td></tr><tr><td>4</td><td>36</td><td>814</td><td>40.0</td><td>0.3</td><td>39</td><td>12.8</td><td>39.7</td><td>0.3</td><td>38</td><td>12.9</td><td>38.2</td><td>0.4</td><td>36</td><td>13.1</td></tr><tr><td>5</td><td>-</td><td>-</td><td>75.3</td><td>1.2</td><td>69</td><td>16.4</td><td>74.4</td><td>0.9</td><td>70</td><td>16.8</td><td>71.1</td><td>0.8</td><td>66</td><td>17.1</td></tr><tr><td>6</td><td>-</td><td>-</td><td>78.5</td><td>2.3</td><td>76</td><td>18.4</td><td>79.2</td><td>1.9</td><td>78</td><td>18.9</td><td>75.7</td><td>1.1</td><td>73</td><td>19.3</td></tr><tr><td>7</td><td>-</td><td>-</td><td>113.1</td><td>3.1</td><td>107</td><td>23.8</td><td>115.2</td><td>3.3</td><td>105</td><td>24.1</td><td>109.9</td><td>1.5</td><td>102</td><td>24.4</td></tr><tr><td>8</td><td>-</td><td>-</td><td>134.8</td><td>3.7</td><td>126</td><td>45.8</td><td>133.3</td><td>3.5</td><td>125</td><td>50.4</td><td>125.1</td><td>2.0</td><td>119</td><td>55.6</td></tr><tr><td>9</td><td>-</td><td>-</td><td>158.9</td><td>3.8</td><td>141</td><td>89.2</td><td>157.2</td><td>3.5</td><td>144</td><td>98.0</td><td>141.0</td><td>2.0</td><td>132</td><td>101.3</td></tr><tr><td>10</td><td>-</td><td>-</td><td>179.2</td><td>3.9</td><td>159</td><td>150.3</td><td>185.8</td><td>3.6</td><td>168</td><td>172.7</td><td>155.6</td><td>2.7</td><td>145</td><td>181.2</td></tr></table>

Results of ANOVA analysis.

<table><tr><td rowspan="2">No.</td><td colspan="2">Factor</td><td colspan="2">Total distance [km]</td><td rowspan="2">% improvement</td><td rowspan="2">No.</td><td colspan="2">Factor</td><td colspan="2">Total distance [km]</td><td rowspan="2">% improvement</td></tr><tr><td>instance</td><td>% fluctuation</td><td>DE</td><td>HDEGO</td><td>instance</td><td>% fluctuation</td><td>DE</td><td>HDEGO</td></tr><tr><td>1-5</td><td>1</td><td>10</td><td>24.0</td><td>24.0</td><td>0.00</td><td>56-60</td><td>4</td><td>50</td><td>41.0</td><td>38.8</td><td>4.93</td></tr><tr><td>6-10</td><td>1</td><td>30</td><td>24.0</td><td>24.0</td><td>0.00</td><td>61-65</td><td>5</td><td>10</td><td>79.6</td><td>69.4</td><td>12.70</td></tr><tr><td>11-15</td><td>1</td><td>50</td><td>24.0</td><td>24.0</td><td>0.00</td><td>66-70</td><td>5</td><td>30</td><td>76.2</td><td>71.0</td><td>6.71</td></tr><tr><td>16-20</td><td>2</td><td>10</td><td>34.4</td><td>34.2</td><td>0.55</td><td>71-75</td><td>5</td><td>50</td><td>72.0</td><td>70.0</td><td>2.66</td></tr><tr><td>21-25</td><td>2</td><td>30</td><td>34.6</td><td>34.2</td><td>1.14</td><td>76-80</td><td>6</td><td>10</td><td>79.4</td><td>72.2</td><td>8.98</td></tr><tr><td>26-30</td><td>2</td><td>50</td><td>34.6</td><td>34.4</td><td>0.55</td><td>81-85</td><td>6</td><td>30</td><td>82.6</td><td>76.2</td><td>7.70</td></tr><tr><td>31-35</td><td>3</td><td>10</td><td>41.0</td><td>39.4</td><td>3.83</td><td>86-90</td><td>6</td><td>50</td><td>80.2</td><td>72.8</td><td>9.17</td></tr><tr><td>36-40</td><td>3</td><td>30</td><td>40.0</td><td>39.4</td><td>1.46</td><td>91-95</td><td>7</td><td>10</td><td>118.2</td><td>108.4</td><td>8.09</td></tr><tr><td>41-45</td><td>3</td><td>50</td><td>40.2</td><td>39.2</td><td>2.45</td><td>96-100</td><td>7</td><td>30</td><td>118.6</td><td>107.8</td><td>8.84</td></tr><tr><td>46-50</td><td>4</td><td>10</td><td>41.6</td><td>38.4</td><td>7.63</td><td>101-105</td><td>7</td><td>50</td><td>119.0</td><td>109.6</td><td>7.61</td></tr><tr><td>51-55</td><td>4</td><td>30</td><td>39.0</td><td>38.2</td><td>10.00</td><td>Average</td><td></td><td></td><td></td><td></td><td>4.97</td></tr></table>

The solutions from using the HDEGO were compared with those from using the traditional DE procedures, which were based on factorial designs according to factor levels. The combination experiments were conducted in quintuplicate. The parameters included the number of problems (Table 1) and the fluctuation of customer demand (10, 30 and 50% of customer demands, which were an average demand). The samples totaled 105, and the results are indicated by the percentage improvement between DE and HDEGO as shown in Table 6.

Table 6 shows 4.97% improvement from the MTVRPB model when the data were analyzed using ANOVA. The percentage improvement difered significantly from actual situation practices at the 95% reliability level, and p was less than 0.05. The parameter explaining this diference was not the fluctuation of demand that yielded the average improvement of DE and HDEGO. Nevertheless, most HDEGO approaches outperformed, getting better total distance solutions than traditional DE, and providing significant transportation cost saving for the company.

## 6. Conclusions

The current transportation environment is becoming increasingly complex, which leads to it being increasingly more competitive. Moreover, the global beverage industry is forecast to grow continuously at a compound annual growth. This study has proposed an integer linear programming formulation and a HDEGO to identify an appropriate route for sequencing customers to be visited by each vehicle of a beverage logistics company, so that all delivery customers are served before any pickup ones. The HDEGO was not only applied with the elitism method to replace the traditional selection operator of the DE, but adaptive auto tuning of the DE algorithm can also regulate parameters during mutation and recombination operators. The experimental results show that the proposed HDEGO outperformed the DE by about 4.97%, with average improvements for all the problem instances (Table 6). The results demonstrate the practical viability of the proposed approach, which can support freight forwarder and customers. A future study can be done to extend the proposed HDEGO approach to allow for more constraints, such as customers’ time windows and mixed VRPB in a real setting. For example, stochastic customer service demands quantity, a load splitting constraint and multiple depots. Also, more studies can be done to develop approaches for multiple objective in the beverage logistic industry.

## CRediT authorship contribution statement

Kanchana Sethanan: Conceptualization, Writing - review & editing. Thitipong Jamrus: Methodology, Validation, Software, Formal analysis, Writing - original draft.

## Acknowledgements

This work was supported by the Research Unit on System Modeling for Industry (Grant No. SMI.KKU 63003), Khon Kaen University, Thailand. The authors would also like to thank Mr. Ian Thomas for critical review of the manuscript.

## References

Braekers, K., Ramaekers, K., & Van Nieuwenhuyse, I. (2016). The vehicle routing problem: State of the art classification and review. Computers & Industrial Engineering, 99, 300–313. https://doi.org/10.1016/J.CIE.2015.12.007.

Brandão, J., & Mercer, A. (1997). A tabu search algorithm for the multi-trip vehicle routing and scheduling problem. European Journal of Operational Research, 100(1), 180–191. https://doi.org/10.1016/S0377-2217(97)00010-6.

Cattaruzza, D., Absi, N., Feillet, D., & Vidal, T. (2014). A memetic algorithm for the mult trip vehicle routing problem. European Journal of Operational Research, 236(3), 833–848. https://doi.org/10.1016/J.EJOR.2013.06.012

Dantzig, G. B., & Ramser, J. H. (1959). The truck dispatching problem. Management Science, 6(1), 80–91. https://doi.org/10.1287/mnsc.6.1.80.

De Backer, B., Furnon, V., Kilby, P., Prosser, P., & Shaw, P. (1997). Local search in constraint programming: Application to the vehicle routing problem. Retrieved from https://pdfs.semanticscholar.org/2666/03a503d1dbb84bb1f570c133745e8b9dc8f0. pdf.

Eksioglu, B., Vural, A. V., & Reisman, A. (2009). The vehicle routing problem: A taxonomic review. Computers & Industrial Engineering, 57(4), 1472–1483. https://doi.org 10.1016/J.CIE.2009.05.009.

François, V., Arda, Y., Crama, Y., & Laporte, G. (2016). Large neighborhood search for multi-trip vehicle routing. European Journal of Operational Research, 255(2), 422–441. https://doi.org/10.1016/J.EJOR.2016.04.065.

García-Nájera, A., Bullinaria, J. A., & Gutiérrez-Andrade, M. A. (2015). An evolutionary approach for multi-objective vehicle routing problems with backhauls q. Doi: 10. 1016/j.cie.2014.12.029.

Jamrus, T., Chien, C.-F., Gen, M., & Sethanan, K. (2015). Multistage production distribution under uncertain demands with integrated discrete particle swarm optimi zation and extended priority-based hybrid genetic algorithm. Fuzzy Optimization and Decision Making, 14(3), 265–287. https://doi.org/10.1007/s10700-014-9200-6.

Jamrus, T., & Chien, C. F. (2016). Extended priority-based hybrid genetic algorithm for the less-than-container loading problem. Computers & Industrial Engineering, 96, 227–236.

Jamrus, T., Wang, H. K., & Chien, C. F. (2020). Dynamic coordinated scheduling for supply chain under uncertain production time to empower smart production for Industry 3.5. Computers & Industrial Engineering, 142, 106375.

Kachitvichyanukul, V. (2012). Comparison of three evolutionary algorithms: GA, PSO and DE. Doi: 10.7232/iems.2012.11.3.215.

Koç, Ç., & Laporte, G. (2018). Vehicle routing with backhauls: Review and research perspectives. Computers & Operations Research, 91, 79–91. https://doi.org/10.1016/J. COR.2017.11.003.

Küçükoğlu, İ., & Öztürk, N. (2014). A diferential evolution approach for the vehicle routing problem with backhauls and time windows. Journal of Advanced Transportation, 48(8), 942–956. https://doi.org/10.1002/atr.1237.

Liu, L., Li, K., & Liu, Z. (2017). A capacitated vehicle routing problem with order available time in e-commerce industry. Engineering Optimization, 49(3), 449–465. https://doi. org/10.1080/0305215X.2016.1188092.

Ong, J. O., & . S. (2011). Vehicle routing problem with backhaul, multiple trips and time window. Jurnal Teknik Industri, 13(1), 1–10. Doi: 10.9744/jti.13.1.1-10.

Panchal, M., Chudasama, C., Shah, S. M., & Processor, A. (2011). Comparison of parents selection methods of genetic algorithm for TSP. In International Journal of Computer Applications®. Retrieved from https://www.researchgate.net/publication/ 285690217.

Potvin, J.-Y., Duhamel, C., & Guertin, F. (1996). A genetic algorithm for vehicle routing with backhauling. Applied Intelligence, 6(4), 345–355. https://doi.org/10.1007/ BF00132738.

Reportlinker. (2019). Growth opportunities in the global beverage market. Retrieved July 7, 2019, from https://www.researchandmarkets.com/reports/4171584/growth-op portunities-in-the-global-beverage-market.

Salhi, S., Wassan, N., & Hajarat, M. (2013). The fleet size and mixed vehicle routing problem with backhauls: Formulation and set partitioning-based heuristics. Transportation Research Part E: Logistics and Transportation Review, 56, 22–35. https:// doi.org/10.1016/J.TRE.2013.05.005.

Shimizu, Y., & Sakaguchi, T. (2013). Generalized vehicle routing problem for reverse logistics aiming at low carbon transportation. Doi: 10.7232/iems.2013.12.2.161.

Shimizu, Y., & Sakaguchi, T. (2014). A hierarchical hybrid meta-heuristic approach to coping with large practical multi-depot VRP. Doi: 10.7232/iems.2014.13.2.163.

Storn, R., & Price, K. (1997). Diferential evolution – A simple and eficient heuristic for global optimization over continuous spaces. Journal of Global Optimization, 11(4), 341–359. https://doi.org/10.1023/A:1008202821328.

Wassan, N., Wassan, N., Nagy, G., & Salhi, S. (2017). The multiple trip vehicle routing problem with backhauls: formulation and a two-level variable neighbourhood search. Computers & Operations Research, 78, 454–467. https://doi.org/10.1016/J.COR.2015. 12.017.

Wisittipanich, W., & Hengmeechai, P. (2015). A multi-objective diferential evolution for just-in-time door assignment and truck scheduling in multi-door cross docking problems. Industrial Engineering and Management Systems, 14(3), 299–311. https://doi. org/10.7232/iems.2015.14.3.299.

Xiao, Y., Zhao, Q., Kaku, I., & Mladenovic, N. (2014). Variable neighbourhood simulated annealing algorithm for capacitated vehicle routing problems. Engineering Optimization, 46(4), 562–579. https://doi.org/10.1080/0305215X.2013.791813.

Yu, M., & Qi, X. (2014). A vehicle routing problem with multiple overlapped batches Transportation Research Part E: Logistics and Transportation Review, 61, 40–55. https:/ doi.org/10.1016/J.TRE.2013.10.004.

Yun, Y., & Gen, M. (2003). Performance analysis of adaptive genetic algorithms with fuzzy logic and heuristics. Fuzzy Optimization and Decision Making, 2(2), 161–175. https://doi.org/10.1023/A:1023499201829.

Zhong, Y., & Cole, M. H. (2005). A vehicle routing problem with backhauls and time windows: A guided local search solution. Transportation Research Part E: Logistics and Transportation Review, 41(2), 131–144. https://doi.org/10.1016/J.TRE.2003.12.003.