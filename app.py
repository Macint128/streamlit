import streamlit as st

# macOS 스타일 Dock을 위한 CSS
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'SF Pro Display', sans-serif;
            background-color: #F5F5F7;
        }

        /* Dock 스타일 */
        .dock-container {
            position: fixed;
            bottom: 20px;
            left: 0;
            width: 100%;
            display: flex;
            justify-content: center;
            gap: 30px;
            padding: 10px;
        }

        .dock-item {
            width: 50px;
            height: 50px;
            background-color: #FFF;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }

        .dock-item:hover {
            transform: scale(1.2);
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.2);
        }

        .dock-item img {
            width: 30px;
            height: 30px;
        }

        /* 앱 이름 스타일 */
        .dock-item-name {
            font-size: 12px;
            margin-top: 8px;
            color: #333;
            text-align: center;
        }

        /* 클릭 이벤트 표시용 */
        .app-name {
            text-align: center;
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Dock 아이콘들
dock_items = [
    {"name": "Safari", "icon": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Safari_browser_logo_2015.svg", "app": "Safari"},
    {"name": "Mail", "icon": "https://upload.wikimedia.org/wikipedia/commons/1/17/Apple_Mail_logo.svg", "app": "Mail"},
    {"name": "Calendar", "icon": "https://upload.wikimedia.org/wikipedia/commons/0/0d/Apple_Calendar_logo.svg", "app": "Calendar"},
    {"name": "Messages", "icon": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Apple_Messages_icon.svg", "app": "Messages"},
    {"name": "Music", "icon": "https://upload.wikimedia.org/wikipedia/commons/a/a7/Apple_Music_logo.svg", "app": "Music"},
]

# Dock 표시
st.markdown('<div class="dock-container">', unsafe_allow_html=True)

# 아이콘 생성
selected_app = None
for item in dock_items:
    if st.button(item["name"], key=item["name"]):
        selected_app = item["app"]
    
    st.markdown(f"""
        <div class="dock-item">
            <img src="{item['icon']}" alt="{item['name']}">
        </div>
        <div class="dock-item-name">{item['name']}</div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# 선택된 앱 이름 표시
if selected_app:
    st.markdown(f"<div class='app-name'>{selected_app} 앱을 선택했습니다!</div>", unsafe_allow_html=True)
