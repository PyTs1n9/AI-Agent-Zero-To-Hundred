"""应用配置。"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass(frozen=True)
class Settings:
	api_key: str
	model: str


def get_settings() -> Settings:
	load_dotenv()

	api_key = os.getenv("OPENAI_API_KEY")
	model = os.getenv("OPENAI_MODEL")

	if not api_key:
		raise ValueError("请在 .env 中设置 OPENAI_API_KEY")
	if not model:
		raise ValueError("请在 .env 中设置 OPENAI_MODEL")

	return Settings(
		api_key=api_key,
		model=model,
	)
