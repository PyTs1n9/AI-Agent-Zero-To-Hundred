from agent.core.runner import run


def test_run_starts(capsys) -> None:
    run()
    assert "Agent 项目已启动" in capsys.readouterr().out
