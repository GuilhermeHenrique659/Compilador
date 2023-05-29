from typing import List
from Token import Token

def inject_token_position(tokens: List[List[Token]]):
    GRAMMAR_SPACE = 1
    pos = 0
    for line in tokens:
        for token in line:
            pos = pos + token.collunm
            token.pos = pos
            pos += GRAMMAR_SPACE