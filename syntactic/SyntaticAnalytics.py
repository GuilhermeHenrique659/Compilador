from lark import Lark
from lark.exceptions import ParseError
from typing import List
from Token import Token
from error.SyntaticExeception import SyntaticExeception
from sourceCode import SourceCode

class SyntaticAnalytics:
    __tokens: List[Token]

    def __init__(self, sourceCode: SourceCode) -> None:
        self.__source_code = sourceCode
        self.__tokens = []

    def __get_token_list(self):
        for token in self.__source_code.source_code_tokenize:
            self.__tokens.extend(token)

    def get_grammar(self) -> str:
        path = './grammar.txt'
        return open(path).read()

    def get_error_token(self, column) -> Token:
            tokens_position = [token.pos for token in self.__tokens]
            tokens_position.append(column)
            tokens_position.sort()
            token = next(filter(lambda x: x.pos == tokens_position[tokens_position.index(column) - 1], self.__tokens))
            return token


    def analytics(self):
        self.__get_token_list()
        parser = Lark(self.get_grammar(), parser='lalr', lexer='contextual')
        code = ''.join(token.get_token() for token in self.__tokens)
        try:
            tree = parser.parse(code)
            print(tree.pretty())
            return tree
        except ParseError as e:
            token = self.get_error_token(e.column)
            source_code_raw = self.__source_code.get_source_code_lines()
            line_error =  source_code_raw[token.line]
            raise SyntaticExeception(token.line, f'\n {line_error} expeted of {e.expected}', self.__source_code.get_file_path(), token.collunm)