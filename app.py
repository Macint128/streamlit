import streamlit as st
import asyncio
import websockets
import json

server_url = "ws://localhost:8000/ws/"

st.title("멀티플레이어 플래피버드")

player_name = st.text_input("닉네임을 입력하세요:", value="Player1")
if "connected" not in st.session_state:
    st.session_state["connected"] = False

if st.button("게임 시작") and not st.session_state["connected"]:
    async def connect():
        async with websockets.connect(server_url + player_name) as ws:
            st.session_state["connected"] = True

            while True:
                data = json.loads(await ws.recv())

                if "error" in data:
                    st.error(data["error"])
                    st.session_state["connected"] = False
                    break

                st.write(f"플레이어 상태: {data}")

    asyncio.run(connect())
