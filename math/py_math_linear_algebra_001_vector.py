"""
机器学习理论
这部分主要是要掌握一些典型的机器学习算法，如分类、聚类、推荐、概率图、神经网络。
（可以分为初级、中级和高级三个阶段，每个阶段的侧重点不同。）

（1）初级阶段
初级阶段推荐可以看《机器学习算法原理与编程实践 》和《机器学习实战》这两本书。

这两本书更偏向于算法的应用方面，学习起来相对轻松一些。如果一上来直接就啃那些纯算法理论，估计很多人是坚持不下去的。

再者，一个东西，当你还不知道它是什么，有什么用，以及怎么用时，让你去硬着头皮啃，你一定会感觉很郁闷，并且根本不可能能够深入理解那些理论。

所以，个人强烈建议不要一上来就贪图那些算法理论的推导，先大胆的去了解各个算法的应用场合并尝试着应用，这对你入门机器学习是一个非常好的选择。

（2）中级阶段
中级阶段就要开始啃那些算法背后的理论了，前面应用是知其然，现在要开始知其所以然。

这个阶段重点推荐看林轩田的《机器学习基石》和《机器学习技法》视频，总共三十二课，每一课都相当精彩，细致学下来需要三个月，我指的是细致的看，每一课都应该写笔记，梳理脉络，强烈建议做笔记。

踏踏实实看完，面试中让你推个svm讲讲adboost，gbdt原理基本就是手到擒来，再辅以李航的《统计学习方法》和周志华的《机器学习》（俗称“西瓜书”）查漏补缺，基础就算比较扎实了。

（3）高级阶段
高级阶段就是要自己开始去灵活运用并组合各个算法了。这个阶段可以在网上找一些比较典型的项目来进行实战演练。

推荐学习资源：Kaggle、CCF、Datacastle、阿里云天池等。

kaggle是国外一个专门做数据挖掘比赛的地方，里面很多比赛比较适合新人，而且里面的氛围也比较好，每个比赛都有对应的论坛，时不时有人会发布自己的代码，大家集思广益一起讨论，可以学到很多。
"""
import numpy as np
# # 1 向量表示
# 行向量表示
A = np.array([1,2,3,4])
# print(A.transpose()) # 一维转置无效
print(A)

# 如何表示列向量 ？？？
# 行向量为 1 x m 的矩阵， 列向量为 n x 1 的矩阵
# 用行向量矩阵生成列向量
A = np.array([[1,2,3]])
print(A.T)
# 用列向量矩阵生成行向量
A = np.array([[4],[5],[6]])
print(A.T)

# # 2 向量的加法: [u1 u2 u3]T + [v1 v2 v3]T = [u1+v1 u2+v2 u3+v3]T
u = np.array([[1,2,3]]).T
v = np.array([[5,6,7]]).T
print(u + v)

# # 3 向量的数乘: c[u1 u2 u3]T = [cu1 cu2 cu3]T
u = np.array([[1,2,3]]).T
print(3 * u)

# # 4 向量的内积: u . v = [u1 u2 u3]T . [v1 v2 v3]T = u1v1 + u2v2 + u3v3 = |u||v|cos theta
# 二维向量的内积的几何意义: 表示 u 的单位向量模乘以 v 在 u 上的投影
# [!] numpy 函数库中的内积运算 dot，参数要求必须是一维行向量
# [!] 二维行向量报错
# u = np.array([[3,5,2]])
# v = np.array([[1,4,7]])
#
# [!] 二维行向量转置报错
# u = np.array([[3,5,2]]).T
# v = np.array([[1,4,7]]).T
#
u = np.array([3,5,2])
v = np.array([1,4,7])
print(np.dot(u, v))

# # 5 向量的外积: u x v = [u1 u2]T x [v1 v2]T = u1v2 - u2v1
# 二维向量的外积的几何意义: 表示两个向量所张成的平行四边形的面积。 u x v = |u||v| sin theta
u = np.array([3,5])
v = np.array([1,4])
print(np.cross(u, v))
# 三维空间外积相对复杂点: u x v = [u1 u2 u3]T x [v1 v2 u3]T = [u2v3-u3v2 u1v3-u3v1 u1v2-u2v1]T 
# 这个向量的几何意义： 表示两个向量所表示的平面的法向量
u = np.array([3,3,9])
v = np.array([1,4,12])
print(np.cross(u, v))

# # 6 向量的线性组合
# 二维线性组合： cu + dv
# 三维线性组合： c u + d v + e w = c [u1 u2 u3]T + d [v1 v2 v3]T + e [w1 w2 w3] T
# 向量的线性组合的几何意义： 结果向量就是最初的起点到最终的终点的有向连接
u = np.array([[1,2,3]]).T
v = np.array([[4,5,6]]).T
w = np.array([[7,8,9]]).T
print(3*u + 4*v + 5*w)

# # 7 向量空间的基底
#
# 不是所有的向量都能作为基底。 
#   譬如二维空间中，非线性无关的两个向量不能作为基底， 需要线性相关的两个向量
#
# 基底中向量的数量需要等于空间的维数，即空间的秩等于基向量的秩，且基向量线性无关。
#   线性相关的两个向量的几何意义是两个向量共线。
#   譬如用两个线性无关的向量作为三维空间的基底， 只能覆盖到三维空间中两个向量所张成的平面
#
# 当且仅当 x1 = x2 = ... = xn = 0 时，线性组合 x1u1 + x2u2 + ... + xnun = 0 才能生成 0 向量， 那么这组向量就线性相关了
#
# n 维空间不等价于 Rn 空间。
#   譬如 2 维空间不仅仅只有 xoy 二维平面这一种情况，
#   一个倾斜在 3 维空间中的过原点的平面依然能被称为 2 维空间。
#   更高维的空间中同样也会包含 2 维空间。
#   需要知道， 谈及二维空间的一组基，不仅仅只有两个线性无关的二维向量，[x1 y1]T 和 [x2 y2]T, 
#     还可以是两个线性无关的三维向量，[x1 y1 z1]T 和 [x2 y2 z1]T，
#     甚至一般化为 n 维都可以构成 2 维空间的一组基，只是各个二维空间的形态不同罢了
#
# 最后， n 维空间中， 对于一组基 e1, e2, ... , en ， 空间中的向量 v 都可以表示成
#   v =  x1e1 + x2e2 + ... + xnen
#   也就是说，n 维空间的基底由 (e1, e2, ... , en) 构成，且 e1, e2, ... , en 必须线性无关。
# 
# 张成空间
#   对于一组向量，它所有线性组合构成的空间，称之为这组向量的张成空间
#   譬如线性无关的二维向量 u1, u2 的张成空间是整个二维空间 R2，
#     线性无关的三维向量 u1, u2, u3 的张成空间是整个三维维空间 R3