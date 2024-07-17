import pytest
from src.app.engine import script_rules
from src.app.engine.script_entities import Command, ScriptCommandLine

class TestScriptRules:

    def test_is_string_empty(self):
        assert script_rules.is_string_empty("") == True
        assert script_rules.is_string_empty("  ") == False
        assert script_rules.is_string_empty("Hello") == False

    def test_is_string_blank(self):
        assert script_rules.is_string_blank("") == False
        assert script_rules.is_string_blank(None) == False
        assert script_rules.is_string_blank("   ") == True
        assert script_rules.is_string_blank("   \t") == True
        assert script_rules.is_string_blank("Hello") == False

    def test_is_string_text(self):
        assert script_rules.is_string_text_line("Hello") == True
        assert script_rules.is_string_text_line(" .Hello") == True
        assert script_rules.is_string_text_line("He.llo") == True
        assert script_rules.is_string_text_line(".text ") == True
        assert script_rules.is_string_text_line(" '") == True

        assert script_rules.is_string_text_line("  ") == False
        assert script_rules.is_string_text_line("") == False
        assert script_rules.is_string_text_line("\t") == False
        assert script_rules.is_string_text_line(".COMMAND") == False


    def test_is_string_command(self):
        assert script_rules.get_string_script_command_text("hello") == None
        assert script_rules.get_string_script_command_text("") == None
        assert script_rules.get_string_script_command_text("Hello") == None
        assert script_rules.get_string_script_command_text(" .AB") == None
        assert script_rules.get_string_script_command_text(". dkjkd") == None

        assert script_rules.get_string_script_command_text(".AB") == ".AB"
        assert script_rules.get_string_script_command_text(".AB.BOLD.ITALIC") == ".AB.BOLD.ITALIC"
        assert script_rules.get_string_script_command_text(".AB.CD ") == ".AB.CD"
        assert script_rules.get_string_script_command_text(".AB.CD addfdfd") == ".AB.CD"

        sCommand = ".BOLD.ITALIC"
        sExtraText = "ThisIsMyLine"
        sFullCommandLine = sCommand + " " + sExtraText
        # use pytest to assert that the next line will throw an exception
        with pytest.raises(Exception):
            command_entity = ScriptCommandLine(1, sFullCommandLine )
        # now we give the children and it should be fine
        command_entity = ScriptCommandLine(1, sFullCommandLine, [Command.BOLD,Command.ITALIC] )

        commands = command_entity.get_child_commands()
        assert len(commands) == 2
        assert Command.ITALIC in commands
        assert Command.BOLD in commands 
        assert Command.NONE not in commands
        assert command_entity.contains_child(Command.BOLD) == True
        assert command_entity.contains_child(Command.ITALIC) == True
        assert command_entity.contains_child(Command.NONE) == False

        assert command_entity.get_command() is None 


        assert command_entity.contains_only_commands([Command.GOSUB]) == False
        assert command_entity.contains_only_commands([Command.BOLD, Command.ITALIC]) == True
        assert command_entity.contains_only_commands([Command.BOLD]) == False

        sCommand = ".BOLD.ITALIC.BLOCK"
        sExtraText = "ThisIsMyLine"
        sFullCommandLine = sCommand + " " + sExtraText
        # use pytest to assert that the next line will throw an exception
        with pytest.raises(Exception):
            command_entity = ScriptCommandLine(1, sFullCommandLine )
        # now we give the children and it should be fine
        command_entity = ScriptCommandLine(1, sFullCommandLine, [Command.BOLD,Command.ITALIC] )

        commands = command_entity.get_child_commands()
        assert len(commands) == 2
        assert Command.ITALIC in commands
        assert Command.BOLD in commands 
        assert command_entity.get_command() == Command.BLOCK





