from error.LexicalException import LexicalExeception
from lexical.TokenTable import TOKENTABLE
from sourceCode import SourceCode
from Token import Token

from typing import List
import re


class LexicalAnalytics:
    def __init__(self, sourceCode: SourceCode) -> None:
        self.__source_code = sourceCode

    def __line_analytics(self, source_code_line: str, line: str) -> List[Token]:
        tokens: List[Token] = []
        collunm = 0
        while collunm < len(source_code_line):
            match = None
            for token_type, pattern in TOKENTABLE:
                regex = re.compile(pattern)
                match = regex.match(source_code_line, collunm)
                if match:
                    value = match.group(0)
                    if token_type:
                        tokens.append(Token(line, collunm, token_type, value))
                    break
            if not match:
                raise LexicalExeception('invalid token', line+1, source_code_line, self.__source_code.get_file_path(), collunm)
            collunm = match.end(0)
        return tokens

    def analytics(self) -> List[List[Token]]:
        array = self.__source_code.get_source_code_lines()
        return list(map(self.__line_analytics, array, range(len(array))))



