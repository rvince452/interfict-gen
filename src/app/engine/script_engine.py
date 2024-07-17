from typing import List
from src.app.engine import script_rules
from src.app.engine.script_blocks import ScriptBlockBase, ScriptBlocks, ScriptCommandBlock, ScriptEmptyBlock, ScriptTextBlock
from src.app.engine.script_entities import TEXT_COMMANDS, Command, ScriptCommandLine, ScriptTextLine
from src.app.utility.file_store import FileStore
from src.app.engine.script_loader import ScriptLoader


class ScriptEngine:
    def __init__(self,
                 storyStore: FileStore):
        self._storyStore = storyStore
        self._scriptLoader = ScriptLoader()


    def getScript(self) -> ScriptLoader:
        return self._scriptLoader
    
    def _process_phase1(self):
        # Phase 1 - just make blocks. Massage them later.
        currentBlock = None
        for iline, line in enumerate(self._storyStore.contents):
            line_index = 1 + iline
            istext = script_rules.is_string_text_line(line)
            isempty = script_rules.is_string_empty(line)
            isblank = script_rules.is_string_blank(line)
            if istext or isblank:
                if not isinstance(currentBlock, ScriptTextBlock):
                    currentBlock = self._scriptLoader.get_new_text_block()
                currentBlock.add_line(ScriptTextLine(line_index, line, False, False))
            elif isempty:
                if not isinstance(currentBlock, ScriptEmptyBlock):
                    currentBlock = self._scriptLoader.get_new_empty_block()
                currentBlock.add_line(line_index)
            else:
                # Command line - always add a new command block?
                commandLine = ScriptCommandLine(line_index, line, TEXT_COMMANDS)
                if not commandLine.is_valid():
                    # todo - raise an exception or write to errors
                    raise Exception("Invalid command line")
                elif commandLine.get_command() is None:
                    if not isinstance(currentBlock, ScriptTextBlock):
                        currentBlock = self._scriptLoader.get_new_text_block()
                        self._checkif_add_textline_to_block(currentBlock, commandLine)
                elif commandLine.get_command() in [Command.BLOCK, Command.GOTO, Command.GOSUB, Command.SUB]:
                    currentBlock = self._scriptLoader.get_new_command_block(commandLine)
                    self._checkif_add_textline_to_block(currentBlock, commandLine)  
                else:
                    pass 

    def _checkif_add_textline_to_block(self, block: ScriptBlockBase, commandLine: ScriptCommandLine):
        isBold = commandLine.contains_child(Command.BOLD)
        isItalic = commandLine.contains_child(Command.ITALIC)
        block.add_line(ScriptTextLine(commandLine.get_id(), 
                                      commandLine.get_remaing_text(),
                                        isBold, isItalic))

    def _process_phase2(self):
        # Phase 2 - massage the blocks
        newBlocks: List[ScriptBlockBase] = []
        lastBlock = None
        for block in self._scriptLoader.get_blocks():
            if isinstance(block, ScriptEmptyBlock):
                if block.get_line_count() <= 1:
                    pass
                else:
                    commandLine = ScriptCommandLine(block.get_startId(), '.ENDPAGE')
                    commandBlock = ScriptCommandBlock(commandLine)
                    newBlocks.append(commandBlock)
            else:
                newBlocks.append(block)

        self._scriptLoader.set_blocks(newBlocks)  
    
    def process(self):
        self._process_phase1()
        self._process_phase2()


        # Read every line with a 1 based index.
        #   RawLine index, text
        # Initialize Errors (index + error string)
        #   LineError rawindex, error
        #
        #  Initialize variables and jump targets
        #   varName, varType, varValue
        #   jumpTargetName, rawline index
        #
        # Phase 1
        #   Loop over all lines and determine type
        #       TEXT, BLANK, COMMAND
        #   Log error for invalid commands
        #   Collect variable names/types/values if any
        #   Collect jump targets
        #   Error for invalid syntax
        #   Error for invalid goto
        # Phase 2
        # Break the script into blocks:
        #   text blocks
        #   blank blocks
        #   commands
        #
        # Iteration 1
        #   Read all text and output as CS text
        #   Read all blanks and output as CS blanks 
        #       If two many blanks then output as CS end pages
    
