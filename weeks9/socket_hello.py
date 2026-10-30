
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
load_dotenv()
import re
BOT_TOKEN = os.environ.get("SLACK_BOT_TOKEN", "")     # xoxb- 보내는 선
APP_TOKEN = os.environ.get("SLACK_APP_TOKEN", "")     # xapp- 받는 선  ★

app = App(token=BOT_TOKEN)

@app.event("app_mention")                              # ★ 누가 @멘션하면 이 함수가 불린다
def on_mention(event, say):
    text = re.sub(r"<@[A-Z0-9]+>\s*", "", event["text"]).strip()   # "<@U07..> 안녕" → "안녕"
    say(
        text=f"pong 🏓  (받은 말: {text or '(없음)'})",
        thread_ts=event.get("thread_ts") or event["ts"],   # 원글의 스레드에 (5주차 thread_ts)
    )

SocketModeHandler(app, APP_TOKEN).start()             # ★ 연결을 열고 여기서 계속 기다린다