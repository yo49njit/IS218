import builtins
import App
from plugins.add import Add

def test_app_command_execution(monkeypatch, capsys):
    # Simulate user input: 'add', '2', '3', then 'exit'
    inputs = iter(['add', '2', '3', 'exit'])
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))

    app = App()
    app.command_handler.register_command("exit", lambda: exit())  # Mock exit to prevent hanging
    app.start()

    captured = capsys.readouterr()
    assert "2.0 + 3.0 = 5.0" in captured.out
