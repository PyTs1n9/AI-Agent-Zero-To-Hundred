"""应用配置。"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
	api_key: str
	model: str
	base_url: str
	memory_max_turns: int


def get_settings() -> Settings:
	load_dotenv()

	api_key = os.getenv("OPENAI_API_KEY")
	model = os.getenv("OPENAI_MODEL")
	base_url = os.getenv("OPENAI_BASE_URL", "https://api.deepseek.com")
	memory_max_turns = int(os.getenv("MEMORY_MAX_TURNS", "10"))

	if not api_key:
		raise ValueError("请在 .env 中设置 OPENAI_API_KEY")
	if not model:
		raise ValueError("请在 .env 中设置 OPENAI_MODEL")
	if memory_max_turns < 1:
		raise ValueError("MEMORY_MAX_TURNS 必须大于 0")

	return Settings(
		api_key=api_key,
		model=model,
		base_url=base_url,
		memory_max_turns=memory_max_turns,
	)
