import os
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
load_dotenv() # .env 를 환경변수로 읽어들인다
token = os.environ.get("SLACK_BOT_TOKEN")
channel = os.environ.get("SLACK_CHANNEL", "#수업-출력물")
if not token: # ← 설정 오류를 여기서 먼저 잡는다 ★
    raise SystemExit("SLACK_BOT_TOKEN 이 없습니다. .env 를 확인하세요.")
client = WebClient(token=token) # 토큰을 쥔 API 클라이언트

def send(text: str) -> str:
    try:
        res = client.chat_postMessage( # ★ 오늘의 핵심 한 줄
        channel=channel,
        text=text,
        )
        print(f"전송 성공 → {channel} (ts={res['ts']})")
        return res["ts"]
    except SlackApiError as e:
        print(f"전송 실패: {e.response['error']}") # not_in_channel 등
        raise # 조용히 넘기지 않는다
if __name__ == "__main__":
    send("안녕하세요! 5주차 실습에서 보내는 첫 메시지입니다. 🎉")
