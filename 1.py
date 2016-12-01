#!/usr/bin/env python3
'''
	Advent of Code 2016
	Day 1

	Below is my initial implementation, I was going for speed of completion.
	I was awarded 69 points for completing both parts.
'''
i = 'L5, R1, R4, L5, L4, R3, R1, L1, R4, R5, L1, L3, R4, L2, L4, R2, L4, L1, R3, R1, R1, L1, R1, L5, R5, R2, L5, R2, R1, L2, L4, L4, R191, R2, R5, R1, L1, L2, R5, L2, L3, R4, L1, L1, R1, R50, L1, R1, R76, R5, R4, R2, L5, L3, L5, R2, R1, L1, R2, L3, R4, R2, L1, L1, R4, L1, L1, R185, R1, L5, L4, L5, L3, R2, R3, R1, L5, R1, L3, L2, L2, R5, L1, L1, L3, R1, R4, L2, L1, L1, L3, L4, R5, L2, R3, R5, R1, L4, R5, L3, R3, R3, R1, R1, R5, R2, L2, R5, L5, L4, R4, R3, R5, R1, L3, R1, L2, L2, R3, R4, L1, R4, L1, R4, R3, L1, L4, L1, L5, L2, R2, L1, R1, L5, L3, R4, L1, R5, L5, L5, L1, L3, R1, R5, L2, L4, L5, L1, L1, L2, R5, R5, L4, R3, L2, L1, L3, L4, L5, L5, L2, R4, R3, L5, R4, R2, R1, L5'

directions = ('n', 'e', 's', 'w')
def part1():
	x = 0
	y = 0
	direction_index = 0
	for step in i.split(', '):
		if step[:1] == 'L':
			direction_index = direction_index - 1
		elif step[:1] == 'R':
			direction_index = direction_index + 1
		if direction_index == -1:
			direction_index = 3
		elif direction_index == 4:
			direction_index = 0

		direction = directions[direction_index]
		blocks = int(step[1:])
		if direction == 'n':
			y += blocks
		elif direction == 's':
			y -= blocks
		elif direction == 'e':
			x += blocks
		elif direction == 'w':
			x -= blocks
		print(direction + ' ' + str(blocks))
	print(str((x, y)))
	return (abs(x) + abs(y))

def part2():
	x = 0
	y = 0
	direction_index = 0
	spot_history = []
	for step in i.split(', '):
		if step[:1] == 'L':
			direction_index = direction_index - 1
		elif step[:1] == 'R':
			direction_index = direction_index + 1
		if direction_index == -1:
			direction_index = 3
		elif direction_index == 4:
			direction_index = 0

		direction = directions[direction_index]
		blocks = int(step[1:])
		while blocks > 0:
			if direction == 'n':
				y += 1
			elif direction == 's':
				y -= 1
			elif direction == 'e':
				x += 1
			elif direction == 'w':
				x -= 1
			blocks -= 1

			if ((x, y)) in spot_history:
				print(str((x, y)))
				return (abs(x) + abs(y))

			spot_history.append((x, y))
	print(str(spot_history))

if __name__ == '__main__':
	print(str(part1()))
	print(str(part2()))
