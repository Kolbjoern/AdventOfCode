import sys

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append(int(line.rstrip()))

	inp.sort()
	inp.insert(0,0)
	inp.append(max(inp) + 3)

	prev1, prev2, prev3, current = 1, 0, 0, 0
	for i in range(1, len(inp)):
		if inp[i] - inp[i-1] <= 3:
			current += prev1

		if i-2 >= 0 and inp[i] - inp[i-2] <= 3:
			current += prev2

		if i-3 >= 0 and inp[i] - inp[i-3] <= 3:
			current += prev3

		prev3 = prev2
		prev2 = prev1
		prev1 = current
		current = 0

	return prev1

if __name__ == '__main__':
	print(main(sys.argv[1:]))