from typing import List
from error.SourceCodeExeception import SourceCodeExeception

class LexicalExeception(SourceCodeExeception):
    def __init__(self,lineNumber: int, line: str | List[str], path: str, collum: int) -> None:
        super().__init__('invalid token', lineNumber + 1, line, path, collum)