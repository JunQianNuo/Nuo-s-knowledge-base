---
raw_title: 03-Stadler-2022
subject: 数学建模-策联杯A题
source: "148271_TT_infotext.pdf"
status: mineru解析
parser: mineru
topics:
  - 试验设计
  - 循环老化
  - 交互项
  - LOOCV
---

This is the author's version (manuscript) of the work that was accepted for publication in Journal of Power Sources The Version of Record is available online at https://doi.org/10.1016/j.jpowsour.2021.230952

# Investigation and modelling of cyclic aging using a design of experiment with automotive grade graphite/NMC lithium-ion cells

Authors: Jochen Stadler<sup>a,b\*</sup>, Carsten Krupp<sup>a</sup>, Madeleine Ecker<sup>a</sup>, Jochen Bandlow<sup>a</sup>, Bernd Spier<sup>a</sup>, and Arnulf Latz<sup>b,c</sup>

<sup>a</sup>Mercedes-Benz AG, Mercedesstr. 120, 70372 Stuttgart, Germany

<sup>b</sup>Institute of Electrochemistry, Ulm University, Albert-Einstein-Allee 47, 89081 Ulm, Germany

<sup>c</sup>Helmholtz Institute for Electrochemical Energy Storage (HIU), Helmholtzstraße 11, 89081 Ulm, Germany \*Corresponding author

Highlights:

 Extensive cyclic aging matrix with large format lithium-ion cells

 Testing with realistic cycling profiles

 Main aging factors unraveled by design of experiment approach

 Model of capacity fade due to cyclic aging

 Incorporation of interdependencies between aging factors

## Abstract:

60 large format automotive grade lithium-ion pouch cells with graphite/NMC chemistry are tested following a design of experiment (DoE) approach. Realistic driving profiles resembling a plugin-hybrid electric vehicle are used with variation of five aging factors: temperature, maximum and minimum state of charge, charging power, and the ratio of charge depleting vs. charge sustaining cycling. Capacity fade is cleaned from calendar aging and multivariate stepwise linear regression is used to parameterize an empirical model of cyclic capacity fade. Temperature and the ratio between charge depleting and charge sustaining cycling show the biggest impact on cyclic aging, whereas charging power has little effect in the chosen range of aging conditions.

The importance of considering interdependencies between aging factors for modeling is pointed out, major interdependencies are found between the factors temperature and charging power and between minimum and maximum state of charge.

Leave-one-out cross validation is used to show the capability of the comparatively simple model approach to predict cyclic aging within the tested range.

<table><tr><td>Keywords:</td></tr><tr><td>Cyclic aging</td></tr><tr><td>Capacity fade</td></tr><tr><td>Design of experiment</td></tr><tr><td>Aging model</td></tr><tr><td></td></tr></table>

## 1. Introduction

Lithium-ion cells are subject to a variety of aging mechanisms, leading to capacity and power fade [1,2]. With a lifetime of only a few years, this degradation is mostly accepted as an unpleasant necessity in consumer electronics. In the automotive context, however, batteries are responsible for the greatest cost in production and thus, premature degradation can get very expensive.

Therefore, it is utterly important to understand the effect of different operating conditions on degradation and to provide tools for accurate lifetime prediction to ensure a well guided development.

Calendar aging, stemming from side reactions that take place during storage, is considered to depend on the state of charge and temperature [3–7] and can be modelled accurately with semi-empiric equations that combine the knowledge of underlying physical processes with data driven parameterization [5,7,8]. For cyclic aging, which is related to operating the battery, there is less consensus in the academic field about the most important influence factors and their effect. While temperature is often reported to show the best lifetime at around $30 \%$ [9,10], and a higher depth of discharge is often contributed with greater volume expansion of active material particles, which leads to mechanical degradation [11,12], the case is not so clear for State of Charge (SoC) endpoints and currents.

The effect of charge and discharge current variation is diversely reported, ranging from significant to not observable, while most publications find at least a small influence of either charging or discharging current rate. Findings depend strongly on the used cycling sequence, with differences between constant current cycling and cycling with driving profiles that resemble a more realistic usage as well as cell chemistry and cell design. [13–16]

For lifetime modelling, one-factor-at-a-time measurements, where influence factors are varied individually, are often used to isolate the influence factors' effects. Lifetime models can then be parameterized as the superposition of the single factors' effects [16,17]. However, experimental effort grows exponentially with an increasing amount of investigated influence factors and, additionally, the interplay between the influence factors is not considered.

Here, the approach of “design of experiment (DoE) can help grasp the main effects and interactions in a complex multi-dimensional problem. A DoE is used in various fields of engineering for optimization [18] and has also found its way into the field of lithium-ion battery development. Rynne, Dubarry, et al. described how a DoE can be set up by example of optimizing the electrode formulation [19].

For estimation of battery aging where accelerated tests can still easily run for 1-3 years and are very costly the number of tests is very restricted. Using a DoE can help identify and describe the effect of the most significant influence factors on cyclic aging and their interdependencies with minimized effort.

Prochazka et al. have used a DoE for identification of aging factors on lab scale lithium-ion cells with two different cathode chemistries [20]. Later, Su et al. used commercially available 18650 cells to screen eight aging factors for their influence and presented a linear aging model [21]. Both have shown the benefits of the DoE in narrowing down the multidimensional problem of cell aging to the most relevant factors. An approach for aging prediction was presented by Dubarry et al., who modelled a continuous aging rate with a second order regression model including interaction terms based on a DoE and detected a time<sup>0.75</sup> relationship for both calendar and cyclic aging under constant currents [22].

In this work, we present an exhaustive test matrix based on a DoE with 62 automotive grade lithium-ion pouch cells that was planned to investigate cyclic aging by using power profiles that are closely related to real world operation. By adjusting measurement data for calendar aging, we are able to seperately analyze the cyclic influence of several relevant factors. We submit a model capable of predicting the cyclic aging trend provoked by certain operating conditions. This can be the basis for a combined calendar and cyclic lifetime prediction model covering a great variance of usage profiles.

## 2. Experimental

## Test setup

62 Lithium-ion pouch bag cells with a nominal capacity of 43 Ah, graphite anode, and a blended cathode of $\mathsf { L i } ( \mathsf { N i } _ { 0 . 6 } \mathsf { M n } _ { 0 . 2 } \mathsf { C o } _ { 0 . 2 } ) \mathsf { O } _ { 2 }$ and $\mathsf { L i } ( \mathsf { N i } _ { 1 / 3 } \mathsf { M n } _ { 1 / 3 } \mathsf { C o } _ { 1 / 3 } ) \mathsf { O } _ { 2 }$ were used.

During the experiment, the cells were clamped in steel-jigs with a constant force of about 1.1kN, ensured with springs. This is similar to the initial compression force during battery-module construction. At the beginning of test, the cells had a state of charge of 75 %.

## Design of Experiment

Five main aging factors have been identified by expert opinion and literature as relevant influencing factors for cyclic aging and were investigated: temperature, $S o C _ { m i n } , S o C _ { m a x } ,$ charging power, and the ratio of energy throughput between micro- and macrocycles, from now on referred to as $E V _ { r a t i o }$

A Central-Composite Design (CCD) was used, where the five factors are varied relative to a central point in two levels, each to larger and smaller values. For three factors, exemplarily shown in Fig 1a for temperature, $S o C _ { m a x } ,$ , and charging power, the resulting test matrix can be visualized as a cube of the test points. Thus, each factor has a total of five different levels of variation specified in 0 that can be normed in a range from -1 to 1.

![](03-Stadler-2022_images/cc8f191308cfcaa1f127bfbb13bd4fb26892d7da99ab364cc0424de4f69fa993.jpg)

![](03-Stadler-2022_images/a851d32f011a9a12c9758f9918850c0791c7f8126a04b04daced55c200fa8bba.jpg)  
Figure 1 a) Schematic of the test matrix when reduced to three factors. Every factor is varied on five levels. Starting with the central point, all factors a varied in two directions, normed to -1 to 1. The outermost points are the star-points at ±1. For the cube points, all factors are varied on their levels ±0 simultaneously. b) Order of the test procedure. c) SoC and Power-signal of the cycling sequence. Charging power and $S o C _ { m a x }$ are varied in interval I. interval II, an EV-profile is used for discharging to $S o C _ { m i n } .$ Afterwards, an HEV profile is repeated in interval III until a specified ratio of energy throughp between EV- and HEV-cycling is reached.

The outermost star points are special, as only the value of the corresponding factor is changed relative to the center point, whereas at the cube points several factors are varied simultaneously. For each factor, a one-factor-at-time (OFAT) series containing the star- and center-points can show the isolated effect of one factor, whereas the cube points are particularly important to describe interaction effects between different factors during the model-building.

This results in a five level, half fractional experiment covering five factors. The design of the test matrix was created with the statistics software Minitab.

Table 1: Levels for each factor that are tested as they are considered important for application. The model is expected to have good predictive capabilities in this range.

<table><tr><td>Factor</td><td>Star -1</td><td>Cube -0.5</td><td>Center 0</td><td>Cube +0.5</td><td>Star +1</td></tr><tr><td>Temp / °C</td><td>11</td><td>21</td><td>28</td><td>41</td><td>50</td></tr><tr><td> $P_{CH}$  / W</td><td>8</td><td>72</td><td>136</td><td>200</td><td>264</td></tr><tr><td> $SoC_{min}$  / %</td><td>21</td><td>25</td><td>29</td><td>33</td><td>37</td></tr><tr><td> $SoC_{max}$  / %</td><td>81</td><td>85</td><td>90</td><td>95</td><td>100</td></tr><tr><td> $EV_{ratio}$  / %</td><td>20</td><td>40</td><td>60</td><td>80</td><td>100</td></tr></table>

The cells were tested with constant aging conditions on 27 different variations according to the CCD as listed in Table 2. Cycling sequences consisting of realistic driving power profiles were alternated with a reference parameter test (RPT) to keep track of capacity and resistance. As the cells are used in a pluginhybrid electric vehicle (PHEV), the power profiles used for cycling were designed accordingly. Additionally, two cells were tested for calendar aging at 50 % SoC and $3 0 ^ { \circ } \mathsf { C }$

Table 2: Factor levels of experimental aging conditions as measured, rounded to whole numbers. Minimum and maximum level of each factor are bold.

<table><tr><td>Test-No.</td><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td><td>16</td><td>17</td><td>18</td><td>19</td><td>20</td><td>21</td><td>22</td><td>23</td><td>24</td><td>25</td><td>26</td><td>27</td></tr><tr><td rowspan="2">Temp</td><td rowspan="2">[C]</td><td colspan="16">Cube points</td><td colspan="10">Star points</td><td>Center</td></tr><tr><td>22</td><td>39</td><td>21</td><td>39</td><td>20</td><td>41</td><td>22</td><td>41</td><td>21</td><td>40</td><td>21</td><td>41</td><td>21</td><td>41</td><td>22</td><td>41</td><td>11</td><td>50</td><td>31</td><td>30</td><td>30</td><td>31</td><td>31</td><td>31</td><td>31</td><td>29</td><td>30</td></tr><tr><td> $P_{Ch}$ </td><td>[W]</td><td>72</td><td>72</td><td>72</td><td>72</td><td>72</td><td>72</td><td>72</td><td>72</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>200</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>136</td><td>8</td><td>264</td><td>136</td><td>136</td><td>136</td></tr><tr><td> $SoC_{min}$ </td><td>[%]</td><td>24</td><td>23</td><td>26</td><td>26</td><td>32</td><td>32</td><td>32</td><td>33</td><td>24</td><td>24</td><td>26</td><td>26</td><td>32</td><td>32</td><td>32</td><td>33</td><td>29</td><td>28</td><td>27</td><td>30</td><td>21</td><td>37</td><td>28</td><td>29</td><td>29</td><td>29</td><td>29</td></tr><tr><td> $SoC_{max}$ </td><td>[%]</td><td>86</td><td>85</td><td>96</td><td>95</td><td>86</td><td>86</td><td>96</td><td>95</td><td>86</td><td>86</td><td>96</td><td>95</td><td>86</td><td>86</td><td>94</td><td>95</td><td>92</td><td>89</td><td>81</td><td>100</td><td>90</td><td>91</td><td>90</td><td>90</td><td>90</td><td>91</td><td>90</td></tr><tr><td> $EV_{ratio}$ </td><td>[%]</td><td>80</td><td>40</td><td>40</td><td>80</td><td>40</td><td>80</td><td>80</td><td>40</td><td>40</td><td>80</td><td>80</td><td>40</td><td>80</td><td>40</td><td>40</td><td>80</td><td>60</td><td>60</td><td>60</td><td>60</td><td>60</td><td>60</td><td>60</td><td>60</td><td>20</td><td>100</td><td>60</td></tr></table>

## Cycling sequences

The cycling sequences can be divided into three phases, as shown in Figure 1b and $\complement ,$ in which the five factors were varied. Starting with phase I, the cell was loaded with a constant-power-constant-voltage protocol (CPCV), where the charging power $\mathsf { P } _ { \mathsf { C H } }$ and charging endpoint $S o C _ { m a x }$ are varied according to Table 2. The definition of the SoC-OCV curve was not changed along with cell aging and is disclosed in the supplementary information S.1. In Phase II, the cell was discharged to $S o C _ { m i n }$ using a charge depleting EV driving profile, which is equivalent to full electrically assisted driving. The required charge throughput Q<sub>DCH</sub> that is necessary to discharge from $S o C _ { m a x }$ to $S o C _ { m i n }$ was calculated for each cyclization sequence on the basis of the capacity $\mathsf { C } _ { \mathsf { a c t } }$ as determined in the last RPT:

$$
Q _ {D c h} = C _ {a c t} \cdot (S o C _ {m a x} - S o C _ {m i n})\tag{1}
$$

After $S o C _ { m i n }$ was reached, a charge sustaining HEV performance profile was used in Phase III. To vary the $E V _ { r a t i o , }$ , the HEV profile was repeated until the ratio of energy throughput in EV mode $\mathsf { E T P } _ { \mathsf { E V } }$ and energy throughput in HEV mode $\mathsf { E T P } _ { \mathsf { H E V } }$ reached the targeted value. The energy throughput due to charging $\mathsf { E T P } _ { \mathsf { C H } }$ was also considered part of the EV mode and thus also increases the $E V _ { r a t i o }$

$$
E V _ {r a t i o} = \frac {E T P _ {E V} + E T P _ {C H}}{E T P _ {E V} + E P T _ {C H} + E T P _ {H E V}}.\tag{2}
$$

Power-profiles for EV and HEV mode were derived from real usage. In their dynamic range, they are roughly comparable to the widely used WLTP test profiles, as, for example, described by Stroe et al. [23].

Within each sequence, Phases I-III of the cyclization were repeated for 14 days.

Variation of the temperature was achieved by testing the cells in climate chambers, which were set to constant temperatures according to the test plan.

## Reference-Parameter Test (RPT)

After completing a cycling sequence of 14 days, all cells were tempered to $2 5 ~ ^ { \circ } \mathsf { C }$ for the RPT, where capacity, resistance, and a 1/10 C discharge potential curve were measured to gain information on the aging process. The RPT utilized 1 C and $1 / 1 0 \textsf { C }$ currents between 4.2 V and 2.5 V to determine usable capacity $\mathsf { C } _ { \mathsf { C } / 1 0 }$ and ${ \mathsf { C } } _ { 1 { \mathsf { C } } } .$ Furthermore, 200 A discharge pulses were performed each after 1 h relaxation at 100 %, 75 %, 50 %, and 25 % SoC to determine the 10 s resistance $\mathsf { R } _ { 1 0 \mathfrak { s } }$ <sub>s</sub>.

$$
R _ {1 0 s} = \frac {U _ {O C , 0 s} - U _ {1 0 s}}{I}\tag{3}
$$

The detailed test procedure of the RPT is available in the appendix S.2.

## Repeatability

For each of the 27 factor combinations, two cells were tested to check for reproducibility. The center point was even repeated 8 times. More repetitions would have been desirable for all test points, but were not feasible considering the enormous effort and cost.

## Modelling

## Data preparation

1/10 C capacity and $\mathsf { R } _ { 1 0 s }$ inner resistance trends along with the corresponding test conditions are shown in Figure 2a.

Overall, the measurement data shows very uniform and continuous aging trends and only few outlier points. A linear to root-shaped behavior as function of cumulative charge throughput (CTP) can be recognized.

Individual cells, depicted in Figure 2, show a comparatively strong and sudden drop in capacity (tests 4, 11, 18, 20), which is paired with a sharp increase in the 10s resistance. This behavior, often referred to as nonlinear aging [9], can have many causes, like accelerated loss of cyclable lithium, electrolyte consumption, electrode dry-out, pore clogging, and plating, most of which are closely related [9,14,24– 26]. However, tests 4, 18 and 20 clearly show that cells tested with the same conditions do not exhibit the same nonlinear aging behavior reproducibly. Therefore, aging processes that induce strong dispersion must be assumed. Our modelling approach of cyclic aging behavior correlates a specific aging trend with the respective aging conditions. Nonlinear aging behavior cannot be predicted with this simplistic model, and is therefore excluded. A detailed analysis of the root causes as well as post-mortem investigations will follow in future work. Along with a few outliers, excluded data points are marked with the symbol x in Figure 2.

The inner resistance $\mathsf { R } _ { 1 0 s }$ is also not used for modelling, as there seems to be no significant changes within the continuous aging trends apart from the previously mentioned sharp increase, which correlates to temperatures of $40 \ ^ { \circ } \mathsf { C }$ or higher.

We focus on modeling of the 1/10 C-capacity, as it is more independent from resistance effects. However, the chosen approach is empirical and thus flexible, and can be used analogously for additional characteristics like 1 C capacity.

![](03-Stadler-2022_images/8bcb8a7fe446332d0c34eb3d1791d24b01f8e4c28ce8d0e85c86b69f9da9a9b0.jpg)

![](03-Stadler-2022_images/401bbbe9df8b4e830efd343eb58d6ac682da83798e8e5854d9f8a5fb6946238d.jpg)  
Figure 2a) Measured 1/10 C capacity trends relative to BOL. b) Measured inner resistance trends relative to BOL. At high temperatures, a sudden increase at 120-150 kAh is observed  
The dashed line resembles the trend at the center point of the test matrix, test 27. Crosses indicate outlier points and points of nonlinear aging behavior, and are not considered for model building. A colored version of this figure can be found in the web-version of this article.

In order to evaluate the influence of stress factors on the pure cyclic aging, the aging curves are first cleaned from calendar aging, where a superposition of calendar and cyclic aging is assumed as applied in several studies. [13,15,17,27]

Calendar aging is described with a semi-empirical aging model of the form

$$
C _ {c a l} = 1 0 0 + p _ {1} * e x p (\frac {p _ {2}}{T + 2 7 3}) * e x p (p _ {3} * V) * t ^ {p _ {4}}\tag{4}
$$

similar to the model discussed by Ecker, Sarasketa-Zabala, and Hahn [4,5,7]. The model is parameterized on an additional calendar aging experiment on the same cell type, which – together with the model parameters – is described in more detail in the appendix S.3. The model approximates a t<sup>0.7</sup> behavior of calendar capacity degradation and fits the measured calendar aging at 50 % SoC and $3 0 ~ ^ { \circ } \mathsf { C }$ well.

For each cell, the SoC and temperature profile during cyclic testing is evaluated. The predicted calendar aging is calculated with a linear damage accumulation approach as discussed by Hahn et al. and Naumann et al. [5,28]. Calendar aging $\complement _ { \mathsf { c a l } }$ is then subtracted from the measured capacities $\complement _ { \mathsf { m e a s } }$ to achieve the purely cyclic capacity aging trends $\mathsf { C } _ { \mathsf { c y c , l o s s } }$

$$
C _ {c y c, l o s s} = C _ {m e a s} - C _ {c a l}\tag{5}
$$

To simplify data handling, all cyclic capacity loss trends are fitted and further inter- and extrapolated between 0 and 300 kAh:

$$
C _ {c y c, l o s s, i n t e r p} = p _ {5} - p _ {6} * C T P ^ {p _ {7}}\tag{6}
$$

## Model building

All models were built using Matlab 2016b with the curve optimization toolbox as well as the statistics and machine learning toolbox. Especially the integrated function stepwiselm for stepwise linear regression models was used.

For the quantitative, model-based evaluation, the $\mathsf { C } _ { \mathsf { c y c , l o s s , i n t e r p } } 1 / 1 0 \mathsf { C }$ capacity values are used, as the influence of the inner resistance effect on the capacity measurement is considered negligible at low currents.

According to Montgomery, a regression model with second-order terms can approximate measurement data with sufficient accuracy in a limited range and is therefore used for empirical modelling in DoE [29].

Here, a second-order response surface model is fitted, utilizing linear and quadratic terms of every influence factor $X _ { i }$ as well as two-way interaction terms between the individual factors $X _ { i }$ and $X _ { j }$ .

$$
C _ {c y c, l o s s @ C T P} = \gamma + \sum_ {i = 1} ^ {n} \beta_ {i, 1} X _ {i} + \sum_ {i = 1} ^ {n} \beta_ {i, 2} X _ {i} ^ {2} + \sum_ {i, j = i + 1} ^ {n} (\beta_ {i, j} X _ {i} \cdot X _ {j}))\tag{7}
$$

As illustrated above, the full model consists of five linear, five squared, and ten interaction terms. Thus, with information of 60 cells, an equation system consisting of the predictor matrix $\mathsf { X } ,$ the corresponding coefficient vector $\beta ,$ and the response matrix ${ \sf Y } ,$ which includes the respective capacity loss of the cell after a certain charge throughput, is created. Using multiple linear regressions, the equation system is approximated according to a smallest error square approach, minimizing the error e.

$$
\gamma + \vec {X} * \vec {\beta} + \vec {e} = \vec {Y}\tag{8}
$$

Since it can be expected that not all terms have a significant influence on cyclic cell aging, a selection is automatically made using a stepwise backwards selection, starting with the full equation and removing terms that do not have a statistically significant effect. The significance is evaluated based on a statistical test, where the probability of getting the experimental results under the assumption that the nullhypothesis (“The term has no significant effect”) is true, is reported as p-value [29]. Terms with a p-value bigger than 0.1 are automatically removed from the model equation step by step, while terms with a pvalue smaller than 0.05 are added.

In order to make the model easily interpretable, the levels of factors $\mathsf { X } _ { \mathrm { i } }$ are normalized to the interval -1 to 1. Hence, the fitted regression coefficient $\beta _ { \mathrm { i } }$ will directly unveil the effect of the corresponding term on capacity loss, due to the variation from center level at 0 to minimum level at -1 or maximum level at +1. [29,30]

$$
X _ {i, n o r m} = \frac {X - ((X _ {i , m a x} + X _ {i , m i n}) / 2)}{(X _ {i , m a x} - X _ {i , m i n}) / 2}\tag{9}
$$

## Predicting trends

Thus far, aging can only be predicted for different aging conditions at one specific charge throughput. To predict the continuous aging trend at certain conditions, four multivariate regression models are created at charge throughputs of 25, 75, 125, and 175 kAh. Based on these snapshot models, the continuous capacity loss trend related to specific aging conditions can be predicted by again fitting equation 0 xx to the obtained four snapshots of the capacity trend.

For validation purposes, the models are created with different shares of experimental data and afterwards tested on the remaining exclusive validation data.

## 3. Results and Discussion

## Capacity distribution at beginning of life

In order to check the significance of the aging experiment, the central point with its eight repetitions is examined in more detail first. Figure 3a shows the variation of 1/10 C capacity at beginning of life (BoL). A mean of 45.79 Ah with a standard deviation of 0.15 Ah (0.3 %), is observed.

In their study including the scattering of cell capacity, produced in series production, Schindler as well as Baumhoefer found a BoL capacity deviation of about 0.5 %, which is in the same order of magnitude. [31,32]

Figure 3b shows the deviation of each aging trend of the center point from the calculated mean of the eight cells. In particular, two of the eight cells exhibit a slightly weaker aging when looking at the relative capacity trends, while showing a slippage from a strong negative to a positive deviation from mean within the absolute capacities. This systematic deviation may origininate in these cells being tested in another climatic chamber and thus being subjected to slight deviations in the temperature profile. However, the deviation is considered to be small at 0.3 % relative to BoL 1/10 C capacity.

Overall, the low deviation allows the attribution of differences in the development of the aging trends to the influence of the tested factors when the effect is significantly bigger than 0.3 % of capacity relative to BoL.

![](03-Stadler-2022_images/b20dd59c87a69f1cf6dba6e8b9a17ec900c1f74f2ac85bc0f11e36b81b701fd7.jpg)

![](03-Stadler-2022_images/e03b24473e2d7bcb566a991db237b53ee8cd4eb6d2bb69e85830aeb28a6bee05.jpg)  
Figure 3 a) 1/10 C capacity distribution for all cells’ BoL with a mean of 45.8 Ah and a standard deviation of 0.15 Ah. b) Capacity distribution of the central point (8 cells) over aging. Left axis shows the 1/10 C capacity trend of the eight cells and their mean, right axis shows the deviation of every cell from the mean. Deviation is in the range of ± 0.2% for all eight cells during the entire experiment.

## Evaluation: Models at fixed charge throughput

For analysis of the effects of the different factors on capacity degradation, the regression model is created and can help visualize the trends. Using all the available data, we first create a single regression model to describe capacity loss at 175 kAh for detailed analysis. The model achieves an ${ \mathsf { R } } ^ { 2 }$ of 0.977 and an RMSE of 0.19 with the significant regression coefficients shown in Figure 4. This is already an impressive result for such a simple modelling approach, as it already describes the aging as a function of five different factors surprisingly accurate. Considering the number of coefficients, overfitting could be suspected at this point, but cross-validation will show that this is not the case.

![](03-Stadler-2022_images/54f1cb2788df535b2f86ecb3cb59c98c18690751cd11d2ea099f96a7c09afd11.jpg)  
Figure 4: Coefficients β and Intercept γ of model terms as fitted from equation (7). The intercept γ describes the relative capacity degradation of the center point at 175 kAh in percent compared to BoL, as factor levels were normalized to -1 to 1. The coefficients β describe the additional cyclic degradation of 1/10 C capacity compared to the center point at 175 kAh charge throughput, caused by raising the factor from its center level to its maximum level

In the following, we show the influences of the individual factors as well as identified interactions between factors. Figure 5 shows the trend of cyclic capacity loss of the center as well as the star points of each factor and can give a qualitative overview of the individual factors' influence. Also, the cyclic capacity loss at 175 kAh charge throughput is plotted for the different factors. The left column of Figure 5 shows the comparison between modelled influence of the five factors and the measurements at center and starpoints.

![](03-Stadler-2022_images/d7c23e728af700d04c5d7e623043f81ff8f525dfb77408c31c1ccc649177c865.jpg)  
Figure 5: Left: Relative capacity loss caused by cyclic aging (calendar aging is subtracted) for center- and star-points of each of the five factors. Starting with the central point (straight line; $3 1 ^ { \circ } \mathsf C , 2 8 \% 5 0 \mathsf C _ { \mathsf { m i n } } ,$ 90 % $\mathsf { S o C } _ { \mathsf { m a x } } ,$ 136 W and 60 % $\mathsf { E v } _ { \mathsf { r a t i o } } )$ , only the titled factor is varied between its minimum (dashed) and maximum level (dotted). Right: Measured relative cyclic capacity loss for center- and star-points at 175 kAh charge throughput, modelled aging behavior as dashed line. Extrapolation beyond the parameterized region should be avoided.

## Temperature

Figure 5a shows the influence of temperature. While the lowest aging can be observed at ${ 3 1 } ^ { \circ } \mathsf C ,$ , both a temperature increase to $5 0 ~ ^ { \circ } \mathsf { C }$ and decrease to ${ 1 1 ~ ^ { \circ } C }$ accelerate aging, where the high temperature is observed to have a more severe effect. This behavior was also observed in several studies and is considered to stem from superimposed aging processes with different temperature dependencies [1,16,20,21]. As the temperature rises, side reactions are presumed to be kinetically favored, following an Arrhenius relation [2,4,27,33,34]. Lower temperatures, on the other hand, are commonly associated with Lithium plating, which also leads to accelerated aging [35–38]. The presence of lithium plating, however, needs to be confirmed via post-mortem analysis.

All the cells cycled at $40 ^ { \circ } \mathsf { C }$ or higher exhibit a sudden and sharp increase in the internal resistance $\mathsf { R } _ { 1 0 s }$ (Fig 2b). This seems to precede the later drop in capacity and can probably be attributed to a drying out of electrolyte through accelerated side reactions such as SEI-growth or electrolyte decomposition at high temperatures. This needs further investigation and will be part of our future studies.

## Charging Power

With an increase in the charging power from 136 W to 264 W, a slight increase in aging can be observed. This may also be induced by lithium plating. Overall, however, the effect is comparatively small. As parts of the test are still running, it will be interesting to see whether the increased charging power will lead to accelerated lithium plating and, thus, a prior capacity drop.

In contrast, cyclic aging seems to be accelerated by the lowering of the charging power to 8 W when plotted over charge throughput. This is probably a remnant of calendar aging behavior, since the slow loading phases cause the cell to remain in the high SoC range longer and the charging phases take a disproportionately large share of the testing time. Before the adjustment for calendar aging, this effect is observed even more strongly, since the temporal part of aging is significantly more important due to the slowed cycle.

$\$ 00$ and $\$ 00$

The upper SoC limit seems to significantly accelerate aging at SoC levels above 90 %. This can be explained by the increased electrochemical side reactions at low anode and high cathode potentials. [39,40]

Surprisingly, degradation is also exacerbated by an increase in the lower SoC limit from 28 % to 37 %. This trend was also reported by Cordoba-Arenas et al. [16]. This could be due to the mean SoC, and thus the kinetics of electrochemical side reactions, being increased to a small extent. Interestingly, the often reported decrease of aging due to smaller DoD [2,33] seems to be outweighed. We suspect that different aging mechanisms correlated with the lithiation degree of the graphite and thus the potential around the chosen $\mathsf { S o C } _ { \mathsf { m i n } } .$ The graphite stage and the potential gradient at this point might have an influence on the degree of inhomogeneity of the aging across the anode surface. This will be part of future studies as well.

However, the decrease of $\mathsf { S o C } _ { \mathsf { m a x } }$ as well as $\mathsf { S o C } _ { \mathsf { m i n } }$ reduces the capacity loss just slightly. The comparison between modelled and measured influence in Figure 5d clearly highlights the weakness of this second order model approach, as the quadratic fit leads to a sharp increase in capacity loss by lowering the SoC, which cannot be explained with the experiments. However, this distortion happens mainly in the area outside of the measurements, leading to the conclusion that this simple approach can be used to interpolate within experimental conditions but may not be used for extrapolation.

## EV ratio

The proportion of EV cycles in the profile shows the greatest impact on cyclic aging. A high ratio of charge throughput accomplished through EV-cycles is observed to significantly accelerate capacity loss. Within the investigated factors, the $\mathsf { E V } _ { \mathsf { r a t i o } }$ is more complex to understand, as it influences several cycling parameters that are associated with cell ageing. First, the EV cycle features a charging to $\mathsf { S o C } _ { \mathsf { m a x } }$ and discharging to $\mathsf { S o C } _ { \mathsf { m i n } }$ with the EV power profile, whereas the HEV cycle accumulates its charge throughput in micro cycles around the lower SoC after an initial discharge through the EV cycle. [16]

With higher ratio of EV-cycles, the cell is therefore charged more frequently and more charge throughput is accumulated through cycles with higher DoD. This leads to more volume work of the active material particles, which is considered to contribute to aging through particle cracking, SEI cracking, or contact loss of particles. [11,12,41]

Second, with the diminishing proportion of micro cycles at low SoC in HEV profile, the mean of SoC over cycling is drastically increased from 34 % to 58 %. Increasing the time at high SoC is also observed to be damaging in the study of Benavente-Araoz et al. [39].

## Interactions

The strength of DoE is certainly that not only the effects of single factors are tested, but that the interactions between two factors can be investigated as well, as several factors are varied simultaneously at the cube points of the test matrix. Thus, the regression model introduces first order interaction terms that describe a two-way interaction. This means that the simultaneous change of two factors can either increase or decrease the aging effect in addition to the effects of the sole factors.

Through backward selection, some of the interaction terms were sorted out as not significant. The interaction terms containing $\mathsf { S o C } _ { \mathsf { m i n } }$ as first and Temperature, $\mathsf { E V } _ { \mathsf { r a t i o } }$ and charging power as second factor were deemed insignificant. Also, the interaction term between $\mathsf { S o C } _ { \mathsf { m a x } }$ and charging power, from now on noted as $\mathsf { S o C } _ { \mathsf { m a x } } .$ :charging power, is considered insignificant. From a physical perspective, one would expect this interaction to cause additional lithium plating, so the insignificance indicates that no substantial lithium plating occurred through simultaneous increase of charging power and $\mathsf { S o C } _ { \mathsf { m a x } }$ in the chosen range.

Figure 6 shows the relevant interaction terms that are included in the model, ordered from the most to the least damaging. The line plots show the effect of one factor on the capacity loss, while all other factors are kept constant. This is evaluated and displayed at three different levels of the interaction partner.

The term $\mathsf { S o C } _ { \mathsf { m a x } } { : } \mathsf { S o C } _ { \mathsf { m i n } } ,$ , depicted in Figure 6a, in has the strongest effect and a negative coefficient. This means that the capacity loss at low $\mathsf { S o C } _ { \mathsf { m i n } }$ and high $\mathsf { S o C } _ { \mathsf { m a x } }$ is even bigger than the superposition of the single effects. This is in accordance with literature, as a higher DoD is considered to be more damaging. At the same time, this term also assigns increased aging to increasing $\mathsf { S o C } _ { \mathsf { m i n } }$ and decreasing $\mathsf { S o C } _ { \mathsf { m a x } } ,$ which is unexpected behavior from a physical point of view. From the single factor effects we already know that increasing $\mathsf { S o C } _ { \mathsf { m i n } }$ is accelerating aging, despite of lowering the DoD. However, we have no evidence pointing to excessive aging at high $\mathsf { S o C } _ { \mathsf { m i n } }$ and low $\mathsf { S o C } _ { \mathsf { m a x } }$ . Until physical confirmation of this behavior, the model should not be used for predictions in this range, as it might overestimate the aging effect.

The interaction term temperature:charging power points towards increased aging at low temperatures and high charging powers, presumably through lithium plating, whereas the charging power shows only a slight influence at $3 0 ^ { \circ } \mathsf { C } . \mathsf { A t } 5 0 ^ { \circ } \mathsf { C } ,$ the aging is also only slightly dependent on the charging power. The accelarated aging at lower charging powers and high temperatures might again be the effect of remnants of the calendar aging.

In case of $\mathsf { E V } _ { \mathsf { r a t i o } } \colon \mathsf { S o C } _ { \mathsf { m a x } } ,$ and $\mathsf { E V } _ { \mathsf { r a t i o } } { : } \mathsf { t e m p e r a t u r e }$ $\mathsf { S o C } _ { \mathsf { m a x } }$ :temperature, and charging power: $\mathsf { E V } _ { \mathsf { r a t i o } } ,$ , (Figure 6c-f) the interactions are small, only slightly increasing or dampening the capacity loss as both factors are changed.

![](03-Stadler-2022_images/6eaf2eb08410b153dbc0c1da10cd37f052735c3e9da0bc905fee24791d6b727b.jpg)  
Figure 6: Left: Cyclic capacity loss in % relative to BoL capacity after 175 kAh as function of two factors. Right: Projection of cyclic capacity loss after 175 kAh related with one factor at three different levels of the partner factor. The more the three curves differ from a parallel course, the greater the modelled interactions between these two factors are.

## Model validation

Using the model approach shown so far, the loss of capacity after one predetermined charge throughput can be described. However, for later application in the lifetime forecast, the model must be able to evaluate the capacity loss at any given charge throughput. Therefore, several models are created at specified load throughputs. Parameters can be found in the appendix S.4. Subsequently, the continuous trend of capacity loss can be obtained by evaluating every individual model at certain aging conditions and fitting a power law through the predicted points.

To validate the entire modelling approach, existing data is separated into both training data for model parameterization and test data for validation.

A more general estimation of model quality can be achieved by means of cross-validation, where the model is created several times, leaving out one test point at a time to use for validation. Figure 7a-e show a selection of comparisons between the modeled aging prediction and the actual measurements. For each plot, a separate model was built, using all data but the shown measurements. Mainly, the model error is in the range of ±0.5 % of capacity relative to BoL. This is also summarized in Figure 7f, plotting the predicted capacity versus the actual measured capacity values. Here, a perfect fit would match the dashed line. Again, the model was parameterized for every aging condition separately, leaving out one test point at a time. These excluded test points are plotted as validation and show that most of the predictions have an error of around ±0.5 % of capacity relative to BoL, while only few fitted trends have an error greater than 1%.

More insight is gained in Figure 7g, which displays the mean RMSE on training and validation range for each aging condition when excluded from the modeling workflow. A mean RMSE of 0.46 is achieved on exclusive test data.

Surprisingly, the model seems to have greater difficulties with predicting the cube points of the test matrix, which can be considered an interpolation task, than with predicting the star points, which require slight extrapolation. This indicates that the single trends of the effects are described more precisely in the mode than the interaction effects.

In addition, for estimating the capability of extrapolation of the test progress, the models were created several times, each with a varying percentage of the last 0-80 % of data being used exclusively for validation (Fig. 7h). Again, the model is capable of predicting cyclic aging with a RMSE as low as 0.32 even when using only 40 % of the data. Increasing the training data even further expectedly leads to worse predictions, but still, with 30 % of the data being used for parameterization, the mean model error is in a comparable range to the interpolation test. As certain conditions are described almost perfectly, whereas others show bigger deviation, the usage of such models always requires at least some user experience in order to assess the plausibility of specific predictions.

![](03-Stadler-2022_images/35628365923d8fce0898a1c846de9bed69d9a508063229cb17b6f615d556bc3b.jpg)

![](03-Stadler-2022_images/73ba37869e0ab397f2b165b15e60efb3210def40dcc8a85ca27543c81cc53e98.jpg)

![](03-Stadler-2022_images/367b65e0a46953ab4296b83a9faf0e2d8f4c51d968286c8fe7335b8d1375e282.jpg)

![](03-Stadler-2022_images/cc351babc7b87330b5a79bbfa859c7dbe9cea9e7cca3bbc74a9ecae05d276376.jpg)

![](03-Stadler-2022_images/e7bc9c2e0ff7292651cdc6b2e9eed8143327688f50944b4cb34bf81548d67bcf.jpg)

f  
![](03-Stadler-2022_images/0b60b4e1baa0d10688c831e191b75d4bdcaece135d0b72f8b2542dfb967a0476.jpg)

![](03-Stadler-2022_images/51dabfb0d72305d70f8928a2f6625e61426ab6f7a1ddf72b7ad0af37374f133e.jpg)

![](03-Stadler-2022_images/70f67101e04c711ccef7242f2ba12f84d83a99495e9c9871b84be0e4ab0aa3fa.jpg)  
Figure 7: a-e) Modell validation on selected conditions using leave-one-out cross validation considering only cyclic aging. The shown measurement is not used for model parameterization. Predictions of the five regression models at 0, 25, 75, 125, and 175 kAh and the resulting continuous fits are shown. f) Predicted cyclic capacity loss versus measured cyclic capacity loss of test data. For each curve, a separate model was parameterized, leaving out the specified test point as validation data. g) RMSE of

every cross validation fold on all used training data (blue) and on the capacity trends that were excluded for validation. h) RMSE of aging models that were parameterized on a specified share of each capacity trend, while the rest was used for validation.

## 4. Conclusion

With the cyclic capacity-aging model of a 43 Ah lithium-ion pouch bag cells, we present a description of a multi-dimensional problem, containing the influence factors temperature, $\mathsf { E V } _ { \mathsf { r a t i o } } , \mathsf { S o C } _ { \mathsf { m a x } } , \mathsf { S o C } _ { \mathsf { m i n } } ,$ and charging power, which was investigated with the empirical approach of DoE. Based on these measurements, we successfully separated calendar and cyclic aging and were able to identify the temperature as well as the ratio of microcyles in the power profile $( E V _ { \mathsf { r a t i o } } )$ as the most significant factors influencing cyclic aging. Raising the lower or upper SoC boundary leads to an increase of capacity loss, whereas the variation of charging power shows no significant effect. Interactions between two factors were analyzed and are considered highly important for modelling. Especially for the influence of lower and upper SoC boundary, a DoD dependency was introduced to the model, predicting a higher aging at the highest DoD, thus being in accordance with literature. The interaction terms also prove to be of high importance to the cross validation, where the prediction of test points with several simultaneously changed factors turns out to be more difficult than an extrapolation task with only one changing factor. This highlights the importance of designing the test matrix to precisely define the range of the relevant factors that are later needed for prediction.

An empirical model for the prediction of a continuous aging trend over charge throughput, built from submodels commonly used in the evaluation of DoE, is presented. For the entire range of the evaluated factors, a mean RMSE of 0.19 is obtained. Moreover, the model shows excellent extrapolation capability for continuous aging trends, being able to extrapolate up to 60% of the data with a RMSE of 0.32.

This empirical approach is a solid basis for future investigations with post-mortem analysis, where we will shed light on the underlying aging mechanisms and transform the model to incorporate more physical knowledge. Ideally, this will further increase inter- and extrapolation capabilities and reduce test effort. Furthermore, the model can be implemented in combination with a calendar aging model, where further investigations are needed to validate the superposition of calendar and cycle aging.

## 5. Acknowledgments and Contributions

Jochen Stadler: Conceptualization, Methodology, Data curation, Formal analysis, Project administration,

Software, Validation, Visualization, Writing - original draft

Carsten Krupp: Conceptualization, Methodology, Project administration

Madeleine Ecker: Supervision, Conceptualization, Writing - review & editing

Jochen Bandlow: Supervision, Conceptualization, Writing - review & editing

Bernd Spier: Conceptualization, Funding acquisition, Writing - review & editing

Arnulf Latz: Supervision, Writing - review & editing

The authors acknowledge the financial support of Mercedes-Benz AG, (Stuttgart, Germany). Alexander Marquardt is thanked for helping with organizational topics regarding the test conduction. Florian Laufer is acknowledged for his help with model development during his internship. Daniel Seiler is thanked for proofreading.

## 6. Supplementary Information

## S.1. SoC-OCV Curve

![](03-Stadler-2022_images/b43dcb3e3499ea8b35e41be28a2129fbfa1a16b135a58dadd34cd37b10ef2f35.jpg)  
Figure S1: SoC-OCV relationship of the tested cell

## S.2. Reference Parameter Test Protocol

Table S2: Test protocol of the used reference parameter test for evaluation of capacity and resistance degradation trends.

<table><tr><td>Step</td><td>Command</td><td>Parameter</td><td>Exit Condition</td><td>Comment</td></tr><tr><td>1</td><td>Set Temperature</td><td>25°C</td><td></td><td>Set temperature to 25°C</td></tr><tr><td>2</td><td>Rest</td><td></td><td>t-step&gt;4h</td><td>4h Pause to reach stable conditions</td></tr><tr><td colspan="5">1C capacity measurement</td></tr><tr><td>3</td><td>Start Loop1</td><td></td><td></td><td></td></tr><tr><td>4</td><td>Charge</td><td>U = 4.2V I=1C</td><td>I&lt;0.05C</td><td>CCCV Charge</td></tr><tr><td>5</td><td>Rest</td><td></td><td>t-step&gt;5min</td><td>5 min Pause</td></tr><tr><td>6</td><td>Discharge</td><td>I=1C</td><td>U&lt;2.5V</td><td>CC Discharge</td></tr><tr><td>7</td><td>Rest</td><td></td><td>t-step&gt;5min</td><td>5 min Pause</td></tr><tr><td>8</td><td>End Loop1</td><td>COUNT=3</td><td></td><td>Repeat Loop1 for 3 times</td></tr><tr><td>9</td><td>Calculate</td><td> $C_{act} = Ah\_DCH$  [STEP 6]</td><td></td><td>Calculate  $C_{act}$  from discharged capacity of step 6.</td></tr><tr><td>10</td><td>Charge</td><td>U=4.2V I=1C</td><td>I&lt;0.05C</td><td>CCCV Charge</td></tr><tr><td colspan="5">0,1C capacity measurement</td></tr><tr><td>11</td><td>Rest</td><td></td><td>t-step&gt;1h</td><td>1h Pause</td></tr><tr><td>12</td><td>Discharge</td><td>I=0.1C</td><td>U0.1C Discharge</td><td>0.1C Discharge</td></tr><tr><td>13</td><td>Rest</td><td></td><td>t-step&gt;1h</td><td>1h Pause</td></tr><tr><td>14</td><td>Charge</td><td>U=4.2V I=1C</td><td>I&lt;0.05C</td><td>CCCV Charge</td></tr><tr><td colspan="5">DCH pulse (30s, 200A) @ 100%, 75%, 50% and 25% SoC</td></tr><tr><td>15</td><td>Start Loop2</td><td></td><td></td><td></td></tr><tr><td>16</td><td>Rest</td><td></td><td>t-step&gt;60min</td><td>1h Pause</td></tr><tr><td>17</td><td>Discharge</td><td>I=200A</td><td>U30s</td><td>200 A discharge pulse for  $R_{10s}$  evaluation.</td></tr><tr><td>18</td><td>Rest</td><td></td><td>t-step&gt;5min</td><td>5 min Pause after pulse</td></tr><tr><td>19</td><td>Discharge</td><td>I=1C</td><td>Ah-step&lt;-0.25 $C_{act}$  + |Ah-Puls|</td><td>Discharge to 75% 50% 25% 0% SoC</td></tr><tr><td>20</td><td>End Loop2</td><td>COUNT=4</td><td></td><td>Repeat Loop2 for 4 times</td></tr><tr><td>21</td><td>Rest</td><td></td><td>t-step&gt;5min</td><td>5 min Pause</td></tr><tr><td>22</td><td>Charge</td><td>U=4.2V I=1C</td><td>I&lt;0.05C</td><td>CCCV Charge.</td></tr><tr><td>23</td><td>Rest</td><td></td><td>t-step&gt;5min</td><td>5 min Pause</td></tr></table>

d

## S.3. Parameterization of the calendar aging model

![](03-Stadler-2022_images/7006f8d022c4be01bd56b41fd8320f4ccbf6ceec665c037ece0b379010662fdb.jpg)

![](03-Stadler-2022_images/c4cc0f918b1f4e0b4f4e6c10eb19bd56f51f4845e2cdf8baf19816b4713cdae5.jpg)

![](03-Stadler-2022_images/34fbc367744785f9be7ac42b6d913701550a92eac4f5e0ca093b77129d91b1df.jpg)

![](03-Stadler-2022_images/7fdc4167467e30b1b3a388e38bcaa84556131157f60df18b6941230240400256.jpg)  
Figure S3: a) Calendar aging was tested at 40 %, 60 %, and 80 % SoC as well as at $45 ^ { \circ } C$ and $6 0 ~ ^ { \circ } C .$ A semi empirical aging model was fitted. b) Trend of SoC influence on capacity fade after 400 days of aging. Points mark the measured aging after 400 days, the line indicates the parameterized aging model. c) Trend of temperature dependency after 400 days of aging. Due to big deviations and the small amount of available test points, an Arrhenius term can not be fitted satisfactorily. d) Validation of calendar model on a measurement at 50 % SoC and $3 0 ~ ^ { \circ } C$ nevertheless matches well.

Calendar measurements were performed with threefold repetition at two temperature levels $( 4 5 ^ { \circ } \mathsf { C }$ and $5 2 . 5 ~ ^ { \circ } \mathrm { C } )$ and on three SoC-levels (40 %, 60 %, 80 %) as depicted in Figure S3a. A calendar aging model of the form

$$
C _ {c a l} = 1 0 0 + p _ {1} * e x p (\frac {p _ {2}}{T + 2 7 3}) * e x p (p _ {3} * V) * t ^ {p _ {4}}
$$

is fitted on calendar aging measurements of the same cell type with parameters: $\mathsf { p } _ { 1 } = - 7 . 3 3 \mathsf { e } \mathrm { - } 6 , \mathsf { p } _ { 2 } = - 5 1 2 . 5 6 ,$ $p _ { 3 } = 1 . 3 7 , \mathsf { p } _ { 4 } = 0 . 7 9$

Unfortunately, the threefold repetition shows significant deviations on both SoC and temperature aging trends (Figure S3b,c), casting doubt on the accuracy of the fitted parameters. An Arrhenius term cannot be fitted to the temperature data satisfactorily, which might lead to an underestimation of calendar aging at very high temperatures. However, using the parameterized aging model to predict the aging of a 50 % SoC calendar aging point at $3 0 ^ { \circ } \mathsf C ,$ which was measured together with the cyclic aging matrix as reference, shows very good matching despite the aging parameters being outside of the parameterized region. Thus, the model is used for correction of cyclic aging, as no other data is present and cannot be measured again in a reasonable time.

S.4. Model coefficients

<table><tr><td></td><td colspan="2">Model at 25 kAh</td><td colspan="2">Model at 75 kAh</td><td colspan="2">Model at 125 kAh</td><td colspan="2">Model at 175 kAh</td></tr><tr><td></td><td>Estimate</td><td>pValue</td><td>Estimate</td><td>pValue</td><td>Estimate</td><td>pValue</td><td>Estimate</td><td>pValue</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Intercept</td><td>0,81</td><td>1,94E-32</td><td>1,65</td><td>3,83E-28</td><td>2,31</td><td>8,53E-31</td><td>2,88</td><td>1,01E-29</td></tr><tr><td> $EV_{ratio}$ </td><td>0,81</td><td>1,55E-25</td><td>1,56</td><td>3,75E-30</td><td>2,19</td><td>7,81E-33</td><td>2,78</td><td>3,46E-32</td></tr><tr><td> $Temperature^2$ </td><td>0,71</td><td>6,53E-13</td><td>1,48</td><td>2,44E-18</td><td>1,94</td><td>1,31E-19</td><td>2,35</td><td>6,82E-18</td></tr><tr><td>Temperature</td><td>-9,90E-05</td><td>9,98E-01</td><td>0,39</td><td>5,44E-09</td><td>0,84</td><td>1,96E-16</td><td>1,30</td><td>1,44E-18</td></tr><tr><td> $EV_{ratio}^2$ </td><td></td><td></td><td>0,45</td><td>4,17E-05</td><td>0,67</td><td>1,14E-06</td><td>0,82</td><td>8,13E-06</td></tr><tr><td> $SoC_{max}^2$ </td><td></td><td></td><td>0,27</td><td>1,30E-02</td><td>0,51</td><td>1,96E-04</td><td>0,79</td><td>2,89E-05</td></tr><tr><td> $SoC_{min}$ </td><td>0,57</td><td>1,52E-18</td><td>0,58</td><td>1,04E-13</td><td>0,63</td><td>2,20E-12</td><td>0,68</td><td>1,04E-09</td></tr><tr><td> $SoC_{min}^2$ </td><td></td><td></td><td>0,30</td><td>5,19E-03</td><td>0,48</td><td>2,73E-04</td><td>0,68</td><td>1,66E-04</td></tr><tr><td> $ChargingPower^2$ </td><td>0,45</td><td>8,85E-08</td><td>0,58</td><td>5,01E-07</td><td>0,62</td><td>4,42E-06</td><td>0,65</td><td>2,07E-04</td></tr><tr><td>SoCmax: $EV_{ratio}$ </td><td>0,30</td><td>3,75E-03</td><td>0,34</td><td>1,35E-02</td><td>0,44</td><td>7,97E-03</td><td>0,57</td><td>1,06E-02</td></tr><tr><td> $EV_{ratio}:ChargingPower$ </td><td></td><td></td><td>0,46</td><td>7,30E-04</td><td>0,50</td><td>2,14E-03</td><td>0,45</td><td>3,44E-02</td></tr><tr><td>Temperature:SoCmax</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0,42</td><td>5,81E-02</td></tr><tr><td>ChargingPower</td><td>-0,06</td><td>1,28E-01</td><td>0,10</td><td>5,60E-02</td><td>0,24</td><td>4,39E-04</td><td>0,35</td><td>1,61E-04</td></tr><tr><td> $SoC_{max}$ </td><td>0,14</td><td>1,47E-03</td><td>0,12</td><td>2,58E-02</td><td>0,19</td><td>5,00E-03</td><td>0,28</td><td>2,87E-03</td></tr><tr><td>Temperature:  $EV_{ratio}$ </td><td>-0,28</td><td>7,86E-03</td><td>-0,42</td><td>2,47E-03</td><td>-0,46</td><td>5,83E-03</td><td>-0,47</td><td>3,49E-02</td></tr><tr><td> $SoC_{max}:SoC_{min}$ </td><td></td><td></td><td>-0,45</td><td>3,31E-03</td><td>-0,67</td><td>4,22E-04</td><td>-0,95</td><td>2,15E-04</td></tr><tr><td>Temperature:ChargingPower</td><td>-0,44</td><td>4,82E-05</td><td>-0,83</td><td>1,43E-07</td><td>-1,07</td><td>3,01E-08</td><td>-1,26</td><td>5,41E-07</td></tr><tr><td> $SoC_{max}:ChargingPower$ </td><td>0,20</td><td>4,89E-02</td><td>0,33</td><td>1,48E-02</td><td>0,36</td><td>2,53E-02</td><td></td><td></td></tr><tr><td> $SoC_{min}:EV_{ratio}$ </td><td></td><td></td><td>-0,26</td><td>6,39E-02</td><td>-0,32</td><td>5,61E-02</td><td></td><td></td></tr></table>

Table S4.1: model coefficients for all four snapshot models, where all factors where normalized to the range of -1 to 1. All available data is used in parameterization. Factors are sorted by effects at the 175 kAh model.

Table S4.2: model coefficients for all four snapshot models, where factor levels where used in their physical quantity. All available data is used in parameterization. Factors are sorted by effect size of the normalized 175 kAh model.

<table><tr><td></td><td colspan="2">Model at 25 kAh</td><td colspan="2">Model at 75 kAh</td><td colspan="2">Model at 125 kAh</td><td colspan="2">Model at 175 kAh</td></tr><tr><td></td><td>Estimate</td><td>pValue</td><td>Estimate</td><td>pValue</td><td>Estimate</td><td>pValue</td><td>Estimate</td><td>pValue</td></tr><tr><td>Intercept</td><td>0,81</td><td>1,94E-32</td><td>1,65</td><td>3,83E-28</td><td>2,31</td><td>8,53E-31</td><td>2,88</td><td>1,01E-29</td></tr><tr><td> $EV_{ratio}$ </td><td>0,81</td><td>1,55E-25</td><td>1,56</td><td>3,75E-30</td><td>2,19</td><td>7,81E-33</td><td>2,78</td><td>3,46E-32</td></tr><tr><td> $Temperature^2$ </td><td>0,71</td><td>6,53E-13</td><td>1,48</td><td>2,44E-18</td><td>1,94</td><td>1,31E-19</td><td>2,35</td><td>6,82E-18</td></tr><tr><td>Temperature</td><td>-9,90E-05</td><td>9,98E-01</td><td>0,39</td><td>5,44E-09</td><td>0,84</td><td>1,96E-16</td><td>1,30</td><td>1,44E-18</td></tr><tr><td> $EV_{ratio}^2$ </td><td></td><td></td><td>0,45</td><td>4,17E-05</td><td>0,67</td><td>1,14E-06</td><td>0,82</td><td>8,13E-06</td></tr><tr><td> $SoC_{max}^2$ </td><td></td><td></td><td>0,27</td><td>1,30E-02</td><td>0,51</td><td>1,96E-04</td><td>0,79</td><td>2,89E-05</td></tr><tr><td> $SoC_{min}$ </td><td>0,57</td><td>1,52E-18</td><td>0,58</td><td>1,04E-13</td><td>0,63</td><td>2,20E-12</td><td>0,68</td><td>1,04E-09</td></tr><tr><td> $SoC_{min}^2$ </td><td></td><td></td><td>0,30</td><td>5,19E-03</td><td>0,48</td><td>2,73E-04</td><td>0,68</td><td>1,66E-04</td></tr><tr><td> $ChargingPower^2$ </td><td>0,45</td><td>8,85E-08</td><td>0,58</td><td>5,01E-07</td><td>0,62</td><td>4,42E-06</td><td>0,65</td><td>2,07E-04</td></tr><tr><td>SoCmax: $EV_{ratio}$ </td><td>0,30</td><td>3,75E-03</td><td>0,34</td><td>1,35E-02</td><td>0,44</td><td>7,97E-03</td><td>0,57</td><td>1,06E-02</td></tr><tr><td> $EV_{ratio}:ChargingPower$ </td><td></td><td></td><td>0,46</td><td>7,30E-04</td><td>0,50</td><td>2,14E-03</td><td>0,45</td><td>3,44E-02</td></tr><tr><td>Temperature:SoCmax</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0,42</td><td>5,81E-02</td></tr><tr><td>ChargingPower</td><td>-0,06</td><td>1,28E-01</td><td>0,10</td><td>5,60E-02</td><td>0,24</td><td>4,39E-04</td><td>0,35</td><td>1,61E-04</td></tr><tr><td> $SoC_{max}$ </td><td>0,14</td><td>1,47E-03</td><td>0,12</td><td>2,58E-02</td><td>0,19</td><td>5,00E-03</td><td>0,28</td><td>2,87E-03</td></tr><tr><td>Temperature:  $EV_{ratio}$ </td><td>-0,28</td><td>7,86E-03</td><td>-0,42</td><td>2,47E-03</td><td>-0,46</td><td>5,83E-03</td><td>-0,47</td><td>3,49E-02</td></tr><tr><td> $SoC_{max}:SoC_{min}$ </td><td></td><td></td><td>-0,45</td><td>3,31E-03</td><td>-0,67</td><td>4,22E-04</td><td>-0,95</td><td>2,15E-04</td></tr><tr><td>Temperature:ChargingPower</td><td>-0,44</td><td>4,82E-05</td><td>-0,83</td><td>1,43E-07</td><td>-1,07</td><td>3,01E-08</td><td>-1,26</td><td>5,41E-07</td></tr><tr><td>SoCmax:ChargingPower</td><td>0,20</td><td>4,89E-02</td><td>0,33</td><td>1,48E-02</td><td>0,36</td><td>2,53E-02</td><td></td><td></td></tr><tr><td>SoCmin:EVratio</td><td>0,81</td><td>1,94E-32</td><td>-0,26</td><td>6,39E-02</td><td>-0,32</td><td>5,61E-02</td><td></td><td></td></tr></table>

## 7. References

[1] J. Vetter, P. Novák, M.R. Wagner, C. Veit, K.-C. Möller, J.O. Besenhard, M. Winter, M. Wohlfahrt-Mehrens, C. Vogler, A. Hammouche, Journal of Power Sources 147 (2005) 269–281. https://doi.org/10.1016/j.jpowsour.2005.01.006.

[2] A. Barré, B. Deguilhem, S. Grolleau, M. Gérard, F. Suard, D. Riu, Journal of Power Sources 241 (2013) 680–689. https://doi.org/10.1016/j.jpowsour.2013.05.040.

[3] M. Broussely, P. Biensan, F. Bonhomme, P. Blanchard, S. Herreyre, K. Nechev, R.J. Staniewicz, Journal of Power Sources 146 (2005) 90–96. https://doi.org/10.1016/j.jpowsour.2005.03.172.

[4] E. Sarasketa-Zabala, I. Gandiaga, L.M. Rodriguez-Martinez, I. Villarreal, Journal of Power Sources 272 (2014) 45–57. https://doi.org/10.1016/j.jpowsour.2014.08.051.

[5] S.L. Hahn, M. Storch, R. Swaminathan, B. Obry, J. Bandlow, K.P. Birke, Journal of Power Sources 400 (2018) 402–414. https://doi.org/10.1016/j.jpowsour.2018.08.019.

[6] P. Keil, S.F. Schuster, J. Wilhelm, J. Travi, A. Hauser, R.C. Karl, A. Jossen, Journal of the Electrochemical Society 163 (2016) A1872-A1880. https://doi.org/10.1149/2.0411609jes.

[7] M. Ecker, J.B. Gerschler, J. Vogel, S. Käbitz, F. Hust, P. Dechent, D.U. Sauer, Journal of Power Sources 215 (2012) 248–257. https://doi.org/10.1016/j.jpowsour.2012.05.012.

[8] M. Storch, S.L. Hahn, J. Stadler, R. Swaminathan, D. Vrankovic, C. Krupp, R. Riedel, Journal of Power Sources 443 (2019) 227243. https://doi.org/10.1016/j.jpowsour.2019.227243.

[9] T.C. Bach, S.F. Schuster, E. Fleder, J. Müller, M.J. Brand, H. Lorrmann, A. Jossen, G. Sextl, Journal of Energy Storage 5 (2016) 212–223. https://doi.org/10.1016/j.est.2016.01.003.

[10] D. Werner, S. Paarmann, A. Wiebelt, T. Wetzel, Batteries 6 (2020) 13. https://doi.org/10.3390/batteries6010013.

[11] I. Laresgoiti, S. Käbitz, M. Ecker, D.U. Sauer, Journal of Power Sources 300 (2015) 112–122. https://doi.org/10.1016/j.jpowsour.2015.09.033.

[12] S. Gantenbein, M. Schönleber, M. Weiss, E. Ivers-Tiffée, Sustainability 11 (2019) 6697. https://doi.org/10.3390/su11236697.

[13] J. Purewal, J. Wang, J. Graetz, S. Soukiazian, H. Tataria, M.W. Verbrugge, Journal of Power Sources 272 (2014) 1154–1161. https://doi.org/10.1016/j.jpowsour.2014.07.028.

[14] J. Keil, N. Paul, V. Baran, P. Keil, R. Gilles, A. Jossen, Journal of the Electrochemical Society 166 (2019) A3908-A3917. https://doi.org/10.1149/2.1271915jes.

[15] M. Naumann, F.B. Spingler, A. Jossen, Journal of Power Sources 451 (2020) 227666. https://doi.org/10.1016/j.jpowsour.2019.227666.

[16] A. Cordoba-Arenas, S. Onori, Y. Guezennec, G. Rizzoni, Journal of Power Sources 278 (2015) 473– 483. https://doi.org/10.1016/j.jpowsour.2014.12.047.

[17] J. de Hoog, J.-M. Timmermans, D. Ioan-Stroe, M. Swierczynski, J. Jaguemont, S. Goutam, N. Omar, J. van Mierlo, P. van den Bossche, Applied Energy 200 (2017) 47–61. https://doi.org/10.1016/j.apenergy.2017.05.018.

[18] M. Uy, J.K. Telford, in: 2009 IEEE Aerospace conference, IEEE, 07.03.2009 - 14.03.2009, pp. 1–10.

[19] O. Rynne, M. Dubarry, C. Molson, D. Lepage, A. Prébé, D. Aymé-Perrot, D. Rochefort, M. Dollé, Batteries 5 (2019) 72. https://doi.org/10.3390/batteries5040072.

[20] W. Prochazka, G. Pregartner, M. Cifrain, J. Electrochem. Soc. 160 (2013) A1039-A1051. https://doi.org/10.1149/2.003308jes.

[21] L. Su, J. Zhang, C. Wang, Y. Zhang, Z. Li, Y. Song, T. Jin, Z. Ma, Applied Energy 163 (2016) 201–210. https://doi.org/10.1016/j.apenergy.2015.11.014.

[22] M. Dubarry, A. Devie, Journal of Energy Storage 18 (2018) 185–195. https://doi.org/10.1016/j.est.2018.04.004.

[23] D.-I. Stroe, M. Swierczynski, S.K. Kaer, E.M. Laserna, E.S. Zabala, in: 2017 IEEE Energy Conversion Congress and Exposition (ECCE), IEEE, 01.10.2017 - 05.10.2017, pp. 5631–5637.

[24] C. Kupper, B. Weißhar, S. Rißmann, W.G. Bessler, Journal of the Electrochemical Society 165 (2018) A3468-A3480. https://doi.org/10.1149/2.0941814jes.

[25] S. Atalay, M. Sheikh, A. Mariani, Y. Merla, E. Bower, W.D. Widanage, Journal of Power Sources 478 (2020) 229026. https://doi.org/10.1016/j.jpowsour.2020.229026.

[26] C.P. Aiken, J.E. Harlow, R. Tingley, T. Hynes, E.R. Logan, S.L. Glazier, A.S. Keefe, J.R. Dahn, J. Electrochem. Soc. 167 (2020) 130541. https://doi.org/10.1149/1945-7111/abbe5b.

[27] J. Schmalstieg, S. Käbitz, M. Ecker, D.U. Sauer, Journal of Power Sources 257 (2014) 325–334. https://doi.org/10.1016/j.jpowsour.2014.02.012.

[28] M. Naumann, M. Schimpe, P. Keil, H.C. Hesse, A. Jossen, Journal of Energy Storage 17 (2018) 153–169. https://doi.org/10.1016/j.est.2018.01.019.

[29] D.C. Montgomery, Design and analysis of experiments, Ninth edition, Wiley, Hoboken NJ, 2017.

[30] R. Mathieu, I. Baghdadi, O. Briat, P. Gyan, J.-M. Vinassa, Energy 141 (2017) 2108–2119. https://doi.org/10.1016/j.energy.2017.11.130.

[31] T. Baumhöfer, M. Brühl, S. Rothgang, D.U. Sauer, Journal of Power Sources 247 (2014) 332–338. https://doi.org/10.1016/j.jpowsour.2013.08.108.

[32] M. Schindler, J. Sturm, S. Ludwig, J. Schmitt, A. Jossen, eTransportation 8 (2021) 100102. https://doi.org/10.1016/j.etran.2020.100102.

[33] I. Bloom, B. Cole, J. Sohn, S. Jones, E. Polzin, V. Battaglia, G. Henriksen, C. Motloch, R. Richardson, T. Unkelhaeuser, D. Ingersoll, H. Case, Journal of Power Sources 101 (2001) 238–247. https://doi.org/10.1016/S0378-7753(01)00783-2.

[34] M. Broussely, S. Herreyre, P. Biensan, P. Kasztejna, K. Nechev, R. Staniewicz, Journal of Powe Sources 97-98 (2001) 13–21. https://doi.org/10.1016/S0378-7753(01)00722-4.

[35] T. Waldmann, B.-I. Hogg, M. Wohlfahrt-Mehrens, Journal of Power Sources 384 (2018) 107–124. https://doi.org/10.1016/j.jpowsour.2018.02.063.

[36] T. Waldmann, M. Wilka, M. Kasper, M. Fleischhammer, M. Wohlfahrt-Mehrens, Journal of Power Sources 262 (2014) 129–135. https://doi.org/10.1016/j.jpowsour.2014.03.112.

[37] A. Tomaszewska, Z. Chu, X. Feng, S. O'Kane, X. Liu, J. Chen, C. Ji, E. Endler, R. Li, L. Liu, Y. Li, S. Zheng, S. Vetterlein, M. Gao, J. Du, M. Parkes, M. Ouyang, M. Marinescu, G. Offer, B. Wu, eTransportation 1 (2019) 100011. https://doi.org/10.1016/j.etran.2019.100011.

[38] M. Ecker, P. Shafiei Sabet, D.U. Sauer, Applied Energy 206 (2017) 934–946. https://doi.org/10.1016/j.apenergy.2017.08.034.

[39] F. Benavente-Araoz, M. Varini, A. Lundblad, S. Cabrera, G. Lindbergh, J. Electrochem. Soc. 167 (2020) 40529. https://doi.org/10.1149/1945-7111/ab78fd.

[40] K. Asakura, M. Shimomura, T. Shodai, Journal of Power Sources 119-121 (2003) 902–905. https://doi.org/10.1016/S0378-7753(03)00208-8.

[41] S. Müller, P. Pietsch, B.-E. Brandt, P. Baade, V. de Andrade, F. de Carlo, V. Wood, Nature communications 9 (2018) 2340. https://doi.org/10.1038/s41467-018-04477-1.