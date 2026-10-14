$$\checkmark$$

$$\checkmark$$

<table border="1" ><tr>
<td>425<br>426<br>428<br>429<br>430<br>431<br>432<br>43.3<br>434<br>43.5<br>436<br>437<br>438<br>430<br>440<br>441<br>442<br>443<br>444<br>445</td>
<td>#all$_num=len(data_get)$＃print(f”次品个数：$\{no_num\}$，整体数目： $\{all_num$ $\}")$###<br>＃＃检验一<br>＃print（”检验一”）<br>＃#'smaller＇代表低于alpha 时成立，<br>#zstat, $p_val=proportions_ztest$(nonum,allnum,wannap0, alternative='smaller')<br>8print $(f"Z$statistic:$\{z_stat\}$, $P-value:\{p_val\}")$#<br>＃＃判断原假设<br>#$\text {alpha}=0.05$#if $p_val<alpha:$#print（”拒绝零假设：即认为有95 ％的把握认为次品率低于10 ％”）<br>#else:<br>#print（”接受零假设：即没有足够的证据认为次品率低于10 ％”）<br>###<br>＃＃检验二<br>#print（”检验二”）<br>＃#'larger＇代表高于alpha 时成立，<br>#$z_stat,$ $p_val=$proportionsztest(nonum,allnum,wannap0,,alternativ $e='larger')$# print(f"Zstatistic:$\{z_stat\}$ $P-value:\{p_val\}")$</td>
</tr><tr>
<td rowspan="2">446<br>448<br>449<br>450<br>451<br>452<br>453<br>454<br>455<br>456<br>457<br>458<br>459<br>400<br>461<br>462<br>463<br>404<br>465<br>466<br>467<br>468<br>460<br>470<br>471<br>473<br>473</td>
<td>#<br>＃＃判断原假设<br>*$\text {alpha}=0.10$#if $p_val<alpha:$#print（”拒绝零假设：即认为有90 ％的把握认为次品率大于10 ％”）<br>#else:<br>#print（”接受零假设：即没有足够的证据认为次品率大于10 ％”）<br>＃todo ：生成合理的样本</td>
</tr><tr>
<td>import numpy as np<br>import pandas as pd<br>＃样本总数确定<br>data $\text {num}=1000$data0 $\text {num=int(data_{num}*}0.12\text {)}$data1 $\checkmark$ $um=int(data_num-data_0_num)$＃样本生成<br>np.random.seed(1024)<br>data $\text {get=np}$.concatenate $((np.zeros(data_0_num)$ $,np.ones(data_1_num)))$np.random.shuffle(dataget)<br>＃样本保存<br>$\mathrm {df}=\mathrm {pd}$.DataFrame(dataget,columns=|样本（0 为次品，1 为合格）']）<br>$f1=$第一间／问题一数据，xlsx ＇<br>$to_excel(f1,index=False)$df.t<br>print ( f ”样本已成功生成并保存到｛f1 ｝文件中。”）<br>中国大学生在线ov.cn</td>
</tr></table>

题一代码

dxs.n

<!-- 31 -->

