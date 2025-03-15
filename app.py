import streamlit as st

st.title("안녕")
st.write("이건 간단한 웹패이지야.")

def button():
    if st.button("버튼을 눌러보세요!"):
        st.write("버튼이 눌렸어요!")
