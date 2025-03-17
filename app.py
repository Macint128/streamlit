import streamlit as st

# macOS 스타일 적용을 위한 CSS
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'SF Pro Display', sans-serif;
            background-color: #F5F5F7;
        }

        .stButton>button {
            border-radius: 8px;
            background: #007AFF;
            color: white;
            font-weight: bold;
            padding: 8px 20px;
            border: none;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
        }

        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 1px solid #D1D1D6;
            padding: 10px;
            font-size: 16px;
        }

        .macos-window {
            background: white;
            width: 600px;
            margin: 20px auto;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            position: relative;
        }

        .window-buttons {
            position: absolute;
            top: 10px;
            left: 10px;
            display: flex;
            gap: 8px;
        }

        .window-button {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            display: inline-block;
        }

        .close { background: #FF605C; }
        .minimize { background: #FFBD44; }
        .maximize { background: #00CA4E; }

    </style>
    """,
    unsafe_allow_html=True
)

# macOS 스타일 창
st.markdown('<div class="macos-window">', unsafe_allow_html=True)

# macOS 창 버튼
st.markdown(
    """
    <div class="window-buttons">
        <span class="window-button close"></span>
        <span class="window-button minimize"></span>
        <span class="window-button maximize"></span>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("macOS 스타일 앱")
st.write("이것은 macOS 디자인을 Streamlit으로 구현한 예제입니다.")

# macOS 스타일 입력 필드
text = st.text_input("이름을 입력하세요", "")

# macOS 스타일 버튼
if st.button("확인"):
    st.success(f"안녕하세요, {text}님!")

st.markdown('</div>', unsafe_allow_html=True)
