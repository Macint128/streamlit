import streamlit as st

st.title('나만의 웹앱')

st.write("이건 간단한 웹앱입니다!")

user_input = st.text_input("이름을 입력하세요:")
st.write(f"안녕하세요, {user_input}님!")
