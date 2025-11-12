# tracelang_parser.py
import ply.yacc as yacc

from tracelang_lexer import tokens


def p_program(p):
    "program : statement_list"
    p[0] = ("program", p[1])


def p_statement_list(p):
    """statement_list : statement_list statement
    | statement"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_statement_assign(p):
    "statement : ID ASSIGN expression SEMICOLON"
    p[0] = ("assign", p[1], p[3])


def p_statement_print(p):
    "statement : PRINT LPAREN expression RPAREN SEMICOLON"
    p[0] = ("print", p[3])


def p_expression_binop(p):
    """expression : expression PLUS expression
    | expression MINUS expression"""
    p[0] = ("binop", p[2], p[1], p[3])


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = ("num", p[1])


def p_expression_id(p):
    "expression : ID"
    p[0] = ("var", p[1])


def p_error(p):
    print("Syntax error!")


parser = yacc.yacc()
