def find_num(list):
	for num1 in list:
		for num2 in list:
			for num3 in list:
				if num1 + num2 + num3 == 2020:
					return num1 * num2 * num3

file_handle = open('input.txt')
numbers = list()
for line in file_handle:
	line = line.rstrip()
	numbers.append(int(line))

print(find_num(numbers))