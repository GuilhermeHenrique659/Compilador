import sys
from error.FileExeception import FileExeception
from sourceCode import SourceCode


def main():
    args = sys.argv
    if len(args) < 1:
        raise FileExeception('not file input')

    sourceCode = SourceCode(args[1])
    print(sourceCode.get_file())
    print(f'File "{sourceCode.get_file_path()}", line 3, {sourceCode.get_file()[2]}')





main()