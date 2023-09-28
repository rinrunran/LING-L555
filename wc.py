import sys

counter = 0

tokens = 0

characters = 0

for c in sys.stdin.read():
	if c == "\n":
		counter = counter + 1
	if c == " ":
		tokens = tokens + 1
	#c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
	characters = characters + 1
print(counter)
print(tokens)
print(characters)



"""
this code is meant to count the new lines, the total number of characters, 
and the number of words.

Currently, it is gining out output very different from the 
$ cat wiki.txt | wc 
command in ubuntu :(
"""
