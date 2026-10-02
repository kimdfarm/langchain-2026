from langchain_core.runnables import RunnableLambda
from send_slack_message import send # 실습 5의 함수를 그대로 재사용
# 3교시에서 만든 분해 체인 (least_to_most.py 의 chain)

def to_slack(answer: str) -> str:
    send(f"*분석 결과가 나왔습니다*\n\n{answer}")
    return answer # 뒤에 더 이을 수 있게 그대로 돌려준다 ★
notified = RunnableLambda(to_slack) # ← 체인 끝에 한 칸 추가
notified.invoke({"problem": "리뷰 50건에서 반복 불만과 개선 우선순위를 정리하라"})