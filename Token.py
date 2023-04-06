class Token:
    def __init__(self, line: int, collunm: int, token_type: str, lex: str) -> None:
        self.line = line
        self.collunm = collunm
        self.token_type = token_type
        self.lex = lex

    def getToken(self):
        return {
            'Line': self.line,
            'Collunm': self.collunm,
            'Token': f'<{self.token_type},{self.lex}>'
        }

    def __str__(self) -> str:
        return self.lex
