from collections import Counter

file_handle = open('input.txt')
inp = list()
for line in file_handle:
	inp.append(line.rstrip())

inp.append("")
total, persons, answers = 0, 0, [Counter()]
for line in inp:
	if not line:
		total += len([1 for c in answers[-1] if answers[-1][c] is persons])
		answers.append(Counter())
		persons = 0
		continue

	persons += 1
	answers[-1] += Counter([char for char in line])

print(total)