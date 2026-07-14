"""应用运行器。"""

from dotenv import load_dotenv
from agent.configs.settings import get_settings
from agent.prompts.system import SYSTEM_PROMPT
from agent.tools.llm import chat


def run() -> None:
    # 读取 .env：密钥、模型名等配置
    settings = get_settings()

    print("PT Agent 已启动，输入 exit 退出。")

    while True:
        user_message = input("\n你：").strip()

        if user_message.lower() == "exit":
            print("再见。")
            break

        if not user_message:
            continue

        answer = chat(
            api_key=settings.api_key,      # DeepSeek 密钥
            model=settings.model,          # deepseek-v4-flash
            system_prompt=SYSTEM_PROMPT,   # 给 AI 的规则
            user_message=user_message,     # 你的问题
        )
        print(f"\nPT Agent：{answer}")