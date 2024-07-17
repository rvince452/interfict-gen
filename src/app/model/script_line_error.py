class ScriptLineError:
    def __init__(self, line_index, error_text):
        self.__error_text: str = error_text
        self.__line_index: int = line_index

    @property
    def line_index(self):
        return self.__line_index 

    @property
    def error_text(self):
        return self.__error_text


    def __str__(self):
        return f"Line {self.line_index()}: {self.error_text()}"
