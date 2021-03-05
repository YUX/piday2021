import streamlit as st
import streamlit.components.v1 as components
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import math



    
def app():

    st.title("两个物体发生完全弹性碰撞的次数是多少?")
    mass = st.select_slider(
        '选择大物体质量:',
        options=['1kg', '100kg', '10000kg', '1000000kg', '100000000kg', '10000000000kg'])

    
    video_file = open(f'./videos/{mass}.webm', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    st.write(f"$Mass = {mass[:-2]}$")
    l = int(math.log(int(mass[:-2]), 100)+0.01)
    st.write(f"$log_{{100}}(Mass) = {l}$")
    Collisions = "31415926"[:l+1]
    st.write(f"$Collisions = {Collisions}$")
    st.latex(r"""\pi = \cfrac{Collisions}{10^{log_{100}(Mass)}} =""")
    picollis = int(Collisions)/10**(l)
    picollis = 3 if picollis == 3.0 else picollis
    with open('style.html', 'r', encoding='utf-8') as f:
        pretty_number = f.read()
        pretty_number += "<div align=\"center\" class=\"pi\">"
        pretty_number += "".join(
            [f"<span class=\"d{x}\"><font size=\"6\">{x}</font></span>" for x in str(picollis)])
        pretty_number += "</div>"
        components.html(pretty_number)
    
    st.write(
    '''
    ***
    ### Reference📄
    1. [圆周率](https://zh.wikipedia.org/wiki/%E5%9C%93%E5%91%A8%E7%8E%87)
    2. [Yet another π computation algorithms](https://algomaths.tech/yet-another-pi-computation-algorithms/)
    3. [一个计数谜题的意外答案](https://www.bilibili.com/video/BV1nt411p7F9)
    4. [为什么方块碰撞能够用来计算π？](https://www.bilibili.com/video/BV1bt41147H5)
    5. [如何将碰撞的方块等效为光线...来计算π？](https://www.bilibili.com/video/BV1Mb41187jL)
    6. [如何从碰撞过程求圆周率π？一个奇妙的物理、代数、几何结合问题](https://www.bilibili.com/video/BV1gZ4y1H78s)
    '''
    )