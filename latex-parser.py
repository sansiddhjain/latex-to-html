import ply.lex as lex
import ply.yacc as yacc

tokens = [ 'NEWLINE','UL_ST','UL_EN','OL_ST','OL_EN', 'ITEM_ST', 'TEXT', 'DOTS' ]

t_ignore = " \t\r\n"
t_NEWLINE = r'\\\\'
t_DOTS = r'\\dots'
t_OL_ST = r"\\begin\{enumerate\}"
t_OL_EN = r"\\end\{enumerate\}"
t_UL_ST = r"\\begin\{itemize\}"
t_UL_EN = r"\\end\{itemize\}"
t_ITEM_ST = r"\\item"
t_TEXT = r"[a-zA-Z0-9_,. ]+"

def t_error(t):
    raise TypeError("Unknown text '%s'" % (t.value,))


lex.lex()

# data_test = "\\begin{enumerate}\n\\item Like this,\n\\item and like this.\n\\end{enumerate}\n\\dots or bullet points \\dots\n\\begin{itemize}\n\\item Like this,\n\\item and like this.\n\\end{itemize}"
file = open('latex-examples/test.tex', 'r')
data = file.readlines()
data = ''.join(data)
lex.input(data)
for tok in iter(lex.token, None):
    print repr(tok.type), repr(tok.value)

#YACC waala part

def p_pexp(p):
	'''pexp : p_ol | p_ul'''

def p_ol(p):
	'''ol : OL_ST list OL_EN'''
	print p[1]
	print p[2]
	print p[3]

def p_ul(p):
	'''ul : UL_ST list UL_EN'''
	print p[1]
	print p[2]
	print p[3]

def p_listitem(p):
	'''listitem : ITEM_ST TEXT'''
	p[0] = p[1]+' '+ p[2]

def p_list_multi(p):
	'''list : list listitem'''
	p[0] = p[1]+p[2]

def p_list_unary(p):
	'''list : listitem'''
	p[0] = p[1]

# def p_error(p):
#     print "Syntax error at '%s'" % p.value

yacc.yacc()
file = open('latex-examples/test.tex', 'r')
data = file.readlines()
data = ''.join(data)
t = yacc.parse(data)
# print t
