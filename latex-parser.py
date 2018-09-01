import ply.lex as lex
import ply.yacc as yacc
from anytree import Node, RenderTree

tokens = ['ENDDOCUMENT','DOCUMENT','TITLE','AUTHOR','NEWLINE','UL_ST','UL_EN','OL_ST','OL_EN','ITEM_ST','TEXT','DOTS','UNDERLINE','BOLD',
'ITALICS','SECTION','SUBSECTION','USEPACKAGE','USEPACKAGEPARAM','BODY','HREF','URL','DOLLAR','NEWLINEMATHSTART','NEWLINEMATHEND','LATEX',
'DOUBLEQUOTESSTART','DOUBLEQUOTESEND','LCURLY','RCURLY', 'PAR']

t_DOCUMENT = r'\\documentclass\[.*\]\{.*\}'
t_TITLE = r'\\title\{.*\}'
t_AUTHOR = r'\\author\{.*\}'
t_SUBSECTION = r"\\subsection"
t_NEWLINE = r'\\\\'
t_PAR = r'\\par'
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
t_ENDDOCUMENT = r"\\end\{document\}"
t_USEPACKAGE = r"\\usepackage\{.*\}"
t_USEPACKAGEPARAM = r"\\usepackage\[.*\]\{.*\}"
t_BODY = r"\\begin\{document\}"
t_HREF = r"\\href\{.*\}\{.*\}"
t_URL = r"\\url\{.*\}"
t_DOLLAR = r"\$"
t_NEWLINEMATHSTART = r"\\\["
t_NEWLINEMATHEND = r"\\\]"
t_LATEX = r"\\LaTeX{}"
t_DOUBLEQUOTESSTART = r"``"
t_DOUBLEQUOTESEND = r"''"
t_SECTION = r"\\section"
t_TEXT = r"[a-zA-Z0-9_,!?\"'()`:;\.\- ]+"
t_ignore = " \t\r\n"

def t_error(t):
   raise TypeError("Unknown text '%s'" % (t.value,))


lex.lex()

file = open('latex-examples/test.tex', 'r')
data = file.readlines()
data = ''.join(data)
lex.input(data)
# for tok in iter(lex.token, None):
#    print repr(tok.type), repr(tok.value)

#YACC waala part

def p_document(p):
	'''document : DOCUMENT document
				| TITLE document
				| AUTHOR document
				| BODY document
				| section document
				| ENDDOCUMENT
				'''
	try:
		# print p[1]+";"+p[2]
		p[0] = p[1]+" ; "+p[2]
	except:
		# print "In except block - " + p[1]
		p[0] = p[1]
		# print p[0]
	# print p[0]

def p_section(p):
	'''section : SECTION LCURLY sentence RCURLY section
			   | section subsection
			   | subsection
			   | sentence
				'''
	try:
		p[0] = 'title - ' + p[3] + p[5]
	except:
		try :
			p[0] = p[1] + p[2]
		except:
			p[0] = p[1]
	# print p[0]

def p_subsection(p):
	'''subsection : SUBSECTION LCURLY sentence RCURLY subsection
				  | subsection subsectioncon
				  | subsectioncon
				  '''
	try:
		p[0] = 'title - ' + p[3] + p[5]
	except:
		try: 
			p[0] = p[1] + p[2]
		except:
			p[0] = p[1]
	# print p[0]

def p_subsectioncon(p):
	'''subsectioncon : subsectioncon sentence
					 | subsectioncon ul
					 | subsectioncon ol
					 | sentence
					 | ol
					 | ul'''
	try:
		p[0] = p[1] + p[2]
	except:
		p[0] = p[1]
	# print p[0]

# def p_paragraph(p):
#    '''paragraph : paragraph PAR
#                 | paragraph sentence
#                 | paragraph NEWLINE
#                 | sentence
#                 | NEWLINE
#                 | PAR
#                 '''
#    try:
#        p[0] = '<par>' + p[2]
#    except:
#        p[0] = p[1]
#    print "para print:", p[0]


def p_math(p):
	'''math : DOLLAR expr DOLLAR
			| NEWLINEMATHSTART expr NEWLINEMATHEND
			'''
	p[0] = p[2]

def p_expr(p):
	'''expr : '''

def p_ol(p):
	'''ol : OL_ST list OL_EN'''
	# print p[1]
	# print p[2]
	# print p[3]

def p_ul(p):
	'''ul : UL_ST list UL_EN'''
	# print p[1]
	# print p[2]
	# print p[3]

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
   '''sentence : UNDERLINE LCURLY sentence RCURLY sentence
               | BOLD LCURLY sentence RCURLY sentence
               | ITALICS LCURLY sentence RCURLY sentence
               | sentence TEXT
               | TEXT sentence
               | TEXT
               '''
   if p[1]=="\\underline":
       #p[0] = "<UNDERLINE>" + p[3] +";" + p[5]
       p[0] = '<U>' +p[3]+"<\U> "+p[5]
   elif p[1]=="\\textbf":
       #p[0] = "<BOLD>" + p[3] +";" + p[5]
       p[0] = '<B>'+ p[3]+"<\B> " +p[5]
   elif p[1]=="\\textit":
       #p[0]="<ITALICS>" + p[3] + ";" + p[5]
       p[0] = '<I>'+p[3]+ "<\I> "+ p[5]
   else:
       try:
           p[0]= p[1]+" "+p[2]   
       except:
           p[0]=p[1]
   #print p[0]


def p_error(p):
   print "|||||| Syntax error at '%s'" % p.value

yacc.yacc()
file = open('latex-examples/test.tex', 'r')
data = file.readlines()
data = ''.join(data)
t = yacc.parse(data)
# print t