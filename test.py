import streamlit as st

# 웹페이지 제목
st.title("Streamlit 웹페이지 예제")

# 사이드바 추가
st.sidebar.header("사이드바 메뉴")
page = st.sidebar.selectbox("페이지 선택", ["홈", "소개", "연락처"])

# 페이지에 따라 다른 내용 표시
if page == "홈":
    st.header("홈 페이지")
    st.write("이곳은 홈 페이지입니다. Streamlit을 이용해 만든 웹앱입니다.")
    
elif page == "소개":
    st.header("소개 페이지")
    st.write("이 웹페이지는 Streamlit을 이용하여 만들어졌습니다.")

elif page == "연락처":
    st.header("연락처 페이지")
    st.write("문의사항이 있으면 아래 이메일로 연락주세요.")
    st.email_input("이메일 입력")

# 사용자 입력 예제
name = st.text_input("이름을 입력하세요:")
if name:
    st.write(f"반갑습니다, {name}님!")

# 버튼 예제
if st.button("클릭하세요!"):
    st.write("버튼이 클릭되었습니다!")

# 숫자 입력 슬라이더
age = st.slider("나이를 선택하세요", 1, 100, 25)
st.write(f"선택한 나이: {age}")

# 파일 업로드
uploaded_file = st.file_uploader("파일을 업로드하세요")
if uploaded_file is not None:
    st.write("파일이 업로드되었습니다!")
