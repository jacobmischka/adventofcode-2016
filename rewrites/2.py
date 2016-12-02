#!/usr/bin/env python3
'''
	Advent of Code 2016 Day 2
	http://adventofcode.com/2016/day/2

	And I'm officially off the overall leaderboard already :(
'''

from operator import add

with open('../inputs/2.txt') as f:
	instructions = [line for line in f]


def part1():
	buttons = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	return main(buttons, (1, 1))

def part2():
	buttons = [
		[' ', ' ', '1', ' ', ' '],
		[' ', '2', '3', '4', ' '],
		['5', '6', '7', '8', '9'],
		[' ', 'A', 'B', 'C', ' '],
		[' ', ' ', 'D', ' ', ' ']
	]
	return main(buttons, (0, 2))

matrices = {
	'R': (1, 0),
	'L': (-1, 0),
	'U': (0, -1),
	'D': (0, 1)
}

def main(buttons, start):
	(x, y) = start
	code = []
	for line in instructions:
		for movement in line:
			if movement in matrices:
				matrix = matrices[movement]
				(to_x, to_y) = tuple(map(add, (x, y), matrix))
				if to_x >= 0 and to_y >= 0:
					try:
						if buttons[to_y][to_x] != ' ':
							(x, y) = (to_x, to_y)
					except:
						pass
		code.append(str(buttons[y][x]))

	return ''.join(code)


if __name__ == '__main__':
	print(part1())
	print(part2())
