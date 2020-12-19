import sys
import copy
import re

def createRules(fileName):
	inp = list()
	for line in open(fileName):
		inp.append((line.rstrip()))

	rules, messages = {}, []
	for line in inp:
		if line == "":
			continue

		if re.search(':', line):
			num, rule = line.split(':')
			rule = rule.strip()
			rule = rule.strip("\"")

			if num == '8':
				rules[num] = '42+'
			elif num == '11':
				rules[num] = '42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31 | 42 42 42 42 42 42 31 31 31 31 31 31 | 42 42 42 42 42 42 42 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31'
			else:
				rules[num] = rule
		else:
			messages.append(line)

	return rules, messages


def main(argv):
	file = "input.txt" if not argv else argv[0]
	rules, messages = createRules(file)
	changed = [n for n in rules if rules[n] in 'ab']
	
	newChanged = []
	while len(changed) > 0:
		for n in rules:
			for change in changed:
				if change in rules[n]:
					if '|' in rules[change]:
						num = [j for j in rules[n].split()]
						for a, k in enumerate(num):
							if k == change:
								num[a] = '('+rules[change]+')'
							elif k == change+'+':
								num[a] = '('+rules[change]+')+'

						rules[n] = ' '.join(num)
					else:
						num = [j for j in rules[n].split()]
						for a, k in enumerate(num):
							if k == change:
								num[a] = rules[change]
							elif k == change+'+':
								num[a] = '('+rules[change]+')+'

						rules[n] = ' '.join(num)
						
			test = rules[n]
			if '42' in test:
				test = test.replace('42','')

			if not re.search('\d', test) and n not in changed and n not in newChanged:
				newChanged.append(n)

		for c in changed:
			if c != '0':
				del rules[c]

		changed = copy.deepcopy(newChanged)
		newChanged = []


	rule0 = rules['0'].replace(' ','')
	return sum([1 for message in messages if re.fullmatch(rule0, message)])

if __name__ == '__main__':
	print(main(sys.argv[1:]))