import sys

text = sys.stdin.read()

for c in text:
	if c != "\n":
		print(text)

"""
third part of the for loop section in the Python Basics

trying to make the program output text without a new line after each 
character, and instead put a new line after each word.
"""
