#!/usr/bin/env python3
'''
	Advent of Code 2016 Day 2
	http://adventofcode.com/2016/day/2
	
	And I'm officially off the overall leaderboard already :(
'''

with open('./inputs/2.txt') as f:
	instructions = [line for line in f]


def part1():
	x = 2
	y = 2
	buttons = [
		[1, 2, 3],
		[4, 5, 6],
		[7, 8, 9]
	]
	code = []
	for line in instructions:
		for movement in line:
			if movement == 'R':
				if x < 2: x += 1
			elif movement == 'L':
				if x > 0: x -= 1
			elif movement == 'D':
				if y < 2: y += 1
			elif movement == 'U':
				if y > 0: y -= 1
		code.append(str(buttons[y][x]))

	return ''.join(code)

def part2():
	x = 0
	y = 2
	buttons = [
		[' ', ' ', '1', ' ', ' '],
		[' ', '2', '3', '4', ' '],
		['5', '6', '7', '8', '9'],
		[' ', 'A', 'B', 'C', ' '],
		[' ', ' ', 'D', ' ', ' ']
	]
	code = []
	for line in instructions:
		for movement in line:
			if movement == 'R':
				try:
					if buttons[y][x+1] != ' ':
						x += 1
				except:
					pass
			elif movement == 'L':
				try:
					if buttons[y][x-1] != ' ':
						x -= 1
				except:
					pass
			elif movement == 'D':
				try:
					if buttons[y+1][x] != ' ':
						y += 1
				except:
					pass
			elif movement == 'U':
				try:
					if buttons[y-1][x] != ' ':
						y -= 1
				except:
					pass
		code.append(str(buttons[y][x]))

	return ''.join(code)

if __name__ == '__main__':
	print(part1())
	print(part2())
