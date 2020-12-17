import sys
import copy

def nodeIsActive(pocket, x, y, z, w):
	return pocket[w][z][y][x] == '#'

def nodeIsInactive(pocket, x, y, z, w):
	return pocket[w][z][y][x] == '.'

def nodeExist(pocket, x, y, z, w, pocketBuffer):
	if w in pocket and z in pocket[w] and y in pocket[w][z] and x in pocket[w][z][y]:
		return True

	if w not in pocketBuffer:
		pocketBuffer[w] = {}		

	if z not in pocketBuffer[w]:
		pocketBuffer[w][z] = {}

	if y not in pocketBuffer[w][z]:
		pocketBuffer[w][z][y] = {}

	if x not in pocketBuffer[w][z][y]:
		pocketBuffer[w][z][y][x] = '.'

	return False

def countActive(pocket, x, y, z, w, pocketBuffer):
	count = 0
	xMod, yMod, zMod, wMod = -1, -1, -1, -1
	while xMod <= 1 and yMod <= 1 and zMod <= 1 and wMod <= 1:
		if nodeExist(pocket, x+xMod, y+yMod, z+zMod, w+wMod, pocketBuffer) and nodeIsActive(pocket, x+xMod, y+yMod, z+zMod, w+wMod):
			if xMod == 0 and yMod == 0 and zMod == 0 and wMod == 0:
				pass
			else:
				count += 1

		wMod += 1
		if wMod > 1:
			wMod = -1
			zMod += 1
			if zMod > 1:
				zMod = -1
				yMod += 1
				if yMod > 1:
					yMod = -1
					xMod += 1

	return count

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	pocketBuffer = {}
	pocket = {}
	init = []
	for line in inp:
		l = [node for node in line]
		init.append(l)

	pocket[0] = {}
	pocket[0][0] = {}
	for i, line in enumerate(init):
		pocket[0][0][i] = {}
		for k, node in enumerate(init[i]):
			pocket[0][0][i][k] = node

	
	pocketBuffer = copy.deepcopy(pocket)

	for w in range(-1,2):
		for z in range(-1,2):
			for y in range(-1,len(init)+1):
				for x in range(-1,len(init[0])+1):
					nodeExist(pocket, x, y, z, w, pocketBuffer)

	pocket = copy.deepcopy(pocketBuffer)

	for i in range(0,6):
		pocketBuffer = copy.deepcopy(pocket)
		for w in pocket:
			for z in pocket[w]:
				for y in pocket[w][z]:
					for x in pocket[w][z][y]:
						numActive = countActive(pocket, x, y, z, w, pocketBuffer)
						if nodeIsActive(pocket, x, y, z, w) and (numActive != 2 and numActive != 3):
							pocketBuffer[w][z][y][x] = '.'

						if nodeIsInactive(pocket, x, y, z, w):
							if numActive == 3:
								pocketBuffer[w][z][y][x] = '#'

		pocket = copy.deepcopy(pocketBuffer)

	total = 0
	for w in pocket:
		for z in pocket[w]:
			for y in pocket[w][z]:
				for x in pocket[w][z][y]:
					if nodeIsActive(pocket, x, y, z, w):
						total += 1

	return total

if __name__ == '__main__':
	print(main(sys.argv[1:]))