from src.app.model.script_line import ScriptLine


class TestScriptLine:
    def test_ScriptLine(self):
        s1 = ScriptLine("Hello", 2)
        assert "Hello" == s1.line_text
        assert 2 == s1.line_index

