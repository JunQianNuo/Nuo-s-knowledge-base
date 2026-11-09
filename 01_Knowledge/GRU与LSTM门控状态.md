---
schema_version: 2
type: concept
time: '2026-11-08T09:17:40+08:00'
topics:
- '[[02_Maps/MOC-深度学习]]'
source:
- '[[03_Sources/Courses/深度学习/课堂笔记/2026-11-02-第18节-深度学习理论与RNN原理授课]]'
---
# GRU与LSTM门控状态

## 严格定义与核心内容

GRU用复位门r和更新门z调节旧态参与候选及新态混合；本来源约定h_t=z_t⊙h_{t−1}+(1−z_t)⊙h̃_t，所以z近1保留旧态。

不同实现的命名和矩阵位置可变，须按定义对照。

LSTM另有记忆s_t=f_t⊙s_{t−1}+i_t⊙g_t，h_t=o_t⊙tanh(s_t)，f/i/o分别遗忘、写入、输出，门由Sigmoid计算而非人工常数。

加法记忆通路帮助长依赖，但不保证无训练困难。

LSTM全称Long Short-Term Memory。
