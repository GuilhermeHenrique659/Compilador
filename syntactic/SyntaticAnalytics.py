from lark import Lark
from lark.exceptions import ParseError
from typing import List
from Analytics import AbstractAnalytics
from Token import Token
from error.SyntaticExeception import SyntaticExeception
from helpers.getTokenValue import get_token_value
from sourceCode import SourceCode

class SyntaticAnalytics(AbstractAnalytics):
    __tokens: List[Token]

    def __init__(self, source_code: SourceCode) -> None:
        self.__source_code = source_code
        self.__tokens = []

    def __get_token_list(self):
        list(map(lambda token: self.__tokens.extend(token), self.__source_code.source_code_tokenize))

    def get_grammar(self) -> str:
        return open('./grammar.txt').read()

    def get_error_token(self, column) -> Token:
        tokens_position = list(map(lambda token: token.pos, self.__tokens))
        tokens_position.append(column)
        tokens_position.sort()
        token = next(filter(lambda token: token.pos == tokens_position[tokens_position.index(column) - 1], self.__tokens))
        return token


    def analytics(self):
        self.__get_token_list()
        parser = Lark(self.get_grammar(), parser='lalr', lexer='contextual')
        code = ''.join(list(map(lambda token: token.get_token(), self.__tokens)))
        try:
            tree = parser.parse(code)
            print(tree.pretty())
            self.__source_code.set_source_code_tree(tree)
        except ParseError as e:
            token = self.get_error_token(e.column)
            expected = get_token_value(list(e.expected))
            raise SyntaticExeception(token.line, f'\n after: {token.lex} expected {expected}', self.__source_code.get_file_path(), token.collunm)