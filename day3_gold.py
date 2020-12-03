file_handle = open('input.txt')
grid = list()
for line in file_handle:
	grid.append(line.rstrip())

counters = [0, 0, 0, 0, 0]
index = 0
slopesX = [1, 3, 5, 7, 1]
slopesY = [1, 1, 1, 1, 2]
lineCounter = 0

for slope in range(5):
	index = 0
	for line in grid[slopesY[slope]:]:
		if lineCounter % slopesY[slope] is not 0:
			lineCounter = lineCounter + 1
			continue

		lineCounter = lineCounter + 1
		index = index + slopesX[slope]
		if index >= (len(line)):
			index = index - len(line)

		if line[index] == "#":
			counters[slope] = counters[slope]+1

res = 1
for c in counters:
	res = res * c

print(res)