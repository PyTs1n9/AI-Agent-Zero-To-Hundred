"""应用运行器。"""

from dotenv import load_dotenv


def run() -> None:
    """加载环境配置并启动 Agent。"""
    load_dotenv()
    print("Agent 项目已启动，等待接入任务逻辑。")
