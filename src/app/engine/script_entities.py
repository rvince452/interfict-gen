from enum import Enum
from typing import List
from typing import Set

from src.app.engine import script_rules



class Command(Enum):
    NONE = ''
    BOLD = 'BOLD'
    ITALIC = 'ITALIC'
    GOTO = 'GOTO'
    GOSUB = 'GOSUB'
    BLOCK = 'BLOCK'
    SUB = 'SUB'
    SET = 'SET'
    CHOICE = 'CHOICE'
    ENDCHOICE = 'ENDCHOICE'
    ENDPAGE = 'ENDPAGE'

ALL_COMMAND_VALUES = {command.value for command in Command}
TEXT_COMMANDS = {Command.BOLD,Command.ITALIC}



class ScriptBaseLine:
    def __init__(self, id: int, text: str):
        self._id = id
        self._text = text

    def get_id(self) -> int:
        return self._id

    def get_text(self) -> str:
        return self._text

class ScriptVariableLine(ScriptBaseLine):
    def __init__(self, id: int, text: str):
        super().__init__(id, text)
        self._value = None
        self._valType = None

class ScriptEmptyLine(ScriptBaseLine):
    pass        

class ScriptTextLine(ScriptBaseLine):
    def __init__(self, id: int, text: str, isBold: bool, isItalic: bool):
        super().__init__(id, text)
        self._isBold = isBold
        self._isItalic = isItalic
            
    def is_bold(self) -> bool:
        return self._isBold

    def is_italic(self) -> bool:
        return self._isItalic

class ScriptTargetLine(ScriptBaseLine):
    pass

class ScriptCommandLine(ScriptBaseLine):
    def __init__(self, id: int, text: str, childCommandList:List[Command] = None):
        super().__init__(id, text)
        self._isValid = False
        self._commandText = None
        self._remainingText = text
        self._allCommands : Set[Command] = set()
        self._childCommands : Set[Command] = set()
        self._knownChildCommands : List[Command] = childCommandList if childCommandList else []
        self._command: Command = None 
        self._validate()

    def is_valid(self) -> bool:
        return self._isValid
    def get_remaing_text(self) -> str:
        return self._remainingText
    def get_child_commands(self) -> Set[Command]:
        return self._childCommands
    def get_command(self) -> Command:
        return self._command
    def get_possible_child_commands(self) -> List[Command]:
        return self._knownChildCommands
    
    def contains_child(self, command:Command) -> bool:
        return command in self._allCommands
    def contains_only_commands(self, commands:Set[Command]) -> bool:
        # return true if self._commands contains only those in commands
        retvalue = self._allCommands.issubset(commands)
        return retvalue

    # Place commands in child list if on the child list else
    def _fill_commands_from_command_text(self, text: str):
        commandStrings = script_rules.get_string_script_command_text(text).split('.')
        for commandString in commandStrings:
            if commandString:
                if commandString in ALL_COMMAND_VALUES:
                    command: Command = Command(commandString)
                    self._allCommands.add(command)
                    if command in self._knownChildCommands:
                        self._childCommands.add(command)
                    else:
                        if (self._command is None) or (command == self._command):
                            self._command = command
                        else:
                            # todo - raise an exception or write to errors
                            raise Exception("Multiple commands in command line")
                else:
                    # todo - raise an exception or write to errors
                    pass

    def _validate(self):
        self._isValid = False
        self._commandText = script_rules.get_string_script_command_text(self._text)
        if self._commandText:
            self._fill_commands_from_command_text(self._commandText)
            if self._command or self._childCommands:
                self._isValid = True
                self._remainingText = script_rules.get_string_script_remaining_text(self._text, self._commandText)
    
    
