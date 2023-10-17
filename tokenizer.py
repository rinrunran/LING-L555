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
	print('# text = %s' % (sentence))
	for word in wordbword:
		word_id = word_id + 1
		print(f'{word_id}\t{word}\t_\t_\t_\t_\t_\t_\t_\t_')
	wordbword = sentence.split(' ')
	sentence = sys.stdin.readline()
	word_id = 0
	print("\n")
