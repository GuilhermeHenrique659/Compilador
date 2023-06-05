from helpers.TokenTypeEnum import TokenTypeEnum


class Token:
    pos: int

    def __init__(self, line: int, collunm: int, token_type: str, lex: str) -> None:
        self.line = line
        self.collunm = collunm
        self.token_type = token_type
        self.lex = lex

    def get_token(self):
        if self.token_type == TokenTypeEnum.BASIC_MATH_OP.value:
            return self.lex
        return self.token_type

    def get_data(self):
        return {
            'Line': self.line,
            'Collunm': self.collunm,
            'Token': f'<{self.token_type},{self.lex}>',
            'pos': self.pos
        }

    def __str__(self) -> str:
        return self.lex
