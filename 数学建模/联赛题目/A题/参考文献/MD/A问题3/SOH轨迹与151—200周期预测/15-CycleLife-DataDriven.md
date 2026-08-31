---
raw_title: 15-CycleLife-DataDriven
subject: 数学建模-策联杯A题
source: "Cycle life prediction of lithium-ion batteries based on data-driven methods.pdf"
status: mineru解析
parser: mineru
topics:
  - 数据驱动
  - 循环寿命预测
  - 综述
---

# Cycle life prediction of lithium-ion batteries based on data-driven methods

![](15-CycleLife-DataDriven_images/f9073cf6ca1d28acaefbf106e206d0026b2707fa57cbf7acd30ff5811d9a96ef.jpg)

Laisuo Su $^{a,*}$ , Mengchen Wu $^{a}$ , Zhe Li $^{b}$ , Jianbo Zhang $^{b,**}$

$^{a}$ Department of Mechanical Engineering, Carnegie Mellon University, Pittsburgh, PA, USA

$^{b}$ State Key Laboratory of Automotive Safety and Energy, School of Vehicle and Transportation, Tsinghua University, Beijing, China

## ARTICLE INFO

Article history:
Received 5 December 2020
Received in revised form
30 August 2021
Accepted 22 September 2021
Available online 24 September 2021

Keywords:  
Lithium-ion battery  
Cycle life  
Machine learning  
Feature extraction  
Neural network  
Convolutional neural network

## A B S T R A C T

Predicting the cycle life of lithium-ion batteries (LIBs) is crucial for their applications in electric vehicles. Traditional predicting methods are limited by the complex and nonlinear behavior of the LIBs, whose degradation mechanisms have not been fully understood. Recently, machine learning techniques attract increasing attention for empirically learning and predicting battery behavior. Herein, we first generate a comprehensive dataset with 104 commercial $\mathrm{LiNi_{0.8}Co_{0.15}Al_{0.05}O_2}$ /graphite 18650-series batteries under a wide range of demanding test conditions by systematically varying the ambient temperature, charge/discharge current, and cut-off voltages. Next, a linear regression model, a conventional neural network (NN) model, and a convolutional NN model are built to predict the cycle life. Models based on experts-extracted features achieve around $35\%$ of the training error and the test error. In comparison, the model based on algorithm-extracted features can achieve $9.28\%$ of the training error and $22.73\%$ of the test error. These algorithm-extracted hidden features show higher covariance (0.88) with the cycle life of LIBs than experts-extracted features (0.71). This study demonstrates the capability of machine learning techniques to capture hidden features for complex, nonlinear systems, which can be used to accurately predict their cycle life.

© 2021 Elsevier B.V. All rights reserved.

## 1. Introduction

Lithium-ion batteries (LIBs) attract extensive attention because of their high energy and power density, long life, low cost, and reliable safety compared to other commercialized batteries $[1]$ . They are considered promising power sources to substitute conventional combustion engines in vehicles to address environmental issues of greenhouse gas emissions and global warming $[2]$ . To ensure reliable and safe use in electric vehicles, LIBs need to be monitored for their voltage, temperature, state of charge (SOC), state of health (SOH), remaining capacity, and cycle life $[3–6]$ . Some of these parameters (voltage, temperature) can be directly measured from sensors, while other parameters (SOC, SOH) need to be estimated using algorithms based on measured properties $[7]$ . Predicting the cycle life of LIBs is essential but challenging, if not impossible, because LIBs are complex and nonlinear systems whose degradation mechanisms are not fully understood.

Different types of models have been built to predict the cycle life of LIBs, including empirical models, semi-empirical models, and mechanism models. Thomas et al. built empirical models to predict the life of LIBs based on data from accelerated aging experiments as part of the US Department of Energy's (DOEs) Advanced Technology Development program $[8]$ . The models describe not only the cycle life but also the uncertainty bounds. Bloom et al. performed pioneer works on building semi-empirical models to predict calendar life and cycle life of LIBs based on solid-electrolyte-interface (SEI) layer growth mechanisms $[9]$ . The models suggest that the impedance increase and power fading follow square-root-of-time kinetics. Safari et al. built a multimodal, physics-based aging model to predict the life of LIBs by assuming SEI growth at the carbonaceous anode materials as the source of capacity fade $[10]$ . The model can simulate a wide variety of battery aging profiles, such as open-circuit and constant-voltage storage, charge/discharge cycling. Semi-empirical and mechanism-based models have also been built based on lithium plating $[11]$ and active material loss $[12]$ to predict the life of LIBs. Although these models have been shown to be applicable in specific situations, developing models that can describe battery performance in general, realistic operation conditions remains challenging. Part of the challenge comes from the varieties of degradation modes that affect capacity fading of LIBs, such as loss of lithium inventory $[13]$ , loss of active material $[14]$ , mechanical degradation of electrode materials $[15]$ , and electrodes heterogeneous degradation $[16]$ . These mechanisms may couple with each other, and their contribution may vary at different aging stages. Additionally, the degradation of LIBs is path-dependent $[4,17]$ , which further complicates the prediction of the cycle life of LIBs.

Data-driven methods have recently been explored for their capability to estimate the health and capacity $[18,19]$ , the remaining useful life $[20]$ , and the cycle life $[21]$ of LIBs. The general idea is to estimate the long-term performance of LIBs based on limited tested data without considering the modes of degradation, either empirically or mechanistically $[22,23]$ . Most of the existing works require at least 25% along the trajectory to failure to accurately predict later stage performance $[24,25]$ . Severson et al., however, use the information from the first 100 cycles, when the batteries barely degrade, to predict the cycle life of $LiFePO_{4}/graphite$ LIBs and achieve a remarkably low 9.1% test error $[21]$ . Their work illustrates the promising power of data-driven techniques to predict the behavior of complex nonlinear systems. However, Kristen's study is based on one battery system ( $LiFePO_{4}/graphite$ ) under one specific cycling condition (fast-charging). The applicability of the data-driven techniques for other battery systems under more general usage conditions warrants further investigation.

Inspired by Severson's work $[21]$ , this paper applies data-driven techniques to predict the cycle life of $LiNi_{x}Co_{y}Al_{z}O_{2}/graphite$ batteries using the first 40 cycles data, using no prior knowledge of degradation mechanisms. A dataset of 104 batteries is generated using 84 different cycling conditions by varying ambient temperature, charge and discharge current, charge and discharge cut-off voltage, and holding time at the maximum and minimum voltage. Human expertise and machine learning techniques are applied to extract features relevant to the degradation of LIBs. Three different data-driven models are then built to predict the cycle life of LIBs, including a linear regression model, a neural network (NN) model, and a convolutional neural network (CNN) model. Compared to the first two models, the CNN model shows much smaller errors for both the training and the test processes. The superior performance of the CNN model comes from its ability to extract hidden features that are highly correlated to the cycle life of LIBs. We demonstrate the capability of data-driven techniques to extract hidden features of the complex, nonlinear systems from short term results for predicting their long-term behavior.

## 2. Experiments

Commercial 18650-type LIBs with $\mathrm{LiNi_xCo_yAl_zO_2}$ as the cathode material and graphite as the anode material were selected for the experiment. The nominal capacity is 2.85 Ah (tested at C/3), and the specifications of the LIBs are listed in Table 1. All cycling tests were conducted using MACCOR Series 4000 cyclers, and the ambient temperatures were controlled by three environmental chambers (GDW/JB-0100, Naya, China). Batteries were cycled three times at C/2 and room temperature (25 °C) within a voltage range of 2.5–4.2 V to obtain stable electrochemical performance before conducting other tests. A custom-designed test was then conducted to obtain the specific capacity and discharge resistance of batteries. The custom-designed test protocol included a constant current (CC) - constant voltage (CV) charge at C/2 to 4.2 V, followed with a CC-CV discharge process at C/2 to 2.5 V. The cut-off current was set to C/50 during the CV stage for both charge and discharge processes. A 10-mins rest period was embedded in the CC discharge process every 10% of SOC to monitor the resistance. A schematic of the custom-designed test protocol has been introduced in our previous publications [3].

Specification of the commercial 18650-type lithium-ion batteries.

<table><tr><td>Parameter</td><td>Specification</td></tr><tr><td>Cathode</td><td> $LiNi_{x}Co_{y}Al_{z}O_{2}$ </td></tr><tr><td>Anode</td><td>Graphite</td></tr><tr><td>Nominal capacity</td><td>2.85 Ah (at C/3)</td></tr><tr><td>Maximum charge current</td><td>1C</td></tr><tr><td>Maximum discharge current</td><td>2C</td></tr><tr><td>Charge cut-off voltage</td><td>4.2 V</td></tr><tr><td>Discharge cut-off voltage</td><td>2.5 V</td></tr><tr><td>Charge operating temperature</td><td>0–45 °C</td></tr><tr><td>Discharge operating temperature</td><td>-20 to 60 °C</td></tr></table>

A general CC-CV charge followed with a CC-CV discharge protocol was considered to cycle all LIBs, as shown in Fig. S1 (supporting information). Six parameters, including charge current, charge cut-off voltage, holding time during the charge at maximum voltage, discharge current, discharge cut-off voltage, holding time during discharge at minimum voltage, defined the CC-CV cycling protocol. Additionally, the ambient temperature was also considered as a condition because it significantly affected the cycle life of LIBs. These seven parameters were used to design the experiment for data collection. Table 2 shows the range of the parameters restrained by the specification of the batteries (Table 1). Five different levels of each parameter were selected, and a total of 86 different experimental conditions were tested on 104 batteries. The details of each experimental condition are listed in the supporting excel (SI\_ Experiment conditions).

The electrochemical performance of each battery was monitored every 50 cycles by taking it out for a reference performance test (RPT). The details of the RPT have been introduced in our previous papers [3]. The purpose of the RPT was to obtain the battery discharge capacities at C/2, C/50, and the resistances at different state-of-charge (SOC). The terminating test criterion of a battery was set to be the discharge capacity reached $50\%$ of the initial capacity. However, a few batteries that cycled at low rates were forced to stop before they reached the terminating criteria when most of the tests were finished. Batteries with capacity fading over $20\%$ are considered in this study. Codes for analyzing experimental data and building models were written in Python 3 (Jupyter notebook).

## 3. Results and discussion

## 3.1. Data generation and features extraction

Fig. 1a shows the capacity retention of the 104 tested LIBs during cycling. There is an interruption of the capacity retention for most of the tested batteries every 50 cycles. The interruption was caused by the RPT test, which had a different experimental condition compared to the cycling protocols. The RPT test showed little effect on the overall electrochemical performance and a LIB cycle life because the capacity retention returned to its original trend after a few cycles. The experimental conditions for testing the LIBs are summarized in the supporting excel (SI\_Experimental conditions). Fig. 1b shows that the cycle lives of LIBs tested under the experimental conditions of 1–36. The cycle life of a LIB was defined as the number of cycles of the battery when it reaches 80% of its initial discharge capacity. Experiments 1–18 and experiments 19–36 have the same conditions to examine the samples' repeatability. The result suggests that the two samples tested at the same experimental conditions had a similar cycle life. The averaged error of the cycle life between the two samples among the 18 experiments is 3.2% based on equation (1). The small error suggests that the testing of the LIB samples was highly repeatable, and, thus, only one sample was utilized in the rest of the 68 different experimental conditions.

The experimental range of different parameters chosen based on the specification listed in Table 1.

<table><tr><td>No.</td><td>Parameter</td><td>Range</td></tr><tr><td>1</td><td>Temperature [°C]</td><td>0–50</td></tr><tr><td>2</td><td>Charge current [C]</td><td>0.2–1</td></tr><tr><td>3</td><td>Charge cut-off voltage [V]</td><td>3.96–4.3</td></tr><tr><td>4</td><td>Holding time during the charge at max voltage [min]</td><td>0–30</td></tr><tr><td>5</td><td>Discharge current [C]</td><td>0.2–2</td></tr><tr><td>6</td><td>Discharge cut-off voltage [V]</td><td>2.4–3.5</td></tr><tr><td>7</td><td>Holding time during the discharge at min voltage [min]</td><td>0–30</td></tr></table>

(a)  
![](15-CycleLife-DataDriven_images/c7115b28aec85b9669b72d9ca77f5ef8da8e0dfaa38118bfbe22482e5c22de1a.jpg)

![](15-CycleLife-DataDriven_images/0ad3cea269f4777a7c9626bf8525e183f1f826bf3b44f0191deae161d7aace0e.jpg)

![](15-CycleLife-DataDriven_images/2b4022630e0f8ce4b259a50627bc68b05dfb13a56f8d0bc6f97d1e8038da8b36.jpg)

![](15-CycleLife-DataDriven_images/fc90fa6aacf7e0ff55e102c2a04736b014fa0dad470ecb8542ede61f28f4a3d4.jpg)  
Fig. 1. The cycling performance and some preliminary analysis of the tested LIBs. (a) Discharge capacity retention of the tested LIBs during cycling. The color denotes the cycle life of each battery. The dark blue corresponds to cells with long cycle life; the dark red corresponds to cells with short cycle life. (b) The examination of the repeatability of experimental data by cycling two samples in 18 different experimental conditions. (c) Statistics of the cycle life of the tested batteries. (d) The relationship between the change of the discharge capacity in the first 40 cycles and log cycle life. The inserted value shows the covariance between them. Color should be used for (a) in print. (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

$$
E r r o r = 2 \times \left| \frac {y _ {1} - y _ {2}}{y _ {1} + y _ {2}} \right| \times 100\%\tag{1}
$$

Fig. 1c shows the statistics of the battery cycle life. The results suggest that there were around 20 batteries that showed a cycle life of fewer than 50 cycles. The fast capacity degradation was caused by the extreme experimental conditions (SI\_Experiment conditions), such as low temperature (0 °C), large charge current (1C), high cut-off voltage (4.3 V), and large discharge current (2C). The effect of these parameters on capacity degradation has been discussed in our previous paper [3].

This study aims to predict the cycle life of LIBs based on the first few cycles, such as 10, 20, or 40 cycles. A linear extrapolation of the capacity retention in the first 40 cycles could not accurately predict the cycle life, even though some batteries showed a linear degradation in their initial aging period. Fig. 1d shows the relationship between the log cycle life of LIBs and the change of discharge capacity after 40 cycles calculated from equation (2). The covariance between them is only 0.563, suggesting a poor linear relationship between the two variables and, thus, a low prediction accuracy based on the linear extrapolation method.

$$
\text { Discharge   capacity } _ {4 0 / 1} = \frac {\text { Discharge   capacity   at   the } 4 0 ^ {t h} \text { cycle }}{\text { Discharge   capacity   at   the } 1 ^ {s t} \text { cycle }}\tag{2}
$$

The cycling curves of a battery contain numerous information on the battery's electrochemical performance, where the discharge capacity is only the last data point of a discharge curve. Analyzing the cycling curves provides more characteristic features to represent the degradation of a battery. For example, Severson et al. show that the variance of the voltage curves at different cycles correlates strongly with the $\mathrm{LiFePO_4}$ /Graphite battery cycle life [21]. Fig. 2 illustrates the features extraction process from discharge curves.

![](15-CycleLife-DataDriven_images/990a7d2dae5de3d040cc589b94a7aaa6f2b1fe2ceb48e536664dfc47a6612ea1.jpg)

Fig. 2a compares the discharge curves of a battery at the first cycle and the 40th cycle. The difference between the two curves included the discharge capacity, the discharge energy, and the shape of the discharge curve. The discharge capacity and discharge energy can be derived directly from the dataset, while the shape of the discharge curve is more difficult to be described quantitatively. Fig. 2a–c shows a method to derive quantitative features for describing the shape of a discharge curve. The voltage and capacity of two discharge curves were normalized to the range of [0, 1] using equations (3) and (4).

$$
\text { Normalized   voltage } = \frac {\text { Voltage } - \text { Voltage } _ {\min}}{\text { Voltage } _ {\max} - \text { Voltage } _ {\min}}\tag{3}
$$

$$
\text { Normalized   capacity } = \frac {\text { Capacity } - \text { Capacity } _ {\min}}{\text { Capacity } _ {\max} - \text { Capacity } _ {\min}}\tag{4}
$$

![](15-CycleLife-DataDriven_images/177cb0e85cdea80963cc0fe9e4613ecd7c9a1f43526d6e3162a18beb304cc889.jpg)

![](15-CycleLife-DataDriven_images/65dcb512a6e0eee45f2e5ff53830bfe60c7371adca9f6eb47403713e4850f53c.jpg)

![](15-CycleLife-DataDriven_images/dda8fdbcc8d3d964ff54a450bed5a787a7ce9ffdca3afd7b173c952c327e4e77.jpg)

![](15-CycleLife-DataDriven_images/50ce5f7d48d9f23653af23ddeb1f983ad9d3c1365af524d98847cc29ab4aa258.jpg)  
Fig. 2. Features extraction from discharge curves to represent the cycle life of the tested LIBs. (a) Discharge curves of a battery at the first cycle and the 40th cycle. (b) Normalization of the discharge capacity and the voltage to the range of [0, 1] for analyzing the shape of the discharge curve. (c) The voltage difference between the two normalized discharge curves. The first raw moment (mean), the second central moment (variance), the third central moment (skewness), and the fourth central moment (kurtosis) of the difference are considered as experts-extracted features to represent the shape of the discharge curve. (d) The relationship between the variance of the discharge curve and the cycle life. (e) The ranking of the covariance between 12 experts-extracted features and the cycle life of tested batteries. The first symbol C/D of the notation stands for charge/discharge curve. The second symbol 1–4 stands for the 1st-4th moment, c stands for capacity, and e stands for energy. For example, C2 represents the 2nd moment (variance) of the charge curve. Color should be used for figures (a) (b) in print. (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

Fig. 2b compares the two normalized discharge curves. The mismatch between them indicated the change of the battery performance, and it contained information that could represent the degradation of the battery. The difference between the two normalized discharge curves was further analyzed by investigating the change of the normalized voltage, as shown in Fig. 2c. Fig. 2d shows the relationship between the cycle life of LIBs and the variance of the discharge curves between the 1st cycle and the 40th cycle. The absolute value of the covariance was 0.621, which was higher than the covariance between the log cycle life and discharge capacity (Fig. 1d). The higher covariance value suggested that the variance of the discharge curves had more substantial connections with the cycle life of LIBs, and, thus, it was a better feature for predicting the cycle life. However, the absolute value of the covariance was much lower than the value reported by Severson et al., where they show that the covariance reaches -0.92 [21]. Such a difference could be from the different battery systems and the different cycling protocols in our study. The relatively small covariance highlights the need to extract new features and develop new models to predict the cycle life of LIBs in other battery systems, such as NCA/graphite.

To accurately represent the degradation of the LIBs, Table S1 (supporting information) lists 12 experts-extracted features based on charge and discharge curves in the first 40 cycles. These 12 features included four moments (mean, variance, skewness, kurtosis) from discharge curves, four moments from charge curves, charge capacity, discharge capacity, charge energy, and discharge energy. The covariances between the 12 experts-extracted features and the cycle life of tested LIBs are ranked in Fig. 2e. Among the 12 features, eight of them showed a relatively strong covariance with the cycle life. The covariances between these eight features and the cycle life are displayed in Fig. S2, where the variance of the charge curve difference shows the highest covariance with the cycle life (0.71). These experts-extracted features would be used as the inputs for building models to predict the cycle life of LIBs.

It needs to be mentioned that batteries with a cycle life of less than 40 were not used for the training and the test processes. The information of the first 40 cycles was utilized as the input. The batteries' cycle life with less than 40 cycles was known, and, thus, these batteries should not be used in the test dataset. In addition, including these batteries in the training dataset would tailor the parameters space towards these samples, affecting the accuracy for predicting other samples with long cycle life.

## 3.2. Model description

Three models were developed to predict the cycle life of LIBs, including a linear regression model, a conventional NN model, and a CNN model. In addition, a dummy regressor was used to show the effectiveness of the three models, which predicts the mean of the training set. Linear regression models are generally straightforward for predicting the behavior of simple systems. However, they face challenges when modeling complex and nonlinear systems such as LIBs. In comparison, a conventional feedforward neural network overcomes these challenges by hierarchically adding hidden layers and activation functions to represent the complexity and nonlinearity. Experts-extracted features were utilized as inputs in these two types of models for predicting the cycle life of LIBs. In addition, a CNN mode, taking experimental raw data as inputs, was further developed to extract hidden features using convolutional layers $[26]$ . These hidden features were patterns from the charge and discharge curves, which could represent the behavior of LIBs for predicting their cycle life. The linear regression model was built on the Scikit-learn open-source Python module $[27]$ . The NN and CNN models were built on TensorFlow open-source Python packages

[28].

Fig. 3a displays the schematics of the three models based on the initial performance, i.e., the first 40 cycles data. Table S1 lists experts-extracted features that were used as the inputs for the linear regression model and the NN model. The output of the models was cycle life. 80% of the experimental data was used to train parameters, while the remaining 20% of the data was used to evaluate the accuracy of these models. The average percentage error of the cycle life was chosen to evaluate the performance of each model, as shown in equation (5)

$$
E r r o r = \frac {1}{n} \sum_ {i = 1} ^ {n} \frac {\left| y _ {i} - \widehat {y _ {i}} \right|}{y _ {i}}\tag{5}
$$

where $y_{i}$ is the observed cycle life, $\widehat{y}_{i}$ is the predicted cycle life, and n is the total number of experimental data.

## 3.3. Linear regression model

A general form of a linear model used for this study is shown in equation (6).

$$
\widehat {y _ {i}} = \widehat {w} ^ {T} x _ {i}\tag{6}
$$

where $\hat{y}_{i}$ is the predicted cycle life of battery i, $\hat{w}$ is the vector that contains model parameters. $x_{i}$ is the feature vector of the battery i. Mean square error (MSE) is applied as the target function for fitting the parameters. The MSE is defined in equation (7).

$$
M S E = \frac {1}{n} \sum_ {i = 1} ^ {n} \left(y _ {i} - \widehat {y _ {i}}\right) ^ {2}\tag{7}
$$

where $y_{i}$ is the observed cycle life, $\widehat{y}_{i}$ is the predicted cycle life, and n is the total number of experimental data. Regularization terms were not included in this study because they did not improve the model accuracy. The optimal parameter $\widehat{w}$ was determined through the least square method by minimizing the MSE. A logarithm treatment was conducted for both inputs (features) and the output (cycle life) to avoid a negative output.

Fig. 4 shows the performance of the linear regression model. Fig. 4a shows the training and the test error with respect to the number of input features. Five-fold cross-validation was applied to examine the prediction ability of the model. The data were evenly divided into five subsets, where four subsets were used as the training data, and the remaining subset was used as the test data. The process repeated five times by choosing a different dataset as the test data each time. Fig. 4a indicates that the training error monotonically decreased with the number of input features. The error decreased to around 40% when all the 12 features (Table S1) are used as the input. Similarly, the test error decreased with the increased number of input features. The minimum test error was around 50% when eight input features were used. Keeping increasing the number of input features had little effect on the test error. This result matched well with the covariance plot, as shown in Fig. 2e, where eight features showed a much higher covariance value to the battery cycle life than the remaining four features.

Fig. 4b, c, d displays the performance of the linear regression model with different given cycling information. The result suggests that the accuracy of the model increased when more cycling information was given as the input. Fig. 4b shows that the training and the test error were 48.41% and 76.30% when only the first ten cycles were given as the input, suggesting a poor prediction performance of the model. The training and test errors were significantly reduced to 42.78% and 54.03% when the information of the first 20 cycles was given (Fig. 4c). Keeping increasing the number of cycles as the input showed little effect on the training and test errors. For example, Fig. 4d shows that the training and the test error were $42.86\%$ and $48.66\%$ when the cycle number increased to 40. Severson et al. achieved a $9.1\%$ prediction error for the cycling life of LFP/graphite batteries using a linear regression model [21]. The large error in this study was from the relatively small covariance between the experts-extracted features and the battery cycle life. Therefore, more robust models needed to be developed to improve the prediction accuracy of the battery cycle life.

![](15-CycleLife-DataDriven_images/0bc04a3cbcf802ceec6d39fd358e8816f0eae52fa6d2c32103c2109a6bffa4cb.jpg)  
Fig. 3. Three models to predict the cycle life of LIBs based on the information from the first 40 cycles, including a linear regression model, a conventional neural network model, and a convolutional neural network model. The first two models use features extracted by human experts, while the last model is based on features extracted by convolutional layers.

![](15-CycleLife-DataDriven_images/4558a1032e1d244b78c5a94ceb3bf9bbee40c50f486c1ac84aff67bf194dd719.jpg)

![](15-CycleLife-DataDriven_images/e04e2cb7d3359426d54741118aed89835b4b3000f4c4a4505afa624de652cd42.jpg)

(c)  
![](15-CycleLife-DataDriven_images/5f248ce18539d1ce170bca7551121360906036a258a616c86255dd727de8aaa9.jpg)

![](15-CycleLife-DataDriven_images/6be7ae40e9e8cc1fc6bb19ffc0b2aa0b079b42ab63ad92609c2416bbe1d79110.jpg)  
Fig. 4. The training and the test error of the linear regression model. (a) The variance of the test and training errors with the number of features. Five-fold cross-validation is applied to check the model, and the error bar shows the standard deviation of the five-fold cross-validation results. The training and the test performance of the linear regression model based on the expert-extracted features in the first (b) 10 cycles, (c) 20 cycles, and (d) 40 cycles. Color should be used for all figures in print. (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

## 3.4. Fully connected neural network model

A fully connected NN is recognized as a universal function approximator. It can approximate all mathematical functions with a single hidden layer $[29]$ . A multilayer NN with sufficient nodes in each layer can model complex and nonlinear systems and predict their performance $[30]$ . Thus, a NN with a reasonable number of hidden layers and nodes has the opportunity to predict the cycle life of LIBs with higher accuracy compared to the linear regression model.

Fig. 5a shows the structure of the NN applied for this study. The NN included three hidden layers with 32, 16, and 8 nodes in each layer. Nodes in the adjacent layers were correlated by a linear function followed by an activation function (8).

$$
y ^ {(n)} = f \left(w y ^ {(n - 1)} + b\right)\tag{8}
$$

where $y^{(n)}$ is the value in the nth layer, $y^{(n-1)}$ is the value in the (n-1) $^{th}$ layer, w is the vector that contains model parameters, b is the bias term, and f is the activation function. LeakyReLU was used as the activation function because it solves the dying ReLU problem but retaining the useful properties of the ReLU family $[31]$ . MSE was chosen as the objective function, as defined in equation (7). Model parameters (w) were derived by backpropagation $[32]$ . Adam optimizer was used to accelerate training by combining adaptive learning rate and momentum methods $[33]$ .

![](15-CycleLife-DataDriven_images/a245dc4c49c8b8e0efecdf7757492436c61cb070c3f8fed6d36246be5ca17d45.jpg)

![](15-CycleLife-DataDriven_images/dd9c0f095dc4a7a63b4055ebb4c1092b75e78e4a4a6d33a06ebfdcc1f44df7f5.jpg)

(c)  
![](15-CycleLife-DataDriven_images/b91e19e885619e225535e279634b2b1acf877912b2a9ab1d6431354cf7c72c0e.jpg)

(d)  
![](15-CycleLife-DataDriven_images/bcf2cd1b10d86501b4b8f6c6ca927b926fb254cae53e9a8d6c22dc2dce351d76.jpg)  
Fig. 5. (a) A schematic to show the structure of the fully connected NN used in this study, which includes three hidden layers with 32, 16, and 8 nodes in each layer. The training and the test performance of the NN model based on the experts-extracted features in the first (b) 10 cycles, (c) 20 cycles, and (d) 40 cycles. Color should be used for figures (b) (c) (d) in print. (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

Instead of using only the information from the 40th cycle and the first cycle, we supplied all information from the first 40 cycles as the input in the NN model. The six most important features were selected to reduce the number of inputs and reduce the complexity of the NN model. These features were charge capacity, charge energy, discharge capacity, discharge energy, the charge curve difference (variance), and the discharge curve difference (variance). Fig. 5b,c,d displays the performance of the NN model with different given cycling information. The result suggests that the accuracy of the NN model increased when more cycling information was given as the input. Fig. 5b shows that the training and the test error were $59.42\%$ and $100.02\%$ when only the first ten cycles were given as the input, suggesting a poor prediction performance of the model. The training and test errors were significantly reduced to $33.82\%$ and $48.31\%$ when the information of the first 20 cycles was given (Fig. 5c). Additionally, the training and test errors were further reduced to $29.68\%$ and $36.24\%$ when the cycle number increased to 40 (Fig. 5d).

A five-fold cross-validation test was conducted to examine the dependence of the NN model on dataset selection, as shown in Fig. S3. The result shows that the training error was 30.2%, and the test error was 42.8%. These errors were lower than that from the linear regression model (training error 40%, test error 50%), suggesting the better prediction performance of the neural network model than the linear regression model. However, the accuracy of the model was limited by the number of the training sample and the number of the cycle test given as the input information. Further increasing the complexity of the NN model did not increase the predicting accuracy, suggesting the limitation of the experts-extracted features. Therefore, better features were required to reduce the prediction errors in the NN model.

## 3.5. Convolutional neural network model

A convolutional neural network is a class of deep neural networks. It is considered as an automatic feature extractor that has been widely used in images and video processing $[34]$ . Instead of connecting each pair of nodes between two layers in a fully connected NN, CNN only considers the effect of a node and its neighbors using convolutional filters to capture hidden features, which vastly reduces the number of parameters $[35]$ . Therefore, a CNN model can capture hidden features in a battery system, hard to be extracted and understood by human experts, for predicting its cycle life.

Fig. 6 demonstrates the general idea of capturing hidden features from voltage profiles of two selected batteries using convolutional layers. Fig. 6a, c shows that the voltage profiles of the two batteries were different as they were discharged at different C-rates. Medium voltage is generally used to differentiate the two voltage profiles, which is the voltage when the capacity reaches half of the overall capacity in the cycle. However, it simplifies the difference between the two voltage profiles and ignores many essential features, such as the shape of the voltage curves. A CNN applies filters to capture features in the voltage profiles, as shown in Fig. 6b, d. The size of the filter is a hyper-parameter, and 3-by-3 filters were selected in this study. The filters scanned through the whole dataset and captured the evolution of the voltage values.

Fig. 7a shows the structure of the CNN model applied in this study, including three convolutional layers and two fully connected layers. In each convolutional layer, zero paddings were first used to preserve the dimension of the layer input. Four 3-by-3 filters with strides of 1-by-1 were then applied to extract features from the layer input, followed by a batch normalization to standardize layer inputs and stabilize the learning process [36]. LeakyReLU was used as the activation function in each layer, and a 2-by-2 max-pooling was applied to reduce the dimensionality of extracted features. A fully connected NN with two hidden layers was utilized to predict the cycle life of LIBs.

Fig. 7b and c shows the performance of the CNN model. The accuracy of the model increased when more cycling information was given as the input. Fig. 7b shows the training and the test error were 16.02% and 31.81% when only the first 20 cycles were given as the input in the model. The training and the test error were reduced to 9.28% and 22.73% when the cycle number increased to 40 (Fig. 7c). It needs to be mentioned that every other cycle was selected when 40 cycles were used as the input. A five-fold cross-validation test was further conducted to examine the dependence of the CNN model on dataset selection, as shown in Fig. S4. The result shows that the training error was 12.37%, and the test error was 21.07%. These errors were much lower than that from the linear regression model (training error 40%, test error 50%) and the NN model (training error 30.2%, test error 42.8%), suggesting the better prediction performance of the CNN model than the other two models.

![](15-CycleLife-DataDriven_images/bd412e6b0862a34c1b37cc11bf2c71983671283b3045c7a05eb007627b51a3f3.jpg)

![](15-CycleLife-DataDriven_images/c233c873c3afb9ff3992c534fa6c1f87a93324529b99f97bc700422953ead05e.jpg)

![](15-CycleLife-DataDriven_images/9b8c86a7aa1132e0bbbcc2b87c3e946569b69c5e9f23d0248926512e43927c60.jpg)

![](15-CycleLife-DataDriven_images/4c9e3059c618ad31825471852174a0ae5538c958d54e350b37c03002b9f62713.jpg)  
Fig. 6. Schematics of feature extraction by convolutional layers in a CNN model. The first 40 cycles of discharge voltage profile of a battery tested (a) at 0.5C and (c) at 2C. The voltage profiles of the two batteries are different because of different discharge C-rates. (b) (d) Feature extraction of the voltage profiles using 3-by-3 filters. Color should be used for all figures in print. (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

The training error was much smaller than the test error in the CNN model, indicating an overfitting issue caused by the limited number of samples in this study. The overfitting issue could not be resolved without sacrificing the training and test accuracy. The accuracy could be further improved by providing more experimental data and more samples, which is not trivial, considering the enormous time and effect required for the cycling test of LIBs. Nevertheless, these errors were much smaller than the NN model results, as shown in Fig. 5c and d. Therefore, the features captured by convolutional layers represented the cycling performance better than experts-extracted features.

To better understand the improved accuracy from the CNN model, Fig. 7d shows the covariance between the battery cycle life and the 16 hidden features extracted by the convolutional layers. The hidden features are the 16 flattened nodes from the convolutional layers (Fig. 7a). Compared to the experts-extracted features (Fig. 2e), most of these hidden features showed higher covariances with the cycle life of tested batteries. The highest covariance reached 0.88, as indicated by the 16th hidden feature in Fig. 7d. Five hidden features showed a covariance of over 0.77, which was larger than the highest covariance value (0.71) based on the experts-extracted features. The high covariance values suggested that the hidden features extracted by the convolutional layers could represent the cycle life of LIBs better than the experts-extracted features. Therefore, the CNN model reached the lowest training and test errors compared to the other two models.

Table 3 summarizes the training and test errors of different models for predicting the cycle life of LIBs in this study. Compared to the dummy predictor that predicts the mean of the training set, all the three proposed models reduce the training and test errors. Moreover, the training and test errors are reduced when more information is given as input. The errors predicted from the 40 cycles are the smallest for all three models. The CNN model offers the highest prediction accuracy by extracting relevant hidden features (Fig. 7d). The training and test errors are reduced from 176.34% to 150.17%–9.28% and 22.73%, respectively.

## 4. Conclusion

Data-driven techniques are promising to investigate and predict the behavior of complex, nonlinear systems. In this study, different types of data-driven machine learning models are introduced and compared to predict the cycle life of LIBs. We demonstrate the ability of a convolutional neural network for capturing hidden features to predict the cycle life of LIBs. Compared to the experts-extracted features, the hidden features extracted by convolutional layers show higher covariances with the battery cycle life, leading to a better prediction for the cycle life of LIBs. Based on the data

![](15-CycleLife-DataDriven_images/26b9b021a7d5b397392da4c52d044d33943da47fd381f94852572bf7a36479f8.jpg)

![](15-CycleLife-DataDriven_images/bea21fde921a3962d9c87ea2e4ee60f4e8fcca1a804305a53c4e16dfd1857a1f.jpg)

![](15-CycleLife-DataDriven_images/8c92ea125a0b654ece8775c807e89d00555111bec50f7dfb0d93ef81ca40191a.jpg)

(d)  
![](15-CycleLife-DataDriven_images/70ed2d32dc9222507c48694b4d15512e9f311dd32338ecc28bdadb333b4e44db.jpg)  
Fig. 7. (a) A schematic to show the structure of the CNN model. Experimental data were interpolated to the dimension of 20 for the four variables in each cycle, including voltage, capacity, energy, and resistance. (b, c) The training and the test error of the CNN model are based on the raw experimental data in the first (b) 20 cycles and (c) 40 cycles. (d) The covariance between the cycle life of tested LIBs and the hidden features extracted by the convolutional layers in the CNN model. Color should be used for figures (a) (b) (c) in print. (For interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)

## Table 3

Comparing the training and test error of different models when applying the first 10 cycles, 20 cycles, and 40 cycles as the input. A dummy model that predicts the mean of the training set is included to show the effectiveness of the three models.

<table><tr><td rowspan="2"></td><td colspan="2">10 cycles</td><td colspan="2">20 cycles</td><td colspan="2">40 cycles</td></tr><tr><td>train error [%]</td><td>test error [%]</td><td>train error [%]</td><td>test error [%]</td><td>train error [%]</td><td>test error [%]</td></tr><tr><td>Dummy model</td><td>176.34</td><td>150.17</td><td>176.34</td><td>150.17</td><td>176.34</td><td>150.17</td></tr><tr><td>Linear model</td><td>48.41</td><td>76.30</td><td>42.78</td><td>54.03</td><td>42.86</td><td>48.66</td></tr><tr><td>NN model</td><td>59.42</td><td>100.02</td><td>33.82</td><td>48.31</td><td>29.68</td><td>36.24</td></tr><tr><td>CNN model</td><td>16.30</td><td>40.67</td><td>16.02</td><td>31.81</td><td>9.28</td><td>22.73</td></tr></table>

from the first 40 cycles of around 100 NCA/graphite batteries, the CNN model can reach a training error of 9.28% and a test error of 22.73% in predicting their cycle life. In comparison, the best models based on experts-extracted features show over 30% of the training and the test error. In addition, the CNN model takes raw experimental data as the inputs that reduce the effort for extracting features by experts. The methodology and the data-driven methods presented in this work can be applied for predicting the behavior of other complex and nonlinear systems that are hard to predict by physical and semi-empirical models.

## CRediT authorship contribution statement

Laisuo Su: Conceptualization, Data curation, Software, Formal analysis, Writing – original draft. Mengchen Wu: Software, Formal analysis, Writing – original draft. Zhe Li: Conceptualization, Funding acquisition. Jianbo Zhang: Conceptualization, Writing – review & editing.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgment

This work was supported by National Natural Science Foundation of China under the grant number of U1864214, 51577104 and the supported by the National Key Research and Development Program of China under the grant number of 2017YFB0102201. The authors thank Prof. Amir Barati Farimani and Dule Shu at Carnegie Mellon University for helpful discussion on the machine learning algorithms. The authors acknowledge Caijuan Wang and Yang Song from the General Administration of Quality Supervision, Inspection and Quarantine of China for their assistance on the experimental data collection.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at https://doi.org/10.1016/j.etran.2021.100137.

## References

[1] Opitz A, Badami P, Shen L, Vignarooban K, Kannan AM. Renew Sustain Energy Rev 2017;68:685–92.

[2] Hofmann J, Guan D, Chalvatzis K, Huo H. Appl Energy 2016;184:995–1003.

[3] Su L, Zhang J, Wang C, Zhang Y, Li Z, Song Y, Jin T, Ma Z. Appl Energy 2016;163:201–10.

[4] Su L, Zhang J, Huang J, Ge H, Li Z, Xie F, Liaw BY. J Power Sources 2016;315:35–46.

[5] Lu L, Han X, Li J, Hua J, Ouyang M. J Power Sources 2013;226:272–88.

[6] Liu Z, Li Z, Zhang J, Su L, Ge H. Energies 2019;12:757.

[7] Jiang J, Zhang G, Zeng X, Su L, Zhang J, Li Z. Apparatus and method for detecting battery state of health. U.S. Patent 2020;10,712,395.

[8] Thomas EV, Bloom I, Christophersen JP, Battaglia VS. J Power Sources

2008;184:312-7.

[9] Bloom I, Cole BW, Sohn JJ, Jones SA, Polzin EG, Battaglia VS, Henriksen GL, Motloch C, Richardson R, Unkelhaeuser T, Ingersoll D, Case HL. J Power Sources 2001;101:238–47.

[10] Safari M, Morcrette M, Teyssot A, Delacourt C. J Electrochem Soc 2009;156: A145.

[11] Yang X, Leng Y, Zhang G, Ge S, Wang C. J Power Sources 2017;360:28–40.

[12] Zhang Q, White RE. J Power Sources 2008;179:793–8.

[13] Zhang Y, Li X, Su L, Li Z, Liaw BY, Zhang J. ECS Trans. 2017;75:37.

[14] Han X, Ouyang M, Lu L, Li J, Zheng Y, Li Z. J Power Sources 2014;251:38–54.

[15] Choi P, Parimalam BS, Su L, Reeja-Jayan B, Litster S. ACS Appl Energy Mater 2021;4:1657–65.

[16] Su L, Weaver JL, Groenenboom M, Nakamura N, Rus E, Anand P, et al. ACS Appl Mater Inter 2021;13:9919–31.

[17] Dubarry M, Baure G, Devie A. J Electrochem Soc 2018;165:A773–83.

[18] Li Y, Liu K, Foley AM, Zülke A, Berecibar M, Nanini-Maury E, Van Mierlo J, Hoster HE. Renew Sustain Energy Rev 2019;113:109254.

[19] Shen S, Sadoughi M, Chen X, Hong M, Hu C. J. Energy Storage 2019;25:100817.

[20] Ma G, Zhang Y, Cheng C, Zhou B, Hu P, Yuan Y. Appl Energy 2019;253:113626.

[21] Severson KA, Attia PM, Jin N, Perkins N, Jiang B, Yang Z, Chen MH, Aykol M, Herring PK, Fraggedakis D, Bazant MZ, Harris SJ, Chueh WC, Braatz RD. Nat Energy 2019;4:383–91.

[22] Fermín-Cueto P, McTurk E, Allerhand M, Medina-Lopez E, Anjos MF, Sylvester J, Dos Reis G. Energy and AI 2020;1:100006.

[23] V. Sulzer, P. Mohtat, S. Lee, J. B. Siegel and A. G. Stefanopoulou, arXiv preprint arXiv:2010.07460, 2020.

[24] Zhang Y, Xiong R, He H, Pecht MG. IEEE T Ind Electron 2019;66:1585–97.

[25] Zhang Y, Xiong R, He H, Pecht MG. IEEE T Veh Technol 2018;67:5695–705.

[26] Goodfellow I, Bengio Y, Courville A, Bengio Y. Deep learning. MIT press Cambridge; 2016.

[27] Pedregosa F, Varoquaux G, Gramfort A, Michel V, Thirion B, Grisel O, Blondel M, Prettenhofer P, Weiss R, Dubourg V. J Mach Learn Res 2011;12:2825–30.

[28] M. Abadi, P. Barham, J. Chen, Z. Chen, A. Davis, J. Dean, M. Devin, S. Ghemawat, G. Irving and M. Isard, 2016.

[29] Sonoda S, Murata N. Appl Comput Harmon Anal 2017;43:233–68.

[30] Karsoliya S. Int J Eng Trends Technol 2012;3:714–7.

[31] L. Lu, Y. Shin, Y. Su and G. E. Karniadakis, arXiv preprint arXiv:1903.06733, 2019.

[32] Rumelhart DE, Hinton GE, Williams RJ. Nature 1986;323:533–6.

[33] D. P. Kingma and J. Ba, arXiv preprint arXiv:1412.6980, 2014.

[34] A. Krizhevsky, I. Sutskever and G. E. Hinton, 2012.

[35] V. Dumoulin and F. Visin, arXiv preprint arXiv:1603.07285, 2016.

[36] S. Ioffe and C. Szegedy, arXiv preprint arXiv:1502.03167, 2015.