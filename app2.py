import streamlit as st
import streamlit.components.v1 as components
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def app():

    st.title("随机点落在四分之一扇形区域的概率是多少?")

    MonteCarlomethod = Image.open('MonteCarlomethod.jpg')
    st.image(MonteCarlomethod, caption='Monte Carlo method',use_column_width=True)

    n = st.slider(label="选择随机实验次数:", min_value=100, max_value=10000,value=5000,step=1)
    p = np.random.rand(n, 2)
    pointIn = [(x, y) for x, y in p if x**2 + y**2 < 1]
    pointOut = [(x, y) for x, y in p if x**2 + y**2 >= 1]

    piexpe = 4*len(pointIn)/n


    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.scatter(*zip(*pointIn), marker='x')
    plt.scatter(*zip(*pointOut), marker='+')
    st.pyplot(plt)
    st.write(f"总随机点数 n = {n}, 距离原点小于1的点数 m = {len(pointIn)}")
    st.latex(r'''\pi=4*\frac{n}{m} =''')
    with open('style.html', 'r', encoding='utf-8') as f:
        pretty_number = f.read()
        pretty_number += "<div align=\"center\" class=\"pi\">"
        pretty_number += "".join(
            [f"<span class=\"d{x}\"><font size=\"6\">{x}</font></span>" for x in str(piexpe)])
        pretty_number += "</div>"
        components.html(pretty_number)

    st.write(
    '''
    ***
    ### Reference📄
    1. [圆周率](https://zh.wikipedia.org/wiki/%E5%9C%93%E5%91%A8%E7%8E%87)
    2. [怎样计算圆周率](https://math.nuist.edu.cn/mathlab/3667/list.htm)
    3. [六种方法计算圆周率](http://littledva.cn/article-16/)
    4. [Yet another π computation algorithms](https://algomaths.tech/yet-another-pi-computation-algorithms/)
    5. [Numberphile - FOUR interesting ways to calculate Pi](https://www.bradyharanblog.com/blog/2015/10/1/calculating-pi)
    '''
    )