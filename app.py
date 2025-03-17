import streamlit as st
import time

# 초기 돌 크기 설정
if 'stone_size' not in st.session_state:
    st.session_state.stone_size = 1  # 돌 크기 초기값

# 돌을 키우는 함수
def grow_stone():
    st.session_state.stone_size += 1

# 제목 표시
st.title("돌 키우기 게임")

# 돌의 현재 크기 표시
st.write(f"현재 돌의 크기: {st.session_state.stone_size}")

# 돌을 키우는 버튼
if st.button("돌 키우기"):
    with st.spinner("돌이 자라고 있습니다..."):
        time.sleep(1)  # 돌이 자라는 애니메이션 효과 (1초 딜레이)
    grow_stone()
    st.success("돌이 커졌습니다!")

# 돌 크기를 리셋하는 버튼
if st.button("돌 리셋"):
    st.session_state.stone_size = 1
    st.success("돌이 초기화되었습니다.")