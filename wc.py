import sys

counter = 0

for c in sys.stdin.read():
	if c == "\n":
		counter = counter + 1
print(counter)

"""
this code is meant to count the new lines
"""

counter = 0

for c in sys.stdin.read():
	if c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZaeiouAEIOU":
		counter = counter + 1
print(counter)

"""
this code is meant to count the total number of characters

however, it is currently returning 0 as a value. maybe there is
a new way to type all the characters instead of the long list?
"""
