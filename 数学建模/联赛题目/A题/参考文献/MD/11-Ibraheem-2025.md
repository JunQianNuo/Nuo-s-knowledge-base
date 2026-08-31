---
raw_title: 11-Ibraheem-2025
subject: 数学建模-策联杯A题
source: "Robust survival model for the prediction of Li-ion battery lifetime reliability and risk functions.pdf"
status: mineru解析
parser: mineru
topics:
  - Cox生存模型
  - 右删失
  - 可靠性
  - 风险函数
---

Edinburgh Research Explorer

# Robust Survival Model for the Prediction of Li-ion Battery lifetime Reliability and Risk Functions

Citation for published version: Ibraheem, R, Cannings, TI, Sell, T & Dos Reis, G 2025, 'Robust Survival Model for the Prediction of Li-ion Battery lifetime Reliability and Risk Functions', Energy and AI, vol. 19, 100465. https://doi.org/10.1016/j.egyai.2024.100465

## Digital Object Identifier (DOI):

10.1016/j.egyai.2024.100465

Link to publication record in Edinburgh Research Explorer

## Document Version:

Peer reviewed version

## Published In:

Energy and AI

## General rights

Copyright for the publications made accessible via the Edinburgh Research Explorer is retained by the author(s) and / or other copyright owners and it is a condition of accessing these publications that users recognise and abide by the legal requirements associated with these rights.

## Take down policy

The University of Edinburgh has made every reasonable effort to ensure that Edinburgh Research Explorer content complies with UK legislation. If you believe that the public display of this file breaches copyright please contact openaccess@ed.ac.uk providing details, and we will remove access to the work immediately and investigate your claim.

## Graphical Abstract

Robust Survival Model for the Prediction of Li-ion Battery lifetime Reliability and Risk Functions

Rasheed Ibraheem, Timothy I Cannings, Torben Sell, Gonc¸alo dos Reis

![](11-Ibraheem-2025_images/c0cfc7c73f3376bf34e9e37de7a0267a83bd2e2efab9d901e822f9f7c5fdb000.jpg)

## Highlights

Robust Survival Model for the Prediction of Li-ion Battery lifetime Reliability and Risk Functions

Rasheed Ibraheem, Timothy I Cannings, Torben Sell, Gonc¸alo dos Reis

• Battery reliability and risk prediction from a single survival model

• Model validation on data regions capturing protocol-to-protocol and cell-tocell variability

• Demonstrated application in battery dynamic warranty adjustment and stock management

• Rigorous model testing including robustness to low-training sample and data sparsity

• Documented modelling code publicly available

# Robust Survival Model for the Prediction of Li-ion Battery lifetime Reliability and Risk Functions

Rasheed Ibraheem<sup>a</sup>, Timothy I Cannings<sup>a</sup>, Torben Sell<sup>a</sup>, Gonc¸alo dos Reis<sup>a,b,∗</sup>

<sup>a</sup>Maxwell Institutefor Mathematical Sciences, School ofMathematics, University ofEdinburgh, The Kings buildings, Edinburgh, EH9 3JF, Scotland

<sup>b</sup>Center for Mathematics and Applications (NOVA Math), NOVA School of Science and Technology (NOVA FCT), Caparica, 2829-516, Portugal

## Abstract

Single-value prediction such as the End of Life and Remaining Useful Life is a common method of estimating the lifetime of Li-ion batteries. Information from such prediction is limited when the entire degradation pattern is needed for practical applications such as dynamic adjustment of battery warranty, improved maintenance scheduling, and battery stock management. In this research, a predictive, semi-parametric survival model called the Cox Proportional Hazards is proposed for the prediction of cell degradation in the form of survival probability (battery reliability) and cumulative hazard (battery risk) functions. Once this model is trained, the two functions can be obtained directly for a new cell without having to predict several cogent points. The model is trained on the first 50 cycles of only the voltage profile from either the charge or discharge data regime, implying that our methodology is data region agnostic. The signature method with both desirable mathematical and machine learning properties was adopted as a feature extraction technique.

The developed models are tested rigorously using application-driven strategies involving model robustness to the number of cycles of data required for model training and prediction, diferent fractions of training samples, and systematic data sparsity. The codes for modelling and testing are publicly available.

Keywords: Battery degradation, Cox Proportional Hazards, Path signature methodology, Survival probability function, Cumulative hazard function, Survival analysis, Reliability and risk functions

## 1. Introduction

Common models predicting the lifetime of batteries focus on a single-point prediction. Such models include those that predict the End of Life (EOL) [1, 2] and Remaining Useful Life (RUL) [3, 4, 5]. These models have limitations regarding the prediction of the entire degradation trajectory which is more informative as battery reliability can be obtained for each cycle count. Several works have addressed these limitations on predicting the full capacity and internal resistance (IR) of Li-ion cells [6, 7, 3]. While addressing the limitations, these full-curve models rely on the prediction of several cogent points such as the knees of the capacity curves [8] and elbows of IR rise curves [9]. Thus, the prediction of the entire battery degradation reduces to building multiple models to predict these cogent points. This poses challenges in terms of resources (both time and computation infrastructure) needed to train multiple models. In addition, they are not trained to handle incomplete data, i.e., data that fails to meet degradation prediction criteria and is thus removed from modelling. An example of this scenario is when a cell is not cycled to the EOL due to either deliberate dropout, testing failure or error in data measurement. The corresponding data obtained under such a scenario cannot be used for building models that predict the EOL or entire capacity/IR curves, nor can predictions be made on such data.

With all these challenges mentioned, we propose a novel modelling methodology which uses the concept of survival analysis to predict the degradation pattern of Li-ion cells in the form of battery survival probability and hazard rate functions. Survival analysis refers to a collection of statistical methods used for the analysis of data that involves time to occurrence of an event [10]. In this research, we considered the event of a cell reaching the EOL and proposed survival models that model the time to this event. Two powerful and versatile battery degradation predictions are obtained from a single trained survival model: the survival probability and the cumulative hazard functions. The former gives the probability of a cell surviving past a given time while the latter provides the instantaneous rate at which a cell approaches its failure (in this case the EOL), and thus quantifies the risk of battery capacity failure. In terms of incomplete data mentioned earlier, survival analysis is natural for handling incomplete data through incorporating a dichotomy variable which is 0 if the cell does not reach the EOL (and is thus right censored) and 1 otherwise.

After giving a concise introduction to survival analysis, we review some relevant past work on its application to battery lifetime prediction and highlight the challenges therein which we aim to address in this study. Survival analysis was used in [11] to estimate the optimum age at which to replace a medical equipment battery and distinguish between groups of cells with the shortest and longest lifespans. The Kaplan–Meier [12] methodology and Log-Rank Test [13] were used for the estimation of survival probability and hypothesis testing respectively. We emphasise that no predictive models were developed in these works, they instead focus on the estimation of survival curves of groups of cells to be able to use the Log-Rank Test for distribution comparison. In addition, the Kaplan–Meier survival estimate does not take into consideration the cause of battery degradation as no covariates or health indicators are used (only the event time and indicator are needed). In contrast to the work of [11], a data-driven, predictive survival model was developed in [14] using a Random Survival Forest [15] to predict the battery reliability function (i.e., the survival probability function). The data used in the study belongs to the lead-acid starter battery of trucks and were recorded during one of the workshop’s maintenance visits. We point out that the data does not contain measurements directly related to battery health indicators and no time series of battery health profiles are available. Thus, their proposed models were developed on covariates specific to a given workshop’s maintenance routines. This poses challenges of wide adoption, generalisability and versatility of the developed models. In particular, its adoption in electric vehicle battery prognostics will be limited as popular health indicator data captured in this case are voltage, current, temperature, capacity, and IR (which are not used in their case). On the use of data that directly impact battery degradation for lifetime prediction, an Accelerated Failure Time (AFT) model was developed in [16] to predict the EOL using cycling data including temperature, current, and State of Charge (SOC); the AFT model is a parametric survival model which only predicts the expected time to event, and neither survival nor hazard curves. Here, we emphasise two points. First, the parametric nature of the AFT model poses the challenge of choosing a suitable distribution for the survival time. Second, only a single-point lifetime estimate was considered (the EOL) and hence no information about degradation at every cycle can be accounted for.

Following the challenges and gaps in the literature highlighted above, we present the following contributions of our study to address them:

1. A predictive, semi-parametric survival model called Cox Proportional Hazards (Cox PH) [10] is proposed which does not require the knowledge of the survival time distribution but only a baseline hazard function (which is learned entirely from the data). This model does not only provide a survival probability function once it is trained but also the cumulative hazard function which can be used to quantify battery risk of failure at a point in time.

2. The proposed model was trained and validated on two diferent cycling data regimes (one at a time): the charge voltage (which captures protocol-toprotocol variabilities) and the constant-current (CC) discharge voltage (which encodes cell-to-cell variabilities). This implies only the voltage profile was considered as the health indicator and the modelling methodology worked seamlessly under the popular battery data regions: charge and discharge. In extracting features from the voltage curve, the signature method [17, 7] was adopted. This method is versatile and uniquely captures cogent information for each cell from the corresponding voltage curve. In addition, it has strong mathematical properties (such as uniqueness, universal nonlinearity, and time and translation invariance) that are desirable for a supervised machine learning task.

3. We propose several rigorous and application-driven model tests including robustness to the number of cycles of data required for model training and making inferences, diferent fractions of training samples, and systematic data sparsity at the training and inference levels. These tests were deployed on the proposed models to guarantee their performance and reliability.

The practical applications of the proposed models are clear. One of these is the dynamic adjustment of warranty. Battery manufacturers can use the predicted survival probability/hazard functions of battery cells to dynamically adjust warranty terms and conditions. This is made possible because predictions are curves rather than single value such as the EOL. Being able to adjust warrant dynamically has lots of benefits including ofering personalized and accurate warranty periods, potentially extending warranties for cells with higher survival probabilities; reduction in the costs associated with warranty claims by anticipating failures and proactively addressing potential issues; improvement of transparency and customer trust and satisfaction because warranty update is backed by a data-driven approach (with battery survival probabilities/hazard rates). Another application is in data-driven and improved maintenance scheduling. Fleet operators and service providers can leverage predicted survival probabilities to optimize maintenance schedules for battery-powered systems and devices. With this, maintenance can be performed proactively, preventing unexpected failures and downtime. Also, eficient allocation of maintenance resources can be achieved by focusing on high-risk batteries and thus unnecessary maintenance on low-risk ones will be reduced. Another benefit lies in battery stock management. Companies working with batteries can plan stock more reliably rather than having a large stock of spare batteries, they can order them on a rolling basis accounting for the expected number of dying batteries, for instance, in a month. Data-driven selection procedure is another application where a battery user may want to ensure that the battery survives a certain time with high probability. Survival analysis allows a more bespoke selection of batteries, rather than going for a point estimate such as EOL.

The rest of this paper is arranged as follows: Section 2 provides the description of the data used in this study; Section 3 gives an introduction to survival analysis, feature extraction techniques and model building procedures; results and discussion are presented in Section 4; and conclusions were left to Section 5. The mathematical description of the signature method is presented in the Methods Section (after the conclusions Section 5).

## 2. Data source and data description

## 2.1. Data source and cycling procedures

The data used in this research is obtained from the Toyota data [1, 18]. This data contains 373 Lithium Ferrosphosphate (LFP)/graphite A123 APR18650M1A cells grouped into 8 batches (b1-b8). On the high level, each cell has an initial capacity and voltage of 1.1 Ah and 3.3 V respectively. They are cycled using similar conditions of an ambient temperature of 30<sup>◦</sup>C and the same discharging C-rate of 4C constant current-constant voltage (CC-CV) to a minimum voltage of 2.0 V. On the other hand, each cell is charged from 0-80% SOC using one of over 80 different charging policies and then charged with the same C-rate (1C CC-CV) from 80% to 100% SOC (reaching a maximum voltage of 3.6 V). As a note, batches 1, 2, 3, and 8 are cycled to EOL while the rest are not cycled to EOL but to a maximum of 120 cycles. From the above descriptions, it can be deduced that the dataset contains two variabilities: protocol-to-protocol and cell-to-cell variabilities. The protocol-to-protocol diferences arise from the charge regime where diferent charging policies are used to cycle cells resulting in diferent cycling conditions. As for the cell-to-cell variability, it stems from the discharge regime where cells are discharged identically to observe intrinsic diferences among cells. The number of cells in each batch before and after preprocessing is provided in Table 1. Overall, a total of 373 cells were downloaded from the source but 362 (11 cells were dropped after preprocessing) cells were used in this research for all the modeling and experimentation.

Table 1: The number of cells in each batch. The ‘Original’ column refers to the actual number of cells in the downloaded Toyota data. After data preprocessing, the ‘Processed’ column corresponds to the number of cells in each batch. For the Toyota data, 373 cells were originally downloaded, 5 cells were carried into b2 but belonged to b1 and thus removed from b2, and 6 cells from b3 were also removed because of noisy channels, leaving a total of 362.

<table><tr><td rowspan="2">Dataset</td><td rowspan="2">Batches</td><td colspan="2">Number of cells</td></tr><tr><td>Original</td><td>Processed</td></tr><tr><td rowspan="8">Toyota</td><td>b1</td><td>46</td><td>46</td></tr><tr><td>b2</td><td>48</td><td>43</td></tr><tr><td>b3</td><td>46</td><td>40</td></tr><tr><td>b4</td><td>46</td><td>46</td></tr><tr><td>b5</td><td>46</td><td>46</td></tr><tr><td>b6</td><td>48</td><td>48</td></tr><tr><td>b7</td><td>48</td><td>48</td></tr><tr><td>b8</td><td>45</td><td>45</td></tr><tr><td></td><td>Total</td><td>373</td><td>362</td></tr></table>

## 2.2. Data analysis: feature and label data

We emphasise the diferent charging policies that have a direct impact on the charging profiles and introduce more variability in the dataset. With this and the fact that charging profiles in electric vehicles and other battery-powered devices can be controlled during the real-life usage of a battery (unlike discharging profiles which are dependent on the depth of usage, chosen route, level of trafic, and driver habits), the charging voltage profiles were considered as one of the data for feature extraction in this study; see Figure 1(a) for a sample of charging voltage profile for all cells. In addition, the second data regime considered for feature engineering is discharging; see Figure 1(b) for a sample of CC discharging voltage profile for all cells. This is motivated by the fact that some situations might warrant using identical and controlled cycling conditions to study intrinsic or cell-to-cell variabilities (which is the case in the Toyota discharge data regime). Examples of such situations are quality control done by cell manufacturers [19] and in storage for renewable energy where the derived energy is controlled and monitored [6]. Figure 2 shows the degree of cycle-to-cycle variability. The $l _ { 2 } { \mathrm { - n o r m } }$ of the diference between the signatures (see Section 3.4 for the details of signature calculation) of the first cycle voltage curve and each of cycle n $( 2 \leq n \leq 5 0 , n \in \mathbb { N } )$ was calculated and plotted against n. The norm serves as an indication of ‘similarity’ between cycle 1 and $n > 1$ . This was taken to show the diference of cycle-to-cycle variability in charge and discharge data regimes. It can be seen that variability is more pronounced in the discharge data than in the charge. This is because the discharge data indicate the actual use of a battery (energy is being derived from it), thus, a higher deviation between cycles is expected.

Labels for the survival model are EOL and an event indicator (a dichotomy variable which is 1 if a cell is cycled to its EOL, otherwise 0) were obtained from the capacity curves. The EOL is defined as the cycle corresponding to an 80% decrease in capacity relative to the first capacity value. The EOL of all the cells (in each batch) used in this research are presented in Figure 3. It can be seen that the datasets considered covered a wide range of EOL with a minimum and maximum value of 101 and 2235 cycles, respectively. The figure also shows that batches b4- b7 of the Toyota data were not cycled to EOL and that the last cycle was taken as EOL (thus are censored with an event indicator of 0).

a  
![](11-Ibraheem-2025_images/1014c648598e49a74240ca89fb8b9e0f51d7aa844236fccf782897bcc1cc6915.jpg)

![](11-Ibraheem-2025_images/f2d115a38fd7f7e052d1d71dbe672c271897674e1d8dcb4a9f62748c06dfb6c4.jpg)

![](11-Ibraheem-2025_images/44904dd600c47d6cde1e1c1b025a74fb3f8ca0281481e4d006c3559ae2c4ba16.jpg)

![](11-Ibraheem-2025_images/bbc35fde566e7100c35da98cc45a8989e63707ad83baab5a2451bf197a73997b.jpg)

![](11-Ibraheem-2025_images/ba3fc77f9d1ebfa9506d692d3654308de21de7b72956c22dc2cd5630589e9937.jpg)

![](11-Ibraheem-2025_images/c76a67579061948803a89edbe5d3a8fa387d736bb964d804fc7b4f29476122d3.jpg)

![](11-Ibraheem-2025_images/054d6fe77bbf2e351ae6b4f7597bbd3687517c29f4bd08cc2aea23827587e3de.jpg)

![](11-Ibraheem-2025_images/1f5ed0a941de6f101745c49c878e5d3d97de09aa0e20bf0c6a88460eef3eb2ef.jpg)

b  
![](11-Ibraheem-2025_images/b64f476d43e28bbe9e0ef75dca072c9eea67ee5da44532bee680a4ed3a4e258d.jpg)

![](11-Ibraheem-2025_images/78e4a98d742005b1f1fe9186d1c08a172625f75ba78b63f7ef597fd943025b5b.jpg)

![](11-Ibraheem-2025_images/2f0062b26722d0d5d3e9b1068a7da66b7cb0a1e28a825f8f658f4371cf882155.jpg)

![](11-Ibraheem-2025_images/deee72f431dcd7572df46d8161c29790f4b5bf8d7bba0efdb70350ac8a283562.jpg)

![](11-Ibraheem-2025_images/9b4587b35f0568935800e941a2e46fdfb63a4ced9a7e8365c379ec9d1f2e5fc2.jpg)

![](11-Ibraheem-2025_images/9620ec5db655426fcda70c831ac3f144179562628f8301b8473e677b6f7737ec.jpg)

![](11-Ibraheem-2025_images/7ad69adad310dbf75667158f11154f659e58a4c6dcbf4e41c476b3262ba494eb.jpg)

![](11-Ibraheem-2025_images/2201fe993cd920e45922fe4d8e53409f1d466b7ffde5de5c84996f771ac88a0a.jpg)  
Figure 1: (a) Charge and (b) CC discharge voltage curves of the Toyota data for cycle 50. All cells from each batch are considered in each figure block. For the charge regime, it can be seen that variability in the curves exists induced by the diferent charging policies. As for the discharge regime, cell-to-cell variabilities exist in the curves induced by the intrinsic property of the cells despite the cells being cycled identically.

a  
![](11-Ibraheem-2025_images/926cc0e2320aea537cd0a80407d9384aebb89f2dd27a166eef09223729c26955.jpg)  
b

![](11-Ibraheem-2025_images/3415ef2337ea2dbb43a682c42e1f7a5bc64a1fc656106c6fb07a297a088e08a2.jpg)

![](11-Ibraheem-2025_images/561fa6ff58141b074310754513d1daf32c69a52eca41e66da1ceb3b20baf3e2a.jpg)

d  
c  
![](11-Ibraheem-2025_images/dc2315797d0e003eff84489cc0c154b2c85838f7ff8f2c59c05784401b2aeecd.jpg)  
f

![](11-Ibraheem-2025_images/6c25b5d768d7ab90f4437c485a9f2f7cd94207cd54dd03645570baddc6042d3c.jpg)

![](11-Ibraheem-2025_images/85f5c888c64ea610cb22de7ee61d1cca469a2462eaaf955c52bff1f19d821caf.jpg)

g  
![](11-Ibraheem-2025_images/a5619c3f605c74799bb5eda1832b1e21c207cc50d9a06855aebf9ef84081294b.jpg)

h  
![](11-Ibraheem-2025_images/c071c2f2995866046ec5577991dd234a3597c7abcef354db5d3c937454b689c7.jpg)  
Figure 2: Cycle-to-cycle variabilities in the charge and discharge curves for a sample cell from each batch: (a)-(h) corresponding to batches b1-b8 respectively. The $l _ { 2 } .$ -norm of the diference in truncated signatures (calculated up to depth 3) of the voltage curves corresponding to the first cycle and cycle n $( 2 \leq n \leq 5 0 , n \in \mathbb { N } )$ was used as a quantitative measure of variability. There is more variability in the discharge curves than in the charge. Details about signatures are discussed in Section 3.4 and the Methods section.

![](11-Ibraheem-2025_images/5e7c5cc436e8174f9cb10334e6a8d9baef1012c1f05b42c243d24583443b95b7.jpg)  
Figure 3: EOL distribution and censorship summary of cells in each batch. Censored cells are cells that did not witness the event of being cycled to the EOL while uncensored reach the EOL by the end of cycling. All cells from b4 to b7 are censored.

## 3. Modelling and Methodology

## 3.1. Overview ofSurvival Analysis

Survival analysis is a set of statistical techniques that focus on analysing the time to the occurrence of an event. Time can be measured in diferent scales or units, for instance, days, months, years, or cycle counts from the start of a procedure until an event of interest occurs. An event is a particular experience that may happen to a subject during their lifetime. This can be the death of an individual, recovery from a disease, or a cell reaching its EOL. In this study, an assumption of one and only one event is adopted. In other words, a subject experiences an event only once in their lifetime. In addition, the subjects in our case are battery cells and an event is reaching the EOL. The EOL is defined as the cycle at which a cell capacity falls to 80% of its initial capacity. The time until EOL is regarded here as survival time and EOL is depicted as a failure. When a cell is cycled to failure, we say that cell is uncensored otherwise right censored. Right censoring of a cell may result from losing measurement tracking before reaching EOL or a deliberate dropout.

Following the convention in [10], we denote the random survival time of a cell as $T \geq 0$ (for us this is the number of cycles until EOL) and a specific realization of it as t. To specify whether a cell is cycled to failure or right-censored, a binary $( 0 , 1 )$ random variable δ is introduced into the analysis and is defined as

$$
\delta = \left\{ \begin{array}{l l} 0, & \text { if   a   cell   is   censored } \\ 1, & \text { if   a   cell   is   cycled   to   failure. } \end{array} \right.\tag{1}
$$

After defining the underlying survival variables, we now introduce and describe two functions which are the quantities of interest in any survival analysis. These are the survival function, $S \left( t \right)$ , and the hazard function, $h ( t )$ . The former provides the probability that a cell survives longer than a given time t, and the latter gives the instantaneous rate at which a cell is approaching its EOL at a time t given that the cell has survived up to t. These are defined mathematically as follows (where P denotes the probability of an event):

$$
S (t) = \mathbb {P} (T > t); \quad h (t) = \lim _ {\Delta t \rightarrow 0} \frac {\mathbb {P} (t \leq T <   t + \Delta t | T \geq t)}{\Delta t};\tag{2}
$$

and they are related via

$$
S (t) = e ^ {- H (t)}; \quad h (t) = - \frac {\frac {d S (t)}{d t}}{S (t)}.\tag{3}
$$

where

$$
H (t) := \int_ {0} ^ {t} h (u) d u\tag{4}
$$

is known as the cumulative hazard function (usually used to characterize $h ( t ) )$

The survival function is monotone decreasing, and further, it holds that $S ( 0 ) =$ $1 \ ( \mathrm { i . e . }$ , a cell survives past 0 cycles with probability 1), and $S ( \infty ) = 0$ (meaning if a cell is cycled or used indefinitely, its probability of survival will eventually collapse to 0). In practice, on the other hand, $S \left( t \right)$ is usually estimated using a step function instead of smooth curves (denoted as $\hat { S } ( t ) )$ ), and this approach is adopted in this study. The hazard function is nonnegative $( h ( t ) \geq 0 )$

## 3.2. Cox proportional hazards model

The Cox Proportional Hazards (Cox PH) model formula is expressed in terms of the hazard model, which gives the hazard rate at time t for a set of covariates or predictors. Given the covariate for a subject $\pmb { x } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { p } )$ , the Cox PH model is given as

$$
h (t, \boldsymbol {x}) = h _ {0} (t) \exp \left[ \sum_ {i = 1} ^ {p} \beta_ {i} x _ {i} \right],\tag{5}
$$

where $h _ { 0 } ( t )$ is the baseline hazard function independent of $x .$ We emphasise that $h ( t , \boldsymbol { x } )$ is the hazard function $h ( t )$ of Equation (2) for a subject with covariate x. In this research, we consider the case where x is time-independent.

There are three important properties of the Cox PH model. First, it assumes that the model reduces to the baseline hazard function when all covariates are nil (note that this does not necessarily mean zero in all problems as it might not make sense). Second, it is a semiparametric model because $h _ { 0 } ( t )$ is not specified and needs to be estimated. Third, it does not have an intercept term, and hazard functions for two subjects with covariates $\boldsymbol { x } _ { s _ { i } }$ and $\boldsymbol { x } _ { s _ { j } }$ are proportional at any time $t ,$ which motivates the “proportional hazard” assumption highlighted in the model’s name. In mathematical terms, using Equation (5), we have the proportional hazards given by

$$
\frac {h (t , \boldsymbol {x} _ {s _ {i}})}{h (t , \boldsymbol {x} _ {s _ {j}})} = \exp \left[ (\boldsymbol {x} _ {s _ {i}} - \boldsymbol {x} _ {s _ {j}}) \cdot \boldsymbol {\beta} \right], \quad \boldsymbol {\beta} \in \mathbb {R} ^ {p}
$$

where the right-hand side is independent of time.

Two questions now arise: is it necessary to check the proportional hazards assumption when using Cox PH for predictive regression? How can we best estimate $h _ { 0 } ( t )$ and how can we find $\beta$ via maximum likelihood estimation? To answer the first question, if the goal is to predict the survival function (and thus the hazard function as in the case of this study), then it is not necessary to check for proportional hazards [20]. This is because the goal is to maximize some scoring function (e.g. concordance index), which is independent of how predictions are generated. This is in contrast to a scenario where the survivals of two or more groups are investigated for significant survival diferences. To answer the second question, one of the ways of estimating $h _ { 0 } ( t )$ is by using the Breslow estimator [21]. To demonstrate this, suppose that the m times of an event are $0 < t _ { 1 } < t _ { 2 } < . . . < t _ { m }$ where $t _ { i } \neq t _ { j }$ for $i \neq j$ and each $t _ { i }$ does not include censored times. Denote $s _ { i }$ as subject with event time $t _ { i }$ . We define the risk set $R _ { i }$ as the set of all subjects $s _ { j }$ such that $t _ { j } \geq t _ { i } ; \mathrm { i . e . }$

$$
R _ {i} = \left\{s _ {j}: t _ {j} \geq t _ {i} \right\}.\tag{6}
$$

Using these ordered event times, the probability that the subject $s _ { i }$ experiences the event at time $t _ { i }$ is the ratio of its hazard at $t _ { i }$ to the sum of the hazards of all subjects who are available to get the event at $t _ { i } ,$ that is

$$
\mathbb {P} (s _ {i} | t _ {i}) = \frac {h _ {0} (t _ {i}) e ^ {\boldsymbol {\beta} \cdot \boldsymbol {x} _ {s _ {i}}}}{\sum_ {s _ {j} \in R _ {i}} h _ {0} (t _ {i}) e ^ {\boldsymbol {\beta} \cdot \boldsymbol {x} _ {s _ {j}}}} = \frac {e ^ {\boldsymbol {\beta} \cdot \boldsymbol {x} _ {s _ {i}}}}{\sum_ {s _ {j} \in R _ {i}} e ^ {\boldsymbol {\beta} \cdot \boldsymbol {x} _ {s _ {j}}}},
$$

where $\boldsymbol { x } _ { s _ { i } }$ are the covariates for subject $s _ { i }$ . It can be seen that this probability is independent of $t _ { i }$ but depends on the order of the occurrences of the events.

Breslow’s estimator for the baseline hazard and cumulative hazard is given by

$$
\hat {h} _ {0} (t _ {i}) = \frac {1}{\sum_ {s _ {j} \in R _ {i}} e ^ {\boldsymbol {\beta} \cdot \boldsymbol {x} _ {s _ {j}}}}; \quad \hat {H} _ {0} (t) = \sum_ {t _ {i} \leq t} \hat {h} _ {0} (t _ {i}),
$$

and the corresponding likelihood function $\mathcal { L } ( \beta )$ (called the partial likelihood because it only accounts for unique uncensored event times) and log-likelihood $\ell ( \beta )$ are given by

$$
\mathcal {L} (\boldsymbol {\beta}) = \prod_ {i = 1} ^ {m} \frac {e ^ {\boldsymbol {\beta} \cdot \boldsymbol {x} _ {s _ {i}}}}{\sum_ {s _ {i} \in R _ {i}} e ^ {\boldsymbol {\beta} \cdot \boldsymbol {x} _ {s _ {j}}}}; \quad \ell (\boldsymbol {\beta}) = \sum_ {i = 1} ^ {m} \left[ \boldsymbol {x} _ {s _ {i}} \cdot \boldsymbol {\beta} - \log \sum_ {s _ {j} \in R _ {i}} e ^ {\boldsymbol {\beta} \cdot \boldsymbol {x} _ {s _ {j}}} \right].\tag{7}
$$

## 3.3. Implementation of Cox PH models

Implementing the Cox PH models can be categorized mainly into ordinary and regularized regression, tree-based and ensemble models, and deep learning approaches. In the programming language Python, these three categories have been implemented by popular libraries such as lifelines [20], scikit-survival [22] and $p y .$ cox [23, 24]. Our implementation choice is that of scikit-survival because of its seamless integration with the scikit-learn [25] library (and thus allows the use of most of its functionalities such as cross-validation and hyperparameter tuning).

Diferent algorithms were explored in scikit-survival including ordinary Cox regression, regularized Cox regression, random survival forest [15], extratrees, and gradient boosting [26, 27]. Of all these, the gradient boosting algorithm was able to capture the feature-label relation most as quantified by the metrics considered. The gradient boosting algorithm is similar to how random forest works but difers in how built trees are combined. While random forest averages the predictions made by fitted trees, gradient boosting builds greedily and sequentially (additively) such that a new tree (called base or weak learner) is added by fitting it on the residuals of the previous tree. Thus, the overall model f (which takes the role ${ \pmb x } \cdot { \pmb \beta } )$ is given as

$$
f (\boldsymbol {x}) = \sum_ {i = 1} ^ {N _ {T}} w _ {i} g _ {i} (\boldsymbol {x}; \theta_ {i});\tag{8}
$$

where $N _ { T }$ is the total number of base learners, $w _ { i }$ are weights, and $g _ { i }$ is a function that represents each tree structure parameterized by $\theta _ { i }$ . The partial log-likelihood function in Equation (7) is modified by replacing ${ \boldsymbol { x } } \cdot { \boldsymbol { \beta } }$ with $f$ and introducing the binary random variable in Equation (1) to allow the following optimization problem on the uncensored unique event times:

$$
\arg \max _ {f} \sum_ {i = 1} ^ {m} \delta_ {i} \left[ f (\boldsymbol {x} _ {s _ {i}}) - \log \sum_ {s _ {j} \in R _ {i}} e ^ {f (\boldsymbol {x} _ {s _ {j}})} \right].
$$

Three metrics were considered for evaluating the chosen model: the concordance index (C-index), the cumulative dynamic receiver operating characteristic curve (cumulative dynamic AUC), and the integrated Brier score. The C-index measures the rank correlation between the predicted risk scores and observed event times. To define it, we need to define concordance. Given two subjects s<sub>i</sub> and $s _ { j } .$ they are said to be comparable if their observed event times $t _ { i } , t _ { j }$ satisfies $t _ { j } > t _ { i }$ and $\delta _ { i } = 1$ ; i.e., the subject with lower observed time experienced the event. Comparable subjects $s _ { i } , s _ { j }$ are said to be concordant if their predicted risks $\hat { r } _ { i } , \hat { r } _ { j }$ satisfies $\hat { r } _ { i } > \hat { r } _ { j }$ and $t _ { j } > t _ { i } ;$ i.e. the subject with lower risk has a larger observed survival time (and vice versa). Thus, the C-index is the ratio of the number of concordant pairs to the number of comparable pairs:

$$
\text { C - index } = \frac {\# \text {   concordant   pairs }}{\# \text {   comparable   pairs }}.\tag{9}
$$

In situations of equal predicted risk scores for a comparable pair, the number of concordant pairs is incremented by 0 5 instead of 1. To define the cumulative dynamic AUC, it is necessary to introduce cumulative and dynamic subjects. The former are all subjects that experience an event before or at time t (all subjects $s _ { i }$ such that $t _ { i } \leq t )$ and the later are subjects whose survival times satisfy $t _ { i } > t .$ . Following these definitions, the cumulative dynamic AUC measures the efectiveness of a fitted survival model to distinguish cumulative from dynamic subjects:

$$
\operatorname{AUC} (t) = \frac {\sum_ {i = 1} ^ {n} \sum_ {j = 1} ^ {n} \mathbb {1} (t _ {j} > t) \mathbb {1} (t _ {i} \leq t) \omega_ {i} \mathbb {1} \left(\hat {r} (\boldsymbol {x} _ {s _ {j}}) \leq \hat {r} (\boldsymbol {x} _ {s _ {i}})\right)}{\left[ \sum_ {i = 1} ^ {n} \mathbb {1} (t _ {i} > t) \right] \left[ \sum_ {i = 1} ^ {n} \mathbb {1} (t _ {i} \leq t) \omega_ {i} \right]}
$$

Here, 1 is an indicator function, $\omega = 1 / \hat { G } ( t )$ is the inverse probability of censoring weights (IPCW) estimated from the Kaplan–Meier estimate of the censoring survival function (i.e Kaplan–Meier formula applied to censored times in which censored times are treated as failure times and vice versa), $\hat { G } ( t )$ , defined by

$$
\hat {G} (t) = \prod_ {\{i | t _ {i} <   t \}} 1 - \frac {n _ {i}}{| R _ {i} |},\tag{10}
$$

where $n _ { i }$ is the number of subjects that fail at time $t _ { i }$ and $R _ { i }$ is the risk set defined in Equation (6).The function ${ \hat { r } } ( { \boldsymbol { x } } )$ is the model’s predicted risk score for a subject with covariate x. For an ordinary Cox regression, it is estimated by ${ \hat { r } } ( { \pmb x } ) = { \pmb x } \cdot { \pmb \beta }$ while for a gradient boosting ensemble model (as in the case of this study), it is estimated by ${ \hat { r } } ( { \pmb x } ) = f ( { \pmb x } )$ where $f$ is as defined in Equation (8). To summarize this metric, its mean value over a time range $t \in [ a , b ]$ is considered:

$$
\overline {{\mathrm{AUC}}} (a, b) = \frac {1}{\hat {S} (a) - \hat {S} (b)} \int_ {a} ^ {b} \mathrm{AUC} (t) d \hat {S} (t)\tag{11}
$$

where $\hat { S } ( t )$ is the estimated survival function. As for the time-dependent Brier score, it measures the mean squared error of survival states at time t:

$$
\operatorname{BS} (t) = \frac {1}{n} \sum_ {i = 1} ^ {n} \left[ \mathbb {1} (t _ {i} \leq t \land \delta_ {i} = 1) \frac {(0 - \hat {\pi} (t | \boldsymbol {x} _ {s _ {i}})) ^ {2}}{\hat {G} (t _ {i})} + \mathbb {1} (t _ {i} > t) \frac {(1 - \hat {\pi} (t | \boldsymbol {x} _ {s _ {i}})) ^ {2}}{\hat {G} (t)} \right]
$$

where ${ \hat { \pi } } ( t | x )$ is the model’s predicted probability of remaining event-free up to time t for a given covariate $( \mathrm { i . e . , } \ \hat { S } ( t )$ for a subject or sample with covariate $\pmb { x } ) _ { - } ^ { \prime }$ ; and $\hat { G } ( t )$ is the Kaplan–Meier estimate of the censoring survival function given by Equation (10). The corresponding integrated Brier score calculated in the time interval $t \in [ a , b ]$ is given by

$$
\operatorname{IBS} (a, b) = \int_ {a} ^ {b} \operatorname{BS} (t) d w (t); \quad w (t) = t / b.\tag{12}
$$

The scikit-survival implementation of all these metrics was considered and further information can be found in the library documentation. To the best of our knowledge, there are no standardized benchmarks for the values of each of the metrics in the literature and thresholds are treated case-by-case based on the nature of the problem under consideration. Moreover, the literature reviewed in this study (see [24, 15, 22]) has reported $\ge 0 . 6 5$ for C-index/cumulative dynamic AUC; and $\leq 0 . 2 5$ for integrated Brier score.

## 3.4. Data modelling

In this study, two groups of features were used as covariates for the Cox PH models. The first group was extracted from the charge voltage curves and the second from the discharge voltage curves. The two groups were engineered from the first n cycles of the corresponding profile, where the integer $n \in [ 2 , 1 0 0 ]$ is chosen via cross-validation. The choice of this cycle number interval was motivated by the notion of using the minimum cycle data possible for modelling. Information from these curves was extracted via path signatures. This extraction involves creating a two-dimensional path $X _ { t } ~ = ~ \{ t , V ( t ) \}$ where t (in minutes) and $V ( t )$ are the time and voltage values respectively. Signatures up to depth k were then extracted from this path using the iisignature Python library [28]; see the Methods section for the mathematical description and properties of the signature transform. The signature depth, $k \in \{ 2 , 3 , 4 \}$ was tuned to balance between model accuracy and computational complexity. The higher the value of $k ,$ the more information is derived from the voltage-time profile, however, the higher the feature space dimension and thus the more complex the resulting model. In particular,

$$
\operatorname{Sig} ^ {k} \circ X _ {t} ^ {i} := \left(S ^ {1}, S ^ {2}, S ^ {1, 1}, S ^ {1, 2}, S ^ {2, 1}, \dots , S ^ {i _ {1}, \dots , i _ {k}}\right)
$$

are the truncated signatures of depth k of a time-voltage path of cycle i corresponding to a given cell. The matrix of signatures of the time-voltage path was then calculated for the first n cycles resulting in

$$
\operatorname{Sig} ^ {k} \circ X _ {t} ^ {1: n} := \left[ \begin{array}{c c c c c c c} S _ {1} ^ {1} & S _ {1} ^ {2} & S _ {1} ^ {1, 1} & S _ {1} ^ {1, 2} & S _ {1} ^ {2, 1} & \ldots & S _ {1} ^ {i _ {1}, \ldots , i _ {k}} \\ S _ {2} ^ {1} & S _ {2} ^ {2} & S _ {2} ^ {1, 1} & S _ {2} ^ {1, 2} & S _ {2} ^ {2, 1} & \ldots & S _ {2} ^ {i _ {1}, \ldots , i _ {k}} \\ S _ {3} ^ {1} & S _ {3} ^ {2} & S _ {3} ^ {1, 1} & S _ {3} ^ {1, 2} & S _ {3} ^ {2, 1} & \ldots & S _ {3} ^ {i _ {1}, \ldots , i _ {k}} \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ S _ {n} ^ {1} & S _ {n} ^ {2} & S _ {n} ^ {1, 1} & S _ {n} ^ {1, 2} & S _ {n} ^ {2, 1} & \ldots & S _ {n} ^ {i _ {1}, \ldots , i _ {k}} \end{array} \right] \in \mathbb {R} ^ {n \times 2 (2 ^ {k} - 1)}.\tag{13}
$$

Then, a path $P ^ { c } = \{ i , ( { \mathrm { S i g } } ^ { k } \circ X _ { t } ^ { 1 : n } ) _ { c } \}$ consisting of cycles $i \in [ 1 , n ]$ as the first component and column c of the matrix $\operatorname { S i g } ^ { k } \circ X _ { t } ^ { 1 : n }$ as the second component was formed. Finally, the truncated signatures of $P ^ { c }$ were calculated up to depth k for each column $^ { c , }$ and the resulting vectors were stacked horizontally forming a single vector for each cell. Thus for a cell, its corresponding stacked row feature vector is given by

$$
\boldsymbol {f} _ {\text { cell }} := \left(\operatorname{Sig} ^ {k} \circ P ^ {1}, \operatorname{Sig} ^ {k} \circ P ^ {2}, \operatorname{Sig} ^ {k} \circ P ^ {3}, \dots , \operatorname{Sig} ^ {k} \circ P ^ {2 (2 ^ {k} - 1)}\right) \in \mathbb {R} ^ {4 (2 ^ {k} - 1) ^ {2}},\tag{14}
$$

where each of $\mathrm { S i g } ^ { k } \circ P ^ { c }$ has exactly $2 ( 2 ^ { k } - 1 )$ elements.

The target for survival analysis is a structured array in which each element is the pair $( T , \delta )$ where T and δ are the EOL and the binary random variable defined in Equation (1) respectively. Thus, the target vector y of all 362 cells considered in this research is given by

$$
\boldsymbol {y} := \left[ \begin{array}{c} (T _ {1}, \delta_ {1}) \\ (T _ {2}, \delta_ {2}) \\ (T _ {3}, \delta_ {3}) \\ \vdots \\ (T _ {3 6 2}, \delta_ {3 6 2}) \end{array} \right].
$$

## 3.5. Model training

As described in Section 3.3, the model of choice is the gradient boosting implementation of the Cox PH model. Two models were proposed based on whether they use features extracted from charge or discharge data regime: the charge, and discharge models; see Table 2 for the summary of each model description. The charge model was trained using the features extracted from the charge voltage profiles of the first n cycles for each cell. On the other hand, the discharge model was built on top of features engineered from the CC discharge voltage.

The rationale behind these proposed models is as follows. When there is data that captures the protocol-to-protocol or cycling conditions variabilities, the charge model can be built to predict the survival and hazard functions of cells. On the other hand, when the available data captures the cell-to-cell variability (a situation where all cells are cycled identically to capture the intrinsic properties of cells), then the discharge model will be preferred. Thus, these two modelling options were proposed to handle the two well-known cycling options and to show their robustness (to diferent data regimes) and versatility.

For the two models, the 80-20% train-test split strategy was adopted, and hyperparameter tuning was achieved via a grid search using the C-index as the scoring metric. The train-test splitting was done in a way that each batch maintains the split ratio in the train and test set to ensure unbiased representation. Each model was trained and evaluated across 100 train-test splits (each split was randomly generated). This ensures that accurate and representative performance metrics are obtained for each model. Performance metrics on the test set were estimated using the three metrics defined in Equations (9), (11) and (12).

Table 2: Description of the proposed survival models considered in this study. Predicted survival probability is denoted as S<sup>ˆ</sup> (t) and cumulative hazard function as H<sup>ˆ</sup> (t), which are the estimates of S (t) (given in Equation (3)) and H(t) (given in Equation (4)) respectively.

<table><tr><td>Model name</td><td>Model input</td><td>What is predicted</td></tr><tr><td>Charge model</td><td>Charge voltage profiles of the first n cycles were used to extract features in Equation (14) for each cell.</td><td> $\hat{S}(t)$  and  $\hat{H}(t)$ </td></tr><tr><td>Discharge model</td><td>CC discharge voltage profiles of the first n cycles were used to extract features in Equation (14) for each cell.</td><td> $\hat{S}(t)$  and  $\hat{H}(t)$ </td></tr></table>

## 4. Results and discussion

## 4.1. Choosing the signature depth and number of cycles of data for modelling

Central to this study is the choice of the number of cycles of data required to achieve accurate models. To accomplish this, 50 cycles worth of data was first fixed for both the charge and discharge models to choose the right value of signature depth k. As discussed in Section 3.4, $k \in \{ 2 , 3 , 4 \}$ was considered and the crossvalidated results (using the C-index) on the train data are presented in Figure 4(a). The C-index in both charge and discharge models significantly increases as k rises from 2 to 3, however, the diference at $k = 3$ and k = 4 is less significant. While this trend may not apply consistently for $k > 4 , k = 3$ was chosen for signature depth in extracting features from charge and discharge data regimes.

As for choosing the number of cycles n of data for modelling, integer values $n \in [ 2 , 1 0 0 ]$ were considered. Features under each cycle were fed to the charge and discharge models for cross-validation on the training data. The results of this experiment are presented in Figure 4(b). It was observed that each model’s performance increases between cycles 2 and 50, but approximately remain the same over the rest of the cycles. In this regard, the optimal cycle number was chosen to be 50 throughout the rest of the experiments performed in this study.

Further in this experiment, it was observed that the charge model appears less sensitive to changes in the selected signature depth and cycle threshold than the discharge model. This is because inter-cycle variability in voltage curves is more significant in the discharge data than in the charge data. As a result, the discharge model is expected to be more sensitive to both changes in signature depth and cycle number; this finding also agrees with the results of Section 4.4.

![](11-Ibraheem-2025_images/0fde83948015d26a91bfa34976046dceba3b46e5f9457dc12d01604bee1d82e0.jpg)  
Figure 4: Choosing optimal (a) signature depth for feature extraction and (b) number of cycles of data for modelling. For brevity, 50 cycles were fixed to observe the efect of signature depth on model performance. Signature depth k = 3 was chosen as optimal depth and was used to extract features under diferent cycle number thresholds to show the efect of varying cycle numbers on model performance. Lastly, 50 cycles worth of data was chosen as the optimal threshold for all other experiments in this study.

## 4.2. Model performance

The performance metrics of the charge and discharge models calculated on the test set are given in Table 3. In both models, the performance across the 100 traintest splits is consistent and this is evident in the low standard deviation (≈ 0 03 for all models and metrics). In addition, both models perform similarly on the test set and this implies that the modelling methodology employed in this research is robust to diferent data regimes used for feature extraction. Thus, if either cell-tocell or protocol-to-protocol variabilities need to be captured, the proposed models can be used for the early prediction of battery survival probability and hazard rate curves.

Figures 5 and 6 show the predicted survival and cumulative hazard functions for the test cells in each batch. For brevity, only results obtained under the discharge model were presented. It can be seen that each batch has diferent survival patterns which suggests there is a significant variability in degradation across batches. This trend is also repeated within a batch. The variability in survival can be linked to diferences in cells’ intrinsic properties as survival is taken as a function of features extracted from the identically discharged voltage curves.

Table 3: Performance metrics of the charge and discharge models on the test set. The mean ( ¯x) and standard deviation (<sub>σ</sub>) of the metrics were calculated across 100 train-test splits. Both the cumulative dynamic AUC and integrated Brier score were calculated for t ∈ [500 1000]. For both C-index and cumulative dynamic AUC (both in the range [0 1]), the higher they are the better the model while the reverse is the case for the integrated Brier score.

<table><tr><td rowspan="2">Model</td><td colspan="2">C-index</td><td colspan="2">Cumulative dynamic AUC</td><td colspan="2">Integrated Brier score</td></tr><tr><td> $\bar{x}$ </td><td> $\sigma$ </td><td> $\bar{x}$ </td><td> $\sigma$ </td><td> $\bar{x}$ </td><td> $\sigma$ </td></tr><tr><td>Charge</td><td>0.7944</td><td>0.0281</td><td>0.9015</td><td>0.0269</td><td>0.1122</td><td>0.0163</td></tr><tr><td>Discharge</td><td>0.8098</td><td>0.0302</td><td>0.9149</td><td>0.0248</td><td>0.1046</td><td>0.0152</td></tr></table>

![](11-Ibraheem-2025_images/f37dcab404595cdc6c097c992c0eca582328ce3f68993ef208dcb13a542ed1d0.jpg)

![](11-Ibraheem-2025_images/85f2cb55e1e87e1245785133218d5ea463334bb712a9b75611bfa335f63ecceb.jpg)

![](11-Ibraheem-2025_images/1758183e52b297800348991faa4da1cfdeb0b83a8fd23962fa6d20082912ac74.jpg)

![](11-Ibraheem-2025_images/346f7e6a50f6551b35551a698d9b556682da3d4640a941fe10eb383449d2ef72.jpg)

![](11-Ibraheem-2025_images/b653bc9c57a81bd3a6aa2e913d7e00f0ced336660a29bcc7b98d771ce40f3f5b.jpg)

![](11-Ibraheem-2025_images/5497c20140022b0deb32fe49222495b63be8672073e7513cd9b942297fb30bcb.jpg)

![](11-Ibraheem-2025_images/0809aec06600f8c6f2e90e954a795a7df9e4d408111dc2d87ba2d098efbe553f.jpg)

![](11-Ibraheem-2025_images/fed59169eab15481e3d238116bfffa1aa3d2c2be2e2f6fbd370c7f426e8f8fde.jpg)  
Figure 5: Predicted survival probabilities for the test data using the discharge model. Survival functions for all cells in each batch ((a)-(i) correspond to batches b1-b8 respectively) are plotted in a single figure block.

![](11-Ibraheem-2025_images/464c4ab02377a2318b012c17478d2b8ec8aa577c601df48cd8a7504456f2f46e.jpg)  
Figure 6: Predicted cumulative hazards for the test set using the discharge model. Each cumulative hazard is transformed using log $( 1 + { \hat { H } } ( t ) )$ to see diferences within a batch. Cumulative hazards for all cells in each batch ((a)-(i) correspond to batches b1-b8 respectively) are plotted in a single figure block.

## 4.3. Efect of number of training samples on model performance

This section focuses on the efect of varying the number of training samples on the models’ performances. This experiment is motivated by two practical reasons: (i) a practical model should improve in accuracy as the number of training samples increases; (ii) we want to investigate how the proposed models perform under small training samples. For this experiment, we fixed a train-test split (80-20%), and then sampled (without replacement) a given fraction of cells from the whole training set. These sampled cells were then used to train the charge and discharge models. The resulting models were evaluated on the fixed test set. We considered sample fractions in the set {0 2 0 3 1 0}. Each sample fraction was repeated 100 times and the corresponding metrics were averaged. The results of this investigation are presented in Figure 7. As expected, both models’ accuracy improves (C-index and cumulative dynamic AUC increases while the integrated Brier score decreases accordingly) as the sample fraction increases. The proposed models demonstrate robust performance in our experiments even with limited training data. Specifically, under scenarios with low sample sizes, the model consistently achieves high accuracy (C-index, cumulative dynamic AUC, and integrated Brier score of approximately 0.72, 0.84, and 0.18 for both models) compared to the highest sample fraction of 1.0 (C-index, cumulative dynamic AUC, and integrated Brier score of approximately 0.82, 0.93, and 0.10 for both models), indicating its efectiveness in data-scarce environments. This performance can be attributed to the quality of features (signatures) extracted from the charge and discharge regimes.

![](11-Ibraheem-2025_images/9475030f765ae5f42167da4f10ce832295bbee07fd6685ef68a1fdd455aa3b69.jpg)  
Figure 7: Results of the training sample increment experiment. The charge and discharge models were trained on varying sample fractions from the whole training set and then validated on a fixed test set. The averaged metric value is presented at each sample fraction for (a) C-index, (b) cumulative dynamic AUC, and (c) integrated Brier score.

## 4.4. Low-cycle prediction experiment

The feature extraction technique introduced in Section 3.4 allows for the use of diferent numbers of cycles of data when training models and when using trained models for inferences. This is because the final feature vector of Equation (14) will always have a fixed length (for a given signature depth) regardless of the number of rows of the matrix in Equation (13). However, as the number of rows of the matrix increases (i.e. increasing the number of cycles of data used), more information is expected to be derived from the voltage of a given data region. In this section, we investigate the performance of the proposed models when they are trained on the first 50 cycles worth of data but making predictions with a lower number of cycles of data. This experiment is applicable in a low-data situation at inference time. Each model was trained on training data with 50 cycles worth of voltage profiles and then evaluated on test data with an increasing number of cycles (integer cycle numbers $n \in [ 3 , 5 0 ]$ were considered). This procedure was repeated 100 times for each testing cycle using a diferent random train-test split at each repetition. The resulting performance metrics were averaged over the considered repetitions.

The results of this experiment are presented in Figure 8. For the charge model, model performance improves steadily in the first 10 cycles but becomes less significant over the rest of the cycle numbers. On the other hand, the discharge model’s performance rises slightly in the first 10 cycles, remains approximately the same between cycles 10 and 30, and eventually increases from cycle 20 until it plateaus at the 40-cycle mark. These results suggest that the charge model shows a significant level of robustness in a low-data prediction situation with C-index and cumulative dynamic AUC climbing over 0 75 in $1 0 \leq n \leq 3 0$ . In contrast, when using low-cycle numbers $( n \leq 3 0 )$ in the discharge regime, the C-index and cumulative dynamic AUC values are approximately 0 5, indicating a limited predictive accuracy in these low-cycle scenarios. The reason behind the diference in robustness is not far-fetched. Cycle-to-cycle variability in voltage curves is more pronounced in the discharge data region than the charge counterpart, thus the resulting model is expected to be more sensitive to the cycle number drift at inference time.

![](11-Ibraheem-2025_images/2a4a3a698c2ee42b27804b7fd69ce7d0e4a55f6233435f41af5f2faf232a3da3.jpg)  
Figure 8: Results of the low-cycle prediction experiments. The charge and discharge models were trained on features extracted from 50 cycles of voltage profiles but validated on features obtained under diferent cycle number thresholds. The charge model was observed to be more robust under low-cycle data situations at inference time. The averaged metric value is presented at each cycle number threshold for (a) C-index, (b) cumulative dynamic AUC, and (c) integrated Brier score.

## 4.5. Efect of voltage curve sparsity on model performance

In this section, we investigate the impact of data sparsity on the predictive performance of the proposed models. By data sparsity, we mean systematically considering only voltage values recorded at every index step $i \in \{ 1 , 2 , 3 , \ldots , 1 0 \}$ For instance if $V ~ = ~ [ 2 . 0 , 2 . 5 , 3 . 0 , 3 . 5 , 4 . 0 ]$ and $i \ = \ 2$ , the corresponding sparse $V _ { \mathrm { s p a r s e } } = [ 2 . 0 , 3 . 0 , 4 . 0 ]$ . Note that the case i = 1 gives the original voltage curve and this was considered for benchmark purposes. To obtain more representative results, each case of i was repeated 100 times using a diferent random train-test split at each repetition. We considered two cases of sparsity: (i) sparsity at the training data level, where sparsity was introduced to voltage curves used for training models, and (ii) sparsity at the test data level, where sparsity was considered in the voltage curves used for model testing.

The results of this investigation are presented in Figure 9. In both sparsity cases, the discharge model was robust to every resulting sparse voltage curve and its performance was relatively the same compared to the original voltage curves (when i = 1). In contrast to the charge model, model performance decreases as the degree of voltage curve sparsity increases, suggesting that the charge model is less robust. The diference in sparsity is most likely due to the induced variation in the voltage curves. Because the charge model used the charge voltage values and variations in the charge data region are induced by the diferent charging protocols, it will be more sensitive to the distribution of recorded measurements and value omission. In addition, within a given charge voltage curve, at least 3 diferent charging policies were employed, and thus more variations are introduced into voltage value distributions. However, the discharge model utilized data from the discharge data region, where variabilities are only induced by the intrinsic diferences of the cells as the cells were discharged identically. As a result, the corresponding voltage distribution geometry will be conserved even in the presence of systematic sparseness. Another factor that is likely to contribute to the significant diference in sparsity robustness is the duration of each data region considered. The CC discharge regime takes approximately 15 minutes for the maximum cycle 50 while that of the charge takes between 9 to 13 minutes (see Figure 1). Given that data are recorded at the same rate in both regions, more points are expected to be concentrated at the CC discharge than at the charge region, thus resulting in a diferent degree of sparsity at the same index step.

![](11-Ibraheem-2025_images/cd2ea5688c3395af9c639ffe4494ab4290750c3da82673bfe71af8e49a076d3d.jpg)  
Figure 9: Efect of voltage curve sparsity on the proposed models’ performance. Sparsity was introduced at training (a-c) and test (d-f) data levels. It was observed that the discharge model was more robust to the systematic sparsity introduced at both levels.

## 5. Conclusion

A study has been carried out using diferent battery data regimes to develop battery survival models. We have proposed battery survival models which work seamlessly with features extracted from either the charge or discharge regime. This is outstanding as the models cater for both protocol-to-protocol diferences (using diferent cycling conditions) and cell-to-cell variabilities (when cells are cycled identically). The models are meant to be used for making predictions at the early life of batteries taking only the first 50 cycles of the voltage profiles. In addition, the models are robust to small training samples and decent/accurate predictions can be achieved even at low training sample rates. When more training data are available, the proposed models’ performances have been shown to improve steadily. All models were trained on an HP EliteBook 850 G7 Notebook PC with 32 GiB RAM and 1 0 TB Disk capacity. Each model training takes approximately 20 78 seconds (wall-clock time) to run for the dataset considered in this study.

We conducted additional real-life application-driven experiments: (i) robustness to low-cycle data at prediction time, and (ii) robustness to data sparsity at both training and inference time. Both proposed models show a significant degree of robustness when given less than 50 cycles worth of data at prediction time. In this case, the charge model showed a more significant robustness. On data sparsity, we carried out a systematic sub-sampling of voltage values at diferent degrees both at training and test data levels. The discharge model accuracy maintains its predictive performance at all sparsity degrees and levels while the charge model performance decays as the sparsity rate rises. This is an indication that the discharge model is preferable for a sparsity-aware application.

The predicted cells’ survival and cumulative hazard functions are great tools for battery manufacturers and fleet operators. They can be used to adjust the battery warranty and schedule data-informed maintenance. In terms of future research, other known data regimes such as the Electrochemical Impedance Spectroscopy (EIS) and Reference Performance Test (RPT) data could be investigated for potential data for feature extraction to further show the versatility and robustness of the proposed methods.

## Methods

## Introduction to signature method

The signature method is a set of feature extraction strategies for multivariate time series data. It takes a continuous, piecewise smooth path representing the multivariate time series and transforms it into a sequence of real numbers that encode the area, segmental, and geometric information of such path over a real interval. The truncated sequence (of fixed length) of the transform can then be used as features for any machine learning task such as supervised learning. Its application to machine learning problems has been studied extensively. This includes, among others, sound compression [29], handwriting character recognition [30], detecting hand-to-face touch with supervised contrastive learning [31], and early detection of sepsis in patients [32]. More recently, its application in the prediction of battery lifetime was introduced in [7] where signatures of a two-dimensional path consisting of the time and the discharge voltage of the CC were used as features for machine learning models that predict the full capacity and IR curves. In light of the success above of the signature method, we adopted it in this research with an additional layer to capture signature changes as a function of cycle number; see Section 3.4 for how the signature method was deployed in this research.

After giving high-level information about the signature, we delve into its mathematical build-up and structures. We first define a path, iterated integrals and finally present a formal definition of path signature.

Definition 5.1 (Path). A d-dimensional real-valued path $X _ { t }$ is a continuous mapping from a real interval $[ a , b ] \ni t$ into a d-dimensional real space:

$$
X _ {t} = \{X _ {t} ^ {1}, X _ {t} ^ {2}, X _ {t} ^ {3}, \ldots X _ {t} ^ {d} \}: [ a, b ] \mapsto \mathbb {R} ^ {d}.\tag{15}
$$

Definition 5.2 (Iterated integral [17]). Suppose $X _ { t }$ is a real d-dimensional, continuous piecewise smooth path defined on $[ a , b ]$ as given in Equation (15). Then the k-th level iterated integral ofX<sub>t</sub> is given by

$$
S (X _ {t}) _ {a, t} ^ {i _ {1}, \ldots , i _ {k}} := \int_ {a <   t _ {k} <   t} \dots \int_ {a <   t _ {1} <   t _ {2}} d X _ {t _ {1}} ^ {i _ {1}} \ldots d X _ {t _ {k}} ^ {i _ {k}},\tag{16}
$$

where $i _ { 1 } , \ldots , i _ { k } \in \{ 1 , \ldots , d \}$

Definition 5.3 (Signature [17]). The path signature of $X _ { t }$ over $[ a , b ]$ is defined as an infinite sequence of all possible calculated iterated integrals defined in Equation (16):

$$
S i g \circ X _ {t} := \left(1, S (X _ {t}) _ {a, b} ^ {1}, S (X _ {t}) _ {a, b} ^ {2}, S (X _ {t}) _ {a, b} ^ {1, 1}, S (X _ {t}) _ {a, b} ^ {1, 2}, \ldots , S (X _ {t}) _ {a, b} ^ {i _ {1}, \ldots , i _ {k}}, \ldots\right).
$$

If the sequence is truncated at depth k (as in the case offeature extraction for machine learning task), then we obtain a truncated signature of $X _ { t }$ (of fixed length) given by

$$
S i g ^ {k} \circ X _ {t} := \left(1, S (X _ {t}) _ {a, b} ^ {1}, S (X _ {t}) _ {a, b} ^ {2}, S (X _ {t}) _ {a, b} ^ {1, 1}, S (X _ {t}) _ {a, b} ^ {1, 2}, \dots , S (X _ {t}) _ {a, b} ^ {i _ {1}, \dots , i _ {k}}\right).
$$

Usually, the first value of the sequence $\operatorname { S i g } ^ { k } \circ X _ { t }$ is omitted during feature extraction as this will be constant for all samples. An example of the signature of a two-dimensional continuous piecewise path $X _ { t } = \{ f ( t ) , g ( t ) \}$ } calculated up to depth $k = 2$ is

$$
\begin{array}{c} \operatorname{Sig} ^ {2} \circ X _ {t} = \left(1, \int_ {a} ^ {b} f ^ {\prime} d t, \int_ {a} ^ {b} g ^ {\prime} d t, \int_ {a} ^ {b} \left[ \int_ {a} ^ {t _ {2}} f ^ {\prime} (t _ {1}) d t _ {1} \right] f ^ {\prime} (t _ {2}) d t _ {2}, \int_ {a} ^ {b} \left[ \int_ {a} ^ {t _ {2}} f ^ {\prime} (t _ {1}) d t _ {1} \right] g ^ {\prime} (t _ {2}) d t _ {2}, \right. \\ \left. \int_ {a} ^ {b} \left[ \int_ {a} ^ {t _ {2}} g ^ {\prime} (t _ {1}) d t _ {1} \right] f ^ {\prime} (t _ {2}) d t _ {2}, \int_ {a} ^ {b} \left[ \int_ {a} ^ {t _ {2}} g ^ {\prime} (t _ {1}) d t _ {1} \right] g ^ {\prime} (t _ {2}) d t _ {2}\right). \end{array}
$$

Properties ofsignature transform

The path signature has some properties that make it natural to extract information from a time series data that can be carved into a path. These properties also enable signatures to be used for various machine-learning tasks. We state and discuss three of these properties in this section which most relate to feature extraction and machine learning; see [17, 33] for the details of other properties. The first property focuses on the uniqueness of the signature of a path. This essentially implies that there is no loss of information from a path when its signature is calculated as its encoding.

Proposition 5.1 (Uniqueness of Path Signature [34, 17]). Suppose $X _ { t }$ is a real ddimensional, continuous piecewise smooth path defined on $[ a , b ]$ as given in Equation (15). Then $S i g \circ X _ { t }$ uniquely characterizes $X _ { t }$ up to translation.

Next, a function of the path $X _ { t }$ can be approximated by a linear function of its signature. This is called the universal nonlinearity property of signature [33, 35]. This property is applicable in a supervised learning task. For a machine learning problem of predicting a label y by learning a function $f$ of the path $X _ { t } \left( \mathrm { i . e . , } f ( X _ { t } ) = \right.$ $y )$ , the universal nonlinearity implies that we can instead learn a linear function $L$ of the signature of $X _ { t }$ without losing information about $f .$ . This is powerful as $f$ might be highly nonlinear and $X _ { t }$ might also be highly dimensional with a large number of data points.

Proposition 5.2 (Universal nonlinearity [33, 35]). Suppose $X _ { t }$ is a real d-dimensional, continuous piecewise smooth path defined on [a b] as given in Equation (15). Let f be a real-valued continuousfunction defined on all $X _ { t }$ and let C be a compact set ofall X<sub>t</sub>. Ifthe translation invariance is removedfor all $X _ { t } \in C _ { i }$ , then there exists a linear function L such that for all $X _ { t } \in C _ { i }$

$$
\left| f (X _ {t}) - L (S i g \circ X _ {t}) \right| <   \epsilon , \quad \epsilon > 0.
$$

Lastly, the signature is invariant to time reparameterisations and translation. This property is a direct consequence of the signature being a sequence of iterated path integrals. Invariance to time reparameterisation is important when encoding information about the order in which a given measured data profile arrives at a point without caring about when it precisely arrives at such a point. Thus, if one desires features that are both invariant to time parameterization and translation of the underlying path, then signature transform is a natural choice.

Proposition 5.3 (Time reparameteriation invariance [36, 17]). Suppose $X _ { t }$ is a real d-dimensional, continuous piecewise smooth path defined on $[ a , b ]$ as given in Equation (15). Let $\psi : [ a , b ] \mapsto [ a , b ]$ be a reparametrisation (a continuously diferentiable, non-decreasing, and subjectivefunction). Then $S i g \circ X _ { t } = S i g \circ X _ { \psi ( t ) }$

## Data availability

The data used for all the experiments and modelling in this research is from [1, 18] and can be downloaded from https://data.matr.io/1/.

## Code availability

The codes for all modelling and experiments performed in this research can be found in this well-documented GitHub repository: https://github.com/ Rasheed19/battery-survival.

## Funding

This project was funded by an industry-academia collaborative grant EPSRC EP/R511687/1 awarded by EPSRC & University of Edinburgh program Impact Acceleration Account (IAA).

R. Ibraheem is a PhD student in EPSRC’s MAC-MIGS Centre for Doctoral Training. MAC-MIGS is supported by the UK’s Engineering and Physical Science Research Council (grant number EP/S023291/1).

G. dos Reis acknowledges partial support from the FCT – Fundac¸ao para a˜ Ciencia e a Tecnologia, I.P., under the scope of the projects UIDBˆ /00297/2020 (https://doi.org/10.54499/UIDB/00297/2020) and UIDP/00297/2020 (https: //doi.org/10.54499/UIDP/00297/2020) (Center for Mathematics and Applications, NOVA Math). G. dos Reis acknowledges support the Faraday Institution [grant number FIRG049].

## Author contributions

All authors provided domain expertise, edited and reviewed the manuscript.

R.I.: methodology, software, visualisation, data curation, interpretation of results, writing, review and editing.

T.I.C. & T.S.: interpretation of results, review, and editing.

G.d.R.: conceptualisation, visualisation, supervision, funding acquisition, interpretation of results, writing, review and editing.

## Competing interest declaration

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Additional information

This work has no supplementary information file.

## References

[1] K. A. Severson, P. M. Attia, N. Jin, N. Perkins, B. Jiang, Z. Yang, M. H. Chen, M. Aykol, P. K. Herring, D. Fraggedakis, M. Z. Bazant, S. J. Harris, W. C. Chueh, R. D. Braatz, Data-driven prediction of battery cycle life before capacity degradation, Nature Energy 4 (5) (2019) 383–391. doi:10.1038/ s41560-019-0356-8. URL http://dx.doi.org/10.1038/s41560-019-0356-8

[2] N. H. Paulson, J. Kubal, L. Ward, S. Saxena, W. Lu, S. J. Babinec, Feature engineering for machine learning enabled early prediction of battery lifetime, Journal of Power Sources 527 (2022) 231127. doi:10.1016/j.jpowsour. 2022.231127. URL http://dx.doi.org/10.1016/j.jpowsour.2022.231127

[3] C. Strange, G. dos Reis, Prediction of future capacity and internal resistance of li-ion cells from one cycle of input data, Energy and AI 5 (2021) 100097. doi:10.1016/j.egyai.2021.100097. URL http://dx.doi.org/10.1016/j.egyai.2021.100097

[4] C. Strange, R. Ibraheem, G. dos Reis, Online lifetime prediction for lithiumion batteries with cycle-by-cycle updates, variance reduction, and model ensembling, Energies 16 (7) (2023) 3273. doi:10.3390/en16073273. URL http://dx.doi.org/10.3390/en16073273

[5] J. Hong, D. Lee, E.-R. Jeong, Y. Yi, Towards the swift prediction of the remaining useful life of lithium-ion batteries with end-to-end deep learning, Applied Energy 278 (2020) 115646. doi:10.1016/j.apenergy.2020. 115646. URL http://dx.doi.org/10.1016/j.apenergy.2020.115646

[6] R. Ibraheem, C. Strange, G. dos Reis, Capacity and internal resistance of lithium-ion batteries: Full degradation curve prediction from voltage response at constant current at discharge, Journal of Power Sources 556 (2023) 232477. doi:10.1016/j.jpowsour.2022.232477. URL http://dx.doi.org/10.1016/j.jpowsour.2022.232477

[7] R. Ibraheem, Y. Wu, T. Lyons, G. dos Reis, Early prediction of lithium-ion cell degradation trajectories using signatures of voltage curves up to 4-minute sub-sampling rates, Applied Energy 352 (2023) 121974. doi:10.1016/j. apenergy.2023.121974. URL http://dx.doi.org/10.1016/j.apenergy.2023.121974

[8] P. M. Attia, A. Bills, F. B. Planella, P. Dechent, G. Dos Reis, M. Dubarry, P. Gasper, R. Gilchrist, S. Greenbank, D. Howey, et al., “knees” in lithiumion battery aging trajectories, Journal of The Electrochemical Society 169 (6) (2022) 060517.

[9] C. Strange, S. Li, R. Gilchrist, G. dos Reis, Elbows of internal resistance rise curves in li-ion cells, Energies 14 (4) (2021) 1206. doi:10.3390/ en14041206. URL http://dx.doi.org/10.3390/en14041206

[10] G. K. David, K. Mitchel, Survival analysis: a Self-Learning text, Spinger, 2012.

[11] D. Kuhajda, Using survival analysis to evaluate medical equipment battery life, Biomedical instrumentation & technology 50 (3) (2016) 184–189. doi: 10.2345/0899-8205-50.3.184.

[12] E. L. Kaplan, P. Meier, Nonparametric estimation from incomplete observations, Journal of the American Statistical Association 53 (282) (1958) 457– 481. doi:10.1080/01621459.1958.10501452. URL https://www.tandfonline.com/doi/abs/10.1080/01621459. 1958.10501452

[13] D. Machin, Y. B. Cheung, M. Parmar, Survival analysis: a practical approach, John Wiley & Sons, 2006.

[14] S. Voronov, E. Frisk, M. Krysander, Data-driven battery lifetime prediction and confidence estimation for heavy-duty trucks, IEEE Transactions on Reliability 67 (2) (2018) 623–639. doi:10.1109/TR.2018.2803798.

[15] H. Ishwaran, U. B. Kogalur, E. H. Blackstone, M. S. Lauer, Random survival forests, The Annals of Applied Statistics 2 (3) (2008) 841 – 860. doi:10. 1214/08-AOAS169. URL https://doi.org/10.1214/08-AOAS169

[16] M. Santhira Sekeran, M. Zivadinovi<sup>ˇ</sup> c, M. Spiliopoulou,´ Transferability of a battery cell end-of-life prediction model using survival analysis, Energies 15 (8) (2022). doi:10.3390/en15082930. URL https://www.mdpi.com/1996-1073/15/8/2930

[17] I. Chevyrev, A. Kormilitzin, A primer on the signature method in machine learning (2016). doi:10.48550/ARXIV.1603.03788. URL https://arxiv.org/abs/1603.03788

[18] P. M. Attia, A. Grover, N. Jin, K. A. Severson, T. M. Markov, Y.-H. Liao, M. H. Chen, B. Cheong, N. Perkins, Z. Yang, P. K. Herring, M. Aykol, S. J. Harris, R. D. Braatz, S. Ermon, W. C. Chueh, Closed-loop optimization of fast-charging protocols for batteries with machine learning, Nature 578 (2020) 397–402.

[19] A. Geslin, B. van Vlijmen, X. Cui, A. Bhargava, P. A. Asinger, R. D. Braatz, W. C. Chueh, Selecting the appropriate features in battery lifetime predictions, Joule 7 (9) (2023) 1956–1965. doi:https://doi.org/10.1016/j.joule.2023.07.021. URL https://www.sciencedirect.com/science/article/pii/ S2542435123003197

[20] C. Davidson-Pilon, lifelines: survival analysis in python, Journal of Open Source Software 4 (40) (2019) 1317. doi:10.21105/joss.01317. URL https://doi.org/10.21105/joss.01317

[21] N. Breslow, Covariance analysis of censored survival data, Biometrics (1974) 89–99.

[22] S. Polsterl,¨ scikit-survival: A library for time-to-event analysis built on top of scikit-learn, Journal of Machine Learning Research 21 (212) (2020) 1–6. URL http://jmlr.org/papers/v21/20-729.html

[23] H. Kvamme, Ø. Borgan, I. Scheel, Time-to-event prediction with neural networks and cox regression, Journal of machine learning research 20 (129) (2019) 1–30. URL http://jmlr.org/papers/v20/18-424.html

[24] J. L. Katzman, U. Shaham, A. Cloninger, J. Bates, T. Jiang, Y. Kluger, Deepsurv: personalized treatment recommender system using a cox proportional hazards deep neural network, BMC medical research methodology 18 (2018) 1–12.

[25] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Thirion, O. Grisel, M. Blondel, A. Mueller, J. Nothman, G. Louppe, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cournapeau, M. Brucher, M. Perrot, E. Duchesnay, Scikit-learn: Machine learning in python, Journal of Machine Learning Research (2012). doi:10.48550/ARXIV.1201.0490. URL https://arxiv.org/abs/1201.0490

[26] J. H. Friedman, Greedy function approximation: A gradient boosting machine., The Annals of Statistics 29 (5) (Oct. 2001). doi:10.1214/aos/

1013203451. URL http://dx.doi.org/10.1214/aos/1013203451

[27] J. H. Friedman, Stochastic gradient boosting, Computational Statistics & Data Analysis 38 (4) (2002) 367–378, nonlinear Methods and Data Mining. doi:https://doi.org/10.1016/S0167-9473(01)00065-2. URL https://www.sciencedirect.com/science/article/pii/ S0167947301000652

[28] J. F. Reizenstein, B. Graham, Algorithm 1004: The iisignature library: Efficient calculation of iterated-integral signatures and log signatures, ACM Transactions on Mathematical Software 46 (1) (2020) 1–21. doi:10.1145/ 3371237. URL http://dx.doi.org/10.1145/3371237

[29] T. J. Lyons, N. Sidorova, Sound compression: a rough path approach, in: Proceedings of the 4th international symposium on Information and communication technologies, Trinity College Dublin, 2005, pp. 223–228.

[30] C. Li, X. Zhang, L. Jin, Lpsnet: a novel log path signature feature based hand gesture recognition framework, in: Proceedings of the IEEE International Conference on Computer Vision Workshops, 2017, pp. 631–639.

[31] M. R. Ibrahim, T. Lyons, Facetouch: Detecting hand-to-face touch with supervised contrastive learning to assist in tracing infectious diseases, Plos one 19 (6) (2024) e0288670.

[32] S. N. Cohen, J. Foster, P. Foster, H. Lou, T. Lyons, S. Morley, J. Morrill, H. Ni, E. Palmer, B. Wang, et al., Subtle variation in sepsis-iii definitions markedly influences predictive performance within and across methods, Scientific Reports 14 (1) (2024) 1920.

[33] P. Kidger, P. Bonnier, I. Perez Arribas, C. Salvi, T. Lyons, Deep signature transforms, Advances in Neural Information Processing Systems 32 (2019).

[34] B. Hambly, T. Lyons, Uniqueness for the signature of a path of bounded variation and the reduced path group, Annals of Mathematics 171 (1) (2010) 109–167. doi:10.4007/annals.2010.171.109. URL http://dx.doi.org/10.4007/annals.2010.171.109

[35] I. P. Arribas, Derivatives pricing using signature payofs, arXiv preprint arXiv:1809.09466 (2018).

[36] T. J. Lyons, Diferential equations driven by rough signals., Revista Matematica Iberoamericana 14 (2) (1998) 215–310.´ URL http://eudml.org/doc/39555