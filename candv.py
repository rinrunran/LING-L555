import sys

consonants = 0

vowels = 0

tokens = 0

for c in sys.stdin.read():
	if c in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
		consonants = consonants + 1
	if c in "aeiouAEIOU":
		vowels = vowels + 1
	if c == " ":
		tokens = tokens + 1

print(consonants)
print(vowels)

syllables = vowels/tokens

print(syllables)

"""
this program is writted to count the number of consonants, vowels,
and additionally syllables per word (which is represented by 'syllables'.

I think some drawbacks of this method involve the method in which the token variable is obtained.
Since the token variable simply counts the amount of whitespaces, it is ubable to account
for words at the ends of sentences. To improve accuracy, maybe periods could also be counted in
conjunction with whitespaces to include previously miscounted sentence final words.
"""
