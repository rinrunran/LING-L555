import sys
#import the jamo python library
import jamo
#import these from the jamo library
from jamo import h2j, j2hcj, hangul_to_jamo

#define sentence number
sent_id = 0
#read the input line by line and store it in the variable "sentence"
sentence = sys.stdin.readline()
#split the sentences on the spaces to give a word by word list
wordbword = sentence.split(' ')

word_id = 0
#using the jamo library, store the result of the word by word decomposition into jamo (letters) in the variable hangul
hangul = (hangul_to_jamo for w in wordbword)

#create a while loop to find the sentences of interest and perform the following functions...
while sentence:
	#ignore leading and trailing whitespaces
	if sentence.strip() == '':
		sentence = sys.stdin.readline()
		wordbword = sentence.split(' ')
		#after resetting the variables, continue
		continue
	#increase the sent_id variable to account for the sentence found
	sent_id = sent_id + 1
	#print a statement that announces the number id of the sentence
	print('# sent_id = %d' % (sent_id))
	print('# text = %s' % (sentence.strip()))
	#make a loop that searches for punctuation characters in wordbword, and then replace it with a space and then the character
	#to make punctuation appear in their own lines
	for ch in ('.','/','`','(',')','?','!','$','%','~','^','&','#','@',':',';'):
		if ch in sentence:
			sentence = sentence.replace(ch,' '+ch)
			wordbword = sentence.split(' ')
			continue
	#for each word in wordbword, increase the word id by 1 and add it to the output print statement
	for word in wordbword:
		word_id = word_id + 1
		print(f'{word_id}\t{word}\t_\t_\t_\t_\t_\t_\t_\t_')

	#redefine the variables
	sentence = sys.stdin.readline()
	wordbword = sentence.split(' ')
	hangul = (hangul_to_jamo for w in wordbword)
	word_id = 0
	print("\n")
