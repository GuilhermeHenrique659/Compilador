from error.FileExeception import FileExeception
from error.errorHandle import handle_error
from helpers.InjectTokenPosition import inject_token_position
from lexical.LexicalAnalytics import LexicalAnalytics
from sourceCode import SourceCode

import os
import sys

from syntactic.SyntaticAnalytics import SyntaticAnalytics

@handle_error
def main():
    args = sys.argv
    if len(args) <= 1:
        raise FileExeception('not file input')

    source_code = SourceCode(os.path.abspath(args[1]))
    lexical = LexicalAnalytics(source_code)
    tokens = lexical.analytics()
    source_code.source_code_tokenize = tokens
    inject_token_position(tokens)
    syntatic = SyntaticAnalytics(source_code)
    syntatic.analytics()




main()