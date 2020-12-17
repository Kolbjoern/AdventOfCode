import sys
import copy

def nodeIsActive(pocket, x, y, z):
	return pocket[z][y][x] == '#'

def nodeIsInactive(pocket, x, y, z):
	return pocket[z][y][x] == '.'

def nodeExist(pocket, x, y, z):
	if z in pocket and y >= 0 and y < len(pocket[z]) and x >= 0 and x < len(pocket[z][y]):
		return True

	return False

def countActive(pocket, x, y, z):
	count = 0
	xMod, yMod, zMod = -1, -1, -1
	while xMod <= 1 and yMod <= 1 and zMod <= 1:
		if nodeExist(pocket, x+xMod, y+yMod, z+zMod) and nodeIsActive(pocket, x+xMod, y+yMod, z+zMod):
			if xMod == 0 and yMod == 0 and zMod == 0:
				pass
			else:
				count += 1

		zMod += 1
		if zMod > 1:
			zMod = -1
			yMod += 1
			if yMod > 1:
				yMod = -1
				xMod += 1


	return count
	
def expandZ(pocket, newZ1, newZ2):
	pocket[newZ1] = []
	pocket[newZ2] = []
	for i in range(0, len(pocket[0])):
		pocket[newZ1].append(['.'] * (len(pocket[0][0])))
		pocket[newZ2].append(['.'] * (len(pocket[0][0])))

def expand(pocket):
	for z in pocket:
		pocket[z] = [['.'] * len(pocket[0][0])] + pocket[z]
		pocket[z] = pocket[z] + [['.'] * len(pocket[0][0])]
		for y, line in enumerate(pocket[z]):
			pocket[z][y].insert(0, '.')
			pocket[z][y].append('.')


def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	pocketBuffer = []
	pocket = {}
	pocket[-1] = []
	pocket[0] = []
	pocket[1] = []
	pocket[-1].append(['.'] * (len(inp[0])+2))
	pocket[0].append(['.'] * (len(inp[0])+2))
	pocket[1].append(['.'] * (len(inp[0])+2))
	for line in inp:
		l = [node for node in line]
		pocket[-1].append(['.'] * (len(l)+2))
		pocket[0].append(['.'] + l + ['.'])
		pocket[1].append(['.'] * (len(l)+2))

	pocket[-1].append(['.'] * (len(inp[0])+2))
	pocket[0].append(['.'] * (len(inp[0])+2))
	pocket[1].append(['.'] * (len(inp[0])+2))

	zLow = -1
	zHight = 1
	for i in range(0,6):
		pocketBuffer = copy.deepcopy(pocket)
		for z in pocket:
			for y, line in enumerate(pocket[z]):
				for x, node in enumerate(line):
					z = int(z)
					numActive = countActive(pocket, x, y, z)
					if nodeIsActive(pocket, x, y, z) and (numActive != 2 and numActive != 3):
							pocketBuffer[z][y][x] = '.'

					if nodeIsInactive(pocket, x, y, z) and numActive == 3:
						pocketBuffer[z][y][x] = '#'


		pocket = copy.deepcopy(pocketBuffer)
		zLow -= 1
		zHight += 1
		expandZ(pocket, zLow, zHight)
		expand(pocket)
	
	total = 0
	for z in pocket:
		for y, line in enumerate(pocket[z]):
			for x, node in enumerate(line):
				if nodeIsActive(pocket, x, y, z):
					total += 1

	return total

if __name__ == '__main__':
	print(main(sys.argv[1:]))