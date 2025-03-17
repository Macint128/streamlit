import streamlit as st
import time

st.title("안녕하세요")
st.write("이것은 간단한 웹페이지 입니다")

while True:
    if st.button("눌러봐"):
        st.write("버튼이 눌렸습니다")
        time.sleep(0.5)
    else:
        st.write(" ")