from error.SourceCodeExeception import SourceCodeExeception
from helpers.ErrorMessage import print_error_message
from error.FileExeception import FileExeception

def handle_error(function):
    def wrapper():
        try:
            function()
        except SourceCodeExeception as error:
            print_error_message(f"Error: {error.message}")
            print_error_message(f'\tFile "{error.path}", line {error.lineError}, {error.line}')
        except FileExeception as error:
            print_error_message(error.args[0])
    return wrapper

