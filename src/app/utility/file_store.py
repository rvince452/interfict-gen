from typing import List
class FileStore:
    def __init__(self, filePath: str):
        self.filePath = filePath
        self.contents:List[str] = []

    def addLine(self, line:str):
        self.contents.append(line)  
    

    def setContents(self, contents:List[str]):
        self.contents = contents

    def __str__(self):
        return f"FileStore(filePath='{self.filePath}', contents={self.contents})"
