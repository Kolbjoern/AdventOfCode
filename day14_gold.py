import sys
import itertools as it
import copy
import re

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	mask = ''
	memory = dict()
	for line in inp:
		if line.startswith('mask'):
			mask = [w for w in line.split('=')[1].strip()]
			continue

		front, back = line.split('=')
		num = re.findall(r'\d+', front)[0]
		value = back.strip()

		bit = bin(int(num))[2:]
		bit = '0' * (36-len(bit)) + bit
		bit = [w for w in bit]

		indices = []
		for i, m in enumerate(mask):
			bit[i] = m if m != '0' else bit[i]
			if m == 'X': indices.append(i)
			
		floatResults = []
		comb = [0] * len(indices)
		for i in range(0,len(comb)+1):
			if i-1 >= 0:
				comb[i-1] = 1

			perm = list(it.permutations(comb, len(comb)))
			perm = list(dict.fromkeys(perm))
			for combo in perm:
				ls = list(combo)
				bitcopy = copy.deepcopy(bit)
				for i, index in enumerate(indices):
					bitcopy[index] = str(ls[i])
					if bitcopy not in floatResults:
						floatResults.append(bitcopy)

		for res in floatResults:
			address = int(''.join(res),2)
			memory[address] = int(value)

	return sum(memory.values())

if __name__ == '__main__':
	print(main(sys.argv[1:]))