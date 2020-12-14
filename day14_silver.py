import sys
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
		
		bit = bin(int(back.strip()))[2:]
		bit = '0' * (36-len(bit)) + bit
		bit = [w for w in bit]

		for i, m in enumerate(mask):
			bit[i] = m if m != 'X' else bit[i]

		memory[num] = ''.join(bit)

	total = 0
	for mem in memory:
		num = int(memory[mem],2)
		total += num

	return total

if __name__ == '__main__':
	print(main(sys.argv[1:]))