# tracelang_compiler.py
import sys

from tracelang_interpreter import run
from tracelang_lexer import lexer
from tracelang_parser import parser


def main():
    if len(sys.argv) < 2:
        print("Usage: python tracelang_compiler.py <sourcefile>")
        return

    source_file = sys.argv[1]
    with open(source_file, "r") as f:
        code = f.read()

    ast = parser.parse(code, lexer=lexer)
    print("AST:", ast)  # optional, for debugging

    env = {}
    run(ast, env)


if __name__ == "__main__":
    main()
