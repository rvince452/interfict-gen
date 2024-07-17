import re
from typing import List
import re



def is_string_empty(string):
    if len(string) == 0:
        return True
    else:
        return False

def is_string_blank(string):
    if (string) and (string.strip() == ''):
        return True
    else:
        return False
    

def get_string_script_command_text(text):
    pattern = r'^(\.[A-Z]+)+'
    match = re.match(pattern, text)
    if match:
        return match.group()
    else:
        return None
    
def get_string_script_remaining_text(text, commandText):
    return text[len(commandText):].lstrip()

    



def is_string_text_line(text):
    return not is_string_empty(text) and not is_string_blank(text) and not get_string_script_command_text(text)


def parse_sentence(sentence):
    pattern = r'(\w+)(?:=(\w+))?\s?(\w+)?'
    match = re.match(pattern, sentence)
    if match:
        value1 = match.group(1)
        value2 = match.group(2)
        value3 = match.group(3)
        return value1, value2, value3
    else:
        return None
