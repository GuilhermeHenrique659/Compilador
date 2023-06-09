from typing import List


class SourceCodeExeception(Exception):
    def __init__(self, message: str, lineNumber: int, line: str | List[str], path: str, collunm: int) -> None:
        self.message = message
        self.lineError = lineNumber
        self.line = line
        self.path = path
        self.collunm = collunm