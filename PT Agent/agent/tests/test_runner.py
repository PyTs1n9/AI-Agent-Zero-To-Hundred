from agent.core.runner import run
from types import SimpleNamespace
from unittest.mock import patch


@patch("agent.core.runner.chat", return_value="你好")
@patch("builtins.input", side_effect=["你好", "exit"])
@patch("agent.core.runner.get_settings")
def test_run_can_chat(mock_settings, mock_input, mock_chat, capsys):
    mock_settings.return_value = SimpleNamespace(
        api_key="test-key",
        base_url="https://example.com",
        model="test-model",
        memory_max_turns=10,
    )
    run()

    output = capsys.readouterr().out
    assert "Agent：你好" in output


@patch("agent.core.runner.chat", side_effect=["第一次回答", "第二次回答"])
@patch("builtins.input", side_effect=["第一个问题", "第二个问题", "exit"])
@patch("agent.core.runner.get_settings")
def test_run_passes_previous_turn_to_chat(
    mock_settings, mock_input, mock_chat, capsys
):
    mock_settings.return_value = SimpleNamespace(
        api_key="test-key",
        base_url="https://example.com",
        model="test-model",
        memory_max_turns=10,
    )

    run()

    second_call = mock_chat.call_args_list[1].kwargs
    assert second_call["history"] == [
        {"role": "user", "content": "第一个问题"},
        {"role": "assistant", "content": "第一次回答"},
    ]


@patch("agent.core.runner.chat", side_effect=["第一次回答", "第二次回答"])
@patch(
    "builtins.input",
    side_effect=["第一个问题", "/clear", "第二个问题", "exit"],
)
@patch("agent.core.runner.get_settings")
def test_clear_command_removes_history(mock_settings, mock_input, mock_chat, capsys):
    mock_settings.return_value = SimpleNamespace(
        api_key="test-key",
        base_url="https://example.com",
        model="test-model",
        memory_max_turns=10,
    )

    run()

    assert mock_chat.call_args_list[1].kwargs["history"] == []
    assert "上下文记忆已清空" in capsys.readouterr().out
