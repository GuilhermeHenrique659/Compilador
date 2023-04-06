from error.FileExeception import FileExeception
from error.LexicalException import LexicalExeception
from error.errorHandle import handle_error
from lexical.LexicalAnalytics import LexicalAnalytics
from sourceCode import SourceCode

import sys

@handle_error
def main():
    args = sys.argv
    if len(args) <= 1:
        raise FileExeception('not file input')

    source_code = SourceCode(args[1])
    lexical = LexicalAnalytics(source_code)
    tokens = lexical.analytics()
    for lines in tokens:
        for token in lines:
            print(token.getToken())


main()