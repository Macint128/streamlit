import streamlit as st

# HTML과 CSS를 이용한 원형 버튼 스타일 적용
st.markdown("""
    <style>
    .round-button {
        display: inline-block;
        background-color: #4CAF50;  /* 버튼 배경 색 */
        color: white;  /* 텍스트 색 */
        padding: 20px;
        border-radius: 50%;  /* 원형으로 만들기 */
        text-align: center;
        font-size: 18px;
        cursor: pointer;
        width: 80px;
        height: 80px;
        border: none;
    }
    </style>
    <button class="round-button" onclick="window.location.href='#'">Click</button>
""", unsafe_allow_html=True)
