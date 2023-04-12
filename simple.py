from error.FileExeception import FileExeception
from error.LexicalException import LexicalExeception
from error.errorHandle import handle_error
from lexical.LexicalAnalytics import LexicalAnalytics
from sourceCode import SourceCode

import os
import sys

@handle_error
def main():
    args = sys.argv
    if len(args) <= 1:
        raise FileExeception('not file input')

    source_code = SourceCode(os.path.abspath(args[1]))
    lexical = LexicalAnalytics(source_code)
    tokens = lexical.analytics()
    source_code.source_code_tokenize = tokens
    for lines in source_code.source_code_tokenize:
        for token in lines:
            print(token.getToken())


main()