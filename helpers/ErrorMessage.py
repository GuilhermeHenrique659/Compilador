def print_error_message(message: str):
    FAIL = '\033[91m' 
    WHITE = '\033[37m'
    print(FAIL + message)
    print(WHITE)