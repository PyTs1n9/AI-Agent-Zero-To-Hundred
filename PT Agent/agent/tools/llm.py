"""DeepSeek 调用工具。"""

from collections.abc import Sequence
from openai import OpenAI

from agent.memory.conversation import ChatMessage


def chat(
    api_key: str,
    base_url: str,
    model: str,
    system_prompt: str,
    user_message: str,
    history: Sequence[ChatMessage] = (),
) -> str:
    """将用户消息发送给 DeepSeek，并返回回答。"""
    client = OpenAI(
        api_key=api_key,
        base_url=base_url,
    )

    response = client.chat.completions.create(
        model=model,
        messages=(
            [{"role": "system", "content": system_prompt}]
            + list(history)
            + [{"role": "user", "content": user_message}]
        ),
    )

    return response.choices[0].message.content or ""
