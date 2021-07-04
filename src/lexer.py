from rply import LexerGenerator
from .tokens import TOKENS

lg = LexerGenerator()

lg.add(TOKENS[0], r'\d+')
lg.add(TOKENS[1], r'\+')
lg.add(TOKENS[2], r'-')
lg.add(TOKENS[3], r'\*')
lg.add(TOKENS[4], r'/')
lg.add(TOKENS[5], r'\(')
lg.add(TOKENS[6], r'\)')
lg.add(TOKENS[7], r'lbs')
lg.add(TOKENS[8], r'rbs')
lg.add(TOKENS[9], r'>')
lg.add(TOKENS[10], r'<')


lg.ignore('\s+')

lexer = lg.build()
