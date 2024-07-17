from typing import List
from enum import Enum




class VarTypes(Enum):
    STRING = 'string'
    BOOL = 'bool'

class RenderLine:
    def __init__(self, text: str, isBold: bool = None, isItalic: bool = None,  isEOL: bool = None):
        self.isBold = isBold
        self.isItalic = isItalic
        self.text = text
        self.isEOL = isEOL

class RenderBlock:
    def __init__(self, indentLevel: int, lines: List[RenderLine]):
        self.indentLevel = indentLevel
        self.lines = lines

class RenderVariable:
    def __init__(self, name: str, vartype: VarTypes, value = None):
        self.name = name
        self.vartype = vartype
        self.value = value

        






