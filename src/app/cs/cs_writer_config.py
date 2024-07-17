
from src.app.engine.script_blocks import ScriptCommandBlock
from src.app.engine.script_entities import Command
from src.app.utility.file_store import FileStore
from src.app.utility.file_util import write_file_store

OPTION_START_BLOCK_WITH_CONTINUE = True
OPTION_START_BLOCK_WITH_CUSTOM_PROMPT = True
CS_LINE_BREAK = '*line_break'
CS_PAGE_BREAK = '*page_break'
CS_PAGE_BREAK_FMT = CS_PAGE_BREAK + ' {}'
CS_START_BOLD = '[b]'
CS_END_BOLD   = '[/b]'
CS_START_ITALIC = '[i]'
CS_END_ITALIC   = '[/i]'
CS_LABEL_FMT = '*label {}'
CS_SUB_FMT = '*label {}'
CS_GOTO_FMT = '*goto {}'
CS_GOSUB_FMT = '*gosub {}'

class CSWriterConfig:
    def __init__(self, 
                 out_folder_path: str,
                 out_story_store: FileStore,
                 template_stats: FileStore,
                template_startup: FileStore ):
        self._out_folder_path: str = out_folder_path
        self._out_story_store: FileStore = out_story_store
        self._template_stats: FileStore = template_stats
        self._template_startup: FileStore = template_startup

    def append_command_to_story(self, commandBlock: ScriptCommandBlock):
        if Command.ENDPAGE == commandBlock.get_command():
            self.append_text_line_to_story(CS_PAGE_BREAK)
        elif Command.GOTO == commandBlock.get_command():
            labelText = commandBlock.get_lines()[0].get_text()
            self.append_text_line_to_story(str.format(CS_GOTO_FMT, labelText))
        elif Command.GOSUB == commandBlock.get_command():
            labelText = commandBlock.get_lines()[0].get_text()
            self.append_text_line_to_story(str.format(CS_GOSUB_FMT, labelText))
        elif Command.SUB == commandBlock.get_command():
            labelText = commandBlock.get_lines()[0].get_text()
            self.append_text_line_to_story(str.format(CS_SUB_FMT, labelText))
        elif Command.BLOCK == commandBlock.get_command():
            labelText = commandBlock.get_lines()[0].get_text()
            self.append_text_line_to_story(str.format(CS_LABEL_FMT, labelText))
            if OPTION_START_BLOCK_WITH_CONTINUE:
                if OPTION_START_BLOCK_WITH_CUSTOM_PROMPT:
                    self.append_text_line_to_story(str.format(CS_PAGE_BREAK_FMT, labelText))
                else:
                    self.append_text_line_to_story(CS_PAGE_BREAK)
        else:
            pass
    
    def append_text_line_to_story(self, line: str):
        self.append_text_to_story(line)
        self.append_text_to_story(CS_LINE_BREAK)

    def append_text_to_story(self, line: str):
        self._out_story_store.addLine(line)

    def format_text(self, text:str, doBold:bool, doItalics:bool)-> str:
        retvalue = text
        if doBold:
            retvalue = CS_START_BOLD + retvalue + CS_END_BOLD
        if doItalics:
            retvalue = CS_START_ITALIC + retvalue + CS_END_ITALIC

        return retvalue 

    def write_all(self):
        # write all of the stores to disk
        write_file_store(self._out_story_store)
        write_file_store(self._template_stats)
        write_file_store(self._template_startup)

