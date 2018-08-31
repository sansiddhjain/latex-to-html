import ply.lex as lex
import ply.yacc as yacc

tokens = [ 'NEWLINE','UL_ST','UL_EN','OL_ST','OL_EN', 'ITEM_ST', 'TEXT', 'DOTS', 'UNDERLINE', 'BOLD', 'ITALICS', 'SECTION', 'SUBSECTION', 'USEPACKAGE', \
 'USEPACKAGEPARAM', 'BODY', 'TITLE', 'HREF', 'URL', 'DOLLAR', 'NEWLINEMATHSTART', 'NEWLINEMATHEND', 'LATEX' ]

t_NEWLINE = r'\\\\'
t_DOTS = r'\\dots'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_OL_ST = r"\\begin\{enumerate\}"
t_OL_EN = r"\\end\{enumerate\}"
t_UL_ST = r"\\begin\{itemize\}"
t_UL_EN = r"\\end\{itemize\}"
t_ITEM_ST = r"\\item"
t_UNDERLINE = r"\\underline"
t_BOLD = r"\\textbf"
t_ITALICS = r"\\textit"
t_SECTION = r"\\section\{.*\}"
t_SUBSECTION = r"\\subsection\{.*\}"
t_TEXT = r"[a-zA-Z0-9_,. ]+"
t_USEPACKAGE = r"\\usepackage\{.*\}"
t_USEPACKAGEPARAM = r"\\usepackage\[.*\]\{.*\}"
t_BODY = r"\\begin\{document\}"
t_TITLE = r"\\title\{.*\}"
t_HREF = r"\\href\{.*\}\{.*\}"
t_URL = r"\\url\{.*\}"
t_DOLLAR = r"\$"
t_NEWLINEMATHSTART = r"\\\["
t_NEWLINEMATHEND = r"\\\]"
t_LATEX = r"\\LaTeX{}"
t_ignore = " \t\r\n"

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

def p_section(p):
	'''section : section subsection
			   | subsection'''
	print "section found"

def p_subsectioncon(p):
	'''subsectioncon : subsectioncon sentence
					 | subsectioncon ul
		   			 | subsectioncon ol
		   			 | sentence
		   			 | ol
		   			 | ul'''
	print "subsection content found"

def p_subsection(p):
	'''subsection : SUBSECTION LCURLY sentence RCURLY subsectioncon'''
	print "subsection found"

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

def p_sentence(p):
    '''sentence : UNDERLINE '{' sentence '}' sentence
                | BOLD '{' sentence '}' sentence
                | ITALICS '{' sentence '}' sentence
                | sentence TEXT
                | TEXT 
                '''
    if p[1]=="\\underline":
        p[0] = "<UNDERLINE>" + p[3] +";" + p[5]
    elif p[1]=="\\textbf":
        p[0] = "<BOLD>" + p[3] +";" + p[5]
    elif p[1]=="\\textit":
        p[0]="<ITALICS>" + p[3] + ";" + p[5]
    else:
        try:
            p[0]="<no format>" + p[1] + p[2]    
        except:
            p[0]="<no format>" + p[1]
    print p[0]


def p_error(p):
    print "Syntax error at '%s'" % p.value

yacc.yacc()
file = open('latex-examples/test.tex', 'r')
data = file.readlines()
data = ''.join(data)
t = yacc.parse(data)
# print t


