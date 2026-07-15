"""In-memory conversation history."""

from dataclasses import dataclass, field
from typing import Literal, TypedDict


# 定义一种"字典结构类型"，名称是ChatMessage
# Literal 用来限制变量只能取指定的几个值
# 限制了 role 和 content 的消息结构
class ChatMessage(TypedDict):
	role: Literal["user", "assistant"]
	content: str


@dataclass
class ConversationMemory:
	"""保留最近的完整对话轮次"""

	max_turns: int = 10
	_messages: list[ChatMessage] = field(default_factory=list, init=False)

	def __post_init__(self) -> None:
		if self.max_turns < 1:
			raise ValueError("max_turns 必须最小是 1")

	@property
	def messages(self) -> list[ChatMessage]:
		"""返回一个副本，以便调用者无法修改存储的历史记录"""
		return [message.copy() for message in self._messages]

	def add_turn(self, user_message: str, assistant_message: str) -> None:
		"""Store one complete turn and discard the oldest excess turns."""
		self._messages.extend(
			[
				{"role": "user", "content": user_message},
				{"role": "assistant", "content": assistant_message},
			]
		)
		self._messages = self._messages[-self.max_turns * 2:]

	def clear(self) -> None:
		"""Forget all conversation history."""
		self._messages.clear()
