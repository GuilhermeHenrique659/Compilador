from Analytics import AbstractAnalytics
from error.LexicalException import LexicalExeception
from lexical.TokenTable import TOKENTABLE
from sourceCode import SourceCode
from Token import Token

from typing import List
import re


class LexicalAnalytics(AbstractAnalytics):
    def __init__(self, source_code: SourceCode) -> None:
        self.__source_code = source_code

    def __line_analytics(self, source_code_line: str, line_index: str) -> List[Token]:
        tokens: List[Token] = []
        collunm = 0
        while collunm < len(source_code_line):
            match = None
            for token_type, pattern in TOKENTABLE:
                match = re.compile(pattern).match(source_code_line, collunm)
                if match:
                    value = match.group()
                    if token_type:
                        tokens.append(Token(line_index, collunm, token_type, value))
                    break
            if not match:
                raise LexicalExeception(line_index, source_code_line, self.__source_code.get_file_path(), collunm)
            collunm = match.end()
        return tokens

    def analytics(self) -> List[List[Token]]:
        lines = self.__source_code.get_source_code_lines()
        tokens = list(map(self.__line_analytics, lines, range(len(lines))))
        self.__source_code.set_source_code_tokenize(tokens)




