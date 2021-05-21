import argparse
import os
import eval
import src.lexer
from Flow.src import parser

lex = lexer.lexer
parse = parser.parser


def get_file():
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--file", "-f", default=os.path.getdir(__file__) + "/test.flo", nargs=1)

    args = argparser.parse_args()
    return args.file


file = get_file()
contents = open(file, "r").read()

tokens = lex.lex(contents)
parsed = parse.parse(tokens)
print(eval.eval_program(parsed))
