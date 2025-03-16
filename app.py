import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

st.title("📈 함수 그래프 변환기")

# 위쪽 그래프 출력 영역
with st.container():
    st.subheader("📊 그래프 출력")
    
    # X축 범위 선택 (입력창과 분리, 그래프 위에 배치)
    x_min, x_max = st.slider("X축 범위 설정", -10, 10, (-5, 5))
    
    # 그래프 그리기
    x = np.linspace(x_min, x_max, 400)
    fig, ax = plt.subplots()

    for i, func in enumerate(st.session_state.get("functions", ["x**2", "sin(x)", "cos(x)"])):
        try:
            expr = sp.sympify(func.strip())  # 수식 변환
            f_lambdified = sp.lambdify('x', expr, 'numpy')  # numpy 함수 변환
            y = f_lambdified(x)

            # 색상 적용 (HEX 코드, 유효하지 않으면 기본 'black')
            color = st.session_state.get("colors", ["#FF5733", "#33FF57", "#3357FF"])[i % 3].strip()
            if not color.startswith("#") or len(color) not in [4, 7]:  # 3자리 또는 6자리 HEX 체크
                color = "#000000"

            ax.plot(x, y, label=func.strip(), color=color)
        except Exception as e:
            st.warning(f"⚠️ '{func}' 수식을 해석할 수 없습니다: {e}")

    ax.legend()
    st.pyplot(fig)

st.markdown("---")  # 그래프와 입력창 구분선

# 아래쪽 입력 영역
with st.container():
    st.subheader("📌 수식 입력")
    
    # 수식 입력
    functions = st.text_area("수식을 입력하세요 (쉼표로 구분)", "x**2, sin(x), cos(x)").split(',')
    colors = st.text_area("HEX 색상 코드 입력 (#RRGGBB, 쉼표로 구분)", "#FF5733, #33FF57, #3357FF").split(',')

    # 상태 업데이트 (다시 실행될 때 데이터 유지)
    st.session_state["functions"] = functions
    st.session_state["colors"] = colors