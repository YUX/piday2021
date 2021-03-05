import streamlit as st
import streamlit.components.v1 as components
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
from math import gcd


    
def app():

    st.title("两个自然数互质的概率是多少?")
    st.markdown("""设 $p$ 是一个质数，则两个任取的自然数 $x$ , $y$ 同时被 $p$ 整除的概率就是 $\cfrac{1}{p^2}$ 。于是若对所有的 $p$, $x$ 和 $y$ 均不同时被 $p$ 整除，其概率就是""")
    st.latex(r"""P_{Coprime} = \prod_p \left(1-\frac{1}{p^2}\right) = \left( \prod_p \frac{1}{1-p^2} \right)^{-1} = \frac{1}{\zeta(2)} = \frac{6}{\pi^2}.""")
    n = st.slider(label="选择随机数对个数:", min_value=100, max_value=10000,value=5000,step=1)
    p = np.random.randint(2,100, size=(n, 2))
    df = pd.DataFrame(p,columns=['x', 'y'])
    df["isCoprime"] =  [gcd(x,y)==1 for x,y in p ]
    coprime = len([x for x in df["isCoprime"] if x==1])

    st.dataframe(df.style.applymap(lambda x: 'background-color : yellow' if x==1 else ''))
    st.write(f"在 {n} 个随机自然数对中，有 {coprime} 个数对互质")

    picopr = (6 / (coprime/n))**0.5
    st.latex(r"\pi = \sqrt{\cfrac{6}{P_{Coprime}}} =")
    with open('style.html', 'r', encoding='utf-8') as f:
        pretty_number = f.read()
        pretty_number += "<div align=\"center\" class=\"pi\">"
        pretty_number += "".join(
            [f"<span class=\"d{x}\"><font size=\"6\">{x}</font></span>" for x in str(picopr)])
        pretty_number += "</div>"
        components.html(pretty_number)
    
    st.write(
    '''
    ***
    ### Reference📄
    1. [Generating π from 1,000 random numbers](https://www.youtube.com/watch?v=RZBhSi_PwHU)
    2. [任意两个自然数互质的概率？](https://www.jlao.net/technology/2024/)
    3. [Probability that two random numbers are coprime is $\cfrac{6}{\pi^2}$](https://math.stackexchange.com/questions/64498/probability-that-two-random-numbers-are-coprime-is-frac6-pi2)
    4. [On the probability that two random integers are coprime](https://arxiv.org/abs/1806.00053)
    '''
    )