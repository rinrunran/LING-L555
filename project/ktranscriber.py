import sys

import jamo

from jamo import h2j, j2hcj, hangul_to_jamo

#labeling a new dictionary that pairs characters to ipa
dict = {}

korean_ipa = open('koreanipa.tsv', 'r')

#create a variable for the generator function
sentence = open("karticle.txt", 'r').read()
#split the sentences on the spaces to give list of words in hangul
hangul_words = sentence.split(' ')
#create a variable to store the generator function
jamo = hangul_to_jamo(hangul_words)

#for each of the lines of input from the tsv file
for line in korean_ipa.readlines():
	# strip any excess newlines
	line = line.strip('\n')
	#if there is no tab character, skip the line
	if '\t' not in line:
		continue
	#split the values on the tab
	(t, i) = line.split('\t')
	dict[t] = i

#for each of the lines of input from the ktokenizer.py file
for line in sys.stdin.readlines():
	#strip excess newlines
	line = line.strip('\n')
	#if there is no tab character, skip the line
	if '\t' not in line:
		print(line)
		continue
	#make a list of the cells in the row
	row = line.split('\t')
	#if there are not 10 cells, skip the line and keep going
	if len(row) != 10:
		continue
	#name a new variable ipa as being the value of the input currently in position 1 in the row
	ipa = row[1]
	#redefine line as jamo and use a  incorporate the generator function
	line = jamo
	#create a for loop to loop over each character "t" in the dictionary
	for t in dict:
		#within this for loop use the ipa dictionary that was created and then replace the character by the match in the dictionary.
		#this will loop over all characters in the word and replace them all
		#storing them in the renamed ipa variable
		ipa = ipa.replace(t, dict[t])
		#store the result of the ipa variable in the nineth spot in the row
		row[9] = 'ipa=%s' % (line)
	#print the entire row
	print('\t'.join(row))
#While the result of this code works, I could not find a way to turn the general expression back into a string.
#Since I am working with a text file, it seems like using the other funcitons in the jamo library did not work to transcribe the hangul to jamo then to ipa.
#I think this is a great first step toward the next part of my project where I learn to do morphologically analyze the words to predict changes in pronunciation due to sound change rules based on known morphological rules.
