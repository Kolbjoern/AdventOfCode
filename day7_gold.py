import sys

def create_bag_list(bag_str):
	strip_list = ['bags','bag','no', 'other', 'bags.', 'bag.']
	bags = dict()
	for line in bag_str:
		bag, rest = line.strip().split('bags contain')
		contains = rest.strip().split(',')
		bags[bag.strip()] = []
		for bagList in contains:
			bag_split = [word for word in bagList.split() if word not in strip_list]
			if bag_split:
				sub_bag = dict()
				sub_bag[' '.join(bag_split[1:])] = bag_split[0]
				bags[bag.strip()].append(sub_bag)

	return bags

def find_new(bags, find):
	total = 0
	found_in = []
	for bag_name in bags:
		for bag_tuple in find:
			key, value = bag_tuple
			if bag_name in key:
				for bag in bags[bag_name]:
					for name in bag:
						num = int(bag[name]) * value
						total += num
						found_in.append((name, num))

	return total, found_in

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append(line.rstrip())

	bags = create_bag_list(inp)
	total = 0
	find = [('shiny gold', 1)]
	while len(find) > 0:
		res, find = find_new(bags, find)
		total += res

	print(total)

if __name__ == '__main__':
	main(sys.argv[1:])