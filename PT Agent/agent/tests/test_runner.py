from agent.core.runner import run
from unittest.mock import patch


@patch("agent.core.runner.chat", return_value="你好")
@patch("builtins.input", side_effect=["你好", "exit"])
@patch("agent.core.runner.get_settings")

def test_run_can_chat(mock_settings, mock_input, mock_chat, capsys):
    run()

    output = capsys.readouterr().out
    assert "Agent：你好" in output