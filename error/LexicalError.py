from typing import List
from error.SourceCodeExeception import SourceCodeExeception

class LexicalError(SourceCodeExeception):
    def __init__(self, message: str, lineNumber: int, line: str | List[str], path: str) -> None:
        super().__init__(message, lineNumber, line, path)