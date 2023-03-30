from error.FileExeception import FileExeception
from error.LexicalError import LexicalError
from error.errorHandle import handle_error
from sourceCode import SourceCode

import sys

@handle_error
def main():
    args = sys.argv
    if len(args) < 1:
        raise FileExeception('not file input')

    sourceCode = SourceCode(args[1])
    source_code_lines = sourceCode.get_source_code_lines()
    raise LexicalError('invalid token', 2, source_code_lines[1], sourceCode.get_file_path())




main()