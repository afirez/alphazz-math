# math & markdown

[toc]

## 1 概述

有道云笔记 markdown 编辑数学公式：

- inline模式使用 \`\$…\$\`包裹公式，如果是其他编辑器一般使用 \$…\$ 包裹即可
- 单行模式使用 \`\`\`math…\`\`\`包裹，如果是其他编辑器使用 \$\$…\$\$ 包裹即可
- 以上内容中…表示被包裹的数学公式等

[latex.codecogs.com 生成 Latex 图片](http://latex.codecogs.com/)
在不支持 mardown 预览的情况下使用， 譬如 github。

```partial
# 偏微分方程
\frac{\partial u}{\partial t} = h^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}\right)}

# 矩阵
\begin{bmatrix}
{a_{11}}&{a_{12}}&{\cdots}&{a_{1n}}\\
{a_{21}}&{a_{22}}&{\cdots}&{a_{2n}}\\
{\vdots}&{\vdots}&{\ddots}&{\vdots}\\
{a_{m1}}&{a_{m2}}&{\cdots}&{a_{mn}}\\
\end{bmatrix}
```

![偏微分方程](http://latex.codecogs.com/gif.latex?%5Chuge%20%5Cfrac%7B%5Cpartial%20u%7D%7B%5Cpartial%20t%7D%20%3D%20h%5E2%20%5Cleft%28%20%5Cfrac%7B%5Cpartial%5E2%20u%7D%7B%5Cpartial%20x%5E2%7D%20&plus;%20%5Cfrac%7B%5Cpartial%5E2%20u%7D%7B%5Cpartial%20y%5E2%7D%20&plus;%20%5Cfrac%7B%5Cpartial%5E2%20u%7D%7B%5Cpartial%20z%5E2%7D%5Cright%29%7B%5Ccolor%7BRed%7D%20%7D)

![矩阵](http://latex.codecogs.com/gif.latex?%5Chuge%20%5Cbegin%7Bbmatrix%7D%20%7Ba_%7B11%7D%7D%26%7Ba_%7B12%7D%7D%26%7B%5Ccdots%7D%26%7Ba_%7B1n%7D%7D%5C%5C%20%7Ba_%7B21%7D%7D%26%7Ba_%7B22%7D%7D%26%7B%5Ccdots%7D%26%7Ba_%7B2n%7D%7D%5C%5C%20%7B%5Cvdots%7D%26%7B%5Cvdots%7D%26%7B%5Cddots%7D%26%7B%5Cvdots%7D%5C%5C%20%7Ba_%7Bm1%7D%7D%26%7Ba_%7Bm2%7D%7D%26%7B%5Ccdots%7D%26%7Ba_%7Bmn%7D%7D%5C%5C%20%5Cend%7Bbmatrix%7D)

## 2 希腊字母

如果存在大写形式，则将命令的首字母大写即可，如果不存在相应命令，则直接使用大写形式表示即可。

| 显示内容  | 命令  | 显示内容  | 命令  |
| :---:    | :----: | :---:    | :----: |
| $\alpha$ | \alpha | $\beta$  | \beta |
| $\gamma$ | \gamma | $\delta$ | \delta |
| $\epsilon$ | \epsilon | $\zeta$ | \zeta |
| $\eta$ | \eta | $\theta$ | \theta |
| $\iota$ | \iota | $\kappa$ | \kappa |
| $\lambda$ | \lambda | $\mu$ | \mu |
| $\nu$ | \nu | $\xi$ | \xi |
| $\pi$ | \pi | $\rho$ | \rho |
| $\sigma$ | \sigma | $\Sigma$ | \Sigma |
| $\upsilon$ | \upsilon | $\phi$ | \phi |
| $\chi$ | \chi | $\psi$ | \psi |
| $\omega$ | \omega | $\tau$ | \tau |

## 3 字母修饰

### 3.1 上下标

- 上标 ^: $x^2$
- 下标 _: $x_2$
- 上下标 : $C^2_n$

### 3.2 矢量(向量)

- 单向量 \vec{x}: $\vec{x}$
- 多向量 \overrightarrow{xy}: $\overrightarrow{xy}$
- 多向量 \overleftarrow{xy}: $\overleftarrow{xy}$

### 3.3 字体

| 显示内容  | 命令  | 说明  |
| :---:    | :----: | :---:    |
| $\mathtt{ABC}$ | \mathtt{ABC} | 印刷 标题用  |
| $\mathbb{ABC}$ | \mathbb{ABC} | 黑体 |
| $\mathsf{ABC}$ | \mathsf{ABC} | 宋体 正文用 |

### 3.4 括号等

| 显示内容  | 命令  | 说明  |
| :---:    | :----: | :---:    |
| () | () | 小括号  |
| [] | [] | 中括号 |
| $\lbrace{ABC}\rbrace$| \lbrace{ABC}\rbrace | 大括号 |
| $\langle{ABC}\rangle$ | \langle{ABC}\rangle| 尖括号 |
| $\lceil \frac{x}{2} \rceil$ | \lceil \frac{x}{2} \rceil | 上取整 |
| $\lfloor \frac{x}{2} \rfloor$ |\lfloor \frac{x}{2} \rfloor | 下取整 |
| $\left( \frac{x}{2} \right)$ | \left( \frac{x}{2} \right) | 适应所有括号，使括号与公式相适应 |
| ax+by+c=0 （1.1） | \$\$ax+by+c=0 \tag{1.1}\$\$  | 给公式加编号 (单行)|


### 3.5 分式于根式

| 显示内容  | 命令  | 说明  |
| :---:    | :----: | :---:    |
| $\frac{x}{y}$ | \frac{x}{y} | x/y  |
| $\sqrt[x]{y}$ | \sqrt{指数}{底} |  开根号 |



### 3.6 求和，极限，积分, 偏微分方程

| 显示内容  | 命令  | 说明  |
| :---:    | :----: | :---:    |
| $\sum_{i=1}^{n}{a_i}$ | \sum_{i=1}^{n}{a_i} | 求和  |
| $\prod \frac{1}{i^2}$ | \prod \frac{1}{i^2} |  累乘 |
| $\lim_{x \to 0}$ | \lim_{x \to 0} |  极限 |
| $\lim_{x \rightarrow +\infty}$ | \lim_{x \rightarrow +\infty} |  极限 |
| $\int_{0}^{+\infty}{fxdx}$ | \int _0 ^{+\infty} {fxdx} |  积分 |
| $\mathrm{d}$ | \mathrm{d} |  积分 |
| $\int_2^3 x^2 {\rm d}x$ | \int_2^3 x^2 {\rm d}x |  积分 |
| $\iint$ | \iint |   |
| $\iiint$ | \iiint |   |
| $\oint$ | \oint |   |
| $\prime$ | \prime |   |

偏微分方程

```partial
$\frac{\partial u}{\partial t} = h^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}\right)$
```
即显示为
$\frac{\partial u}{\partial t} = h^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} + \frac{\partial^2 u}{\partial z^2}\right)$

### 3.7 特殊函数，特殊符号，空格

| 显示内容  | 命令   |
| :---:    | :----: |
| $\sin x$ | \sin x |  
| $\ln x$ | \ln x |
| $\max （A，B，C）$ | \max （A，B，C） |
| $\infty$ | \infty |
| $\cup$ | \cup |
| $\cap$ | \cap |
| $\subset$ | \subset |
| $\subseteq$ | \subseteq |
| $\supset$ | \supset |
| $\supseteq$ | \subseteq |
| $\in$ | \in |
| $\notin$ | \notin |
| $\varnothing$ | \varnothing |
| $\forall$ | \forall |
| $\exists$ | \exists |
| $\lnot$ | \lnot |
| $\partial$ | \partial |
| $a \quad b$ | a\quad    b (4个空格) |
| $a\quad b$ | a\quad b (1个空格) |

## 4 矩阵相关

$$
  \left[
  \begin{matrix}
   1 & 2 & 3 \\
   4 & 5 & 6 \\
   7 & 8 & 9
  \end{matrix} \tag{1}
  \right]
$$

### 4.1 基本使用

起始标记 \begin{类型}，结束标记 \end{类型}，根据需求修改“类型”的内容即可。
内部换行使用双反斜杠 \\ ，即表示不同行
元素之间使用 & 分隔，即表示不同列

### 4.2 方程组

- \begin{cases} 和 \end{cases} 包裹

```cases

 ```math
\begin{cases}
a_1x+b_1y+c_1z=d_1 \\
a_2x+b_2y+c_2z=d_2 \\
a_3x+b_3y+c_3z=d_3 \\
\end{cases} \tag{方程组}```

```

即显示为

```math
\begin{cases}
a_1x+b_1y+c_1z=d_1 \\
a_2x+b_2y+c_2z=d_2 \\
a_3x+b_3y+c_3z=d_3 \\
\end{cases} \tag{方程组}
```

### 4.3 矩阵无边框

- \begin{matrix} 和 \end{matrix} 包裹

```matrix
$$
 \begin{matrix}
 1 & 0 & 0 \\
 0 & 1 & 0 \\
 0 & 0 & 1
 \end{matrix} \tag(无边框矩阵)
$$
```

$$
 \begin{matrix}
 1 & 0 & 0 \\
 0 & 1 & 0 \\
 0 & 0 & 1
 \end{matrix} \tag{无边框矩阵}
$$

### 4.4 矩阵边框

$\begin{pmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$, $\begin{bmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$,$\begin{Bmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{Bmatrix}$,$\begin{vmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{vmatrix}$,$\begin{Vmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{Vmatrix}$

- pmatrix ：小括号边框

$$
 \begin{pmatrix}
 1 & 0 & 0 \\
 0 & 1 & 0 \\
 0 & 0 & 1
 \end{pmatrix} \tag{小括号边框矩阵}
$$

- bmatrix ：中括号边框

$$
 \begin{bmatrix}
 1 & 0 & 0 \\
 0 & 1 & 0 \\
 0 & 0 & 1
 \end{bmatrix} \tag{中括号边框矩阵}
$$

- Bmatrix ：大括号边框

$$
 \begin{Bmatrix}
 1 & 0 & 0 \\
 0 & 1 & 0 \\
 0 & 0 & 1
 \end{Bmatrix} \tag{大括号边框矩阵}
$$

- vmatrix ：单竖线边框

$$
 \begin{vmatrix}
 1 & 0 & 0 \\
 0 & 1 & 0 \\
 0 & 0 & 1
 \end{vmatrix} \tag{单竖线边框矩阵}
$$

- Vmatrix ：双竖线边框

$$
 \begin{Vmatrix}
 1 & 0 & 0 \\
 0 & 1 & 0 \\
 0 & 0 & 1
 \end{Vmatrix} \tag{单竖线边框矩阵}
$$

使用上述内容替换 \begin{matrix}和 \end{matrix} 中的 matrix 即可达到相应的效果


### 4.5 矩阵包含省略元素

- 横省略 \cdots : $\cdots$
- 竖省略 \vdots : $\vdots$
- 斜省略 \ddots : $\ddots$

```matrix
$$
\begin{bmatrix}
{a_{11}}&{a_{12}}&{\cdots}&{a_{1n}}\\
{a_{21}}&{a_{22}}&{\cdots}&{a_{2n}}\\
{\vdots}&{\vdots}&{\ddots}&{\vdots}\\
{a_{m1}}&{a_{m2}}&{\cdots}&{a_{mn}}\\
\end{bmatrix}
$$
```

即显示为

$$
\begin{bmatrix}
{a_{11}}&{a_{12}}&{\cdots}&{a_{1n}}\\
{a_{21}}&{a_{22}}&{\cdots}&{a_{2n}}\\
{\vdots}&{\vdots}&{\ddots}&{\vdots}\\
{a_{m1}}&{a_{m2}}&{\cdots}&{a_{mn}}\\
\end{bmatrix} \tag{包含省略元素的矩阵}
$$

### 4.6 阵列 Array

- 起始标记 \begin{array}，结束标记 \end{array}
- 在 \begin{array}{} 中声明各列的对齐方式
  - l: 左对齐 ；c: 居中；r：右对齐
  - |：竖直线，用于分隔
  - \hline：插入水平线

```matrix
$$
\begin{array}{c|lll}
{\downarrow}&{a}&{b}&{c} \\
\hline
{R_1}&{c}&{b}&{a}\\
{R_2}&{b}&{c}&{c}\\
\end{array}
$$
```

即显示为

$$
\begin{array}{c|lll}
{\downarrow}&{a}&{b}&{c} \\
\hline
{R_1}&{c}&{b}&{a}\\
{R_2}&{b}&{c}&{c}\\
\end{array} \tag{阵列 Array}
$$
