12 ■定义市场售价与调换损失

13 productprice=200

14 replacementloss=40

26 ＃使用提存保存已计算的状

17 memo={}

18 decisiontrace=(

19

20 ■状态转移数

21 def statetransition(state,decision,parts):

22

newstate=state.copy()

if decision=="inspectpart':

24

for part in parts:

part['detected']=True

26

part['isdefective']=(part['defectrate']&gt;=0.1)

27

newstate['allpartsinspected']=True

28

elif decision w='assenbletosemi":

newstate['semiproductpass']=all(not part['isdefective'] for part in parts)

30

elif decision == 'assenbletofinal':

newstate['finalproductpass']=nexstate.get('semiproductpass',False)

32

elif decision =='disassenblefinal':

newstate['recycled']=True

34

elif decision =n'disassenblesemi':

35

if not newstate.get('semiproductpass',False):

36

newstate['recycled']=True

37

return newstate

38

39 ■计算销售限

40 def calculatesalesprofit(state):

41

return productprice if state.get("finalproductpass',False)else 0

2

■计算回收益

44 def calculaterecyeleprofit(state,parts):

45

recycleprofit=0

46

if state.get('recycled',False):

47

for part in parts:

48

if part['detected']and not part['isdefective']:

recycleprofit += part['purchaseprice']+part['inspectioncost']

50

if state.get('seniproductpass',False):

51

recycleprofit +=sun([part['purchaseprice']+part['inspectioncost'] for part in parts])

52

return recycleprofit

53

54 ＃计算总成本

55 **def** calculatecost(decision,parts):

**if** decision=="inspectpart':

57

return sum([part['inspectioncost'] for part in parts])

58

elif decisiona='assenbletosemi':

59

return sun([part["assenblycost'] for part in parts])

60

elif decision='disassemblefinal'or decision =='disassembleseni':

61

return sum([part['disassemblycost'] for part in parts])

62

return 0

63

64 ＃动规函数

65 **def** dynamicprogramning(state,parts,depth=0):

66

if depth&gt;20:＃的深度，防止无限通归

67

return **0**

68

69

＃使用元组表示状作为存限

70

**statekey=tuple(sorted(state.itens()))**

71

72

＃如果状态已经计算过，直接返

73

**if statekey** in meno:

中国大学生在线

74

return meno[statekey]

dxs.moe.gov.cn

<!-- 29 -->

