
import os
import re

from error.FileExeception import FileExeception


fileNameRegex = re.compile('[a-zA-Z][a-zA-Z0-9_.]*.sl')
pathToSearchRegex = re.compile('[a-zA-Z0-9:_./]*/[a-zA-Z][a-zA-Z0-9_.]*.sl')

class SourceCode:
    __filepath: str
    __source_code_file: str

    def __init__(self, soruceCodeFile: str) -> None:
        self.__source_code_file = soruceCodeFile

    def get_file_path(self):
        return self.__filepath

    def validate_source_code(self):

        if pathToSearchRegex.match(self.__source_code_file):
            sourceCodePath: str = fileNameRegex.split(self.__source_code_file)[0]
            sourceCodeFileName: str = fileNameRegex.findall(self.__source_code_file)[0]
        
            print(sourceCodePath)
            if os.path.exists(sourceCodePath + sourceCodeFileName):
                if not fileNameRegex.match(sourceCodeFileName):
                    raise FileExeception('this file not .sl')
                
                self.__filepath = sourceCodePath + sourceCodeFileName
            else:
                raise FileExeception(f'file {self.__source_code_file} not found')
        else:
            sourceCodeFileName = fileNameRegex.findall(self.__source_code_file)[0]
            if not fileNameRegex.match(sourceCodeFileName):
                    raise FileExeception('this file not sl')
            self.__filepath = './' + sourceCodeFileName

    def get_file(self):
        self.validate_source_code()
        file = open(self.__filepath)
    
        return file.readlines()






