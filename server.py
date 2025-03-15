from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import json

app = FastAPI()
players = {}  # 현재 접속한 플레이어 목록

@app.websocket("/ws/{player_name}")
async def websocket_endpoint(websocket: WebSocket, player_name: str):
    await websocket.accept()

    if player_name in players:
        await websocket.send_text(json.dumps({"error": "중복된 이름입니다!"}))
        await websocket.close()
        return

    players[player_name] = {"y": 250}  # 초기 Y좌표

    try:
        while True:
            data = await websocket.receive_text()
            move = json.loads(data)
            if move.get("jump"):
                players[player_name]["y"] -= 30  # 점프
            else:
                players[player_name]["y"] += 5   # 낙하
            
            # 모든 플레이어 상태 업데이트
            await websocket.send_text(json.dumps(players))

    except WebSocketDisconnect:
        del players[player_name]

