class ScriptLine:
    def __init__(self, line_index, line_text):
        self.__line_text: str = line_text
        self.__line_index: int = line_index

    @property
    def line_number(self):
        return self.__line_index + 1

    @property
    def line_text(self):
        return self.__line_text


    def __str__(self):
        return f"Line {self.line_number()}: {self.line_text()}"
