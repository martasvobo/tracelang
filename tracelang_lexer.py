# tracelang_lexer.py
import ply.lex as lex

tokens = (
    "ID",
    "NUMBER",
    "FLOAT",
    "STRING",
    # Arithmetic operators
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "MODULO",
    # Assignment operators
    "ASSIGN",
    "PLUSASSIGN",
    "MINUSASSIGN",
    "TIMESASSIGN",
    "DIVIDEASSIGN",
    # Comparison operators
    "EQ",
    "NE",
    "LT",
    "GT",
    "LE",
    "GE",
    # Logical operators
    "AND",
    "OR",
    "NOT",
    # Increment/Decrement
    "INCREMENT",
    "DECREMENT",
    # Delimiters
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "LBRACKET",
    "RBRACKET",
    "SEMICOLON",
    "COMMA",
    # Keywords
    "IF",
    "ELSE",
    "WHILE",
    "FOR",
    "FUNCTION",
    "RETURN",
    "PRINT",
    "TRUE",
    "FALSE",
    "TRACE",
    "INT",
    "FLOAT_TYPE",
    "STRING_TYPE",
    "BOOL",
    "ARRAY",
)

# Compound operators (must be before simple ones)
t_PLUSASSIGN = r"\+="
t_MINUSASSIGN = r"-="
t_TIMESASSIGN = r"\*="
t_DIVIDEASSIGN = r"/="
t_INCREMENT = r"\+\+"
t_DECREMENT = r"--"
t_EQ = r"=="
t_NE = r"!="
t_LE = r"<="
t_GE = r">="
t_AND = r"&&"
t_OR = r"\|\|"

# Simple operators
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_MODULO = r"%"
t_ASSIGN = r"="
t_LT = r"<"
t_GT = r">"
t_NOT = r"!"

# Delimiters
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_SEMICOLON = r";"
t_COMMA = r","

reserved = {
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "for": "FOR",
    "function": "FUNCTION",
    "return": "RETURN",
    "print": "PRINT",
    "true": "TRUE",
    "false": "FALSE",
    "trace": "TRACE",
    "int": "INT",
    "float": "FLOAT_TYPE",
    "string": "STRING_TYPE",
    "bool": "BOOL",
    "array": "ARRAY",
}


def t_COMMENT(t):
    r"//.*"
    pass  # No return value. Token discarded


def t_FLOAT(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Remove quotes
    # Handle escape sequences
    t.value = t.value.replace("\\n", "\n")
    t.value = t.value.replace("\\t", "\t")
    t.value = t.value.replace('\\"', '"')
    t.value = t.value.replace("\\\\", "\\")
    return t


def t_ID(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, "ID")
    return t


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


t_ignore = " \t\r"


def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}")
    t.lexer.skip(1)


lexer = lex.lex()
