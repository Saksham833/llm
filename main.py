from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import requests
import json

app = FastAPI()

@app.websocket("/ws/llm")
async def websocket_llm(websocket: WebSocket):
    await websocket.accept()
    try:
        prompt = await websocket.receive_text()

        # Send prompt to local LLM (Ollama) with streaming enabled
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "phi3", "prompt": prompt, "stream": True},
            stream=True
        )

        for line in response.iter_lines():
            if line:
                decoded = json.loads(line.decode("utf-8"))
                token = decoded.get("response", "")
                await websocket.send_text(token)

        await websocket.send_text("[[END]]")

    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        await websocket.send_text(f"[[ERROR]] {str(e)}")
