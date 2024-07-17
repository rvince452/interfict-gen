from src.app.engine.script_loader import ScriptLoader


class TestScriptLine:
    def __init__(self) -> None:
            self.data1 = ["Hello", "World"]
            self.scriptLoader = ScriptLoader()
    def test_ScriptLoader(self):

        results = self.scriptLoader.load_script(self.data1)
        assert 2 == len(results)
