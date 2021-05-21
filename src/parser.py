from rply import ParserGenerator
from Flow.src.error import *
from Flow.src.ast import *

pg = ParserGenerator(
    # A list of all token names, accepted by the parser.
    ['NUMBER', 'OPEN_PARENS', 'CLOSE_PARENS',
     'PLUS', 'MINUS', 'MUL', 'DIV', 'LSHIFT', 'RSHIFT'
     ],
    # A list of precedence rules with ascending precedence, to
    # disambiguate ambiguous production rules.
    precedence=[
        ('left', ['PLUS', 'MINUS', 'LSHIFT']),
        ('left', ['MUL', 'DIV', 'RSHIFT'])
    ]
)


@pg.production('expression : NUMBER')
def expression_number(p):
    # p is a list of the pieces matched by the right hand side of the
    # rule
    return Number(int(p[0].getstr()))


@pg.production('expression : OPEN_PARENS expression CLOSE_PARENS')
def expression_parens(p):
    return p[1]


@pg.production('expression : expression PLUS expression')
@pg.production('expression : expression MINUS expression')
@pg.production('expression : expression MUL expression')
@pg.production('expression : expression DIV expression')
@pg.production('expression : expression RSHIFT expression')
@pg.production('expression : expression LSHIFT expression')
def expression_binop(p):
    left = p[0]
    right = p[2]
    if p[1].gettokentype() == 'PLUS':
        return Add(left, right)
    elif p[1].gettokentype() == 'MINUS':
        return Sub(left, right)
    elif p[1].gettokentype() == 'MUL':
        return Mul(left, right)
    elif p[1].gettokentype() == 'DIV':
        return Div(left, right)
    elif p[1].gettokentype() == 'RSHIFT':
        return Rshift(left, right)
    elif p[1].gettokentype() == 'LSHIFT':
        return Lshift(left, right)
    else:
        raise AssertionError('Oops, this should not be possible!')


@pg.error
def error_handler(token):
    raise Error("Randomly ran into a %s token at col %a line %a" % (token.gettokentype().lower(),  token.getsourcepos().colno,
                                                   token.getsourcepos().lineno))


parser = pg.build()
