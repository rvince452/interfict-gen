
from src.app.cs.cs_writer_config import CSWriterConfig
from src.app.engine.script_blocks import ScriptCommandBlock, ScriptEmptyBlock, ScriptTextBlock
from src.app.engine.script_entities import Command, ScriptTextLine
from src.app.engine.script_loader import ScriptLoader


class CSEngine:
    def __init__(self,
                 csWriterConfig: CSWriterConfig,
                 scriptLoader: ScriptLoader):
        self._csWriterConfig: CSWriterConfig = csWriterConfig
        self._scriptLoader: ScriptLoader = scriptLoader

    def get_csWriterConfig(self) -> CSWriterConfig:
        return self._csWriterConfig
    
    def get_scriptLoader(self) -> ScriptLoader:
        return self._scriptLoader

    def process(self):
        # loop over all the blocks in the scriptLoader
        for block in self._scriptLoader.get_blocks():
            # if block is a text block, process it
            if isinstance(block, ScriptTextBlock):
                self._process_text_block(block) 
            elif isinstance(block, ScriptEmptyBlock):
                # Raise exception - illegal block
                raise Exception("Empty block found in phase 2")
            elif isinstance(block, ScriptCommandBlock):
                self._process_command_block(block)
            else:
                # Raise exception - unknown block type
                raise Exception("Unknown block type found in phase 2")
                

    def _process_text_block(self, textBlock: ScriptTextBlock):
        # loop over each element in textBlock and call the appropriate method on the csWriterConfig
        for line in textBlock.get_lines():
            final_text = self._csWriterConfig.format_text(line.get_text(), line.is_bold(), line.is_italic())
            self._csWriterConfig.append_text_line_to_story(final_text)


    def _process_command_block(self, commandBlock: ScriptCommandBlock):
        if commandBlock.get_command() in [Command.ENDPAGE, 
                                          Command.BLOCK, 
                                          Command.GOTO, 
                                          Command.GOSUB, 
                                          Command.SUB]:
            self._csWriterConfig.append_command_to_story(commandBlock)  
        else:
            raise Exception("Unknown command block found in phase 2")
 