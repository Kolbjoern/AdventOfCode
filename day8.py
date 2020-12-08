import sys

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append(line.rstrip())

	commands = []
	for line in inp:
		com, num = line.split()
		commands.append((com, num))

	index, acc = 0, 0
	indexRunned = []
	currentChange, lastChanged = 0, -1
	jmpAndNopCommands = []
	while True:
		if index >= len(commands):
			break

		command, step = commands[index]

		if index in indexRunned:
			currentChange += 1
			lastIndex = jmpAndNopCommands[-currentChange]
			prevCom, prevNum = commands[lastIndex]
			commands[lastIndex] = ("jmp", prevNum) if prevCom == "nop" else ("nop", prevNum)

			if lastChanged != -1:
				lastCom, lastNum = commands[lastChanged]
				commands[lastChanged] = ("jmp", lastNum) if lastCom == "nop" else ("nop", lastNum)

			lastChanged = lastIndex
			indexRunned.clear()
			index, acc = 0, 0
			continue

		indexRunned.append(index)
		num = int(step[1:])
		inf = step[0]

		if command == "acc":
			acc += num if inf == '+' else -num
		else:
			jmpAndNopCommands.append(index)

		if command == "jmp":
			index += num if inf == '+' else -num
		else:
			index += 1
		
	return acc

if __name__ == '__main__':
	print(main(sys.argv[1:]))