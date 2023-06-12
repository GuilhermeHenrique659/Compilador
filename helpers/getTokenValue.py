from typing import List
from helpers.enum.TokenTable import TokenTableEnum

def get_token_value(tokens: List[str]) -> str:
    try:
        res = list(map(lambda token: TokenTableEnum[str(token)].value, tokens))
        return ' or '.join(res)
    except KeyError as error:
        return f'unexpected token {str(error)}'