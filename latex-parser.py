import ply.lex as lex
import ply.yacc as yacc
from anytree import Node, RenderTree
import copy

class Node:
	def __init__(self,type,children=None,value=None):
		self.type = type
		if children:
			self.children = children
		else:
			self.children = []
		self.value = value

	def preOrder(self):
		print self.type
		if self.value != None:
			if isinstance(self.value, Node):
				self.value.preOrder()
			else:
				print "value :- " + str(self.value)
		if self.children != []:
			for child in self.children:
				if isinstance(child, Node):
					child.preOrder()
				else:
					print child

	def convertToHTMLTree(self):
		if (self.type == 'document-entity') and (not isinstance(self.children[0], Node)):
			print self.children
			
			if '\\documentclass' in self.children[0]:
				self.type = 'html'
			print self.children
			
			if '\\title' in self.children[0]:
				xs = self.children[0]
				value = xs.split('{')[1].split('}')[0]
				self.type = 'title'
				self.value = value
			
			if '\\author' in self.children[0]:
				xs = self.children[0]
				value = xs.split('{')[1].split('}')[0]
				self.type = 'author'
				self.value = value
			
			if '\\begin{document}' in self.children[0]:
				xs = self.children[0]
				value = xs.split('{')[1].split('}')[0]
				self.type = 'body'
			# self.children = [self.children[1]]

		if self.type == 'section':
			self.type = 'h1'
		if self.type == 'subsection':
			self.type = 'h3'

		if self.type == 'text-underline':
			self.type = '<u>'
		if self.type == 'text-bold':
			self.type = '<b>'
		if self.type == 'text-italics':
			self.type = '<i>'

		if self.children != []:
			i = 0
			for child in self.children:
				i += 1
			for idx in range(i):
				if isinstance(self.children[idx], Node):
					self.children[idx].convertToHTMLTree()


	def writeToFile(self, file):
		# Visit children in if block
		if self.type == 'html':
			file.write("<html>\n")
			if self.children != []:
				for child in self.children:
					if isinstance(child, Node):
						child.writeToFile(file)
			file.write("</html>\n")

		if self.type == 'title':
			file.write("<head>\n")
			file.write("<title>\n")
			file.write(str(self.value)+"\n")
			file.write("</title>\n")


		if self.type == 'author':
			file.write('<meta name="author" content="'+str(self.value)+'">\n')
			file.write("</head>\n")

		# Visit children in if block
		if self.type == 'body':
			file.write('<body>\n')
			if self.children != []:
				for child in self.children:
					if isinstance(child, Node):
						child.writeToFile(file)
			file.write("</body>\n")
			
		# Visit children in if block
		if 'entity' in self.type:
			if self.children != []:
				for child in self.children:
					if isinstance(child, Node):
						child.writeToFile(file)

		if self.type == 'h1':
			file.write("<h1>\n")
			if not isinstance(self.value, Node):
				file.write(str(self.value)+"\n")
			else:
				self.value.writeToFile(file)
			file.write("</h1>\n")

		if self.type == 'h3':
			file.write("<h3>\n")
			if not isinstance(self.value, Node):
				file.write(str(self.value)+"\n")
			else:
				self.value.writeToFile(file)
			file.write("</h3>\n")

		if self.type == '<b>':
			file.write("<b>\n")
			if not isinstance(self.value, Node):
				file.write(str(self.value)+"\n")
			else:
				self.value.writeToFile(file)
			file.write("</b>\n")

		if self.type == '<i>':
			file.write("<i>\n")
			if not isinstance(self.value, Node):
				file.write(str(self.value)+"\n")
			else:
				self.value.writeToFile(file)
			file.write("</i>\n")

		if self.type == '<u>':
			file.write("<u>\n")
			if not isinstance(self.value, Node):
				file.write(str(self.value)+"\n")
			else:
				self.value.writeToFile(file)
			file.write("</u>\n")

		if self.type == 'text':
			if not isinstance(self.value, Node):
				file.write(str(self.value)+"\n")
			else:
				self.value.writeToFile(file)
		
		# Visit children in if block
		if self.type == 'ordered-list':
			file.write("<ol>\n")
			if self.children != []:
				for child in self.children:
					if isinstance(child, Node):
						child.writeToFile(file)
			file.write("</ol>\n")

		# Visit children in if block
		if self.type == 'unordered-list':
			file.write("<ul>\n")
			if self.children != []:
				for child in self.children:
					if isinstance(child, Node):
						child.writeToFile(file)
			file.write("</ul>\n")

		if self.type == '<li>':
			file.write("<u>\n")
			if not isinstance(self.value, Node):
				file.write(str(self.value)+"\n")
			else:
				self.value.writeToFile(file)
			file.write("</li>\n")

		if not ((self.type == 'html') or (self.type == 'body') or (self.type == 'ordered-list') or (self.type == 'unordered-list') or ('entity' in self.type)):
			if self.children != []:
				for child in self.children:
					if isinstance(child, Node):
						child.writeToFile(file)
		
	
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
		# p[0] = p[1]+" ; "+p[2]
		# if '\\title' in p[1]:
		# 	value = p[1].split('{')[1].split('}')[0]
		# 	p[0] = Node(type='title', value=value, children=[p[2]])
		# elif '\\author' in p[1]:
		# 	value = p[1].split('{')[1].split('}')[0]
		# 	p[0] = Node(type='author', value=value, children=[p[2]])
		# elif '\\begin{document}' in p[1]:
		# 	p[0] = Node(type='body', children=[p[2]])
		# elif '\\documentclass' in p[1]:
		# 	p[0] = Node(type='html', children=[p[2]])
		# else:
		p[0] = Node(type='document-entity', children=[p[1], p[2]])
	except:
		# print "In except block - " + p[1]
		p[0] = Node(type='document-end')
		# p[0] = p[1]
		# print p[0]
	print p[0]

def p_section(p):
	'''section : SECTION LCURLY sentence RCURLY section
			   | section subsection
			   | subsection
			   | sentence
				'''
	try:
		p[0] = Node('section', value=p[3], children=[p[5]])
	except:
		try :
			p[0] = Node('section-entity', children=[p[1], p[2]])
		except:
			p[0] = p[1]
	# print p[0]

def p_subsection(p):
	'''subsection : SUBSECTION LCURLY sentence RCURLY subsection
				  | subsection subsectioncon
				  | subsectioncon
				  '''
	try:
		p[0] = Node('subsection', value=p[3], children=[p[5]])
	except:
		try: 
			p[0] = Node('subsection-entity', children=[p[1], p[2]])
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
		p[0] = Node('subsectioncon-entity', children=[p[1], p[2]])
	except:
		p[0] = p[1]
	# print p[0]

def p_ol(p):
	'''ol : OL_ST list OL_EN'''
	# print p[1]
	# print p[2]
	# print p[3]
	p[0] = Node('ordered-list', children=[p[2]])

def p_ul(p):
	'''ul : UL_ST list UL_EN'''
	# print p[1]
	# print p[2]
	# print p[3]
	p[0] = Node('unordered-list', children=[p[2]])

def p_listitem(p):
	'''listitem : ITEM_ST sentence'''
	# p[0] = p[1]+' '+ p[2]
	p[0] = Node('list-item', value=[p[2]])

def p_list_multi(p):
	'''list : list listitem'''
	# p[0] = p[1]+p[2]
	p[0] = Node('list-entity', children=[p[1], p[2]])

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
	   p[0] = Node('text-underline', value=p[3], children=[p[5]])
   elif p[1]=="\\textbf":
	   #p[0] = "<BOLD>" + p[3] +";" + p[5]
	   p[0] = Node('text-bold', value=p[3], children=[p[5]])
	   # p[0] = '<B>'+ p[3]+"<\B> " +p[5]
   elif p[1]=="\\textit":
	   #p[0]="<ITALICS>" + p[3] + ";" + p[5]
	   p[0] = Node('text-italics', value=p[3], children=[p[5]])
	   # p[0] = '<I>'+p[3]+ "<\I> "+ p[5]
   else:
	   try:
		   p[0]= Node('text-entity', children=[p[1], p[2]])
	   except:
		   p[0]=Node('text', value=p[1])
   #print p[0]


def p_error(p):
   print "|||||| Syntax error at '%s'" % p.value

yacc.yacc()
file = open('latex-examples/test.tex', 'r')
data = file.readlines()
data = ''.join(data)
t = yacc.parse(data)
print t.preOrder()
t.convertToHTMLTree()

html_file = open('test.html', 'w')
t.writeToFile(html_file)
html_file.close()