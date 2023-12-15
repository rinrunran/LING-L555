import sys

#labeling a new dictionary that pairs characters to ipa
dict = {}

tagalog_ipa = open('tagalogipa.tsv', 'r')

#for each of the lines of input from the tsv file
for line in tagalog_ipa.readlines():
	# strip any excess newlines
	line = line.strip('\n')
	#if there is no tab character, skip the line
	if '\t' not in line:
		continue
	#split the values on the tab
	(t, i) = line.split('\t')
	dict[t] = i

#for each of the lines of input from the tokenizer.py file
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
	#create a for loop to loop over each character "t" in the dictionary
	for t in dict:
		#within the loop, take the predefined ipa (which was the tagalog word)
		#and then replace the character by the match in the dictionary.
		#this will loop over all characters in the word and replace them all
		#storing them in the renamed ipa variable
		ipa = ipa.replace(t, dict[t])
		#store the result of the ipa variable in the nineth spot in the row
	row[9] = 'ipa=%s' % (ipa)
	#print the entire row
	print('\t'.join(row))
