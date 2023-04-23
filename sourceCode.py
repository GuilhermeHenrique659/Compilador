
import os
import re
from typing import List
from error.FileExeception import FileExeception
from Token import Token

pathToSearchRegex = re.compile('[a-zA-Z0-9:_.\\\/]*[a-zA-Z][a-zA-Z0-9_.]*.sl')

class SourceCode:
    __filepath: str
    __source_code_raw: str
    source_code_tokenize: List[List[Token]]

    def __init__(self, soruceCodeFile: str) -> None:
        self.__filepath = soruceCodeFile
        self.__source_code_raw = None
        self.source_code_tokenize = None

    def get_file_path(self):
        return self.__filepath

    def __validate_source_code(self):
        if not(pathToSearchRegex.match(self.__filepath)) or not(os.path.exists(self.__filepath)):
            raise FileExeception(f'file {self.__filepath} not found')

    def get_source_code_lines(self):
        if not(self.__source_code_raw):
            self.__validate_source_code()
            self.__source_code_raw = open(self.__filepath)
        return self.__source_code_raw.readlines()






