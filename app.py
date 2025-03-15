import streamlit as st

st.title('안녕')
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-color: #ADD8E6; /* 연한 파란색 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

user_input = st.text_input("이름을 입력하세요:")
st.write(f"안녕하세요, {user_input}님!")
