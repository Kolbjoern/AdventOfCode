import sys

def createDecks(inp):
	players, currentPlayer = {}, ''
	for line in inp:
		if line == "": continue
		if line.startswith('Player'):
			currentPlayer = line.split()[1].replace(':','')
			players[currentPlayer] = []
			continue

		players[currentPlayer].append(int(line))

	return players

def play(player1, player2):
	prevGames = {}
	while True:
		if len(player1) == 0: return '2'
		if len(player2) == 0: return '1'

		game = tuple([tuple(player1), tuple(player2)])
		if game in prevGames: return '1'
		prevGames[game] = True

		num1 = player1.pop(0)
		num2 = player2.pop(0)

		if len(player1) >= num1 and len(player2) >= num2:
			if play(player1[:num1], player2[:num2]) == '1':
				player1 += [num1, num2]
			else:
				player2 += [num2, num1]
			continue

		if num1 > num2:
			player1 += [num1, num2]
		elif num2 > num1:
			player2 += [num2, num1]

	return ''

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	players = createDecks(inp)
	winner = play(players['1'], players['2'])

	return sum([n * (len(players[winner]) - i) for i, n in enumerate(players[winner])])

if __name__ == '__main__':
	print(main(sys.argv[1:]))