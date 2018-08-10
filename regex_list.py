%%

#PREAMBLE Regex

r"\\documentclass\[sigconf\]\{acmart\}"

r"\\usepackage\{balance\}"
r"\\usepackage\{graphicx\}"

r"\\usepackage\{url\}"  
r"\\usepackage\{amsmath\}"
r"\\usepackage\{mathtools\}"
r"\\usepackage\{tabularx\}"

r"\\usepackage\{caption\}"
r"\\usepackage\{subcaption\}"

r"\\usepackage\{multirow\}"

r"\\usepackage\{graphics\}"

# Ideally - 

r"\\usepackage\{.*\}" #Extract Package Name here. Available packages - one of the above.


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

r"\\begin\{itemize\}" #Begin unordered list
r"\\end\{itemize\}" #End unordered list

r"\\begin\{enumerate\}" #Begin ordered list
r"\\end\{enumerate\}" #End ordered list

r"\\begin\{abstract\}" #Begin abstract
r"\\end\{abstract\}" #End abstract

r"\\title\{.*\}" #Title - extract title name
r"\\author\{.*\}" #Author - extract author name

r"\\section\{.*\}" #Section
r"\\subsection\{.*\}" #Subsection
r"\\section\*\{.*\}" #Section
r"\\subsection\*\{.*\}" #Subsection

r"\\label\{eq:.*\}" #Label - Equation
r"\\label\{sec:.*\}" #Label - Section
r"\\ref\{sec:.*\}" #Referencing Section
r"\\eqref\{.*\}" #Referencing Equation


r"\\includegraphics\[.*\]\{.*\}" #with params, filename
r"width.*\\textwidth" #width parameter
r"angle[ \t]*=[ \t]*[0-9]+" #angle parameter (Rotation in degrees, counter clockwise)
r"\\includegraphics\{.*\}" #with filename (default setting)

#MATHEMATICS

#Special Characters

r"\\omega" #Omega (Lowercase)
r"\\Omega" #Omega (Uppercase)
r"\\infty" #Infinity
r"\\ldots" #3 dots
r"\\sum"	#Sigma

r".+_." 	#Subscript
r".+^." 	#Superscript
r".+_\{.+\}" 	#Subscript with multiple characters
r".+^\{.+\}" 	#Superscript with multiple characters
r"\\operatorname\{.+\}"	#Extract Name of operator
r"\\frac\{.+\}\{.+\}" 	#Fraction. Extract entities in fraction.

r"\$.*\$" 	#Inline Equation
r"\\begin\{equation\}" #Starting of non-inline equation
r"\\end\{equation\}" #Ending of non-inline equation
r"\\begin\{equation\*\}" #Starting of non-inline unordered equation
r"\\end\{equation\*\}" #Ending of non-inline unordered equation
r"\\begin\{align\*\}" #Align set of equations with = sign
r"\&=.*" 			#Align everthing post this with = sign
r"\\end\{align\*\}" #Align set of equations with = sign


%%