import streamlit as st
import streamlit.components.v1 as components
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import requests
import re
import time
import random
from PIL import Image, ImageDraw, ImageFont



def app():
    st.title('输入你的学号, 试试在圆周率中找到它🐈')


    number = st.number_input(label='',
                            min_value=0, max_value=99999999, format="%d")

    if number != 0:

        f'正在Pi中匹配{number}'

        # Add a placeholder
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'{i+1}%')
            bar.progress(i + 1)
            nd = random.random()
            if nd > 0.3:
                time.sleep(0.01)
            elif nd < 0.03:
                time.sleep(0.9)
            else:
                time.sleep(0.1)
        # with st.spinner(text='In progress'):
        #     time.sleep(5)
        #     st.success('Done')
            
                

        n = number
        r = requests.get('http://subidiom.com/pi/piday.asp', params={'s': n})

        html_doc = r.text

        # print(
            # float(re.findall(pattern="Search time was (.*?) second", string=html_doc)[0]))

        rank = re.findall(
            pattern="appears at the ([0-9,]*?)(st|nd|rd|th| )", string=html_doc)[0][0]

        b = re.findall(pattern="<font size=4>(\d*?)<font color=0f00ff>",
                    string=html_doc)[0]
        a = re.findall(pattern="</font>(\d*?)<br>", string=html_doc)[0]

        
        st.success(f'{n} 在 $\pi$ 的第 {rank} 位！')
        st.balloons()

        img_path = 'picat.jpg'
        W, H = (637, 637)
        msg = rank
        im = Image.open(img_path)
        draw = ImageDraw.Draw(im)
        w, h = draw.textsize(msg)
        # myFont = ImageFont.truetype("SimHei.ttf", 30, encoding="utf-8")
        draw.textsize(msg)
        draw.text(((W-w)/2, (H-h)/2), msg, fill="black")
        st.image(im, caption='', use_column_width=True)

        with open('style.html', 'r', encoding='utf-8') as f:
            pretty_number = f.read()
            pretty_number += "<br>"
            pretty_number += "<div align=\"center\" class=\"pi\">"
            if b:
                pretty_number += f"<font color=\"gray\" size=\"5\">...{b}</font>"
            else:
                pretty_number += f"<font color=\"gray\" size=\"5\">3.{b}</font>"
            pretty_number += "".join(
                [f"<span class=\"d{x}\"><font size=\"6\">{x}</font></span>" for x in str(number)])
            pretty_number += f"<font color=\"gray\" size=\"5\">{a}...</font>"
            pretty_number += "</div>"
            components.html(pretty_number)



    st.write("""
    ***
    ## π 中一定包含你的学号么？
    ### 一定
    如果你的学号是 8 位数，那么它一定会在 π 的前 ~18.168 亿位中出现。（认真脸.jpg）
    """)



    st.write("""
    ***
    ## π 中包含了所有可能的数字组合吗？
    ### 不好说
    $\pi$ 是一个无理数，此外 $\pi$ 还是一个超越数——它不是任何有理数系数多项式的根。$\pi$ 的数字序列被认为是随机分布的，但至今未能证明，同样 $\pi$ 的合取性(disjunctive)与正规性(normal)也未在十进制下得到证明。
    """)

    st.write(
    '''
    ***
    ### Reference📄
    1. [圆周率](https://zh.wikipedia.org/wiki/%E5%9C%93%E5%91%A8%E7%8E%87)
    2. [Does 𝜋 contain all possible number combinations?](https://math.stackexchange.com/questions/216343/does-pi-contain-all-possible-number-combinations)
    3. [Pi Does NOT Contain the Universe](http://justinparrtech.com/JustinParr-Tech/pi-does-not-contain-the-universe/)
    4. [π里包含了所有可能的数字组合吗？](https://www.guokr.com/article/439682/)
    '''
    )