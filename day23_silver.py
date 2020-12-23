import sys

def nextValid(numbers, index):
	return index if index < len(numbers) else index - len(numbers)

def popIndex(numbers, index):
	return numbers.pop(nextValid(numbers, index))

def getIndex(numbers, index):
	return numbers[nextValid(numbers, index)]

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	numbers = [int(num) for num in inp[0]]
	maxNum = max(numbers)
	current, currIndex = 0, 0
	destIndex = 0
	destination = 0
	pickUp = [0, 0, 0]
	
	for i in range(0, 100):
		current = getIndex(numbers, currIndex)

		pickIndex = numbers.index(current) + 1
		pickUp[0] = popIndex(numbers, pickIndex)
		pickIndex = numbers.index(current) + 1
		pickUp[1] = popIndex(numbers, pickIndex)
		pickIndex = numbers.index(current) + 1
		pickUp[2] = popIndex(numbers, pickIndex)

		destFind = current - 1
		while True:
			if destFind in numbers and destFind != current:
				destIndex = numbers.index(destFind)
				destination = numbers[destIndex]
				break
			else:
				destFind -= 1
				if destFind <= 0:
					destFind = maxNum

		numbers.insert(destIndex+1, pickUp[0])
		numbers.insert(destIndex+2, pickUp[1])
		numbers.insert(destIndex+3, pickUp[2])
		currIndex = numbers.index(current) + 1
		
	answer = ''
	index = numbers.index(1)+1
	for i in range(0,len(numbers)-1):
		answer += str(numbers[index])
		index += 1
		if index >= len(numbers):
			index = 0

	return answer

if __name__ == '__main__':
	print(main(sys.argv[1:]))