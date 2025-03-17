import streamlit as st

# macOS 스타일 적용을 위한 CSS
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@400;600&display=swap');
        html, body, [class*="css"] { font-family: 'SF Pro Display', sans-serif; background-color: #F5F5F7; }
        .macos-window { background: white; width: 500px; margin: 30px auto; padding: 20px; border-radius: 12px; 
                        box-shadow: 0 4px 10px rgba(0,0,0,0.1); position: relative; }
        .window-buttons { position: absolute; top: 10px; left: 10px; display: flex; gap: 8px; }
        .window-button { width: 12px; height: 12px; border-radius: 50%; display: inline-block; }
        .close { background: #FF605C; } .minimize { background: #FFBD44; } .maximize { background: #00CA4E; }
        .stButton>button { border-radius: 8px; background: #007AFF; color: white; font-weight: bold; padding: 8px 20px; border: none; }
        .stTextInput>div>div>input { border-radius: 8px; border: 1px solid #D1D1D6; padding: 8px; font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

# macOS 창 UI
st.markdown('<div class="macos-window">', unsafe_allow_html=True)
st.markdown('<div class="window-buttons"><span class="window-button close"></span><span class="window-button minimize"></span><span class="window-button maximize"></span></div>', unsafe_allow_html=True)

st.title("macOS 스타일 앱")
text = st.text_input("이름을 입력하세요")
if st.button("확인"):
    st.success(f"안녕하세요, {text}님!")

st.markdown('</div>', unsafe_allow_html=True)