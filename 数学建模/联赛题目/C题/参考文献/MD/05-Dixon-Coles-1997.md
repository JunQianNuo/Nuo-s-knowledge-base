---
raw_title: 05-Dixon-Coles-1997
subject: 数学建模-策联杯C题
source: "[1997] Modelling Association Football Scores and Inefficiencies in the Football Betting Market by Mark Dixon and Stuart Coles.pdf"
status: mineru解析
parser: mineru
topics:
  - 泊松回归
  - 比分建模
  - 投注市场
  - 低比分修正
---

# Modelling Association Football Scores and Inefficiencies in the Football Betting Market

Mark J. Dixon, Stuart G. Coles

Applied Statistics, Volume 46, Issue 2 (1997), 265-280.

Stable URL:

http://links.jstor.org/sici?sici=0035-9254%281997%2946%3A2%3C265%3AMAFSAI%3E2.0.CO%3B2-F

Your use of the JSTOR archive indicates your acceptance of JSTOR's Terms and Conditions of Use, available at http://www.jstor.org/about/terms.html. JSTOR's Terms and Conditions of Use provides, in part, that unless you have obtained prior permission, you may not download an entire issue of a journal or multiple copies of articles, and you may use content in the JSTOR archive only for your personal, non-commercial use.

Each copy of any part of a JSTOR transmission must contain the same copyright notice that appears on the screen or printed page of such transmission.

Applied Statistics is published by Royal Statistical Society. Please contact the publisher for further permissions regarding the use of this work. Publisher contact information may be obtained at http://www.jstor.org/journals/rss.html.

Applied Statistics
©1997 Royal Statistical Society

JSTOR and the JSTOR logo are trademarks of JSTOR, and are Registered in the U.S. Patent and Trademark Office. For more information on JSTOR contact jstor-info@umich.edu.

©2002 JSTOR

# Modelling Association Football Scores and Inefficiencies in the Football Betting Market

By MARK J. DIXON† and STUART G. COLES

Lancaster University, UK

[Received November 1995. Revised September 1996]

## SUMMARY

A parametric model is developed and fitted to English league and cup football data from 1992 to 1995. The model is motivated by an aim to exploit potential inefficiencies in the association football betting market, and this is examined using bookmakers' odds from 1995 to 1996. The technique is based on a Poisson regression model but is complicated by the data structure and the dynamic nature of teams' performances. Maximum likelihood estimates are shown to be computationally obtainable, and the model is shown to have a positive return when used as the basis of a betting strategy.

Keywords: Betting strategy; Expected return; Football (soccer); Maximum likelihood; Poisson distribution

## 1. Introduction

Betting on the outcome of football (soccer) matches has a long tradition in the UK, most popularly in the form of football pools, which typically involve the selection of matches that are thought to be those most likely to be a draw. A recently introduced type of betting, fixed odds betting, is also rapidly increasing in popularity. Bookmakers offer odds on the various outcomes of a match. The simplest version of this uses just the outcome of the match, in the sense of it being a win by either the team playing at home or the team playing away, or a draw. More complicated bets can also be placed on the score or on the half-time and full-time results. In making bets the challenge then is to find 'good bets', in which the considered probability of occurrence is higher than the corresponding probability determined by the bookmakers' odds, so that there is a positive expected return. Unlike in other types of betting, such as in horse-racing, the odds are fixed around one week before the matches are played. This allows a detailed comparison of the bookmakers' odds with estimated probabilities so that any perceived weaknesses in the bookmakers' specification can be exploited. Consequently, a statistical model that is capable of accurately predicting probabilities of the outcome of football matches has the potential to form the basis of a profitable betting strategy. This paper develops a model that meets this requirement.

Various proposals have been made for modelling the outcome of football matches; these are reviewed in Section 2. For a betting strategy, however, probabilities must be estimated on a team-specific basis, so that the probabilities of the various match outcomes between two specific teams on a particular date can be calculated. This degree of resolution falls outside the scope of most of the published models. An exception to this is the model due to Maher (1982), that assumes independent Poisson distributions for the number of goals scored by each of the home and away teams, with means that are specific to each team's past performance. This forms the basis of our modelling approach. However, in attempting to derive a model which is not just a reasonable description of the data, but which also has the potential to provide better estimates of probabilities than the subjective estimates ascribed by bookmakers, we have had to modify and enhance this basic model structure. These modifications account for the fluctuating performance of individual teams and also enable the estimation of match outcomes for cup competitions in which teams from different leagues play one another. One consequence of these modifications is that simple equations for the maximum likelihood estimators are no longer available, but despite the high dimensionality of the model we show that maximum likelihood estimators are still available numerically. From the fitted model, the probabilities of the outcomes of each match are calculated and compared with the bookmakers' odds; this underlies the specification of a betting strategy which, using historical data, we show to have a positive return.

Section 2 reviews the literature discussing the use of statistical methodology in summarizing data from football matches. The data available to us are described in Section 3. Section 4 develops a statistical model, building on the basic model structure of Maher (1982). The application of the model to our assimilated data is described together with some sample results in Section 4. The utility of the model as the basis for a betting strategy is outlined in Section 5. Finally Section 6 suggests refinements which, we believe, would lead to further improvements in return.

## 2. Literature Review

Surprisingly few papers have examined the use of statistical techniques for modelling football data. American National Football League (NFL) football has received much more attention, but the differences between the two sports mean that modelling techniques for NFL football do not naturally transfer to association football.

Early references to statistical modelling of football data concentrate mainly on the distribution of the number of goals scored in a game. Moroney (1956) briefly examined this problem and suggested that, although the Poisson distribution provided an adequate fit to scores, improvements could be obtained by working with the negative binomial distribution. Reep et al. (1971) similarly examined the fit of the negative binomial distribution to scores from football matches and other goal scoring games. They concluded that 'chance dominates the game', finding no way of predicting outcomes within their class of models given the inherent noise in observed data. In contrast Hill (1974) applied a simple comparisons test for final league placings with expert predictions and demonstrated a significant correlation. A more sophisticated analysis of this type was by Fahrmeir (1994), who applied newly developed techniques for time-dependent, ordered, paired comparisons to German football data.

These points illustrate an apparent dichotomy: in the long run, it is not difficult to predict fairly accurately which teams are likely to be successful, but the development of models that have a sufficiently high resolution to exploit this long run predictive capability for individual matches is substantially more difficult. To our knowledge, the only paper that derives a model for football scores in a match between specific teams, accounting for the different quality of the teams involved, is that by Maher (1982). He obtained maximum likelihood estimates for a model in which the scores of the home and away teams in any game are independent Poisson distributions, with means modelled as functions of the respective teams' previous performances. This approach forms the basis of our model in Section 4.

With somewhat different applications in mind, several papers have looked at the effect of specific circumstances on team performances: Barnett and Hilditch (1993) applied standard nonparametric tests to see whether artificial pitches, subsequently banned in the English league, gave a significant advantage to the home team; Ridder et al. (1994) investigated the effect of the sending-off of a player on the outcome of a football match. Other papers have used statistical models to describe aspects of individual matches themselves: Chedzoy (1995) informally investigated times when goals are scored; Reep and Benjamin (1968) modelled the number and type of passing moves within a game; Clarke and Norman (1995) investigated the advantage of playing at home.

In relation to betting strategies, papers on the efficiency and exploitation of betting markets are numerous in the economics literature. Many papers address horse-racing and NFL football betting, and a few also consider betting on football matches, though little use of statistical methodology is made in these. Discussions of various betting markets can be found in Golec and Tamarkin (1991), Hausch et al. (1981) and, specifically in the context of football betting, Pope and Peel (1989).

## 3. Data

A wealth of information is available from each football match played. Obviously scores are recorded, but also the times of the goals, the goal scorers, the team's league position at the time of playing and so on. An individual team's performance in any particular game could also be affected by many external factors: newly signed players or the sacking of a manager for example. Though this information is also available, it is less easily formalized and its qualitative value subjective. Consequently, our model exploits only each team's history of match scores, which we have assimilated over a 3-year period, though the possibility of including other forms of data is investigated in Section 6.

The available data, which comprise 6629 full-time league and cup match results from the seasons 1992–93, 1993–94 and 1994–95, each consist of a home score and an away score. Data from 1995–96 are also available but are used as a validation sample to test the utility of the model subsequently when used as a basis for a betting strategy. The data from 1992 to 1995 provide accurate empirical estimates of various aggregated features. Table 1 gives the relative frequency, expressed as a percentage, of the scores from 0–0 to 4–4. Standard errors on the basis of an underlying multinomial model are shown in parentheses. Aggregating, the ratio of frequencies of home wins, draws and away wins is found to be 46:27:27. Thus, an empirical estimate of the probability of a randomly selected match resulting in a home win, for example, is 0.46. Because of the size of the database, these empirical estimates provide accurate estimates of random match probabilities. Our objective in later sections is to obtain estimates in matches which are not randomly selected but are team specific.

Empirical estimates of each score probability for joint and marginal probability functions†

<table><tr><td rowspan="2">Home goals</td><td colspan="6">Estimates of score probabilities (%) for the following numbers of away goals:</td></tr><tr><td>Away</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td></td><td></td><td>33.4 (0.74)</td><td>36.4 (0.57)</td><td>19.5 (0.49)</td><td>7.9 (0.42)</td><td>2.1 (0.16)</td></tr><tr><td>0</td><td>22.1 (0.36)</td><td>8.2 (0.32)</td><td>7.4 (0.28)</td><td>4.5 (0.23)</td><td>1.4 (0.13)</td><td>0.4 (0.06)</td></tr><tr><td>1</td><td>33.0 (0.65)</td><td>10.3 (0.38)</td><td>12.7 (0.30)</td><td>6.4 (0.24)</td><td>2.7 (0.15)</td><td>0.6 (0.07)</td></tr><tr><td>2</td><td>24.5 (0.51)</td><td>8.2 (0.31)</td><td>9.1 (0.25)</td><td>4.8 (0.22)</td><td>1.9 (0.14)</td><td>0.5 (0.09)</td></tr><tr><td>3</td><td>12.6 (0.40)</td><td>4.2 (0.25)</td><td>4.5 (0.25)</td><td>2.3 (0.19)</td><td>1.2 (0.11)</td><td>0.4 (0.06)</td></tr><tr><td>4</td><td>5.3 (0.31)</td><td>1.6 (0.14)</td><td>1.8 (0.13)</td><td>1.1 (0.13)</td><td>0.6 (0.07)</td><td>0.1 (0.04)</td></tr></table>

†Standard errors are given in parentheses.

The assumption that the marginal distribution of random match scores is Poisson can be examined at this stage. Fitting a Poisson distribution to the aggregated home and away scores in Table 1 reveals that by any criterion the Poisson model is a near perfect fit to the aggregated score data. This gives some reassurance that the Poisson regression model developed in Section 4 is at least plausible for our data, despite concerns raised by other researchers about the general appropriateness of the Poisson assumption. A further assumption of the basic model in Section 4 is that the home and away scores are independent. To assess the validity of this assumption, Table 2 displays

$$
\frac {\tilde {f} (i , j)}{\tilde {f} _ {\mathrm{H}} (i) \tilde {f} _ {\mathrm{A}} (j)}
$$

for each home and away score $(i,j)$ , $i=0,\ldots,6$ and $j=0,\ldots,5$ , where $\tilde{f},\tilde{f}_{H}$ and $\tilde{f}_{A}$ are the joint and marginal empirical probability functions for home and away scores respectively. Bootstrap standard errors are given in parentheses. Table 2 suggests that the assumption of independence between scores is reasonable, except for the scores 0–0, 1–0, 0–1 and 1–1. Based on the estimates and errors alone, the score 0–3 seems to be significantly underestimated by the independence model. However, viewed within the context of all the other results, we regard this as due to sampling error. A modification of the independence assumption in the light of these observations is considered in Section 4.

Estimates of the ratios of the observed joint probability function and the empirical probability function obtained under the assumption of independence between the home and away scores†

<table><tr><td rowspan="2">Home goals</td><td colspan="6">Estimates of ratios for the following numbers of away goals:</td></tr><tr><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>0</td><td>111.5 (3.52)</td><td>92.0 (2.87)</td><td>103.4 (4.18)</td><td>82.1 (7.67)</td><td>96.4 (15.31)</td><td>96.8 (28.12)</td></tr><tr><td>1</td><td>93.7 (2.43)</td><td>105.7 (2.00)</td><td>99.3 (3.74)</td><td>103.7 (6.31)</td><td>86.9 (13.15)</td><td>108.3 (19.99)</td></tr><tr><td>2</td><td>99.6 (2.91)</td><td>101.7 (2.11)</td><td>99.2 (3.78)</td><td>97.4 (7.41)</td><td>95.9 (17.4)</td><td>106.7 (23.77)</td></tr><tr><td>3</td><td>100.3 (4.25)</td><td>98.5 (3.61)</td><td>91.8 (6.51)</td><td>116.6 (11.03)</td><td>139.8 (23.85)</td><td>75.4 (40.5)</td></tr><tr><td>4</td><td>91.0 (7.07)</td><td>93.8 (7.16)</td><td>108.6 (10.74)</td><td>138.0 (16.31)</td><td>111.7 (32.86)</td><td>90.4 (55.33)</td></tr><tr><td>5</td><td>94.1 (13.24)</td><td>102.3 (12.28)</td><td>114.3 (20.6)</td><td>73.3 (31.01)</td><td>120.8 (74.71)</td><td>130.4 (129.7)</td></tr><tr><td>6</td><td>139.1 (31.95)</td><td>49.1 (23.66)</td><td>146.4 (41.33)</td><td>45.3 (57.84)</td><td>174.1 (122.2)</td><td>—</td></tr></table>

†The numbers are multiplied by 100 for clarity. Standard errors are given in parentheses.

## 4. Model and Inference

## 4.1. Model Specification

With the aim of developing a profitable betting strategy, various features are required of a statistical model for football matches. For example:

(a) the model should take into account the different abilities of both teams in a match;

(b) there should be allowance for the fact that teams playing at home generally have some advantage—the so-called 'home effect';

(c) the most reasonable measure of a team's ability is likely to be based on a summary measure of their recent performance;

(d) the nature of football is such that a team's ability is likely to be best summarized in separate measures of their ability to attack (to score goals) and their ability to defend (not to concede goals);

(e) in summarizing a team's performance by recent results, account should be taken of the ability of the teams that they have played against.

It is not practical to obtain empirical estimates of probabilities of match outcomes that account for all these constraints. Instead, we use a statistical model that structurally incorporates each of these features. Our basis is the model proposed by Maher (1982), with modifications to enable the inclusion of non-complete data sets, and data from different divisions simultaneously, and to allow for fluctuations in team performance.

The basic assumption of Maher's model is that the number of goals scored by the home and away teams in any particular game are independent Poisson variables, whose means are determined by the respective attack and defence qualities of each side. More explicitly, in a match between teams indexed $i$ and $j$ , let $X_{i,j}$ and $Y_{i,j}$ be the number of goals scored by the home and away sides respectively. Then

$$
\begin{array}{c} X _ {i, j} \sim \text { Poisson } (\alpha_ {i} \beta_ {j} \gamma), \\ Y _ {i, j} \sim \text { Poisson } (\alpha_ {j} \beta_ {i}), \end{array}\tag{4.1}
$$

where $X_{i,j}$ and $Y_{i,j}$ are independent, $\alpha_{i}, \beta_{i} > 0, \forall i$ , the $\alpha_{i}$ measure the 'attack' rate of the teams, the $\beta_{i}$ measure the 'defence' rates and $\gamma > 0$ is a parameter which allows for the home effect. In fact, Maher (1982) included a more general model specification than this, allowing for separate home and away, and attack and defence parameters for every team. However, like Maher (1982), we have found model (4.1) to be an adequate simplification, though there are still assumptions in this model that would not be supported by detailed study of match data. The essential point is that, although details of the model may be inaccurate, the global structure should be sufficiently accurate to enable the development of a betting strategy with a positive expected (and realized) return.

Some aspects of the model are easily improved on, however. Consider first the assumption of independence. Maher (1982) suggested the use of a bivariate Poisson family as an extension of the basic model, but this family is unable to represent the departure from independence for low scoring games that we identified in Section 3. Instead, we propose the following modification of model (4.1):

$$
\operatorname * {P r} (X _ {i, j} = x, Y _ {i, j} = y) = \tau_ {\lambda , \mu} (x, y) \frac {\lambda^ {x} \exp (- \lambda)}{x !} \frac {\mu^ {y} \exp (- \mu)}{y !}\tag{4.2}
$$

where

$$
\lambda = \alpha_ {i} \beta_ {j} \gamma ,
$$

$$
\mu = \alpha_ {j} \beta_ {i}
$$

and

$$
\tau_ {\lambda , \mu} (x, y) = \left\{ \begin{array}{l l} 1 - \lambda \mu \rho & \text { if } x = y = 0, \\ 1 + \lambda \rho & \text { if } x = 0, y = 1, \\ 1 + \mu \rho & \text { if } x = 1, y = 0, \\ 1 - \rho & \text { if } x = y = 1, \\ 1 & \text { otherwise }. \end{array} \right.
$$

In this model, $\rho$ , where

$$
\max (- 1 / \lambda , - 1 / \mu) \leqslant \rho \leqslant \min (1 / \lambda \mu , 1),
$$

enters as a dependence parameter: $\rho = 0$ corresponds to independence, but otherwise the independence distribution is perturbed for events with $x \leqslant 1$ and $y \leqslant 1$ . It is easily checked that the corresponding marginal distributions remain Poisson with means $\lambda$ and $\mu$ respectively.

Another limitation of the model is that it is static—the attack and defence parameters of each team are regarded as constant through time. This issue will be considered in Section 4.3.

## 4.2. Model Inference

It follows from model (4.2) that with n teams there are attack parameters $\{\alpha_{1},\ldots,\alpha_{n}\}$ , defence parameters $\{\beta_{1},\ldots,\beta_{n}\}$ , the dependence parameter $\rho$ and the home effect parameter $\gamma$ to be estimated. To prevent the model from being overparameterized, we impose the constraint

$$
n ^ {- 1} \sum_ {i = 1} ^ {n} \alpha_ {i} = 1.
$$

For the English league system, which comprises the Premier League and divisions 1-3 of the Football League, $n = 92$ , so the model has 185 identifiable parameters.

Our basic tool of inference is the likelihood function. With matches indexed $k=1,\ldots,N$ , and corresponding scores $(x_{k},y_{k})$ , this takes the form, up to proportionality,

$$
L (\alpha_ {i}, \beta_ {i}, \rho , \gamma ; i = 1, \dots , n) = \prod_ {k = 1} ^ {N} \tau_ {\lambda_ {k}, \mu_ {k}} (x _ {k}, y _ {k}) \exp (- \lambda_ {k}) \lambda_ {k} ^ {x _ {k}} \exp (- \mu_ {k}) \mu_ {k} ^ {\nu_ {k}}\tag{4.3}
$$

where

$$
\begin{array}{c} \lambda_ {k} = \alpha_ {i (k)} \beta_ {j (k)} \gamma , \\ \mu_ {k} = \alpha_ {j (k)} \beta_ {i (k)}, \end{array}\tag{4.4}
$$

and $i(k)$ and $j(k)$ denote respectively the indices of the home and away teams playing in match k. With complete data, in the sense of each team having played every other team equally often, and in the simpler case of independence between home and away team scores ( $\rho = 0$ ), Maher (1982) obtained a system of linear equations whose roots are the maximum likelihood estimates. To achieve greater generality, we are restricted to direct numerical maximization of equation (4.3). The near orthogonality of many parameter combinations means that this is straightforward, despite the high dimensionality of the model.

In equation (4.3), teams from all four divisions are included in the likelihood. This has two consequences: firstly, the parameters for each team should reflect the relative quality of the different divisions and, secondly, the parameters will be estimable only if there is information from matches between teams of different divisions. Fortunately, because there is some mobility between the teams of different divisions at the start of a new season due to promotion and relegation, the issue of parameter identifiability is resolved. The situation is also helped by the inclusion of results from cup games which involve teams of different divisions playing each other. Then, because the parameters are calibrated across the divisions, the model can validly be used to estimate the probabilities of match outcomes involving teams of different divisions, as in cup games for example. These points are illustrated by Table 3, which shows the mean attack and defence parameters for teams in each division. As expected, the average attack and defence rating of teams increases with higher league status, as measured by increasing and decreasing mean values of $\alpha$ and $\beta$ respectively.

## 4.3. Model Enhancement

A structural limitation of model (4.3) is that the parameters are static, i.e. teams are assumed to have a constant performance rate, as determined by $\alpha_{i}$ and $\beta_{i}$ , over time. In reality, a team's performance tends to be dynamic, varying from one time period to another, and this behaviour should be incorporated in the model. In particular a team's performance is likely to be more closely related to their performance in recent matches than in earlier matches. In principle, this behaviour could be modelled by formalizing a stochastic development of the model parameters; this is considered in Section 6. In view of the dimensionality of the model, however, and since we shall always need to estimate the parameters at the fixed time point of making a bet rather than, say, forecasting ahead, we take a more simplistic approach here. Thus we assume that the parameters are, in a loose sense, locally constant through time and that historical information is of less value than recent information, and we determine parameter estimates for each time point t that are based on the history of match scores up to time t. Modifying equation (4.3) we construct a 'pseudolikelihood' for each time point t,

TABLE 3  
Mean attack and defence parameters for teams within each division

<table><tr><td>League</td><td>Mean attack parameter  $\bar{\alpha}$ </td><td>Mean defence parameter  $\bar{\beta}$ </td></tr><tr><td>Premier</td><td>1.38</td><td>0.68</td></tr><tr><td>Division 1</td><td>1.07</td><td>0.86</td></tr><tr><td>Division 2</td><td>0.83</td><td>1.14</td></tr><tr><td>Division 3</td><td>0.73</td><td>1.32</td></tr></table>

$$
L _ {t} \left(\alpha_ {i}, \beta_ {i}, \rho , \gamma ; i = 1, \dots , n\right) = \prod_ {k \in A _ {t}} \left\{\tau_ {\lambda_ {k}, \mu_ {k}} \left(x _ {k}, y _ {k}\right) \exp \left(- \lambda_ {k}\right) \lambda_ {k} ^ {x _ {k}} \exp \left(- \mu_ {k}\right) \mu_ {k} ^ {\nu_ {k}} \right\} ^ {\phi (t - t _ {k})}\tag{4.5}
$$

where $t_{k}$ is the time that match k was played, $A_{t}=\{k:t_{k}<t\}$ , $\lambda_{k}$ and $\mu_{k}$ are as in equations (4.4) and $\phi$ is a non-increasing function of time. This represents a slight abuse of notation since the parameters $\alpha_{i},\beta_{i},\rho$ and $\gamma$ are themselves time dependent.

Maximizing equation (4.5) at time t leads to parameter estimates which are based on games up to time t only. In this way, the model has the capacity to reflect changes in team performance. Moreover, varying the choice of $\phi$ allows historical data to be downweighted in the likelihood to a greater or lesser degree.

## 4.4. Choice of Weighting Function $\phi$

There are various possible choices for the weighting function $\phi$ in equation (4.5). One possibility would be

$$
\phi (t) = \left\{ \begin{array}{l l} 1 & \quad t \leqslant t _ {0}, \\ 0 & \quad t > t _ {0}, \end{array} \right.
$$

in which case, at time t, all results within the last $t_{0}$ time units would be given equal weight in the inference. Instead, we work with the model

$$
\phi (t) = \exp (- \xi t),
$$

in which all previous results, downweighted exponentially according to a parameter $\xi > 0$ , are included in the inference at time t. The static model (4.3) arises as the special case $\xi = 0$ , whereas taking increasingly large values of $\xi$ gives relatively more weight to the most recent results.

Optimizing the choice of $\xi$ is problematic, since equation (4.5) defines a sequence of non-independent ‘likelihoods’, whereas we require $\xi$ such that the overall predictive capability of the model is maximized. In fact, in subsequent sections, we restrict attention to the prediction of match outcomes rather than match scores. Therefore it is pragmatic to choose $\xi$ to optimize the prediction of outcomes. First note that the probability of a home win in match k is estimated as

$$
p _ {k} ^ {\mathrm{H}} = \sum_ {l, m \in B _ {\mathrm{H}}} \operatorname * {P r} (X _ {k} = l, Y _ {k} = m)\tag{4.6}
$$

where $B_{\mathrm{H}}=\{(l,m):l>m\}$ , and the score probabilities are determined from the maximization of model (4.5) at $t(k)$ , the time of match k. Similar expressions hold for $p_{k}^{A}$ and $p_{k}^{D}$ , the probabilities of an away win and a draw respectively. Now define

$$
S (\xi) = \sum_ {k = 1} ^ {N} \left(\delta_ {k} ^ {\mathrm{H}} \log p _ {k} ^ {\mathrm{H}} + \delta_ {k} ^ {\mathrm{A}} \log p _ {k} ^ {\mathrm{A}} + \delta_ {k} ^ {\mathrm{D}} \log p _ {k} ^ {\mathrm{D}}\right)\tag{4.7}
$$

where, for example, $\delta_{k}^{H}=1$ if match k is a home win and $\delta_{k}^{H}=0$ otherwise, and $p_{k}^{H}$ , $p_{k}^{A}$ and $p_{k}^{D}$ are the maximum likelihood estimates from model (4.5), with weighting parameter set at $\xi$ . Considering only the outcomes, and not the scores, equation (4.7) is the analogue of a predictive profile log-likelihood. A plot of $S(\xi)$ against $\xi$ , with time units taken to be half-weeks, is given in Fig. 1. The function is maximized at $\xi=0.0065$ , and all subsequent results are given with respect to this choice of $\xi$ , though in fact the results are robust across a range of $\xi$ -values.

## 4.5. Parameter Estimates and Results

The complete set of parameter estimates, obtained by maximizing equation (4.5) with $\xi=0.0065$ , at each time point t, gives a profile of each team's changing performance in terms of defence and attack abilities. Data from at least 60 half-weeks are required to estimate parameters accurately, so estimates are obtained for t ranging from 60 to 174. For brevity we show only a subset of the results (for the full set of results for the 1996 season, contact M. Dixon). Tables 4 and 5 give the maximum likelihood estimates of the attack and defence parameters on August 5th, 1995, for teams which were in the Premier division and division 2 respectively in 1995–96. In addition, Fig. 2 shows the corresponding sequence of estimates of $\alpha(t)$ and $\beta(t)$ over time for three teams—the non-uniformity in these estimates suggests that teams' performances are genuinely dynamic. Also shown is the sequence of estimates of the home effect parameter $\gamma(t)$ which, as might be expected, remains nearly constant over time. The flat portion from t = 82 to t = 90 corresponds to the summer break in the football season. Furthermore, Table 6 gives a sample of matches and the maximum likelihood estimates of the outcome probabilities. The standard errors of the outcome estimates, particularly those of the draw probability estimates, are small relative to the standard errors of the attack and defence parameter estimates.

![](05-Dixon-Coles-1997_images/6f7c39fad165b9acd616396438eebdbbe54844cfe2105f4d2bd33d8ca752dffa.jpg)  
Fig. 1. $S(\xi)$ versus $\xi$ : the maximum occurs at $\xi = 0.0065$

TABLE 4  
Maximum likelihood estimates and standard errors for the attack and defence rate parameters, on August 5th, 1995, for Premiership teams (in the 1995–96 season)

<table><tr><td>Team</td><td> $\hat{\alpha}$ </td><td> $se(\hat{\alpha})$ </td><td> $\hat{\beta}$ </td><td> $se(\hat{\beta})$ </td></tr><tr><td>Arsenal</td><td>1.235</td><td>0.151</td><td>0.527</td><td>0.078</td></tr><tr><td>Aston Villa</td><td>1.278</td><td>0.178</td><td>0.649</td><td>0.086</td></tr><tr><td>Blackburn</td><td>1.730</td><td>0.209</td><td>0.534</td><td>0.082</td></tr><tr><td>Bolton</td><td>1.183</td><td>0.141</td><td>0.760</td><td>0.100</td></tr><tr><td>Chelsea</td><td>1.238</td><td>0.169</td><td>0.658</td><td>0.089</td></tr><tr><td>Coventry</td><td>1.115</td><td>0.164</td><td>0.699</td><td>0.094</td></tr><tr><td>Everton</td><td>1.177</td><td>0.169</td><td>0.667</td><td>0.091</td></tr><tr><td>Leeds</td><td>1.510</td><td>0.186</td><td>0.583</td><td>0.088</td></tr><tr><td>Liverpool</td><td>1.448</td><td>0.180</td><td>0.561</td><td>0.082</td></tr><tr><td>Manchester City</td><td>1.232</td><td>0.170</td><td>0.728</td><td>0.091</td></tr><tr><td>Manchester United</td><td>1.869</td><td>0.208</td><td>0.402</td><td>0.067</td></tr><tr><td>Middlesbrough</td><td>1.244</td><td>0.152</td><td>0.750</td><td>0.109</td></tr><tr><td>Newcastle</td><td>1.659</td><td>0.195</td><td>0.578</td><td>0.081</td></tr><tr><td>Nottingham Forest</td><td>1.460</td><td>0.170</td><td>0.658</td><td>0.095</td></tr><tr><td>Queen&#x27;s Park Rangers</td><td>1.497</td><td>0.195</td><td>0.717</td><td>0.095</td></tr><tr><td>Sheffield Wednesday</td><td>1.387</td><td>0.179</td><td>0.698</td><td>0.091</td></tr><tr><td>Southampton</td><td>1.446</td><td>0.183</td><td>0.772</td><td>0.098</td></tr><tr><td>Tottenham</td><td>1.622</td><td>0.201</td><td>0.775</td><td>0.100</td></tr><tr><td>West Ham</td><td>1.192</td><td>0.169</td><td>0.649</td><td>0.087</td></tr><tr><td>Wimbledon</td><td>1.281</td><td>0.174</td><td>0.732</td><td>0.094</td></tr></table>

TABLE 5

Maximum likelihood estimates and standard errors for the attack and defence rate parameters on August 5th, 1995, for teams in division 2 (in the 1995–96 season)

<table><tr><td>Team</td><td> $\hat{\alpha}$ </td><td> $se(\hat{\alpha})$ </td><td> $\hat{\beta}$ </td><td> $se(\hat{\beta})$ </td></tr><tr><td>Blackpool</td><td>0.858</td><td>0.110</td><td>1.357</td><td>0.163</td></tr><tr><td>Bournemouth</td><td>0.681</td><td>0.096</td><td>1.095</td><td>0.139</td></tr><tr><td>Bradford</td><td>0.832</td><td>0.107</td><td>1.175</td><td>0.149</td></tr><tr><td>Brentford</td><td>0.967</td><td>0.115</td><td>0.900</td><td>0.129</td></tr><tr><td>Brighton</td><td>0.820</td><td>0.107</td><td>1.032</td><td>0.137</td></tr><tr><td>Bristol City</td><td>0.825</td><td>0.120</td><td>0.873</td><td>0.114</td></tr><tr><td>Bristol Rovers</td><td>0.917</td><td>0.113</td><td>0.965</td><td>0.138</td></tr><tr><td>Burnley</td><td>0.942</td><td>0.116</td><td>1.067</td><td>0.127</td></tr><tr><td>Carlisle</td><td>0.781</td><td>0.100</td><td>0.964</td><td>0.157</td></tr><tr><td>Chesterfield</td><td>0.764</td><td>0.099</td><td>1.024</td><td>0.160</td></tr><tr><td>Crewe</td><td>1.065</td><td>0.125</td><td>1.265</td><td>0.159</td></tr><tr><td>Hull</td><td>0.822</td><td>0.104</td><td>1.069</td><td>0.146</td></tr><tr><td>Notts County</td><td>0.985</td><td>0.132</td><td>0.979</td><td>0.120</td></tr><tr><td>Oxford</td><td>0.956</td><td>0.119</td><td>0.951</td><td>0.119</td></tr><tr><td>Peterborough</td><td>0.829</td><td>0.111</td><td>1.161</td><td>0.133</td></tr><tr><td>Rotherham</td><td>0.852</td><td>0.106</td><td>1.136</td><td>0.143</td></tr><tr><td>Shrewsbury</td><td>0.764</td><td>0.104</td><td>1.060</td><td>0.145</td></tr><tr><td>Stockport</td><td>0.945</td><td>0.115</td><td>1.040</td><td>0.136</td></tr><tr><td>Swansea</td><td>0.798</td><td>0.106</td><td>0.899</td><td>0.122</td></tr><tr><td>Swindon</td><td>1.160</td><td>0.154</td><td>1.091</td><td>0.120</td></tr><tr><td>Walsall</td><td>0.911</td><td>0.114</td><td>1.116</td><td>0.162</td></tr><tr><td>Wrexham</td><td>0.957</td><td>0.116</td><td>1.257</td><td>0.150</td></tr><tr><td>Wycombe</td><td>0.813</td><td>0.105</td><td>0.984</td><td>0.137</td></tr><tr><td>York</td><td>0.916</td><td>0.113</td><td>0.926</td><td>0.131</td></tr></table>

![](05-Dixon-Coles-1997_images/e8003826595ea8b66f8264b635bcae1e176b1d54fe7e0801cdfe3726dec10ff0.jpg)  
(a)

![](05-Dixon-Coles-1997_images/3def87c0cb650fe64545b2450ce09bd6e72f7d655f6048491e4060df447f7882.jpg)  
(b)

![](05-Dixon-Coles-1997_images/ae2de3450883f5a7923b7a9ca41d08c6a58656cdcaa4db87b96f43d1163258fb.jpg)  
(c)  
Fig. 2. (a), (b) Time series of the maximum likelihood estimates of attack and defence rate parameters for Sheffield United (——), Norwich (……) and Everton (− − −); (c) variation of the common home effect parameter with time

Maximum likelihood estimates for match outcome probabilities†

<table><tr><td rowspan="2">Match</td><td colspan="3">Maximum likelihood estimates for the following outcomes:</td></tr><tr><td>Home win</td><td>Draw</td><td>Away win</td></tr><tr><td>Arsenal versus Middlesbrough</td><td>0.535 (0.069)</td><td>0.280 (0.030)</td><td>0.184 (0.046)</td></tr><tr><td>Aston Villa versus Manchester United</td><td>0.214 (0.054)</td><td>0.291 (0.029)</td><td>0.495 (0.072)</td></tr><tr><td>Blackburn versus Queen&#x27;s Park Rangers</td><td>0.615 (0.078)</td><td>0.221 (0.033)</td><td>0.164 (0.049)</td></tr><tr><td>Chelsea versus Everton</td><td>0.457 (0.075)</td><td>0.298 (0.030)</td><td>0.245 (0.057)</td></tr><tr><td>Liverpool versus Sheffield Wednesday</td><td>0.535 (0.076)</td><td>0.262 (0.031)</td><td>0.203 (0.052)</td></tr><tr><td>Blackpool versus Wrexham</td><td>0.428 (0.077)</td><td>0.240 (0.018)</td><td>0.332 (0.070)</td></tr><tr><td>Stockport versus Burnley</td><td>0.480 (0.077)</td><td>0.259 (0.024)</td><td>0.261 (0.062)</td></tr><tr><td>Newcastle versus Stoke</td><td>0.705 (0.073)</td><td>0.198 (0.042)</td><td>0.097 (0.034)</td></tr></table>

†The matches are a subset of the fixtures from August 19th, 1995, plus one other across-division match. Approximate standard errors are calculated using the delta method. Standard errors are given in parentheses.

## 5. Betting Strategy

How useful is the model derived in Section 4, when used as the basis for a betting strategy against odds provided by bookmakers? A detailed investigation into betting strategies for fixed odds football betting is given in Pope and Peel (1989) and Dixon and Pope (1996). Here we address the question by reference to a new set of results, corresponding to the 1995–96 season, for which we have both results and bookmakers' odds. We first use model (4.5), with $\xi = 0.0065$ , at each new time point t to obtain current parameter estimates. Then, by comparing estimated result probabilities with bookmakers' odds for the following week, we determine which games are most advantageous to bet on. We then calculate the net return from such a strategy.

A typical set of bookmakers' odds for a particular match might be (8:13, 12:5, 4:1) for a home win, draw and away win respectively. Thus, in this example, a stake of 13 units on a home win would yield a profit of 8 units if that outcome occurred. Odds $o_1:o_2$ transform to a probability $p$ by using the formula

$$
p = o _ {2} / (o _ {1} + o _ {2}).
$$

The above set of odds then corresponds to the set of probabilities (0.62, 0.29, 0.20), which has a sum of 1.11. This phenomenon is standard in betting markets: if the bookmakers are accurate in their probability specifications, they have an in-built 'take', corresponding to their expected profit, which in the above example is $11\%$ . To win money from bookmakers, in the sense of having a positive expected return, requires a determination of probabilities which is sufficiently more accurate than those obtained from the odds in order to overcome the bookmakers' take. We first rescale multiplicatively the bookmakers' odds so that they sum to 1. Denote these probabilities for match $k$ by $b_k^{\mathrm{H}}$ , $b_k^{\mathrm{D}}$ and $b_k^{\mathrm{A}}$ for a home win, draw and away win respectively, and similarly let $\hat{p}_k^{\mathrm{H}}$ , $\hat{p}_k^{\mathrm{D}}$ and $\hat{p}_k^{\mathrm{A}}$ be the corresponding maximum likelihood estimates for this match under model (4.5). Comparisons of the two sets of probability estimates for each of the result outcomes are given in Fig. 3 for each match in our database. Overall there is reasonable agreement between the probability assessments, but the variability in these plots indicates the potential for positive gain if our model probabilities are accurate.

![](05-Dixon-Coles-1997_images/ce27c0fbb91f0ad3ddf72aaf090cf25c34b5d7580f4324714efbaefb52e40612.jpg)  
(a)

![](05-Dixon-Coles-1997_images/d76809f5a30fe09edba0075574ad8e1378365ba5226638221829ea0be8b4cb86.jpg)

![](05-Dixon-Coles-1997_images/4aeee7065b20d7817b97f14000f653bbedde76b8ef64b716d1720d0b1c7291e6.jpg)  
Fig. 3. Model probability estimates plotted against odds for all matches where odds were available: (a) home wins; (b) draws; (c) away wins

If the model probabilities were without error, then the expected gain from a unit stake bet on a home win, for example, is

$$
E (G) = p _ {k} ^ {\mathrm{H}} / b _ {k} ^ {\mathrm{H}} - 1.\tag{5.1}
$$

If $b_{k}^{H}$ is the true probability then the expected gain will be 0.00, or -0.11 if the bookmakers' take is included. In reality neither $p_{k}^{H}$ nor $b_{k}^{H}$ is the true probability, but we obtain a positive return if our estimates are sufficiently more accurate than the bookmakers'.

From equation (5.1), a natural betting strategy for any particular game k is to bet on a home win, for example, if

$$
\hat {p} _ {k} ^ {\mathrm{H}} / \tilde {b} _ {k} ^ {\mathrm{H}} > r,
$$

![](05-Dixon-Coles-1997_images/26a6ee055ac6829b35e783a0daf1a748eb2ace2dcb9755ecf193d159f3700f6c.jpg)  
Fig 4. Observed mean return plotted against the ratio of model probabilities to bookmakers' probabilities (---, return of -0.11, the expected return under random betting, which is due to the bookmakers' take of 11% for each match; ……, 90% bootstrap intervals): the mean return is calculated only when there are more than 10 sample values

where $\hat{b}_{k}^{H}$ denotes the unscaled bookmakers' probability of a home win in match k, for some predetermined value of r>1, with a corresponding strategy for bets on away wins or draws. Increasing r leads to a stricter betting regime, but consequently fewer bets. The effect of a range of different choices for r can be seen in Fig. 3, in which the line $\hat{p}=rb$ is plotted for r=1.0, 1.1, 1.3. For a particular choice of r, points falling above that line correspond to matches on which this betting strategy would have led to a bet being placed on that particular outcome, with r as specified.

The success of this betting strategy can be assessed by calculating the observed return, if such a strategy had been adopted, given the match results which actually occurred. This is plotted as a function of r in Fig. 4, together with 90% confidence intervals obtained using the bootstrap. There is considerable variability in the plot which makes it difficult to draw definitive conclusions. However, with r = 1.2 our betting strategy leads to a return which is borderline significantly different from -0.11, the expected return under a random betting strategy due to the bookmakers' take, and has a positive expected absolute return for any r > 1.1. It is in this sense that we claim that the model and inference of Section 4 meet our stated objective of deriving a model for estimating football match outcomes which is the basis of a betting strategy with positive returns.

## 6. Conclusions

Our aim has been to derive a method for estimating the probabilities of football results with the potential to achieve a positive expected return when used as the basis of a betting strategy against bookmakers' odds. Our basic model is simple—a bivariate Poisson distribution for the numbers of goals scored by each team, with parameters related to past performance—but refinements necessary to improve the realism and precision of the model make the associated inference a heavy computational burden. None-the-less, the computations are manageable and the resulting model is accurate in many respects.

Our betting strategy is equally simple: we bet on all outcomes for which the ratio of model to bookmakers' probabilities exceeds a specified level. For sufficiently high levels, we have shown that this strategy yields a positive expected return, even allowing for the in-built bias in the bookmakers' odds.

The simplicity of our model and the associated betting strategy is appealing. However, to improve further on the utility of our approach, we perceive that further modifications may be desirable. One possibility is to refine further the Poisson regression model. Stochastically updated parameters are a natural idea in this context, but the detailed implementation may be difficult. Smith (1981) considered a dynamic regression framework for simple Poisson models, but the generalization of these ideas to the scale of model (4.5) is not immediate. Broadening the scope of our model to incorporate additional covariate information is a second area for development. The quantitative value of such data is not always obvious, so such a development might need a Bayesian structure to exploit their subjective value. A third possibility is the betting regime. We have restricted attention so far to fixed odds bets of match outcomes. This leads to a betting strategy in which relatively few bets are actually placed. As bookmakers offer odds on specific match scores, the probabilities of which are also obtained from our model, a betting strategy based on match scores could be developed. More radically, there are several 'market-style' index betting options for football matches, where goal margins are bought and sold like commodities (e.g. Jackson (1994) and Dixon and Robinson (1996)); the implementation of our model for market strategies in such an option is a further possibility.

The lure of scientific improvement of our model and betting strategy, with the purely incidental by-product of winning money from the bookmakers, encourages us to build on the apparent success of the present model in the various ways discussed above.

## Acknowledgements

We thank a referee and the Editor for comments on an earlier version of the paper and Jonathan Tawn for comments that helped to improve the handling of dependence between scores. We are grateful to many colleagues at Lancaster who helped to digitize football league data and bookmakers' odds. For entry of data and odds, we thank Simon Garside, Sara Morris, Mike Robinson and Pete Stewart. The data were obtained from Williams (1992, 1993, 1994), Hugman (1991) and 90-Minutes weekly magazine. Odds were obtained from local branches of major UK bookmakers. We also thank Mike Robinson and Barry Rowlingson for writing some of the software used in the handling of data.

## References

Barnett, V. and Hilditch, S. (1993) The effect of an artificial pitch surface on home team performance in football (soccer). J. R. Statist. Soc. A, 156, 39–50.

Chedzoy, O. (1995) Influences on the distribution of goals in soccer. Private communication.

Clarke, S. R. and Norman, J. M. (1995) Home ground advantage of individual clubs in English soccer. Statistician, 44, 509–521.

Dixon, M. J. and Pope, P. (1996) Inefficiency and bias in the UK football betting market. Submitted to Mangmnt Sci.

Dixon, M. J. and Robinson, M. E. (1996) A point process model for goal times in association football matches. Submitted to J. Am. Statist. Ass.

Fahrmeir, L. (1994) Dynamic-stochastic models for time-dependent ordered paired comparison systems. J. Am. Statist. Ass., 89, 1438–1449.

Golec, J. and Tamarkin, M. (1991) The degree of inefficiency in the football betting market. J. Finan. Econ., 30, 311–323.

Hausch, D. B., Ziemba, W. T. and Rubinstein, M. (1981) Efficiency of the market for racetrack betting. Mangmnt Sci., 27, 1435–1452.

Hill, I. D. (1974) Association football and statistical inference. Appl. Statist., 23, 203–208.

Hugman, B. J. (1991) The Official Football League Yearbook. Chichester: Facer.

Jackson, D. A. (1994) Index betting on sports. Statistician, 43, 309–315.

Maher, M. J. (1982) Modelling association football scores. Statist. Neerland., 36, 109–118.

Moroney, M. J. (1956) Facts from Figures, 3rd edn. London: Penguin.

Pope, P. F. and Peel, D. A. (1989) Information, prices and efficiency in a fixed-odds betting market. Economica, 56, 323–341.

Reep, C. and Benjamin, B. (1968) Skill and chance in association football. J. R. Statist. Soc. A, 131, 581–585.

Reep, C., Pollard, R. and Benjamin, B. (1971) Skill and chance in ball games. J. R. Statist. Soc. A, 134, 623–629.

Ridder, G., Cramer, J. S. and Hopstaken, P. (1994) Estimating the effect of a red card in soccer. J. Am. Statist. Ass., 89, 1124–1127.

Smith, J. Q. (1981) The multiparameter steady model. J. R. Statist. Soc. B, 43, 256–260.

Williams, T. (1992) Football Club Directory. Exeter: Hamsworth Active.

——(1993) Football Club Directory. Exeter: Hamsworth Active.

(1994) Football Club Directory. Exeter: Hamsworth Active.