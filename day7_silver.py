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

def search_bag(bag, find):
	for bag_name in bag:
		if bag_name in find:
			return True

	return False

def find_bag(bags, find):
	total = dict()
	found_in = []
	for bag_name in bags:
		for bag in bags[bag_name]:
			if search_bag(bag, find):
				found_in.append(bag_name)
				total[bag_name] = 1
				
	return total, found_in

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append(line.rstrip())

	bags = create_bag_list(inp)
	total = dict()
	find = ['shiny gold']

	while len(find) > 0:
		res, find = find_bag(bags, find)
		total = {**total, **res}

	print(len(total))

if __name__ == '__main__':
	main(sys.argv[1:])