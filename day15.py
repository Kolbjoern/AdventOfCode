import sys

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	numbers = [int(num) for num in inp[0].split(',')]
	orig, speak, prev, i = 0, 0, 0, 1
	numSpoken = {}
	while i < 30000001:
		if prev in numSpoken and len(numSpoken[prev]) > 1:
			speak = numSpoken[prev][-1] - numSpoken[prev][-2]
		else:
			if orig < len(numbers):
				speak = numbers[orig]
				orig += 1
			else:
				speak = 0

		prev = speak
		if speak not in numSpoken:
			numSpoken[speak] = []

		numSpoken[speak].append(i)
		i += 1

	return speak

if __name__ == '__main__':
	print(main(sys.argv[1:]))