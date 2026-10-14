<table border="1" ><tr>
<td>money $+=sell$del H[0][index0]<br>del HL[0][index0]<br>del H[1][index1]<br>del HL[1][index1]<br>del H[2][index2]<br>del HL[2][index2]<br>$total_profit=money-cost-buy_cost$return totalprofit<br>＃并行计算适应度函数<br>def fitnessparallel(population):<br>with $Pool(processes=cpu_count())$as pool:<br>fitnessscores $=$list(tqdm(pool.imap(montecarlosimulation, population), $total=len(population)$, desc="Evaluating Population"))<br>return fitnessscores</td>
</tr></table>

<table border="1" ><tr>
<td>附录2</td>
</tr><tr>
<td>介绍：使用蚁群算法求解问题二中最优决策的python 代码</td>
</tr><tr>
<td>＃蚁群算法主循环<br>for iteration in tqdm(range(numiterations), desc="Ant Colony Optimization"):<br>$all_solutions=[]$ $all_objective_values=[]$for ant inrange(numants):<br>$result=[random.randint(0,1)$ forin range(4)] ＃随机生成策略<br>$obj_value=objective_function(result)$allsolutions.append(result)<br>allobjectivevalues.append(objvalue)<br>＃更新信息素<br>$pheromone*=(1-rho)$for idx, solution in enumerate(allsolutions):<br>$obj_value=all$objectivevalues[idx]<br>for i in range(len(solution)-1):<br>pheromone[solution[i],solution[i+1]]+=Q/(obj$value+1)$ ＃避免除以0<br>＃记录当前迭代中的最佳利润和对应路径<br>$combined=list(zip(all_$objectivevalues,allsolutions))<br>sortedcombined=sorted(combined,k$key=lambdax:x[0]$ $,reverse=True)$</td>
</tr></table>

<!-- 26 -->

