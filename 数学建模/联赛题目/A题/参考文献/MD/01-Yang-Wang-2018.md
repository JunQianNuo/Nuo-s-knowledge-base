---
raw_title: 01-Yang-Wang-2018
subject: 数学建模-策联杯A题
source: "1-s2.0-S0378775318310462-main.pdf"
status: mineru解析
parser: mineru
topics:
  - 快充三难
  - 析锂
  - 能量密度
  - 循环寿命
---

# Understanding the trilemma of fast charging, energy density and cycle life of lithium-ion batteries

![](01-Yang-Wang-2018_images/947e56fe7c256db0deb63b4fdb11ddf8819ee31b3af2f3d4f7154c12ae82f80c.jpg)

Xiao-Guang Yang, Chao-Yang Wang

Department of Mechanical and Nuclear Engineering and Electrochemical Engine Center (ECEC), The Pennsylvania State University, University Park, PA, 16802, USA

## H I G H L I G H T S

• Temperature-dependent aging behavior of Li-ion battery is studied numerically.

• Overall aging rate depends on the competition of lithium plating and SEI growth.

• The optimal temperature for cycle life increases with charge rate & energy density.

• Raising charging temperature is an e<sup>f</sup>ective method to eliminating lithium plating.

## G R A P H I C A L A B S T R A C T

![](01-Yang-Wang-2018_images/f709d36c0f4fe8b98f0994d0a6bcc2048f583363cbfea3a907cfaaa43f9aed79.jpg)

![](01-Yang-Wang-2018_images/d4467e33cfeb5eebf1c6ce86e2fddb5d97dba2345bb1b5409ab6193ef2749ac0.jpg)

## A R T I C L E I N F O

Keywords: Lithium-ion battery Fast charging Energy density Cycle life Lithium plating Temperature-dependent aging

## A B S T R A C T

Increasing energy density of Li-ion batteries (LiBs) along with fast charging capability are two key approaches to eliminate range anxiety and boost mainstream adoption of electric vehicles (EVs). Either the increase of energy density or of charge rate, however, heightens the risk of lithium plating and thus deteriorates cell life. The trilemma of fast charging, energy density and cycle life are studied systematically in this work utilizing a physicsbased aging model with incorporation of both lithium plating and solid-electrolyte-interphase (SEI) growth. The model is able to capture the key feature of temperature-dependent aging behavior of LiBs, or more speci<sup>fi</sup>cally, the existence of an optimal temperature with the longest cycle life. We demonstrate that this optimal temperature is a result of competition between SEI growth and lithium plating. Further, it is revealed that either the increase of charge rate or of energy density accelerates lithium plating induced aging. As such, the optimal temperature for cell life increases from $\sim 2 0 ^ { \circ } \mathrm { C }$ for a high-power cell at 1C charge to $\sim 3 5 \ – 4 5 \ ^ { \circ } \mathrm { C }$ with the increase of charge rate and/or energy density. It would be bene<sup>fi</sup>cial to further increase the charge temperature in order to enable robust fast charging of high energy EV cells

## 1. Introduction

With the rapid drop in the cost of Li-ion batteries (LiBs) by 80% in the past seven years, the world is now truly embracing electric vehicles (EVs). Numerous countries has announced their timelines to phase out diesel/gasoline vehicles and more than 10 major automakers launched their future EV plans in 2017. Should these plans fructify, we are foreseeing 400 EV models and sales of 25 million units by the year 2025. Despite the promising future, the EV market, as of 2017, still only accounts for 1.7% of annual vehicles sales. Range anxiety, the fear that an EV may run out of juice on the way has long been cited as the key reason keeping consumers from EVs [1]. To tackle this barrier, automakers are targeting higher battery capacities of over 60 kWh that could ofer a driving range of ∼200 miles on a single charge, along with boosting the number of fast charging stations with charging power up to 350 kW, capable of charging a 60 kWh battery in 10–15 min [2].

A critical barrier to fast charging is the issue of lithium plating [3,4]. Most EV batteries utilize graphite as the anode material whose equilibrium potential is fairly close to the reversible potential of lithium deposition/dissolution. At harsh charging conditions when there is large anode polarization, the anode potential could fall below 0 V vs Li/ $\mathrm { L i ^ { + } }$ and triggers lithium plating, leading to drastic capacity loss and even to safety hazards. Extensive e<sup>f</sup>orts have been made to explore the bottlenecks of fast charging [5–9] and to optimize charge protocols [10–14]. It is widely acknowledged that lithium plating is prone to occur at high charge rates and/or low temperatures.

Recent studies showed that lithium plating could be a serious issue in high energy cells even at moderate charge rate and temperature. A typical approach to increase the energy density of LiBs is to increase the areal loading of active materials, which makes the anode thicker, denser and more tortuous [15], leading to larger anode polarization and thus higher risk of lithium plating. Gallagher et al. [16] revealed that the maximum charge rate of LiBs drops with the increase of areal loading. In their study, a cell with 3.3 mAh/cm<sup>2</sup> areal loading had stable capacity retention upon cycling with 1C charge at 30 °C but rapid capacity fade with 1.5C charge. A cell with 4.4 mAh/cm<sup>2</sup> areal loading could not even survive 1C charge at $3 0 ~ ^ { \circ } \mathrm { C } .$ A large amount of metallic lithium was observed after dismantling the aged cells, con<sup>fi</sup>rming the occurrence of lithium plating in these high energy cells, though the charge rate and temperature are moderate. Malifarge et al. [17] recently presented a detailed analysis of the voltage losses in graphite anodes with diferent areal loading (2–6 mAh/cm<sup>2</sup>) and porosity (0.1–0.45) and revealed that the large electrolyte-phase overpotential and the associated non-uniform state of charge (SOC) across the anode are the key reasons yielding lithium plating. Most recently, Spingle et al. [18] con<sup>fi</sup>rmed through thickness measurement, voltage relaxa tion method and post-mortem imaging that a high energy cell (190 Wh/ kg, 98 μm-thick anode) sufered serious lithium plating with only 1.5C charge at 25 °C.

The impacts of fast charging and energy density on cell life are more complicated when considering temperature e<sup>f</sup>ects. In the early stage of literature, it was typically believed that cell aging is faster at higher temperatures due to the faster growth of solid-electrolyte-interphase (SEI) [19]. Waldmann et al. [20] conducted a comprehensive study of temperature effects on LiB aging via cycling of 1.5Ah graphite/NMC 18650 cells with 1C charge at di<sup>f</sup>erent temperatures. Interestingly, it was found that the cell at 25 °C had the longest cycle life; either higher or lower temperatures resulted in faster degradation. Plotting the aging rate against reciprocal temperature, the authors found that the aging rate follows Arrhenius law and there is a transition of activation energy, from a positive value at $\mathrm { ~ T ~ } > \ 2 5 ^ { \circ } \mathrm { ~ C ~ }$ to a negative value at $\mathrm { ~ T ~ } < 2 5 ^ { \circ } \mathrm { C } ,$ indicating a transition of the dominant aging mechanism, which is believed to be SEI growth at $\mathrm { ~ T ~ } > \ 2 5 ^ { \circ } \mathrm { ~ C ~ }$ and lithium plating at $\mathrm { ~ T ~ } < 2 5 ^ { \circ } \mathrm { C }$ . Shimpe et al. [21] tested a set of 3Ah graphite/LFP 26650 cells with 1C charge and also found that the $2 5 ^ { \circ } \mathrm { C }$ cell had the best cycle life. Further, it is worth noting that the cycle life at $1 0 ~ ^ { \circ } \mathrm { C }$ was only about half of that at $2 5 ^ { \circ } \mathrm { C } .$ . Ecker et al. [22] also reported that the cycle life of a 53Ah high power graphite/NMC cell dropped sharply with the reduction of temperature at 0.85C charge, from ∼4000 cycles at $2 0 ^ { \circ } \mathrm { C } \ \mathrm { t o } \ \sim 2 0 0 0$ cycles at $1 0 ^ { \circ } \mathrm { C }$ and only ∼40 cycles at $0 \ { } ^ { \circ } \mathbf { C } .$ . Similarly, the work of Matadi et al. [23] showed that a 16Ah graphite/NMC cell which could sustain 4000 cycles at $2 5 ^ { \circ } \mathrm { C }$ lost 75% capacity in only 50 cycles at $5 ^ { \circ } \mathrm { C } .$ . These results indicate that lithium plating could be a serious issue even at cool temperatures. To that end, it would be bene<sup>fi</sup>cial to charge a cell at high temperatures, which, on the other hand, accelerates SEI growth. The best scenario would be charging a cell always at its optimal temperature where the combined aging rate of SEI growth and lithium plating reaches the minimum. An interesting question is that: is room temperature always the best for cell charging?

A fundamental understanding of the temperature-dependent aging behavior of LiBs is thus of vital signi<sup>fi</sup>cance for extending the lifetime of EVs. Previous studies on this subject were mostly based on the lastgeneration high power cells designed for plug-in hybrid electric vehicles (PHEVs) with relatively low areal capacity (< 2 mAh/cm<sup>2</sup>) and thin electrodes $( < 5 0 \mu \mathrm { m } )$ and at moderate charge rates. As the world is targeting higher energy density and faster charging, there is an urgent need to understand the impacts of energy density and charge rate on the temperature-dependent aging behavior. Indeed, recent studies have shown that cycle life is not always the best at room temperature. Matsuda et al. [24] tested commercial 18650 cells in $2 5 ^ { \circ } \mathrm { C }$ and 45 °C (Fig. S1a). At 1C charge, the cycle life was better at $2 5 ^ { \circ } \mathrm { C }$ than at $4 5 ^ { \circ } \mathrm { C } .$ At 2C charge, however, the $4 5 ^ { \circ } \mathrm { C }$ cell had much longer life than the 25 °C cell. Friesen et al. [25] tested high energy cells with thick anode (74–80 μm) at 1C charge and found that the cycle life at $4 5 ^ { \circ } \mathrm { C }$ was 3x longer than at 20 °C (Fig. S1b). Similarly, Rieger et al. [26] cycled high energy cells (77-μm thick anode) with 1C charge and found that the cells at 25 °C lost 30% capacity in 250–400 cycles whereas the cells at $4 0 ^ { \circ } \mathrm { C }$ lost only 5% capacity after 400 cycles (Fig. S1c). The above results indicate that the optimal temperature for LiBs could shift with the change of charge rate and energy density.

The objective of the present work is to gain a systematic understanding of the impacts of fast charging and energy density on the temperature-dependent aging behavior of LiBs. A physics-based aging model with incorporation of SEI growth and lithium plating is utilized to predict the aging rate of LiBs at di<sup>f</sup>erent temperatures with variou charge rates and areal loadings. Special attention is paid to the competition between SEI growth and lithium plating and to the variation of optimal temperature with charge rate and energy density. Directions for enabling temperature-independent, fast, and healthy charging of high energy cells are also presented.

## 2. Model description

The aging model that we recently developed for modeling of lithium plating induced aging of LiBs [27] is adopted in this work. A key feature of the model is that it accounts for both SEI growth and lithium plating. Further, the model considers the reduction of anode porosity due to continuous SEI growth, which results in onset of lithium plating and thereby in transition from linear to nonlinear capacity fade after prolonged cycling. A brief summary of the model is given below and further details could be found in our previous work [27].

A total of three electrochemical reactions are considered to occur in the anode, including lithium intercalation into graphite (Eq. (1a)), SEI formation (Eq. (1b)), and lithium plating (Eq. (1c)):

$$
C _ {6} + L i ^ {+} + e ^ {-} \leftrightarrow L i C _ {6}\tag{1a}
$$

$$
2 C _ {2} H _ {4} C O _ {3} + 2 e ^ {-} + 2 L i ^ {+} \rightarrow (C H _ {2} O C O _ {2} L i) _ {2} + C _ {2} H _ {4}\tag{1b}
$$

$$
L i ^ {+} + e ^ {-} \rightarrow L i (s)\tag{1c}
$$

The total volumetric current density in the anode is the sum of current density of the above three individual reactions, as:

$$
j _ {t o t} = j _ {g r} + j _ {S E I} + j _ {L i}\tag{2}
$$

where the subscripts tot, $^ { g r , }$ SEI and Li denote total, graphite, SEI formation and lithium plating, respectively. The current density of graphite is calculated via the following Butler-Volmer equation:

$$
j _ {g r} = a i _ {0, g r} \left\{\exp \left(\frac {\alpha_ {a} F}{R T} \eta_ {g r}\right) - \exp \left(- \frac {\alpha_ {c} F}{R T} \eta_ {g r}\right) \right\}\tag{3}
$$

where a is speci<sup>fi</sup>c surface area, $i _ { O }$ the exchange current density, $\alpha _ { a }$ and $\alpha _ { c }$ the anodic and cathodic charge transfer coe<sup>fi</sup>cients, and $\eta _ { g r }$ the overpotential of $\mathrm { L i ^ { + } }$ intercalation into graphite.

The current density of SEI formation is calculated via the following Tafel equation:

Table 1  
Cell design information and key temperature-dependent model parameters.

<table><tr><td rowspan="2">Parameter</td><td colspan="2">PHEV cell</td><td colspan="2">EV cell</td></tr><tr><td>Anode (Graphite)</td><td>Cathode (NMC622)</td><td>Anode (Graphite)</td><td>Cathode (NMC622)</td></tr><tr><td>Thickness (μm)</td><td>48.7</td><td>40.75</td><td>82.5</td><td>75.8</td></tr><tr><td>Initial Porosity</td><td>0.32</td><td>0.33</td><td>0.27</td><td>0.28</td></tr><tr><td>Areal Loading (mAh/cm2)</td><td>2.23</td><td>1.85</td><td>4.07</td><td>3.7</td></tr><tr><td>Negative-Positive (N-P) ratio</td><td>1.2</td><td></td><td>1.1</td><td></td></tr><tr><td>Nominal capacity (Ah)</td><td>10.0</td><td></td><td>10.3</td><td></td></tr><tr><td>Specific energy (Wh/kg)</td><td>175</td><td></td><td>215</td><td></td></tr></table>

Key temperature-dependent parameters

<table><tr><td>Parameters</td><td>Value @ 25 °C</td><td> $E_{act}$  (kJ/mol)</td></tr><tr><td>Graphite exchange current density,  $i_{o,gr}$  (A/m2)</td><td>2.1</td><td>68</td></tr><tr><td>Graphite solid-state diffusivity,  $D_{s,gr}$  (m2/s)a</td><td> $1.6 \times 10^{-14} (1.5-x)^{1.5}$ </td><td>30</td></tr><tr><td>Diffusivity of ethylene carbonate,  $D_{EC}$  (m2/s)</td><td> $2.0 \times 10^{-18}$ </td><td>30</td></tr><tr><td>SEI reaction rate constant,  $k_{SEI}$  (m/s)</td><td> $1.0 \times 10^{-12}$ </td><td>30</td></tr><tr><td>Exchange current density of Li plating,  $i_{o,Li}$  (A/m2)b</td><td>0.001</td><td>68</td></tr></table>

<sup>a</sup> x refers to lithium stoichiometry at graphite surfaces.  
Estimated value from Ref. [27], only irreversible part of lithium plating is considered.

![](01-Yang-Wang-2018_images/20e8800ffa99616b355c04fb6ddb94109abaa6ca4a137bec9a135fb4d0aa4a0f.jpg)

![](01-Yang-Wang-2018_images/7f072b927ed53616cc23df615e3b32a081c3d23fa3d6e35c473279098c8b7b04.jpg)  
Fig. 1. Temperature-dependent aging behavior with the existence of an optimal temperature for cycle life. (a) Capacity retention vs equivalent full cycle (EFC) for a PHEV cell cycled with 1C charge at di<sup>f</sup>erent temperatures. (b) Corresponding aging rate (capacity loss per EFC) versus reciprocal temperature.

$$
j _ {S E I} = - a F k _ {0, S E I} c _ {E C} ^ {s} \exp \left(- \frac {\alpha_ {c , S E I} F}{R T} \eta_ {S E I}\right)\tag{4}
$$

where $k _ { O , S E I }$ is a kinetic rate constant and $c _ { E C } ^ { s }$ is the concentration of ethylene carbonate (EC) at the graphite surfaces. EC di<sup>f</sup>uses from the bulk solution across the surface <sup>fi</sup>lm to graphite surfaces, where it reacts with $\mathrm { L i ^ { + } }$ ions to form new SEI. The surface concentration of EC is calculated by the balance between the rate of EC di<sup>f</sup>usion across the <sup>fi</sup>lm and the rate of EC consumption at graphite surfaces, as:

$$
- D _ {E C} \frac {c _ {E C} ^ {s} - c _ {E C} ^ {0}}{\delta_ {f i l m}} = - \frac {j _ {S E I}}{a F}\tag{5}
$$

where $D _ { E C }$ is EC di<sup>f</sup>usivity, $c _ { E C } ^ { 0 }$ the EC concentration in bulk solution and $\delta _ { f i l m }$ the <sup>fi</sup>lm thickness.

The current density of lithium plating is calculated by the following Tafel equation:

$$
j _ {L i} = - a i _ {0, L i} \exp \left(- \frac {\alpha_ {c , L i} F}{R T} \eta_ {L i}\right)\tag{6}
$$

It is worth mentioning that, in reality, a portion of the plated lithium is reversible. That is, the plated lithium could dissolve and go back to the cathode in the relaxation or discharge process subsequent to charging, leading to a distinct voltage plateau that is often utilized as a method to detect lithium plating [28]. It is, however, still unclear of how large are the relative fractions of reversible and irreversible lithium plating. Since the reversible part of plated lithium does not induce capacity loss, we only consider the irreversible part in this model. Thereby, the exchange current density, $i _ { O , L i } ,$ is treated as a <sup>fi</sup>tting parameter which is adjusted by matching the model-predicted capacity retention curves with the experiment data, as presented in our previous work [27]. The estimated value of $i _ { O , L i }$ is much smaller than the actual exchange current density of lithium metal stripping/plating since the reversible part of lithium plating is neglected.

The amount of SEI and lithium metal are calculated by the Faraday's law:

$$
\frac {\partial c _ {S E I}}{\partial t} = - \frac {j _ {S E I}}{2 F}
$$

$$
\frac {\partial c _ {L i}}{\partial t} = - \frac {j _ {L i}}{F}\tag{7a}
$$

(7b)

a  
![](01-Yang-Wang-2018_images/870620706382f10124b5c2ce979285afda54e377e737ae74fc67a72141fcb9b7.jpg)

b  
![](01-Yang-Wang-2018_images/f45adc3eaf9b6829d257af904d3967a9cdd467a2b7d2fae4996a8c35ead4a71a.jpg)  
C

![](01-Yang-Wang-2018_images/039dec62edf8af515c8f9db88e17deee82aea0d692335ea17b245df1d4c109b8.jpg)  
Fig. 2. Competition between lithium plating and SEI growth. (a) Breakdown of total capacity loss induced by SEI growth and by lithium plating at the end of life (20% total capacity loss). (b&c) Evolution of total capacity loss induced by (b) SEI growth and (c) lithium plating in the cycling process. The cell is a PHEV cell charging at di<sup>f</sup>erent temperatures with 1C charge.

where $c _ { S E I }$ and $c _ { L i }$ are the molar concentrations of SEI and lithium metal per unit volume of the electrode. The SEI and lithium metal together constitute the surface <sup>fi</sup>lm covering graphite particles. In the model, graphite particles are assumed to be spherical and the surface <sup>fi</sup>lm is assumed to be uniform in thickness. As such, the amount of SEI and lithium metal can be transformed to an equivalent thickness of the surface <sup>fi</sup>lm, as:

$$
\delta_ {f i l m} = \frac {1}{a} \left(\frac {c _ {S E I} M _ {S E I}}{\rho_ {S E I}} + \frac {c _ {L i} M _ {L i}}{\rho_ {L i}}\right)\tag{8}
$$

where M is molecular weight and $\rho$ is density. Further, the increase of <sup>fi</sup>lm thickness would reduce anode porosity via the following correlation:

$$
\frac {d \varepsilon}{d t} = - a \frac {d \delta_ {f i l m}}{d t}\tag{9}
$$

The above equations are incorporated into the electrochemical thermal (ECT) model that has been utilized extensively in the literature [29–31] to predict the performance and life of LiBs. A key feature of the ECT model is that all the parameters related to reaction kinetics and transport processes are functions of cell temperature. In this work, electrolyte properties are calculated by interpolating the experimental data, in terms of concentration and temperature, of those reported by Valoen et al. [32]; the properties of electrode materials (e.g. exchange current density, solid-state di<sup>f</sup>usivity, etc.) and the key parameters related to SEI growth and lithium plating (EC di<sup>f</sup>usivity $D _ { E C } ,$ rate constant $k _ { O , S E I }$ and exchange current density of lithium plating $i _ { O , L i } )$ are calculated by the Arrhenius-type correlation as:

$$
\psi = \psi_ {r e f} \exp \left(\frac {E _ {a c t}}{R} \left(\frac {1}{T _ {r e f}} - \frac {1}{T}\right)\right)\tag{10}
$$

where ψ denotes a parameter, $\psi _ { r e f }$ is its reference value at a reference temperature $T _ { r e f } , E _ { a c t }$ is activation energy, R is universal gas constant and T is cell temperature. In this work, the reference temperature is set as $2 5 ^ { \circ } \mathrm { C }$ and the reference values of some key parameters are summarized in Table 1. Other parameters of the ECT model can be found in our previous works [29,31]. It should be mentioned the reference values of the parameters related to SEI growth and lithium plating are set to be the same as those in our previous work [27], where extensive model validations were performed to demonstrate that the model well predicts the capacity retention of a PHEV cell cycled at room temperature as well as the discharge curves of both fresh and aged cells at various currents.

In this work, the above model is extended to study the aging behavior of LiBs at various temperatures with di<sup>f</sup>erent charge rates and energy density. In the following, we start from a PHEV cell at 1C charge to show the model's capability of capturing the temperature-dependent aging behavior of LiBs reported in the literature, i.e. the existence of an optimal temperature with the lowest aging rate. The model is then utilized to study the impacts of charge rate on cell aging, followed by studying the impacts of energy density. Finally, the trilemma among fast charging, energy density and cycle life are assessed with a particular emphasis of their dependence on temperature. Future directions for enabling fast and healthy charging of high energy cells without restrictions of temperature are then discussed. The design information of the cells studied in this work are listed in Table 1. The cycling protocol of all simulated cases is: constant current charge to 4.2 V followed by constant voltage charge at 4.2 V until the current drops below C/10; rest for 5 min; constant current discharge at 1C to 2.8 V, followed by another 5 min rest.

![](01-Yang-Wang-2018_images/8298378a034ed129c28dcc963da54c6f21d25d134fa5e3d5d97e5351f0f461a9.jpg)

![](01-Yang-Wang-2018_images/1303c8158c29fd8a73661e21cb0e0cfed9fa33473eb3b81365334af52a59bbc5.jpg)

![](01-Yang-Wang-2018_images/339c9c5883c76cf45e6d1401940721462d55a73feff64bb409bdb50bca16f90e.jpg)

![](01-Yang-Wang-2018_images/47f638158e3d3911ed76121b98656935cf75150a2525f4d7dab591cdc97216d2.jpg)  
Fig. 3. Earlier onset of lithium plating with the decrease of temperature. Evolutions of lithium deposition potential (LDP) in the 1C charge process of (a) the fresh PHEV cell at diferent temperatures, (b–d) aged PHEV cells after diferent number of cycles at various temperatures: (b) 10 °C, (c) 20 °C and (d) 30 °C.

## 3. Results & discussion

## 3.1. Optimal temperature for cell life

Fig. 1a plots the retention of cell capacity versus the equivalent full cycle (EFC) of the PHEV cell at 1C charge in di<sup>f</sup>erent temperatures. The EFC is de<sup>fi</sup>ned as the ratio of total discharged capacity to the nominal cell capacity. The simulation results show that the cell has the longest cycle life at ∼20 °C. Fig. 1b plots the aging rate of the cell, defined as the total capacity loss (in %) per EFC and plotted in logarithmic scale against the reciprocal temperature (1/T). We can learn that the logarithm of aging rate is linear with respect to 1/T, indicating that the aging rate follows the Arrhenius law. The change of slope $\mathrm { a t } \sim 2 0 ^ { \circ } \mathrm { C }$ denotes a change of activation energy. These results are in good agreement with the experimental results reported in the literature [20,21], revealing that the present model well captures the key features of temperature e<sup>f</sup>ects on cell aging.

It can also be noted from Fig. 1a that the capacity retention curves at $\mathrm { ~ T ~ } > \ 2 0 ^ { \circ } \mathrm { { C } }$ have a square-root dependence on the EFC, a feature wellrecognized as SEI-dominated aging. ${ \mathrm { A t ~ T } } < 2 0 { ^ \circ } { \mathrm { C } } ,$ , the capacity retention curve still depends on the square-root of EFC at the beginning of cycling, but exhibits a rapid capacity drop after a certain number of cycles. This transition to nonlinear capacity fade is attributed to the onset of lithium plating, as elaborated in our previous work [27]. Fig. 2a breaks the total capacity loss at the end of life (i.e. 80% capacity retention) to the capacity loss caused by SEI growth and by lithium plating, respectively. We can learn that lithium plating occurs only in the cases at $\mathrm { ~ T ~ } < 2 0 ^ { \circ } \mathrm { C } _ { \mathrm { i } }$ , and the fraction of capacity loss due to lithium plating increases with the decrease of temperature.

Fig. 2b presents the evolution of capacity loss induced by SEI growth over the cycling process. In each case, SEI grows fast at the beginning and gradually slows down, which is because the SEI growth rate is greatly a<sup>f</sup>ected by the rate of EC di<sup>f</sup>usion across the surface <sup>fi</sup>lm and therefore is inversely proportional to <sup>fi</sup>lm thickness $\left( \operatorname { E q . } \left( 5 \right) \right)$ . As the EC di<sup>f</sup>usivity increases with temperature, the capacity loss induced by SEI growth increases with temperature, leading to a rise of aging rate with temperature ${ \sf a t } \mathrm { ~ T ~ } > 2 0 ^ { \circ } \mathrm { C } \left( \mathrm { F i g . \ 1 b } \right)$

The evolution of total capacity loss induced by lithium plating is plotted in Fig. 2c. It can be learned that lithium plating appears after a certain number of cycles in the cases at $\mathrm { ~ T ~ } < 2 0 { } ^ { \circ } \mathrm { C } .$ . The lower the temperature, the earlier the onset of lithium plating. As explained in our previous work [27], the onset of lithium plating is attributed to continuous growth of SEI, which reduces anode porosity and thus increases the electrolyte-phase overpotential in the anode. Once lithium plating occurs, the solid lithium metal deposited onto graphite surfaces further blocks the pores of the anode, leading to larger anode polarization and thus soaring of the lithium plating rate. This positive feedback e<sup>f</sup>ect results in an exponential rise of lithium plating amount and therefore a rapid decay of cell capacity.

Fig. 3a compares the lithium deposition potential (LDP) at the anode/separator interface in the 1C charge process of the fresh cell at di<sup>f</sup>erent temperatures. Fundamentally, LDP is a<sup>f</sup>ected by the rate capabilities of three processes: conduction and di<sup>f</sup>usion of Li<sup>+</sup> ions in the electrolyte, reaction at graphite surfaces, and di<sup>f</sup>usion of lithium in solid graphite particles. Key parameters governing these processes all

b

C

![](01-Yang-Wang-2018_images/770ea7084610ae1d27dd79d972ffb33de6fda5fdd34bd3684b04064d982a5229.jpg)

![](01-Yang-Wang-2018_images/85db4884b8fa5af02027720e152616469cd25afeee6be3649d12a2334c37daa5.jpg)

![](01-Yang-Wang-2018_images/017958b68c6b3b1502dcda95e21e5baad8c53f1bd9a332d11a0b25dc8914168c.jpg)

![](01-Yang-Wang-2018_images/28151e13d42402f35768b08b385eb8dc5aba33b9f15ccc7331e6dd4df97c17de.jpg)  
Fig. 4. Increase of optimal temperature with charging rate. (a&b) Capacity retention curves of the PHEV cell at di<sup>f</sup>erent temperatures with (a) 2C charge and (b) 3C charge. (c) Comparison of aging rate versus temperature for the PHEV cell with di<sup>f</sup>erent charge rates. The optimal temperature with the lowest aging rate increases from $\sim 2 0 ^ { \circ } \mathrm { C }$ at 1C charge to $3 5 ^ { \circ } \mathrm { C }$ at 2C charge and $4 5 ^ { \circ } \mathrm { C }$ at 3C charge. (d) Comparison of the evolutions of lithium deposition potential in the charging process of the fresh PHEV cell at di<sup>f</sup>erent charge rates and two di<sup>f</sup>erent temperatures.

depend highly on temperature. For instance, the exchange current density of graphite is reported to have an activation energy about 68 kJ/mol [33], indicating a 6x increase from $2 5 ^ { \circ } \mathrm { C }$ to $4 5 ^ { \circ } \mathrm { C }$ or a 7x drop from 25 °C to $5 ^ { \circ } \mathrm { C }$ . The decrease of temperature, therefore, pushes the LDP towards the tipping point of 0 V (Fig. 3a), below which lithium plating would be triggered. As the LDP keeps decreasing in the cycling process due to continuous drop of anode porosity (Fig. 3b–d), lithium plating starts earlier at lower temperatures. As shown in Fig. 3b–d, the LDP drops to 0 V after only 400 cycles in $1 0 ~ ^ { \circ } \mathrm { C }$ (Fig. 3b), at the very end of cycling in $2 0 ^ { \circ } \mathbf { C } \left( \mathbf { F i g } . 3 \mathbf { c } \right)$ , and still well above 0 V at the end of life in $3 0 ~ ^ { \circ } \mathrm { C }$ (Fig. 3d), indicating that lithium plating can be mitigated and even eliminated by increasing cell temperature.

To sum up, the existence of an optimal temperature with the longest cycle life is a result of the competition between SEI growth and lithium plating. At high temperatures where lithium plating is eliminated, the aging rate is mainly a<sup>f</sup>ected by SEI growth, the rate of which increases with temperature. At low temperatures where lithium plating occurs, the decrease of temperature leads to earlier onset of lithium plating and hence to faster fade of cell capacity.

## 3.2. Increase of optimal temperature with charge rate

The e<sup>f</sup>ects of charge rate on the temperature-dependent aging behavior of the above PHEV cell are studied in this section. Fig. 4a and b presents the capacity retention curves of the above PHEV cell at 2C charge and 3C charge, respectively. Compared with the case of 1C charge (Fig. 1a), we can learn that the transition from linear to nonlinear aging, which signals the onset of lithium plating and occurs only at $\mathrm { ~ T ~ } < 2 0 { } ^ { \circ } \mathrm { C }$ with 1C charge, appears in higher temperatures at the increased charge rate. To show this behavior more clearly, we present in Fig. 5a and b the breakdown of total capacity loss induced by SEI growth and by lithium plating at the end of life (20% total capacity loss) for all the cases. Compared with the 1C case (Fig. 2a), the minimum temperature without lithium plating increases from $\sim 2 0 ~ ^ { \circ } \mathrm { C }$ at 1C charge to $\sim 4 0 ^ { \circ } \mathrm { C }$ at 2C charge and to > 50 °C at 3C charge.

The cases at $2 0 ~ ^ { \circ } \mathrm { C }$ and $3 5 ^ { \circ } \mathrm { C }$ are selected for detailed comparison to examine the impacts of charge rate on the onset of lithium plating. Fig. 4d compares the LDP in the charge process of the fresh cell at di<sup>f</sup>erent charge rates. We can learn that the increase of charge rate leads to much lower LDP and therefore to earlier onset of lithium plating as can be seen from Fig. 5c and d where the evolutions of total capacity loss due to SEI growth and lithium plating in the cycling process are plotted. For the cases at $2 0 ^ { \circ } \mathrm { C }$ (Fig. 5c), lithium plating starts at the very end of the cycling (∼3500 EFCs) with 1C charge, but appears after only 700 EFCs at 2C charge and after 200 EFCs at 3C charge. The onset of lithium plating results in rapid capacity decay and thus the cycle life at $2 0 ^ { \circ } \mathrm { C }$ drops signi<sup>fi</sup>cantly as the charge rate increases from 1C to 3C. When the temperature increases to 35 °C (Fig. 5d), the onset of lithium plating is postponed thanks to the elevation of LDP with the increase of temperature (Fig. 4d). The mitigation of lithium plating leads to longer cycle life at $3 5 ^ { \circ } \mathrm { C }$ than at $2 0 ^ { \circ } \mathrm { C }$ for the 2C and 3C cases, though SEI growth is faster at $3 5 ^ { \circ } \mathrm { C }$ than at $2 0 ^ { \circ } \mathbf { C } .$

C  
![](01-Yang-Wang-2018_images/436c1b380893d0b29264d9db28ea752cd46b1a836c5cbc41480c9cecb8bb741b.jpg)

![](01-Yang-Wang-2018_images/45ffbade5a599ecdf2de39f8cd8ea1189fca4a285c4d9d57121aecad30d95690.jpg)

![](01-Yang-Wang-2018_images/e917617023cfcaf706301e3ffa4bd8f4898a161b30d579c481791104a246b4ec.jpg)

![](01-Yang-Wang-2018_images/992c86ccb947dedeaec0cc162f9e32134b589ffb16afec0fa00d99c15995d324.jpg)  
Fig. 5. Increase of lithium plating induced aging with charging rate. (a&b) Breakdown of total capacity loss induced by SEI growth and by lithium plating at the end of life (20% capacity loss) for the PHEV cell charged at di<sup>f</sup>erent temperatures with (a) 2C charge and (b) 3C charge. (c&d) Evolutions of total capacity loss due to SEI growth and lithium plating for the PHEV cell at (c) 20 °C and (d) 35 °C with di<sup>f</sup>erent charge rates.

a  
b  
![](01-Yang-Wang-2018_images/804f5f7a51f84672ce65087b7bc2c3eda68ad210c324e47489e069dca9352432.jpg)

![](01-Yang-Wang-2018_images/25fdf72bd77c4df0f258914ac2b6df74b09ebeb745426da8f86c2551e20d2bbd.jpg)  
Fig. 6. Increase of optimal temperature with energy density. (a) Capacity retention curves of an EV cell cycled with 1C charge at di<sup>f</sup>erent temperatures. (b) Aging rate comparison of the EV cell with the baseline PHEV cell at 1C charge. The EV cell has 2x areal loading density of the PHEV cell, along with lower electrode porosity and smaller N-P ratio.

The aging rates of these cases at the three di<sup>f</sup>erent charge rates are compared in Fig. 4c. It is very interesting to note that the optimal temperature with the longest cycle life increases from $2 0 ^ { \circ } \mathrm { C }$ at 1C charge to $3 5 ^ { \circ } \mathrm { C }$ at 2C charge and $4 5 ^ { \circ } \mathrm { C }$ at 3C charge, indicating that the bene<sup>fi</sup>t of elevating temperature to mitigate lithium plating outpaced the negative impacts of accelerated SEI growth in the cases of higher charge rate. It is worth mentioning that the aging rate with 2C charge is even lower than that with 1C at temperatures $> 4 0 ^ { \circ } \mathrm { C }$ in Fig. 4c. This is because the aging rate is de<sup>fi</sup>ned as capacity loss per EFC. When this PHEV cell is charged with 1C or $2 \mathrm { C } \mathrm { a t } > 4 0 ^ { \circ } \mathrm { C } ,$ , SEI growth is the only aging mechanism and its rate depends mainly on time. If plotting capacity retention against time, all cases of di<sup>f</sup>erent charge rates would fall on the same curve if lithium plating does not occur, as shown in Fig. S2a, which is in accordance with the experimental data of Dahn's group [34]. As the time duration per EFC is shorter at a higher charge rate, cell life, in terms of EFCs, is thus longer at 2C charge than at 1C (Fig. S2b).

![](01-Yang-Wang-2018_images/3d42cc714702db4fe416afdc11287df5cf40f17574b0a900e284fb6f86a99d7a.jpg)

![](01-Yang-Wang-2018_images/1fe14a81973aaa8375d55803609359114c6cbe6fbd6235f8b318a2838c84d234.jpg)

d  
![](01-Yang-Wang-2018_images/03767ab361a4094e2a6e803e2ed2a518103583ee2f3dddca9a499a6acdbfb984.jpg)

![](01-Yang-Wang-2018_images/6f21293306327c9e134add2aee53e8eb18a266db58ebf5b68554b673259b8f26.jpg)  
Fig. 7. More serious lithium plating with the increase of energy density. (a&b) Evolutions of total capacity loss induced by (a) SEI growth and (b) lithium plating in the cycling process of the EV cell at di<sup>f</sup>erent temperatures with 1C charge. (c) Comparison of lithium deposition potential in the 1C charge process of the EV cell and PHEV cell at 20 °C and 35 °C. (d) Breakdown of total capacity loss at the end of life of the EV cell with 1C charge.

## 3.3. Increase of optimal temperature with energy density

The impacts of increasing energy density on the optimal temperature are similar to the impacts of increasing charge rate. Fig. 6a shows the capacity retention curves of a high energy EV cell with 1C charge in di<sup>f</sup>erent temperatures. The EV cell has 2x areal loading density of the PHEV cell, along with lower electrode porosity and smaller negative-topositive (N-P) ratio (see Table 1). The evolutions of the total capacity loss induced by SEI growth and by lithium plating are shown in Fig. 7a and b. Comparing Fig. 7 with Fig. 2, it can be drawn that the increase of areal loading (anode thickness) has negligible impacts on the rate of SEI growth (Fig. 7a vs Fig. 2b) but leads to much earlier onset of lithium plating (Fig. 7b vs Fig. 2c). This can be attributed to the larger electrolyte transport resistance in the thick anode, leading to much lower LDP at the anode/separator interface in the EV cell than that of the PHEV cell (Fig. 7c). We shall note that lithium plating occurs even at 50 °C in the EV cell (Fig. 7d).

The aging rate of the EV cell at 1C charge is compared with the baseline PHEV cell in Fig. 6b. Though the rate of SEI growth is similar in these two cells, the higher rate of lithium plating in the EV cell leads to faster cell degradation. As such, the optimal temperature with the lowest aging rate increases to $\sim 3 5 ^ { \circ } \mathrm { C }$ for the EV cell at 1C charge. It is worth mentioning that these simulation results are in agreement with the recent experimental studies of high energy cells. Winter's group [25] reported that the cycle life of a high energy cell (anode thickness 74–80 μm) at 45 °C is 3x of that at $2 5 ^ { \circ } \mathrm { C }$ with 1C charge (Fig. S1b). Jossen's group [26] also found that a high energy cell with 77-μm thick anode had stable capacity retention at 40 °C (5% capacity loss after 400 cycles), whereas the same cells lost 30% capacity in only 250–400 cy cles at 25 °C (Fig. S1c).

## 3.4. Directions for temperature-independent fast and healthy charging

Fig. 8a presents a summary of the aging rate vs reciprocal temperature of the above PHEV cell at various charge rates when reaching 20% total capacity loss; a contour plot in Fig. 8b shows the dependence of cell life on temperature and charge rate. Similar plots for the EV cell are given in Fig. 8c and d. As discussed above, the overall aging rate depends on the competition between SEI growth and lithium plating and therefore is a strong function of temperature and charge rate. In general, if the charge rate is rather low (e.g. overnight charging of an EV at home), lithium plating would not be a big issue and hence it would be bene<sup>fi</sup>cial to charge the battery at lower temperatures to alleviate SEI growth. If rapid charging is demanded, however, it would be better to charge at higher temperatures in order to mitigate lithium plating. It should be noted that EVs are charged in a wide range of ambient temperatures as they operate in various regions and weather conditions. As such, even with fast charging stations available, the charge rate of an EV shall be strictly restricted in order to prevent lithium plating and maximize cell life. For instance, if we want to achieve a cycle life of at least 1000 EFCs, the charge rate of the PHEV cell (Fig. 8a) in this work shall be lower than 2C at 15 °C, 3C at 25 °C and 4C at 35 °C. For the EV cell (Fig. 8c), the charge rate shall be further reduced to ∼1.5C along with restricting the charging temperature to a narrow window of 30–45 °C if we want to achieve fast charging while maintaining a life of 1000 EFCs simultaneously. Clearly, the charging rate shall be de<sup>fi</sup>ned as a function of temperature and energy density for the sake of cell life. Indeed, a very recent work from Idaho National Lab [35] revealed, based on statistical analysis of on-road data from Nissan Leafs operated as taxi cabs in New York City, that the total charging time increased signi<sup>fi</sup>cantly with the decrease of temperature. For taxi drivers, every minute spent on charging is a minute they are not making money; thus charging at high temperatures to reduce total charging time would be extremely appealing to them.

C  
b  
![](01-Yang-Wang-2018_images/6d3ed548201bc4a5a66a93123d31d1ba38dda51db9c48f5e605dbfcb9f3bb7c0.jpg)

![](01-Yang-Wang-2018_images/9d3bd6cfd6865588a6f0eab3ce2b66917aa24cfa09749023e24ec20680ab469b.jpg)

d  
![](01-Yang-Wang-2018_images/d509df821cd3e79de5d1ef5f596235004a660704434e2b740e95bd02cc158414.jpg)

![](01-Yang-Wang-2018_images/3e0650a5dbe12334ce37b3a5a490bac7550e0bc845fbce546e68fff3b797b4c1.jpg)  
Fig. 8. Temperature e<sup>f</sup>ects on the trilema among fast charging, energy density and cycle life. (a&c) Comparison of aging rate vs temperature for the (a) PHEV cell and (c) EV cell at various charge rates. (b&d) Contour plots showing the impacts of charge rate and temperature on the cycle life of (b) the PHEV cell and (d) the EV cell. The aging rate and cycle life are de<sup>fi</sup>ned at 20% total capacity loss.

Most recently, our group presented a cell structure that can be actively controlled to achieve lithium plating free (LPF) charging in any ambient temperatures [36]. The key idea is to charge a battery alway around its optimal temperature. A rapid heating step is added to heat the cell to its optimal temperature prior to charging. As such, charging from di<sup>f</sup>erent ambient temperatures is transformed to charging at a pre-de<sup>fi</sup>ned optimal temperature that o<sup>f</sup>ers the best cycle life. Rapid heating is essential for this LPF fast charging as the total charging time including the heating step is limited to 10–15 min. Conventional battery heating methods using external heating devices are hindered by the intrinsic con<sup>fl</sup>ict between heating speed and uniformity (i.e. high heating rate leads to localized overheating near cell surfaces) [37] and hence their heating speed is typically $< 1 ^ { \circ } \mathrm { C } / \mathrm { m i n } .$ , which cannot ful<sup>fi</sup>ll the need for fast charging. The LPF cell structure has an internal heating element, a thin nickel foil, embedded inside the cell, which creates immense and uniform heat and enables rapid heating at ∼ 1 °C/sec. As demonstrated in our recent work [36], a LPF cell with an energy density of 170 Wh/kg, similar to the PHEV cell simulated in this work, can be charged from 0% to 80% SOC in ∼15 min even $\mathrm { a t } \ - 5 0 ^ { \circ } \mathrm { C } .$ . Furthermore. this LPF cell sustained 4500 cycles of 3.5C charging at 0 C before losing 20% capacity, whereas an identical cell without the preheating step only survived 50 cycles at the same condition.

The LPF cell structure along with the heated charging method completely removes the restrictions of temperature on battery charging; thereby it o<sup>f</sup>ers a new direction for fast and healthy charging of high energy cells. We can learn from the above analysis that raising the charging temperature is an e<sup>f</sup>ective approach to mitigate lithium plating. For future high energy EV cells with much thicker and denser anodes, a feasible approach to achieve fast charging without lithium plating is to further increase the charging temperature (e.g. to ∼60 °C or even higher). To that end, a critical issue to resolve is to improve electrolyte stability and reduce SEI growth rate at high temperatures. It is worth mentioning that today's commercial electrolytes (LiPF in ECbased solvent) are mostly optimized for operation in a wide range of temperatures which encompass various trade-o<sup>f</sup>s. With the LPF cell structure and heated charging method, the cell is charged always around a pre-de<sup>fi</sup>ned temperature; thus we only need to focus on optimizing electrolyte performance around a single temperature. We are now partnering with the U.S. Department of Energy to develop an extreme fast charging technology based on this new cell structure and the heated charging method. Speci<sup>fi</sup>cally, we shall achieve 6C charging of > 220 Wh/kg cells (based on NMC622 or 811 cathode and graphite anode) with a life of > 1000 cycles.

## 4. Conclusions

We have presented a numerical study of the impacts of fast charging and energy density on cycle life of LiBs. The model well captures the temperature-dependent aging behavior, more speci<sup>fi</sup>cally, the existence of an optimal temperature for cycle life. The optimal temperature is found to be ascribed to the competition between SEI growth and lithium plating and therefore is a strong function of charge rate and energy density. Furthermore, it is revealed that the optimal temperature would increase with the increase of charge rate and/or energy density. Raising the charging temperature therefore would be an ef fective approach to mitigating lithium plating and enabling robust fast charging of EV batteries.

## Acknowledgements

Financial support by Pennsylvania Department of Environmental Protection (grant# 4100068680-1) and U.S. Department of Energy's O<sup>fi</sup>ce of Energy E<sup>fi</sup>ciency and Renewable Energy (EERE) under Award Number DE-EE0008355 is gratefully acknowledged.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https:// doi.org/10.1016/j.jpowsour.2018.09.069.

## References

[1] C.Y. Wang, G. Zhang, S. Ge, T. Xu, Y. Ji, X.G. Yang, Y. Leng, Nature 529 (2016) 515–518.

[2] S. Ahmed, I. Bloom, A.N. Jansen, T. Tanim, E.J. Dufek, et al., J. Power Sources 367 (2017) 250–262

[3] Z. Li, J. Huang, B. Yann Liaw, V. Metzler, J. Zhang, J. Power Sources 254 (2014) 168–182.

[4] T. Waldmann, B.-I. Hogg, M. Wohlfahrt-Mehrens, J. Power Sources 384 (2018) 107–124.

[5] R. Chandrasekaran, J. Power Sources 271 (2014) 622–632.

[6] N. Legrand, B. Knosp, P. Desprez, F. Lapicque, S. Raël, J. Power Sources 245 (2014) 208–216.

[7] S. Tippmann, D. Walper, L. Balboa, B. Spier, W.G. Bessler, J. Power Sources 252 (2014) 305–316.

[8] M.F. Hasan, C.-F. Chen, C.E. Sha<sup>f</sup>er, P.P. Mukherjee, J. Electrochem. Soc. 162 (2015)A1382–A1395

[9] L. Somerville, J. Bareño, S. Trask, P. Jennings, A. McGordon, C. Lyness, I. Bloom, J. Power Sources 335 (2016).189–196

[10] S.S. Zhang, J. Power Sources 161 (2006) 1385–1391.

[11] T. Waldmann, M. Kasper, M. Wohlfahrt-Mehrens, Electrochim. Acta 178 (2015) 525–532.

[12] P. Keil, A. Jossen, J. Energy Storage 6 (2016) 125–141.

[13] E. Grimsmann, T. Gerbert. F. Brauchle. A. Gruhle, J. Parisi, M. Knipper, J. Power Sources 365 (2017) 12–16.

[14] C. Liu, L. Liu J. Electrochem, Soc, 164 (2017) E3254–E3264

[15] J. Landesfeind. J. Hattendorff A. Ehrl. W.A. Wall. H.A. Gasteiger. J. Electrochem

Soc. 163 (2016) A1373–A1387.

[16] K.G. Gallagher, S.E. Trask, C. Bauer, T. Woehrle, S.F. Lux, M. Tschech, P. Lamp, B.J. Polzin, S. Ha, B. Long, Q. Wu, W. Lu, D.W. Dees, A.N. Jansen, J. Electrochem. Soc.163 (2016) A138-A149

[17] S. Malifarge, B. Delobel, C. Delacourt, J. Electrochem. Soc. 165 (2018) A1275-A1287

[18] F.B. Spingler, W. Wittmann, J. Sturm, B. Rieger, A. Jossen, J. Power Sources 393 (2018) 152–160.

[19] B.Y. Liaw, E.P. Roth, R.G. Jungst, G. Nagasubramanian, H.L. Case, D.H. Doughty, J. Power Sources 119–121 (2003) 874–886.

[20] T. Waldmann, M. Wilka, M. Kasper, M. Fleischhammer, M. Wohlfahrt-Mehrens, J. Power Sources 262 (2014) 129–135.

[21] M. Schimpe, M.E. von Kuepach, M. Naumann, H.C. Hesse, K. Smith, A. Jossen, J. Electrochem, Soc, 165 (2018) A181–A193.

[22] M. Ecker, P. Shafiei Sabet, D.U. Sauer, Appl. Energy 206 (2017) 934–946.

[23] B.P. Matadi, S. Geniès, A. Delaille, C. Chabrol, E. de Vito, M. Bardet, J.-F. Martin, L. Daniel. Y. Bultel, J. Electrochem. Soc. 164 (2017) A2374–A2389.

[24] T. Matsuda, M. Myojin, K. Ando, D. Imamura, ECS Trans. 64 (2015) 69–75.

[25] A. Friesen, X. Mönnigho<sup>f</sup>, M. Börner, J. Haetge, F.M. Schappacher, M. Winter, J. Power Sources 342 (2017) 88–97.

[26] B. Rieger, S.F. Schuster, S.V. Erhard, P.J. Osswald, A. Rheinfeld, C. Willmann, A. Jossen, J. Energy Storage 8 (2016) 1–5.

[27] X.G. Yang, Y. Leng, G. Zhang, S. Ge, C.Y. Wang, J. Power Sources 360 (2017) 28–40.

[28] X.G. Yang, S. Ge, T. Liu, Y. Leng, C.Y. Wang, J. Power Sources 395 (2018) 251–261.

[29] Y. Ji, Y. Zhang, C.Y. Wang, J. Electrochem. Soc. 160 (2013) A636–A649

[30] X.G. Yang, C. Bauer, C.Y. Wang, J. Power Sources 327 (2016) 414–422.

[31] W. Fang, O.J. Kwon, C.Y. Wang, Int. J. Energy Res. 34 (2010) 107–115.

[32] L.O. Valøen, J.N. Reimers, J. Electrochem. Soc. 152 (2005) A882–A891.

[33] T.R. Jow, M.B. Marx, J.L. Allen, J. Electrochem. Soc. 159 (2012) A604–A612.

[34] J.C. Burns, D.A. Stevens, J.R. Dahn, J. Electrochem. Soc. 162 (2015) A959–A964.

[35] Y. Motoaki, W. Yi, S. Salisbury, Energy Pol. 122 (2018) 162–168.

[36] X.G. Yang, G. Zhang, S. Ge, C.Y. Wang, Proc. Natl. Acad. Sci. Unit. States Am. 115 (2018) 7266–7271.

[37] X.G. Yang, T. Liu, C.Y. Wang, J. Power Sources 342 (2017) 598–604.

## Nomenclature

a: speci<sup>fi</sup>c surface area, m<sup>−1</sup> c: concentration, mol m<sup>−3</sup> D : di<sup>f</sup>usion coe<sup>fi</sup>cient of ethylene carbonate, m<sup>2</sup> s<sup>−1</sup> E : activation energy, J mol<sup>−1</sup> F: Faraday constant, 96487 C mol<sup>−1</sup> i : exchange current density, A m −2 j: volumetric current density, A m − k: kinetic rate constant, m s<sup>−1</sup> R: universal gas constant, 8.314 J mol<sup>−1</sup> K<sup>−1</sup> t: time, s T: temperature, K

## Greek

α: charge transfer coeficient ε: porosity δ: film thickness, m η: overpotential, V

## Subscripts

gr: graphite Li: lithium EC: ethylene carbonate SEI: solid electrolyte interphase tot: total

## Abbreviations

EC: ethylene carbonate ECT: electrochemical-thermal EFC: equivalent full cycle EV: electric vehicle LDP: lithium depositino potential LIB: lithium ion battery LPF: lithium plating free PHEV: plug-in hybrid electric vehicle SEI: solid-electrolyte-interphase SOC: state of charge