import streamlit as st


st.title('การทดสอบเขียนเว็บด้วย Python')
st.header('สาร์ทจีน บูรณะสุวรรณ')
st.subheader('สาขาวิชาเทคโนโลยีสารสนเทศ')
st.markdown("----")

col1, col2 = st.columns(2)
#col1.write("This is column 1")
#col2.write("This is column 2")
with col1:
    st.image('./pic/Stark.jpg')
with col2:
    st.image('./pic/iris.jpg')

html_1 = """
<div style="background-color:#E7EFF9;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5 style="color:#000000">สถิติข้อมูลดอกไม้</h5></center>
</div>
"""
st.markdown(html_1, unsafe_allow_html=True)
st.markdown("")


import pandas as pd

dt=pd.read_csv('./data/iris.csv')
st.write(dt.head(10))

dt1 = dt['petal.length'].sum()
dt2 = dt['petal.width'].sum()
dt3 = dt['sepal.length'].sum()
dt4 = dt['sepal.width'].sum()

dx = [dt1, dt2, dt3, dt4]
dx2 = pd.DataFrame(dx, index=["d1", "d2", "d3", "d4"])