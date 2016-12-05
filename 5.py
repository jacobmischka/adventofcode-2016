#!/usr/bin/env python3
'''
	Advent of code 2016 day 5
	http://adventofcode.com/2016/day/5
'''

from hashlib import md5

with open('./inputs/5.txt') as f:
	door_id = f.readline().strip()

def part1():
	index = 0
	password = []
	while len(password) < 8:
		char_found = False
		while not char_found:
			index_hash = md5()
			index_hash.update(bytes(door_id + str(index), 'utf8'))
			digest = index_hash.hexdigest()
			if digest[:5] == '00000':
				password.append(str(digest)[5])
				char_found = True

			index += 1

	return ''.join(password)

def part2():
	index = 0
	password = ['-' for x in range(8)]
	print(password)
	for _ in range(8):
		char_found = False
		while not char_found:
			index_hash = md5()
			index_hash.update(bytes(door_id + str(index), 'utf8'))
			digest = index_hash.hexdigest()
			if digest[:5] == '00000':
				try:
					if password[int(str(digest)[5])] == '-':
						password[int(str(digest)[5])] = str(digest)[6]
						char_found = True
				except:
					pass

			index += 1

	return ''.join(password)


if __name__ == '__main__':
	print(str(part1()))
	print(str(part2()))
