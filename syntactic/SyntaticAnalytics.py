from lark import Lark, Token
from lark.exceptions import ParseError

class SyntaticAnalytics:
    def gerar_arvore_derivacao(self, tokens):
        grammar = '''
            start: program
            program: function_decl
            function_decl: "FUNCTION" "IDENTIFIER" "OPEN_PARAN" "CLOSE_PARAN" "OPEN_BRACE" statement* "CLOSE_BRACE"
            statement: variable_decl | assignment
            variable_decl: "INT_TYPE" "IDENTIFIER" "ATRIBUTION" "INTEGER" "LINE_BREAK"
            assignment: "IDENTIFIER" "ATRIBUTION" expr "LINE_BREAK"
            expr: term (("+" | "-") term)*
            term: factor (("*" | "/") factor)*
            factor: "INTEGER" | "IDENTIFIER" | "(" expr ")"
        '''

        parser = Lark(grammar, parser='lalr', lexer='contextual')
        code = ''.join(token.get_token() for token in tokens)
        print(code)
        try:
            tree = parser.parse(code)
            return tree
        except ParseError as e:
            print(e.column)
            for token in tokens:
                if token.pos == e.column:
                    return token