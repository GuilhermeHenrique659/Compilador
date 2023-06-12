from enum import Enum

class TokenTableEnum(Enum):
    ATRIBUTION = '='
    LINE_BREAK = ';'
    INTEGER = 'integer number'
    CLOSE_BRACE = '}'
    OPEN_BRACE = '{'
    INT_TYPE = 'int'
    IDENTIFIER = 'var or function identifier'
    STAR = '*'
    SLASH = '/'
    MINUS = '-'
    PLUS = '+'
    CLOSE_PARAN = ')'
    OPEN_PARAN = '('