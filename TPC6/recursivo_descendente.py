import ply.lex as lex
import ply.yacc as yacc


# ----- Analisador Léxico -----


tokens = ('NUM', 'PA', 'PF', 'MAIS', 'MENOS', 'VEZES')


t_PA = r'\('
t_PF = r'\)'
t_MAIS = r'\+'
t_MENOS = r'\-'
t_VEZES = r'\*'


def t_NUM(t):
    r'\d+'
    t.value = int (t.value)
    return t


t_ignore = ' \t\n'


def t_error(t):
    print('Caracter desconhecido:', t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()




# ----- Analisador Sintático -----


def p_expr_mais(p):
    'expressao : expressao MAIS termo'
    p[0] = p[1] + p[3]

def p_expr_menos(p):
    'expressao : expressao MENOS termo'
    p[0] = p[1] - p[3]

def p_expr_termo(p):
    'expressao : termo'
    p[0] = p[1]

def p_termo_vezes(p):
    'termo : termo VEZES fator'
    p[0] = p[1] * p[3]

def p_termo_fator(p):
    'termo : fator'
    p[0] = p[1]

def p_fator_num(p):
    'fator : NUM'
    p[0] = p[1]

def p_fator_expr(p):
    'fator : PA expressao PF'
    p[0] = p[2]

def p_error(p):
    print("Erro sintático no input!")



# expressao : termo
#           | expressao MAIS termo
#           | expressao MENOS termo
# termo : termo VEZES fator
#       | fator
# fator : NUM
#       | PA expressao PF



parser = yacc.yacc(write_tables=False, debug=False)   # Impede a criação de "parsetab.py" e "parser.out"


while s := input('Expressão > '):
   result = parser.parse(s)
   if result is not None:
       print(result)