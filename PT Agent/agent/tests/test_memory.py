import pytest

from agent.memory import ConversationMemory


def test_memory_keeps_only_recent_complete_turns():
    memory = ConversationMemory(max_turns=2)

    memory.add_turn("问题 1", "回答 1")
    memory.add_turn("问题 2", "回答 2")
    memory.add_turn("问题 3", "回答 3")

    assert memory.messages == [
        {"role": "user", "content": "问题 2"},
        {"role": "assistant", "content": "回答 2"},
        {"role": "user", "content": "问题 3"},
        {"role": "assistant", "content": "回答 3"},
    ]


def test_memory_can_be_cleared():
    memory = ConversationMemory()
    memory.add_turn("问题", "回答")

    memory.clear()

    assert memory.messages == []


def test_memory_rejects_invalid_max_turns():
    with pytest.raises(ValueError):
        ConversationMemory(max_turns=0)
