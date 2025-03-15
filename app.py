import streamlit as st

# HTML, CSS, JavaScript 코드 삽입
st.markdown("""
    <style>
        /* 기본적으로 화면 상단에 노치 영역을 디자인 */
        .notch-container {
            position: fixed;
            top: 10px;
            left: 50%;
            transform: translateX(-50%);
            width: 150px;
            height: 50px;
            background-color: black;
            border-radius: 25px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-size: 16px;
            transition: all 0.3s ease;
        }

        .notch-container.expanded {
            width: 250px;
            height: 80px;
            border-radius: 40px;
            background-color: #000;
        }

        .content {
            padding-top: 100px;
            text-align: center;
        }
    </style>

    <div class="notch-container" id="notch-container">
        Notch
    </div>

    <div class="content">
        <h1>Welcome to Streamlit Dynamic Island Example</h1>
        <button onclick="expandNotch()">Expand Notch</button>
    </div>

    <script>
        function expandNotch() {
            var notch = document.getElementById("notch-container");
            notch.classList.toggle("expanded");
        }
    </script>
""", unsafe_allow_html=True)
