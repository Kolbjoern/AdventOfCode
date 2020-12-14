import sys
import math

def moveWaypoint(direction, steps, x, y):
	if direction == 'N':
		y -= steps
	if direction == 'S':
		y += steps
	if direction == 'E':
		x += steps
	if direction == 'W':
		x -= steps

	return x, y

def moveShip(steps, x, y, xW, yW):
	x += steps * xW
	y += steps * yW
	return x, y

def turn(direction, degrees, xW, yW):
	modifierX = -1 if direction == 'R' else 1
	modifierY = -1 if direction == 'L' else 1
	
	for i in range(0, degrees//90):
		xt = xW
		xW = yW * modifierX
		yW = xt * modifierY

	return xW, yW

def rotate(direction, targetX, targetY, angle):
	sin = math.sin(math.radians(angle))
	cos = math.cos(math.radians(angle))

	if direction == 'R':
		newX = targetX * cos - targetY * sin
		newY = targetX * sin + targetY * cos
	else:
		newX = targetX * cos + targetY * sin
		newY = -targetX * sin + targetY * cos

	return round(newX), round(newY)

def main(argv):
	file = "input.txt" if not argv else argv[0]
	inp = list()
	for line in open(file):
		inp.append((line.rstrip()))

	xW, yW = 10, -1
	x, y = 0, 0
	for line in inp:
		action = line[0]
		num = int(line[1:])

		if action == 'F':
			x, y = moveShip(num, x, y, xW, yW)
		elif action in 'RL':
			xW, yW = rotate(action, xW, yW, num)
		else:
			xW, yW = moveWaypoint(action, num, xW, yW)

	return abs(x) + abs(y)

if __name__ == '__main__':
	print(main(sys.argv[1:]))