%%

#PREAMBLE Regex

r"\\documentclass\[sigconf\]\{acmart\}"

r"\\usepackage\{balance\}" #For balancing the heights of specific pages in two-column mode 
r"\\usepackage\{graphicx\}" # For dealing with images

r"\\usepackage\{url\}"  
r"\\usepackage\{amsmath\}" # For dealing with equations - AMS (American Mathematical Society)
r"\\usepackage\{mathtools\}"
r"\\usepackage\{tabularx\}" # For dealing with tables

r"\\usepackage\{caption\}" #For sideways captioning, continuous captioning, etc etc
r"\\usepackage\{subcaption\}" #Same as above, but for subcaptioning

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
r"\\label\{sec:.*\}" #Label - Figure
r"\\ref\{sec:.*\}" #Referencing Section
r"\\ref\{fig:.*\}" #Referencing Figure
r"\\eqref\{.*\}" #Referencing Equation

#Graphics
r"\\includegraphics\[.*\]\{.*\}" #with params, filename
r"width.*\\textwidth" #width parameter
r"angle[ \t]*=[ \t]*[0-9]+" #angle parameter (Rotation in degrees, counter clockwise)
r"\\includegraphics\{.*\}" #with filename (default setting)
r"\\caption\{.*\}" #caption of image
#Use \begin{figure} if the images have to be labelled in sequence
r"\\begin\{figure\}" #Begin figure
r"\\centering" #Obvio
r"\\end\{figure\}" #End figure


#Tables
r"\\begin\{tabular\}\{.*\}" #Starting of non-inline equation
"""
Content inside the curly braces (the ones after tabular of course) - sequence of 'l's and 'r's denoting the text alignment of the corresponding columns
l - left alignment
r - right alignment
If the sequence is like 'lrr', there are no vertical lines
If the sequence is like '|l|r|r|', there are vertical lines
If the sequence is like '|lr|r|', there is no vertical line between the first and the second line
"""
r"\\end\{tabular\}" #Ending of non-inline equation
r"&" #The endpoint between two specific cells in a particular row


#URL
#!IMPORTANT! - # $ % & ~ _ ^ \ { } : Following characters have special meanings in URL, and need to be escaped.

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