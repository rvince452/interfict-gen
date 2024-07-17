from typing import List
from src.app.engine.script_blocks import ScriptBlocks, ScriptCommandBlock, ScriptTextBlock, ScriptEmptyBlock, ScriptBlockBase
from src.app.engine.script_entities import Command

from src.app.model.script_line import ScriptLine


class ScriptLoader:
    def __init__(self):
        self._scriptBlocks: ScriptBlocks = ScriptBlocks()

    def get_new_command_block(self, command:Command) -> ScriptCommandBlock:
        newblock  = ScriptCommandBlock(command)
        self._scriptBlocks.add_block(newblock)
        return newblock

    def get_new_text_block(self) -> ScriptTextBlock:
        newblock = ScriptTextBlock()
        self._scriptBlocks.add_block(newblock)
        return newblock
    
    def get_new_empty_block(self) -> ScriptEmptyBlock:
        newblock = ScriptEmptyBlock()
        self._scriptBlocks.add_block(newblock)
        return newblock

    def get_blocks(self) -> List[ScriptBlockBase]:
        # Return all _scriptBlocks children that are ScriptTextBlocks
        return [block for block in self._scriptBlocks.get_blocks() ]
    
    def set_blocks(self, blocks: List[ScriptBlockBase]):
        self._scriptBlocks = ScriptBlocks()
        for block in blocks:
            self._scriptBlocks.add_block(block)



