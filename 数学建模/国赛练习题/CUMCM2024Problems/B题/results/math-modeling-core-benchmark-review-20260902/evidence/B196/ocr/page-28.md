<table border="1" ><tr>
<td>allfitness.append(fitnessscores)<br>＃保留最好的精英个体<br>elites =sortedpopulation[:elitesize]<br>＃其余个体通过交叉与变异生成<br>$new_population=elites[:]$ $whilelen(new_population)<pop_size:$:<br>$frandom.random()<crossover_rate$parent1,parent2 = random.sample(sortedpopulation[:popsize//2],2)<br>$child1,child2=crossover(parent1,parent2)$ $new_population.extend([child1,child2])$else:<br>newpopulation.append(random.choice(sortedpopulation[:popsize//2]))<br>＃变异<br>for individual in newpopulation[elitesize:]:＃精英个体不参与变异<br>$ifrandom.random()<mutation_rate:$mutate(individual)<br>$population=new_population$＃计算最终种群的适应度<br>$final_fitness_scores=fitness_parallel(population)$＃按适应度对最终种群排序<br>$top_individuals=sorted(zip(final_fitness_scores$,population), $reverse=True)[:10]$</td>
</tr></table>

中国大学生在线

dxs.moe.gov.cn

<!-- 28 -->

