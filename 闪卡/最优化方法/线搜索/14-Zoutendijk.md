Zoutendijk定理的内容和推论？

---

$\sum_{k=0}^\infty\cos^2\theta_k\|\nabla f(x_k)\|^2<+\infty$

$\theta_k$: 搜索方向与负梯度夹角。

推论: 若$\cos\theta_k\geq\delta>0$（方向不趋近正交），则$\|\nabla f(x_k)\|\to 0$。

最速下降法中$\cos\theta_k=1$，Zoutendijk直接给出梯度趋于零。

是线搜索方法的收敛性基石——需$\nabla f$ Lipschitz连续。
