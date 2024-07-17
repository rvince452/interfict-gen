from typing import List

from src.app.engine.script_entities import Command, ScriptBaseLine, ScriptCommandLine, ScriptTextLine


class ScriptBlockBase:
    pass

class ScriptCommandBlock(ScriptBlockBase):
    def __init__(self, command: Command):
        self.__command: Command = command
        self.__commands: List[ScriptCommandLine] = []

    def add(self, commandLine: ScriptCommandLine):
        self.__commands.append(commandLine)

    def get_command_type(self) -> Command:
        return self.__command

class ScriptEmptyBlock(ScriptBlockBase):
    def __init__(self):
        self.__lineCount: int = 0
        self._startId: int = None
        self._endId: int = None 
    
    def get_line_count(self) -> int:
        return self.__lineCount
    
    def get_startId(self) -> int:
        return self._startId

    def get_endId(self) -> int:
        return self._endId


    def add_line(self, iline: int):
        self.__lineCount += 1
        self._endId = iline 
        if self._startId is None:
            self._startId = iline


        
class ScriptTextBlock(ScriptBlockBase):
    def __init__(self):
        self.__lines: List[ScriptTextLine] = []

    def get_lines(self) -> List[ScriptTextLine]:
        return self.__lines

    def add_line(self, line: ScriptTextLine):
        self.__lines.append(line)
    pass

class ScriptCommandBlock(ScriptBlockBase):
    def __init__(self, commandLine: ScriptCommandLine):
        self._command:Command = commandLine.get_command()
        self._scriptLines: List[ScriptBaseLine] = []

    def get_command(self) -> Command:
        return self._command
    
    def add_line(self, line: ScriptBaseLine):
        self._scriptLines.append(line)

    def get_lines(self) -> List[ScriptBaseLine]:
        return self._scriptLines


class ScriptBlocks:
    def __init__(self):
        self.__blocks: List[ScriptBlockBase] = []

    def add_block(self, block: ScriptBlockBase):
        self.__blocks.append(block)

    def get_blocks(self) -> List[ScriptBlockBase]:
        return self.__blocks

