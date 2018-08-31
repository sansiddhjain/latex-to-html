import ply.lex as lex
import ply.yacc as yacc

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES',
 'DIVIDE', 'EQUALS' ]

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
	r'\d+'
	t.value = int(t.value)
	return t

lex.lex()

#YACC waala part

def p_assign(p):
	'''assign : NAME EQUALS expr'''
	p[0] = ('ASSIGN',p[1],p[3])

def p_expr_plus(p):
	'''expr : expr PLUS term'''
	p[0] = ('+',p[1],p[3])

def p_expr_minus(p):
	'''expr : expr MINUS term'''
	p[0] = ('-',p[1],p[3])

def p_expr_term(p):
	'''expr : term'''
	p[0] = p[1]

def p_term_mul(p):
	'''term : term TIMES factor
			| term DIVIDE factor'''
	p[0] = ('*',p[1],p[3])

def p_term_factor(p):
	'''term : factor'''
	p[0] = p[1]

def p_factor(p):
	'''factor : NUMBER'''
	p[0] = ('NUM',p[1])

yacc.yacc()
data = "x = 3*4 + 5*6"
# data = "x = 4 + 5"
t = yacc.parse(data)
print t