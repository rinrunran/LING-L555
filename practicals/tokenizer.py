import sys

sent_id = 0

sentence = sys.stdin.readline()

wordbword = sentence.split(' ')

word_id = 0

while sentence:
	if sentence.strip() == '':
		sentence = sys.stdin.readline()
		wordbword = sentence.split(' ')
		continue
	sent_id = sent_id + 1
	print('# sent_id = %d' % (sent_id))
	print('# text = %s' % (sentence.strip()))
	for ch in ('.','/','`','(',')','?','!','$','%','~','^','&','#','@',':',';'):
		if ch in wordbword:
			sentence = sentence.replace(ch,' '+ch)
			wordbword = sentence.split(' ')
			continue
	for word in wordbword:
		word_id = word_id + 1
		print(f'{word_id}\t{word}\t_\t_\t_\t_\t_\t_\t_\t_')
	sentence = sys.stdin.readline()
	wordbword = sentence.split(' ')
	word_id = 0
	print("\n")
