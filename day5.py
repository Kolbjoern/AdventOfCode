file_handle = open('input.txt')
inp = list()
for line in file_handle:
	inp.append(line.rstrip())

ids, com = [], {'F': 1, 'B': 0, 'L': 3, 'R': 2}
for line in inp:
	grid = [0, 127, 0, 7]
	for w in line:
		rowHalf = (grid[0] + grid[1]) // 2 + (1 if w in 'B' else 0)
		colHalf = (grid[2] + grid[3]) // 2 + (1 if w is 'R' else 0)
		grid[com[w]] = rowHalf if com[w] < 2 else colHalf

	ids.append(rowHalf * 8 + colHalf)

ids.sort()
print("highest",ids[-1])
print("missing",[i for i in range(ids[0], ids[-1]) if i not in ids])