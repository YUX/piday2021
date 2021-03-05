import streamlit as st
import streamlit.components.v1 as components
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.


with open('3.html', 'r', encoding='utf-8') as f:
    components.html(f.read())

import app1
import app2
import app3
import app4
import app5


PAGES = {
    "在 π 中找到学号🔦": app1,
    "计算🥧的统计方法🎲": app2,
    "计算🥧的数学方法🧮": app3,
    "计算🥧的物理方法🪐": app4,
    "Reference📄": app5,
}

st.sidebar.title('Happy $\pi$ Day!!!!!!!1')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
st.sidebar.write("""
##### Beijing University of Technology
##### Faculty of Science
##### XIAO Yu 18041907
##### 2021.3.1415926535……
***
[![GitHub badge](https://img.shields.io/github/stars/YUX/piday2021.svg?logo=github&style=social)](https://github.com/YUX/piday2021)
""")
page = PAGES[selection]
page.app()