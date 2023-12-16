# Open the wiki.conllu file in read mode
fd = open('wiki.conllu', 'r')

#print(#P Count Tag Form)

m = {}
 = {}

#for each instance in the imported text
for line in fd.readlines():
	#strip newlines
	line = line.strip('\n')
	#skip the line if there isn' any tab character
	if '\t' not in line:
		continue
	#define the row, form, and tag variables
	row = line.split()
	#form is defined as being the value in the 'second' position in the row, which is the tokenized word
	form = row[1]
	#defines the tag variable as being in the third position of the row
	tag = row[3]
	#create a function to add form to the dictionary 'm' if it is not there already and set an empty value for 
	if form not in m:
		m[form]={}
	#create a function to set tag to the form 
	if tag not in m[form]:
		m[form][tag]=0
	m[form][tag] += 1
	if tag not in n:
		n[tag]=0
	n[tag]+= 1
