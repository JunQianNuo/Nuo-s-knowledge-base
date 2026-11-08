---
schema_version: 2
type: method
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-深度学习]]'
source:
- '[[03_Sources/Courses/深度学习/作业/第1-6章-课件与课堂提问汇编作业]]'
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-09-16-第6节-深度学习优化理论讲座]]'
---
# AdaGrad与RMSProp坐标缩放

g为列梯度，ggᵀ是半正定外积矩阵，gᵀg是标量，g⊙g是逐元素平方。矩阵型AdaGrad累计G=∑ggᵀ后用逆平方根缩放，奇异时需广义逆或正则化；实际常取对角近似。RMSProp以v←γv+(1−γ)g⊙g跟踪近期尺度，θ←θ−ηg/(√v+ε)，平方开方除法逐元素。小常数稳定分母，效果仍需按目标与超参数验证。
