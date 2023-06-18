
import os
import re
from lark import Tree
from typing import List
from error.FileExeception import FileExeception
from Token import Token
from helpers.InjectTokenPosition import inject_token_position

pathToSearchRegex = re.compile('[a-zA-Z0-9:_.\\\/]*[a-zA-Z][a-zA-Z0-9_.]*.sl')

class SourceCode:
    __filepath: str
    __source_code_raw: str
    __source_code_tokenize: List[List[Token]]
    __source_code_tree: Tree

    def __init__(self, source_code_file: str) -> None:
        self.__filepath = source_code_file
        self.__source_code_raw = None
        self.__source_code_tokenize = None
        self.__source_code_tree = None

    @property
    def source_code_tokenize(self):
        return self.__source_code_tokenize

    @property
    def source_code_tree(self):
        return self.__source_code_tree

    def get_file_path(self):
        return self.__filepath
    
    def set_source_code_tree(self, tree: Tree):
        self.__source_code_tree = tree
    
    def set_source_code_tokenize(self, tokens: List[List[Token]]):
        inject_token_position(tokens)
        self.__source_code_tokenize = tokens

    def __validate_source_code(self):
        if not(pathToSearchRegex.match(self.__filepath)) or not(os.path.exists(self.__filepath)):
            raise FileExeception(f'file {self.__filepath} not found')

    def get_source_code_lines(self):
        if not(self.__source_code_raw):
            self.__validate_source_code()
            self.__source_code_raw = open(self.__filepath).readlines()
        return self.__source_code_raw






