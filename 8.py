#!/usr/bin/env python3
'''
	Advent of code day 8
	http://adventofcode.com/2016/day/8
'''
from collections import deque

with open('inputs/8.txt') as f:
	instructions = [line.strip() for line in f]

def part1():
	pixels = deque([deque(['.' for _ in range(6)]) for _ in range(50)])
	for instruction in instructions:
		pixels = do_instruction(pixels, instruction)

	num_lit = 0
	for col in pixels:
		for row in col:
			for pixel in row:
				if pixel == '#':
					num_lit += 1
	return num_lit

def part2():
	pixels = deque([deque(['.' for _ in range(6)]) for _ in range(50)])
	for instruction in instructions:
		pixels = do_instruction(pixels, instruction)

	print_screen(pixels)

def do_instruction(screen, instruction):
	words = instruction.split(' ')
	if words[0] == 'rect':
		(a, b) = words[1].split('x')
		return rect(screen, int(a), int(b))
	elif words[0] == 'rotate':
		a = int(words[2][2:])
		b = int(words[-1])
		if words[1] == 'row':
			return rotate_row(screen, a, b)
		elif words[1] == 'column':
			return rotate_column(screen, a, b)

def rect(screen, row, col):
	for x in range(row):
		for y in range(col):
			screen[x][y] = '#'
	return screen

def rotate_column(screen, col, dist):
	screen[col].rotate(dist)
	return screen

def rotate_row(screen, row, dist):
	d = deque()
	for col in range(len(screen)):
		d.append(screen[col][row])
	d.rotate(dist)
	for col in range(len(screen)):
		screen[col][row] = d[col]

	return screen

def print_screen(screen):
	rotated = [['.' for _ in range(50)] for _ in range(6)]
	for x in range(len(screen)):
		for y in range(len(screen[x])):
			rotated[y][x] = screen[x][y]

	print(' ', end='')
	for x in range(50):
		print(str(x).rjust(2)[1:2], end='')
	print()
	y = 0
	for col in rotated:
		print(y, end='')
		y += 1
		for row in col:
			for pixel in row:
				print(pixel, end='')
		print()

if __name__ == '__main__':
	print(str(part1()))
	part2()
