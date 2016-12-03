'''
	Advent of code day 3
	http://adventofcode.com/2016/day/3
'''

with open('inputs/3.txt') as f:
	triangles = [line for line in f]

def part1():
	num_valid = 0
	for triangle in triangles:
		sides = []
		for side in triangle.strip().split(' '):
			if len(side) > 0: sides.append(int(side))
		longest = max(sides)
		sides.remove(longest)
		others = sum(sides)
		if others > longest:
			num_valid += 1

	return num_valid

def part2():
	num_valid = 0
	rows = []
	for triangle_row in triangles:
		row = []
		for side in triangle_row.strip().split(' '):
			if len(side) > 0: row.append(int(side))
		rows.append(row)

	for y in range(3):
		i = 0
		while i < (len(rows) - 2):
			sides = [rows[i][y], rows[i + 1][y], rows[i + 2][y]]
			longest = max(sides)
			sides.remove(longest)
			others = sum(sides)
			if others > longest:
				num_valid += 1
			i += 3


	return num_valid

if __name__ == '__main__':
	print(str(part1()))
	print(str(part2()))
