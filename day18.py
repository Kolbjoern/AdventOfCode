import sys
import re

def findInnerMost(string):
	current_inner = 0
	max_inner = 0
	index = -1

	for i, letter in enumerate(string):
		if letter == '(':
			current_inner += 1

			if current_inner > max_inner:
				max_inner = current_inner
				index = i

		if letter == ')':
			if current_inner > 0:
				current_inner -= 1
			else:
				return -1

	if current_inner != 0:
		return -1

	return index

def calculate(string):
	order = string.split('*')
	adds = [str(calc(s)) for s in order]
	rest = '*'.join(adds)
	return calc(rest)

def calc(string):
	total, currentNum, nextOperation = 0, '', ''
	for letter in string+' ':
		if letter.isnumeric():
			currentNum += letter
		else:
			if len(currentNum) > 0:
				if total == 0:
					total = int(currentNum)
				
				if nextOperation == '+':
					total += int(currentNum)
					nextOperation = ''
				elif nextOperation == '*':
					total *= int(currentNum)
					nextOperation = ''

				currentNum = ''

			if letter in '*+':
				nextOperation = letter	

	return total


def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	total = 0
	for line in inp:
		index = findInnerMost(line)
		while index != -1:
			start = line[index:]
			ending = re.search('\)', start)
			orig = start[:ending.start()+1]
			inner = orig[1:-1]
			value = str(calculate(inner))

			line = line.split(orig)
			line = value.join(line)

			index = findInnerMost(line)

		total += calculate(line)

	return total

if __name__ == '__main__':
	print(main(sys.argv[1:]))