import sys

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	timestamp = int(inp[0])
	bus = [int(word) for word in inp[1].split(',') if word != 'x']

	nextBus = 0
	currentTime = timestamp-1
	running = True
	while running:
		currentTime += 1
		for busTime in bus:
			if currentTime % busTime == 0:
				nextBus = busTime
				running = False
				break

	return nextBus * (currentTime-timestamp)

if __name__ == '__main__':
	print(main(sys.argv[1:]))