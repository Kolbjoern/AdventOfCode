import sys

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append(int(line.rstrip()))

	inp.sort()
	inp.insert(0, 0)
	inp.append(max(inp) + 3)

	diff = {1: 0, 3: 0}

	for i, line in enumerate(inp[:-1]):
		d = inp[i+1] - line
		diff[d] += 1

	return diff[1] * diff[3]

if __name__ == '__main__':
	print(main(sys.argv[1:]))