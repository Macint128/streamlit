import streamlit as st

st.title("카운터 버튼")

# 세션 상태를 활용해 버튼을 누를 때마다 값이 증가하도록 설정
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("카운터 증가"):
    st.session_state.count += 1

st.write(f"현재 카운트: {st.session_state.count}")
