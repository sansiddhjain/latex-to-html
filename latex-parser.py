from pyparsing import Literal, CaselessLiteral, Word, delimitedList, Optional, Regex


r"\\begin\{document\}"	#Starting of document
r"\\end\{document\}"	#End of document
r"[ \t]+"	#Whitespace
r"[\n]"		#New line
r"\\"		#New line
r"``.*\'\'"	#Text in Double Quotes
r"`.*\'"	#Text in Single Quotes
r"\\#"		#Hash
r"\\%"		#Percentage
r"\\\$"		#Dollar Sign
r"\\&"		#Ampersand

r"\\begin\{abstract\}" #Begin abstract
r"\\end\{abstract\}" #End abstract

r"\\title\{.*\}" #Title - extract title name
r"\\author\{.*\}" #Author - extract author name


list = Forward()

ul_st = Regex(r"\\begin\{itemize\}").setName('ul_st') #Begin unordered list
ul_en = Regex(r"\\end\{itemize\}").setName('ul_en') #End unordered list

ol_st = Regex(r"\\begin\{enumerate\}").setName('ol_st') #Begin ordered list
ol_en = Regex(r"\\end\{enumerate\}").setName('ol_en') #End ordered list

item = Regex(r"\\item.*").setName('item')

ul = Group(ul_st + OneOrMore(item) + ul_en).setName('ul')
ol = Group(ol_st + OneOrMore(item) + ol_en).setName('ol')

list << OneOrMore(ul | ol).setName('list')
list.verbose_stacktrace = True
list.parseString()

r"\\section\{.*\}" #Section
r"\\subsection\{.*\}" #Subsection
r"\\section\*\{.*\}" #Section
r"\\subsection\*\{.*\}" #Subsection

inp = "\begin{enumerate}\n\item Like this,\n\item and like this.\n \end{enumerate} \n\dots or bullet points \dots\n \begin{itemize}\n \item Like this,\n \item and like this.\n \end{itemize}\n"