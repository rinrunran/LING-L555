import sys

#Now, if not done before on your computer, you need to import the jamo library

import jamo

#import some of the Hangul Compatibility Jamo using the following commands

from jamo import h2j, j2hcj

#read each line of text and store it in a variable called line
line = sys.stdin.readline()

#create a while loop to segment the text and place each sentence on its own line
while line:
	#replace the periods, exclamation marks, and semi-colons with that character and a new line
	line = line.replace('; ', ';\n').replace('. ', '.\n').replace('! ', '!\n')
	#print the line
	print(line)
	#redefine the variable
	line = sys.stdin.readline()

