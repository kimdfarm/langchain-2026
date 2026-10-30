from fastmcp import FastMCP

mcp = FastMCP("week9")  # 서버 이름

@mcp.tool()
def calculate_tax(income: float) -> float:
    """소득을 입력받아 세금을 계산합니다."""
    return income * 0.2