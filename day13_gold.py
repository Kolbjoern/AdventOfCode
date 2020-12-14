import sys
import itertools as it
import copy
import math
import functools as ft

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	buss = [int(word) for word in inp[1].split(',') if word != 'x']
	inp[1] = inp[1].replace('x','0')
	allBusses = [int(word) for word in inp[1].split(',')]
	
	busses = []
	count, MODS = 0, 10000
	modifiers = [1] * (len(buss))
	for bus in allBusses:
		if bus == 0:
			count += 1
			continue
		
		if count > 0:
			busses.append(MODS + count)
			count = 0

		busses.append(bus)

	numMods = 0
	for i, bus in enumerate(busses):
		if bus > MODS:
			numMods += 1
			modifiers[i-numMods] += (bus-MODS)
			
	i = 0
	currentStamp = buss[0]
	currentModifier = modifiers[0]
	while i < len(buss)-1:
		if (currentStamp + currentModifier) % buss[i+1] != 0:
			power = ft.reduce(lambda a, b: a*b, buss[:i+2])
			currentStamp += power // buss[i+1]
		else:
			i += 1
			currentModifier += modifiers[i]

	return currentStamp

if __name__ == '__main__':
	print(main(sys.argv[1:]))