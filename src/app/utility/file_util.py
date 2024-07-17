from typing import List
from src.app.utility.file_store import FileStore
import os

# On read,  we remove the \n
# On write, we add the \n

def read_strings_from_file(file_path: str) -> List[str]:    
    with open(file_path, 'rt') as file:
        return [line.rstrip('\n') for line in file]
    
def write_strings_to_file(file_path: str, strings: List[str]) -> None:
    with open(file_path, 'wt') as file:
        file.writelines([line + '\n' for line in strings])


def move_file_store(file_store: FileStore, new_folder: str) -> FileStore:
    folder, filename = os.path.split(file_store.filePath)
    file_store.filePath = os.path.join(new_folder, filename)
    return file_store
    
def read_file_store(file_path: str) -> FileStore:
    retvalue = FileStore(file_path)
    retvalue.setContents(
        read_strings_from_file(file_path)
    )
    return retvalue

def write_file_store(file_store: FileStore) -> None:
    write_strings_to_file(file_store.filePath, file_store.contents)
                          
