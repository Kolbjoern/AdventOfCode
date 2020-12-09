import sys

PREAMBLE = 25

def findOutOfRuleNumber(numberList):
	preambleList = numberList[:PREAMBLE]
	for number in numberList[PREAMBLE:]:
		found = False
		for p1, preambleNumber1 in enumerate(preambleList):
			for p2, preambleNumber2 in enumerate(preambleList):
				if p1 != p2 and preambleNumber1 + preambleNumber2 == number:
					found = True

		if found == False:
			return number

		preambleList.pop(0)
		preambleList.append(number)

	return -1

def findEncryptionWeakness(numberList, answer1):
	preambleList = numberList[:PREAMBLE]
	for number in numberList[PREAMBLE:]:
		total = 0
		for p, preambleNumber in enumerate(preambleList):
			total += preambleNumber
			if total == answer1 and p > 0:
				encryptionList = preambleList[:p]
				encryptionList.sort()
				return encryptionList[0] + encryptionList[-1]

		preambleList.pop(0)
		preambleList.append(number)

	return -1

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append(int(line.rstrip()))

	answer1 = findOutOfRuleNumber(inp)
	answer2 = findEncryptionWeakness(inp, answer1)
		
	return "answer1:",answer1,"answer2:",answer2

if __name__ == '__main__':
	print(main(sys.argv[1:]))