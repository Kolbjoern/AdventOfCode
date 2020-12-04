import re

file_handle = open('input.txt')
inp = list()
for line in file_handle:
	inp.append(line.rstrip())

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
currpwd, counter = list(), 0
for line in inp:
	if (line == ""):
		flds = dict()
		for f in currpwd:
			part1, part2 = f.split(':')

			if part1 == 'byr' and len(part2) == 4 and int(part2) in range(1920, 2003):
				flds[part1] = part2

			if part1 == 'iyr' and len(part2) == 4 and int(part2) in range(2010, 2021):
				flds[part1] = part2

			if part1 == 'eyr' and len(part2) == 4 and int(part2) in range(2020, 2031):
				flds[part1] = part2

			if part1 == 'hgt' and re.search("^[0-9]+cm|in", part2):
				height = int(re.findall("(^[0-9]+)", part2)[0])
				if re.search("cm", part2) and height in range(150, 194):
					flds[part1] = part2
				elif re.search("in", part2) and height in range(59, 77):
					flds[part1] = part2

			if part1 == 'hcl' and part2[0] == "#" and len(re.findall('[a-z0-9]{6}', part2[1:])) > 0:
				flds[part1] = part2

			if part1 == 'ecl' and len(re.findall("amb|blu|brn|gry|grn|hzl|oth", part2)) == 1:
				flds[part1] = part2

			if part1 == 'pid' and len(part2) == 9 and part2.isdigit():
				flds[part1] = part2

		counter = counter + 1 if len(flds) == 7 else counter
		currpwd = list()
		continue

	currpwd = currpwd + line.strip().split()

print(counter)