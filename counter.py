import sys

counter = 0

for c in sys.stdin.read():
	if c in 'aeiou':
		counter = counter + 1
"""
This program should give the count of the number of vowels 
"aeiou" in the input "Hola mundo"
"""

print(counter)
