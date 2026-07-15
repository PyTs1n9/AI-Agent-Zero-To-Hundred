"""应用运行器。"""

from agent.configs.settings import get_settings
from agent.memory import ConversationMemory
from agent.prompts.system import SYSTEM_PROMPT
from agent.tools.llm import chat


def run() -> None:
    # 读取 .env：密钥、模型名等配置
    settings = get_settings()
    memory = ConversationMemory(max_turns=settings.memory_max_turns)

    print("PT Agent 已启动，输入 exit 退出，输入 /clear 清空记忆。")

    while True:
        user_message = input("\n你：").strip()

        if user_message.lower() == "exit":
            print("再见。")
            break

        if user_message.lower() == "/clear":
            memory.clear()
            print("上下文记忆已清空。")
            continue

        if not user_message:
            continue

        answer = chat(
            api_key=settings.api_key,      # DeepSeek 密钥
            base_url=settings.base_url,    # DeepSeek 接口地址
            model=settings.model,          # deepseek-v4-flash
            system_prompt=SYSTEM_PROMPT,   # 给 AI 的规则
            user_message=user_message,     # 你的问题
            history=memory.messages,       # 最近的对话上下文
        )
        memory.add_turn(user_message, answer)
        print(f"\nPT Agent：{answer}")
