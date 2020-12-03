file_handle = open('input.txt')
grid = list()
for line in file_handle:
	grid.append(line.rstrip())

counter, index, inc = 0, 0, 3
for line in grid[1:]:
	index = index + inc
	if index >= (len(line)):
		index = index - len(line)

	if line[index] == "#":
		counter = counter+1

print(counter)