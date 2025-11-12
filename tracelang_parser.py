# tracelang_parser.py
import ply.yacc as yacc

from tracelang_lexer import tokens

# Precedence and associativity
precedence = (
    ("left", "OR"),
    ("left", "AND"),
    ("left", "EQ", "NE"),
    ("left", "LT", "GT", "LE", "GE"),
    ("left", "PLUS", "MINUS"),
    ("left", "TIMES", "DIVIDE", "MODULO"),
    ("right", "NOT"),
    ("right", "UMINUS"),
)


def p_program(p):
    """program : statement_list"""
    p[0] = ("program", p[1])


def p_statement_list(p):
    """statement_list : statement_list statement
    | statement"""
    if len(p) == 3:
        p[0] = p[1] + [p[2]]
    else:
        p[0] = [p[1]]


def p_statement(p):
    """statement : declaration
    | assignment
    | compound_assignment
    | increment_decrement
    | if_statement
    | while_statement
    | for_statement
    | return_statement
    | print_statement
    | function_declaration
    | expression SEMICOLON
    | block"""
    p[0] = p[1]


def p_block(p):
    """block : LBRACE statement_list RBRACE
    | LBRACE RBRACE"""
    if len(p) == 4:
        p[0] = ("block", p[2])
    else:
        p[0] = ("block", [])


# Variable declarations
def p_declaration(p):
    """declaration : type ID ASSIGN expression SEMICOLON
    | type ID SEMICOLON
    | TRACE type ID ASSIGN expression SEMICOLON
    | TRACE type ID SEMICOLON"""
    if len(p) == 6:
        p[0] = ("declare", p[1], p[2], p[4], False)
    elif len(p) == 4:
        p[0] = ("declare", p[1], p[2], None, False)
    elif len(p) == 7:
        p[0] = ("declare", p[2], p[3], p[5], True)  # traced variable
    else:
        p[0] = ("declare", p[2], p[3], None, True)  # traced variable


def p_type(p):
    """type : INT
    | FLOAT_TYPE
    | STRING_TYPE
    | BOOL
    | array_type"""
    p[0] = p[1]


def p_array_type(p):
    """array_type : ARRAY LT type GT"""
    p[0] = ("array_type", p[3])


# Assignments
def p_assignment(p):
    """assignment : ID ASSIGN expression SEMICOLON
    | ID LBRACKET expression RBRACKET ASSIGN expression SEMICOLON"""
    if len(p) == 5:
        p[0] = ("assign", p[1], p[3])
    else:
        p[0] = ("array_assign", p[1], p[3], p[6])


def p_compound_assignment(p):
    """compound_assignment : ID PLUSASSIGN expression SEMICOLON
    | ID MINUSASSIGN expression SEMICOLON
    | ID TIMESASSIGN expression SEMICOLON
    | ID DIVIDEASSIGN expression SEMICOLON"""
    p[0] = ("compound_assign", p[1], p[2], p[3])


def p_increment_decrement(p):
    """increment_decrement : ID INCREMENT SEMICOLON
    | ID DECREMENT SEMICOLON"""
    p[0] = ("inc_dec", p[1], p[2])


# Control structures
def p_if_statement(p):
    """if_statement : IF LPAREN expression RPAREN statement
    | IF LPAREN expression RPAREN statement ELSE statement"""
    if len(p) == 6:
        p[0] = ("if", p[3], p[5], None)
    else:
        p[0] = ("if", p[3], p[5], p[7])


def p_while_statement(p):
    """while_statement : WHILE LPAREN expression RPAREN statement"""
    p[0] = ("while", p[3], p[5])


def p_for_statement(p):
    """for_statement : FOR LPAREN for_init SEMICOLON expression SEMICOLON for_update RPAREN statement"""
    p[0] = ("for", p[3], p[5], p[7], p[9])


def p_for_init(p):
    """for_init : type ID ASSIGN expression
    | ID ASSIGN expression
    |"""
    if len(p) == 5:
        # Type declaration in for loop: int i = 0
        p[0] = ("declare", p[1], p[2], p[4], False)
    elif len(p) == 4:
        # Assignment in for loop: i = 0
        p[0] = ("assign", p[1], p[3])
    else:
        p[0] = None


def p_for_update(p):
    """for_update : ID ASSIGN expression
    | ID PLUSASSIGN expression
    | ID MINUSASSIGN expression
    | ID TIMESASSIGN expression
    | ID DIVIDEASSIGN expression
    | ID INCREMENT
    | ID DECREMENT
    |"""
    if len(p) == 4:
        # Assignment: i = i + 1
        p[0] = ("assign", p[1], p[3])
    elif len(p) == 4 and p[2] in ["+=", "-=", "*=", "/="]:
        # Compound assignment: i += 1
        p[0] = ("compound_assign", p[1], p[2], p[3])
    elif len(p) == 3:
        # Increment/decrement: i++
        p[0] = ("inc_dec", p[1], p[2])
    else:
        p[0] = None


# Functions
def p_function_declaration(p):
    """function_declaration : FUNCTION type ID LPAREN parameter_list RPAREN block
    | FUNCTION type ID LPAREN RPAREN block"""
    if len(p) == 8:
        p[0] = ("function", p[2], p[3], p[5], p[7])
    else:
        p[0] = ("function", p[2], p[3], [], p[6])


def p_parameter_list(p):
    """parameter_list : parameter_list COMMA parameter
    | parameter"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_parameter(p):
    """parameter : type ID"""
    p[0] = (p[1], p[2])


def p_return_statement(p):
    """return_statement : RETURN expression SEMICOLON
    | RETURN SEMICOLON"""
    if len(p) == 4:
        p[0] = ("return", p[2])
    else:
        p[0] = ("return", None)


def p_print_statement(p):
    """print_statement : PRINT LPAREN expression RPAREN SEMICOLON"""
    p[0] = ("print", p[3])


# Expressions
def p_expression_binop(p):
    """expression : expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | expression MODULO expression
    | expression EQ expression
    | expression NE expression
    | expression LT expression
    | expression GT expression
    | expression LE expression
    | expression GE expression
    | expression AND expression
    | expression OR expression"""
    p[0] = ("binop", p[2], p[1], p[3])


def p_expression_unary(p):
    """expression : NOT expression
    | MINUS expression %prec UMINUS"""
    p[0] = ("unop", p[1], p[2])


def p_expression_group(p):
    """expression : LPAREN expression RPAREN"""
    p[0] = p[2]


def p_expression_number(p):
    """expression : NUMBER"""
    p[0] = ("num", p[1])


def p_expression_float(p):
    """expression : FLOAT"""
    p[0] = ("float", p[1])


def p_expression_string(p):
    """expression : STRING"""
    p[0] = ("string", p[1])


def p_expression_bool(p):
    """expression : TRUE
    | FALSE"""
    p[0] = ("bool", p[1] == "true")


def p_expression_id(p):
    """expression : ID"""
    p[0] = ("var", p[1])


def p_expression_array_literal(p):
    """expression : LBRACKET argument_list RBRACKET
    | LBRACKET RBRACKET"""
    if len(p) == 4:
        p[0] = ("array", p[2])
    else:
        p[0] = ("array", [])


def p_expression_array_access(p):
    """expression : ID LBRACKET expression RBRACKET"""
    p[0] = ("array_access", p[1], p[3])


def p_expression_function_call(p):
    """expression : ID LPAREN argument_list RPAREN
    | ID LPAREN RPAREN"""
    if len(p) == 5:
        p[0] = ("call", p[1], p[3])
    else:
        p[0] = ("call", p[1], [])


def p_argument_list(p):
    """argument_list : argument_list COMMA expression
    | expression"""
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} ('{p.value}') at line {p.lineno}")
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()
