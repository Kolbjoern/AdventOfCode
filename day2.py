import re

file_handle = open('input.txt')
password = list()
for line in file_handle:
	line = line.rstrip()
	password.append(line)

counter = 0
for pwd in password:
	p = pwd.split()
	occ = p[0].split('-')
	letter = p[1][0]
	found = len([m.start() for m in re.finditer(letter, p[2])])
	fOcc = int(occ[0])
	sOcc = int(occ[1])
	first = (len(p[2]) >= fOcc and p[2][fOcc-1] is letter) and (len(p[2]) >= sOcc and p[2][sOcc-1] is not letter)
	second = (len(p[2]) >= fOcc and p[2][fOcc-1] is not letter) and (len(p[2]) >= sOcc and p[2][sOcc-1] is letter)
	counter = counter + 1 if first or second else counter

print(counter)