---
raw_title: 09-IEEENetwork-2019
subject: 数学建模-策联杯B题
source: "09.pdf"
status: mineru解析
parser: mineru
topics:
  - 城市环境监测
  - 异构车辆
  - 任务分配
  - 智能城市
---

# Collaboration of Heterogeneous Unmanned Vehicles for Smart Cities

Peng Li, Xing Wu, Wenfeng Shen, Weiqin Tong, and Song Guo

## Abstract

Urban environment monitoring is critical for smart cities, but it is challenging because of the complex city environment. Unfortunately, traditional approaches, for example, wireless sensor networks and satellite-based monitoring, have many constraints in practice. In this article, we propose to use heterogeneous unmanned vehicles to monitor an urban environment and study their collaboration in computing workload sharing. Given a number of tasks and vehicles, an eficient algorithm has been proposed to maximize the total weight of completed tasks. Simulation results show that our proposed algorithm significantly outperforms two other heuristic algorithms.

## Introduction

Monitoring an urban environment, such as spatial-temporal changes, crowd distribution and pollution, is critical for smart cities [1]. This information can be used for improving urban services and the city’s sustainability. Internet-of-Things (IoT) technology is promising for efficient urban environment monitoring in smart cities [2, 3]. A large number of sensors can be deployed to collect environmental information, such as air pollution and traffic. All data are gathered and analyzed to enable various services, for example, smart home, traffic control, pollution evaluation and smart grids.

However, IoT-based urban environmental monitoring is challenging due to the following reasons. First, as cities grow, the monitoring region becomes larger, which requires large-scale monitoring systems. Although there exist some recent research eforts on building large-scale sensor networks [4, 5], they are far from achieving the requirements of practical urban environment monitoring because of many unsolved challenges. Second, an urban environment is complex in geography, with streets, buildings, parks, rivers, lakes and so on. A single monitoring and networking technology can hardly work in all scenarios. Furthermore, with the development of cities, the urban environment changes due to the renewal of old districts. The monitoring system should be periodically updated correspondingly. Finally, there are usually multiple monitoring objectives in smart cities. Some applications need to monitor crowd distribution and traffic, which can help design better transportation systems. Air and water quality monitoring is also an important objective when we would like to evaluate the level of pollution in cities.

In this article, we propose to use heterogeneous unmanned vehicles to address the above challenges of urban environment monitoring. As shown in Fig. 1, the vehicles include ground vehicles, air vehicles (also called drones) and water vehicles (also called unmanned boats), which can cover almost all regions within the city. Ground vehicles are powered by fuel or large batteries, so that they can work on streets for long-time monitoring. Air vehicles have limited energy, but with strong moving capability and they are preferred for the monitoring of a larger area. Water vehicles can work in rivers and lakes, and perform tasks like water pollution monitoring [6]. These heterogeneous vehicles can work collaboratively to achieve large-scale and comprehensive urban environmental monitoring. Although there are existing research eforts on vehicle-based sensing [7–11], they mainly focus on a single type of vehicle and there are still many open research issues in the collaboration of heterogeneous vehicles. The main contributions of this article are summarized as follows:

• We study the collaboration of heterogeneous unmanned vehicles for smart cities. We analyze sensing applications in smart cities, as well as the characteristics of vehicles of different types. The main challenges have been summarized.

• We propose a four-layer architecture for efficient collaboration of heterogeneous vehicles and present how it can address the challenges.

• We study a specific problem called network-aware task assignment, which is the most critical issue for vehicle collaboration. The problem is well formulated and solved by an eficient algorithm.

The reminder of this article is organized as follows. We first summarize the main challenges of urban environment monitoring, followed by the architecture of heterogeneous unmanned vehicles. Then, a network-aware task assignment problem is studied. We finally conclude the article.

## Challenges

Although collaboration of heterogeneous unmanned vehicles for urban environment monitoring is promising, we face the following challenges.

The monitoring tasks have different types. Some tasks can be conducted by dedicated vehicles. For example, we use unmanned boats to get water samples for water pollution monitoring. Air vehicles can be applied to build accurate 3-D models of cities. Other tasks can be conducted by multiple types of vehicles. For example, both ground and air vehicles can be used to measure air quality, but with different cost. An important research challenge here is how to efficiently assign tasks to heterogeneous vehicles to maximize monitoring quality while minimizing the monitoring cost.

The vehicles are heterogeneous in functions and moving capability. Even for the same type of vehicles, they may have diferent sensors and hardware [12]. This kind of hardware heterogeneity should be considered in task assignment. In addition, performing a monitoring task usually involves multiple hardware, for example, sensors, CPU, and network. The hardware equipped within a single vehicle may not satisfy the task requirements. For example, air vehicles can take videos or photos for a large region, but they do not have enough energy and powerful enough CPU to conduct video/image processing, which usually involves heavy computation. In our proposal, we offload some computation loads to other nearby vehicles. Although computation offloading has been studied in cloud and edge computing [13], there are many new challenges in heterogeneous vehicle collaboration in smart cities. Specifically, we need to study which parts of tasks should be ofloaded, and which vehicles should be ofloaded to.

![](09-IEEENetwork-2019_images/21445fcd49d7ced5dde0d5a13e30d0a1fd7778946cc4effc73d0bd8cb64c447c.jpg)  
FIGURE 1. Scenario of heterogeneous vehicles for urban environment monitoring in smart cities.

![](09-IEEENetwork-2019_images/de53fbcf4b60982119ddcc1611b1a6617b95061e05f59161a762d2cf82258813.jpg)  
FIGURE 2. System architecture.

Vehicle collaboration relies on efficient network connection among them. This network should have low delay, so that vehicles can quickly share their status information and respond to collaboration requests [14]. It also should provide good support of mobility. A single network technology cannot satisfy these requirements, which motivates us to combine multiple networks and study eficient data transmission.

## Architecture

To enable eficient collaboration among unmanned vehicles, we propose a four-layer design, as shown in Fig. 2, to address the challenges of mission control, resource sharing and networking.

The top layer is the application layer, where various urban environmental monitoring applications can be accommodated into our design. In the mission layer, each application can be modeled as a mission graph, which contains multiple tasks with dependent relationship. Each vertex denotes the task that can be independently conducted by a vehicle and each edge means the dependent relationship between tasks. For example, monitoring water pollution of rivers and lakes includes the tasks of taking photos of water pollution emissions, getting water samples and comprehensive analysis. The photo taking and sampling should be conducted before analyzing. These tasks are assigned to diferent vehicles according to their capability. For example, water sampling should be assigned to only water vehicles. Since the ground vehicles have a powerful CPU and energy, they can do comprehensive analysis with heavy computation. Furthermore, we need to jointly consider other factors, like cost, energy level, network connection, and in task assignment to achieve the optimal performance.

Performing a task involves using multiple hardware resources on a vehicle. In the computing layer, we enable hardware resource sharing by offloading some computation loads to other vehicles or edge computing nodes. We collect information about network quality and computing capability of nearby vehicles. This information is forwarded to an algorithm that makes final offloading decisions.

All above layers are based on the network connection among vehicles. Different kinds of network technologies can be applied in our design, as the network layer shown in Fig. 2. Satellite communication has large coverage, but with low bandwidth and high cost. It can be used to transmit some critical control messages when other networks are not available. Cellular networks can provide high-speed and stable connection. However, they have not yet covered some rural areas. Point-to-point communication technologies, for example, WiFi, can be applied to establish direct network connection between vehicles, but only work within constrained distances. We observe that any single network technology cannot satisfy the requirements of vehicle collaboration. Therefore, we propose to build a hybrid network by integrating multiple networks. Data transmission can go through multiple networks.

We now discuss how the proposed four-layer architecture solves the challenges presented previously. First, it can provide a simplified view about task structure and enable deep study about task assignment. Some sensing applications are usually complicated, involving multiple vehicles. We model applications as mission graphs, where each node in the graph represents an independent function that can be conducted by a vehicle. This kind of modeling provides fine-grained information about task structure, so that we can handle task assignment in the mission layer. Second, vehicles are modeled as mobile computing units with diferent capability. In our task assignment and offloading algorithm design, we first conduct function mapping, that is, which vehicle can provide the sensing function required by a sensing task in the mission graph, and then assign tasks to the best vehicles (e.g., closest to the target area). Finally, cross-layer design will be adopted to enable eficient overall design. In the next section we will show how we address the network challenge by proposing a network-aware task assignment.

## N etwork-Aware Task Assignment

In this section, we study a network-aware task assignment problem to show how cross-layer design should be applied on this system. We consider a number of vehicles with computational tasks that can be ofloaded to other vehicles. We apply the method-level offloading technique, that ${ \mathrm { i } } s ,$ each task is a program method that cannot be split. Each task i is associated with a weight $W _ { j }$ that indicates the importance of this task. We define a binary variable $x _ { i j }$ to denote the offloading decision. If $x _ { j j }$ is 1, task i is offloaded to vehicle j. Otherwise, it is not. Since there are multiple network paths between the vehicle that generates task i and vehicle j, we define another binary variable $y _ { i j } ^ { k }$ to denote whether we choose the k-th path between them. In our system model, we assume that network transmission is much faster than the movement of vehicles. Once we collect the network information, we can quickly solve the optimization problem and deploy tasks according to solving results. During this period, vehicles have limited movement, whose influence to network transmission can be ignored. Furthermore, in the worst case, even if some tasks fail due to vehicle movement, they will be considered in the next round of task assignment, but with a larger weight so that they will be assigned in higher priority.

We consider two kinds of constraints. First, since each vehicle has limited computational capability, the total computational loads that are ofloaded to vehicle j cannot exceed its capacity. We let $d _ { i }$ denote the computational loads of task $i ,$ and $d _ { j }$ is the total load that can be accommodated by vehicle j. The constraint of computational capacity can be expressed by $\Sigma _ { I } d _ { i } x _ { i j } \leq D _ { j } ^ { \cdot } , \forall _ { j } .$

![](09-IEEENetwork-2019_images/f7e50131f8b755cd6015c8b18f0a8229c8362a583735f2fdd59c36d44568dd5f.jpg)  
FIGURE 3. The total weight of completed tasks under diferent number of tasks.

![](09-IEEENetwork-2019_images/21634cd48c7b8d4bfbe288db5ea517c0bd5550934a5ffbf063455b23e6beb782.jpg)  
FIGURE 4. The total weight of completed tasks under computing capability.

Second, when we choose paths for transmitting offloaded tasks, the network link capacity should be considered. We let $e _ { i }$ denote the size of task i and l<sup>pq</sup>  indicates whether link pq is includ ed in the k-path between i and j. The total traffic going through each link pq cannot exceed its capacity $E _ { p q \prime }$ that is, $\Sigma _ { i j k } \mathrm { e } _ { i } x _ { i j } y _ { i j } ^ { k } I _ { p q } ^ { l j K } \le E _ { p q }$

Our objective is to assign a subset S of tasks to vehicles, so that their total weight is maximized. The objective function can be expressed by max $\Sigma _ { i \in S } { \cal W } _ { i } \Sigma _ { j } \times _ { i j } .$ Unfortunately, this problem is NP-hard and it can be proved by reducing the 3-dimensional matching problem.

The problem can be formulated as a mixed-integer nonlinear programming problem. The main difficulty of solving the above formulation is the nonlinear constraint of network link capacity. We relax this constraint by splitting data transmission over multiple paths, so that the $y _ { i j } ^ { k }$ becomes a real variable. The multiplication of variables $x _ { i j } y _ { i j } ^ { k }$ can be replaced by a new variable $z _ { i j } ^ { k }$ and their relationship can be constrained by $0 \leq Z _ { i j } ^ { k } \leq \gamma _ { i j } ^ { k }$ and 1 – ${ x _ { i j } + y _ { i j } ^ { k } \le z _ { i j } ^ { k } \le x _ { i j } } .$ With the above new variables and constraints, the formulation becomes a mixed-integer linear programming problem that can be quickly solved by software tools, for example, CPLEX.

## Performance Evaluation

In this section, we conduct simulations to evaluate the performance of our proposed algorithm. For comparison, we also show the performance of the other three algorithms.

Opt-Unaware: We extend the algorithm proposed in [12] that ignores the network path selection.

Weight-First: We iteratively assign tasks to vehicles. In each iteration, we always select the task with maximum weight and assign it to the vehicle with maximum residential computing capability.

Resource-First: In each iteration, we always choose the task that occupies the minimum network and computing resources. Since more tasks can be assigned, this algorithm can potentially increase the total weight of completed tasks.

We first study the influence of a number of tasks. Tasks are randomly generated on vehicles whose computing capability is a normal distribution with main of 30 units. We change the number of task from 30 to 70 and show the results of all algorithms in Fig. 3. We observe that our proposed algorithm, which is marked as “Optaware”, always outperforms the other three algorithms because it jointly considers the computation capability of vehicles and network connection among them. For example, when there are 30 vehicles, the total weight of “Opt-aware” is about 105.3, which outperforms “Resourcefirst” by 27 percent. The total weight of completed tasks increases as the growths of task number. However, the increasing trend becomes slow because most of the tasks with large weight have been assigned.

Next, we change the mean of computing capability distribution and show the results in Fig. 4. With the growth of computing capability, the total weight under all algorithms increase becomes more tasks can be accommodated. For example, the total weight of “Opt-aware” increas es 34 percent as number of computing capability grows from 30 to 50. It is dificult to have further growth because of the constraint of network capacity. Meanwhile, we observe that our proposed algorithm can achieve larger total weight than the other two heuristic algorithms by at least 10 percent.

## Conclusion and Future Work

In this article, we propose a vehicle-based scheme for urban environment monitoring. Diferent types of vehicles can collaborate on monitoring tasks and share computing workloads. An eficient algorithm has been proposed to maximize the number of completed tasks and its performance has been evaluated via extensive simulations. In future work, we will study the distributed algorithm for task assignment. Furthermore, a prototype will be developed and evaluated using real workload traces.

## Acknowledgment

This work is supported by Japan Society for the Promotion of Science (JSPS) Grants-in-Aid for Young Scientific Research (19K20258) and National Natural Science Foundation of China (61872310).

## References

[1] P. Sismanidis, I. Keramitsoglou, and C. T. Kiranoudis, “Evalu ating the Operational Retrieval and Downscaling of Urban Land Surface Temperatures,” IEEE Geoscience and Remote Sensing Lett., vol. 12, no. 6, June 2015, pp. 1312–16.

[2] P. Rathore et al., “Real-Time Urban Microclimate Analysis Using Internet of Things,” IEEE Internet of Things J., vol. 5, no. 2, Apr. 2018, pp. 500–11.

[3] L. Zhou et al., “Greening the Smart Cities: Energy-Efficient Massive Content Delivery via D2D Communications,” IEEE Trans. Industrial Informatics, vol. 14, no. 4, Apr. 2018, pp. 1626–34.

[4] B. P. L. Lau et al., “Sensor Fusion for Public Space Utilization Monitoring in a Smart City,” IEEE Internet of Things J., vol. 5, no. 2, Apr. 2018, pp. 473–81.

[5] H. Jiang et al., “Connectivity-Based Segmentation in Large Scale 2-D/3-D Sensor Networks: Algorithm and Applications,” IEEE/ACM Trans. Networking, vol. 23, no. 1, Feb. 2015, pp. 15–27.

[6] Y. G. Xing Wu et al., “The Cooperative Defense System by Team of USVs in Complicated Sea Environment,” Proc. 16th Int’l. Conf. New Trends in Intelligent Software Methodologies, Tools and Techniques, 2017.

[7] Y. Wang et al., “Vlnsight: Enabling Open Innovation in Networked Vehicle Sensing and Control,” IEEE Network, vol. 30, no. 4, July 2016, pp. 34–44.

[8] Y. Nishibe et al., “Sensing of Passing Vehicles Using a Lane Marker on a Road with Built-In Thin-Film Mi Sensor and Power Source,” IEEE Trans. Vehicular Technology, vol. 53, no. 6, Nov. 2004, pp. 1827–34

[9] Y. Lai et al., “Distributed Public Vehicle System Based on Fog Nodes and Vehicular Sensing,” IEEE Access, vol. 6, 2018, pp. 22 011–24.

[10] Z. Su, Y. Hui, and T. H. Luan, “Distributed Task Allocation to Enable Collaborative Autonomous Driving with Network Softwarization,” IEEE JSAC, vol. 36, no. 10, Oct. 2018, pp. 2175–89.

[11] D. Zeng et al., “An Improved Stochastic Modeling of Opportunistic Routing in Vehicular CPS,” IEEE Trans. Computers, vol. 64, no. 7, July 2015, pp. 1819–29.

[12] P. Li et al., “Vehicle-Assist Resilient Information and Network System for Disaster Management,” IEEE Trans. Emerging Topics in Computing, vol. 5, no. 3, July 2017, pp 438–48.

[13] L. Lin et al., “Echo: An Edge-Centric Code Ofloading Sys tem with Quality of Service Guarantee,” IEEE Access, vol. 7, 2019, pp. 5905–17.

[14] J. Huang et al., “In-Vehicle Networking: Protocols, Chal lenges, and Solutions,” IEEE Network, vol. 33, no. 1, Jan. 2019, pp. 92–98.

## B iographies

Peng Li [M] received his B.S. degree from Huazhong University of Science and Technology, China, in 2007, and his M.S. and Ph.D. degrees from the University of Aizu, Japan, in 2009 and 2012, respectively. Dr. Li is currently an associate professor at the University of Aizu, Japan. His research interests mainly focus on cloud computing, Internet-of-Things, big data systems, and related wired and wireless networking problems. He won the Young Author Award of the IEEE Computer Society Japan Chapter in 2014. He won the Best Paper Award of IEEE TrustCom 2016. He supervised students to win the First Prize of the IEEE ComSoc Student Competition in 2016.

Xing Wu received his Ph.D. degree from the Department of Computer Science and Technology, Shanghai Jiaotong University in 2010. He is currently an associate professor with the School of Computer Engineering and Science, Shanghai Uni versity, China. His research interests include issues related to artificial intelligence and data mining. He is the author of many research studies published in national and international journals, conference proceedings and book chapters.

Wenfeng Shen received his B.Eng., M.Eng. and Ph.D. degrees in computer engineering and science from Shanghai University, China, in 1996, 2001 and 2016, respectively, and his Ph.D. degree in computer science and engineering from the University of Aizu, Japan, in 2010. He is currently an associate professor with the School of Computer Engineering and Science, Shanghai University, China. His research interests include cardiac computer simulation, parallel computing and High Performance Computing. He is the director of the High Performance Computing Center of Shanghai University.

Weiqin Tong received his Master’s degree and Bachelor’s degree from the Department of Computer Science and Technology, Nanjing University of Science and Technology, in 1987 and 1984, respectively; and his Ph.D. degree from the Department of Computer Science and Technology, Shanghai Jiaotong University in 1995. He is currently a professor with the School of Computer Engineering and Science, Shanghai University, China. His research interests include parallel computing, parallel programming, cloud computing and data intensive computing.

Song Guo is a full professor with the Department of Comput ing, Hong Kong Polytechnic University. His research interests are mainly in the areas of big data, cloud computing, mobile computing, and distributed systems with over 450 papers published in major conferences and journals. His work was recognized by the 2016 Annual Best of Computing: Notable Books and Articles in Computing in ACM Computing Reviews. He is the recipient of the 2018 IEEE TCGCC Best Magazine Paper Award, 2017 IEEE Systems Journal Annual Best Paper Award, and six other Best Paper Awards from IEEE/ACM conferences. Prof. Guo was an associate editor of IEEE Transactions on Paral lel and Distributed Systems and an IEEE ComSoc Distinguished Lecturer. He is now an Associate Editor of IEEE Transaction on Cloud Computing, IEEE Transactions on Emerging Topics in Computing, IEEE Transactions on Sustainable Computing, IEEE Transactions on Green Communications and Networking, and IEEE Network. He has also served as General and Program Chair for numerous IEEE conferences. He currently serves as a Director and member of the Board of Governors of IEEE ComSoc.