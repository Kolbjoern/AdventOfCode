import sys
import itertools as it
import copy
import math
import re
import functools as ft

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	numbersList = [int(num) for num in inp[0]] + [*range(10,1000001,1)]

	current = numbersList[0]
	pickUps = [0, 0, 0]
	destination = 0
	maxnum = max(numbersList)
	
	numbers = {}
	numbers[numbersList[-1]] = current
	for i, num in enumerate(numbersList[:-1]):
		numbers[num] = numbersList[i+1]

	for i in range(0, 10000000):
		pickUps[0] = numbers[current]
		pickUps[1] = numbers[pickUps[0]]
		pickUps[2] = numbers[pickUps[1]]
		destFind = current-1
		
		while True:
			if destFind in numbers and destFind != current and destFind not in pickUps:
				destination = destFind
				break
			else:
				destFind -= 1
				if destFind <= 0:
					destFind = maxnum

		afterPickUp = numbers[pickUps[2]]
		numbers[current] = afterPickUp

		destNext = numbers[destination]
		numbers[destination] = pickUps[0]
		numbers[pickUps[2]] = destNext

		current = numbers[current]

	answer1 = numbers[1]
	answer2 = numbers[answer1]

	print(answer1,answer2)
	return answer1 * answer2

if __name__ == '__main__':
	print(main(sys.argv[1:]))