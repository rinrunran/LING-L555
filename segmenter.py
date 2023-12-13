import sys

line = sys.stdin.readline()

while line:
	line = line.replace('. ', '.\n').replace('; ', ';\n').replace('! ', '!\n')
	print(line)
	line = sys.stdin.readline()

