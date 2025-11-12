# tracelang_lexer.py
import ply.lex as lex

tokens = (
    "ID",
    "NUMBER",
    "STRING",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "ASSIGN",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "SEMICOLON",
    "IF",
    "ELSE",
    "WHILE",
    "PRINT",
    "TRUE",
    "FALSE",
    "TRACE",
)

t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_ASSIGN = r"="
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_SEMICOLON = r";"

reserved = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "print": "PRINT",
    "true": "TRUE",
    "false": "FALSE",
    "trace": "TRACE",
}


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value.strip('"')
    return t


t_ignore = " \t\r\n"


def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


lexer = lex.lex()
