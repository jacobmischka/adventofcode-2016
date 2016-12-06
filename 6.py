#!/usr/bin/env python3
'''
	Advent of code 2016 day 6
	http://adventofcode.com/2016/day/6
'''

with open('inputs/6.txt') as f:
	messages = [line.strip() for line in f]

def part1():
	error_corrected = [{} for _ in range(8)]
	for message in messages:
		for i in range(len(message)):
			char = message[i]
			try:
				error_corrected[i][char] += 1
			except:
				error_corrected[i][char] = 1

	corrected_message = []

	for char in error_corrected:
		corrected_message.append(max(char.keys(), key=(lambda key: char[key])))

	return ''.join(corrected_message)

def part2():
	error_corrected = [{} for _ in range(8)]
	for message in messages:
		for i in range(len(message)):
			char = message[i]
			try:
				error_corrected[i][char] += 1
			except:
				error_corrected[i][char] = 1

	corrected_message = []

	for char in error_corrected:
		corrected_message.append(min(char.keys(), key=(lambda key: char[key])))

	return ''.join(corrected_message)

if __name__ == '__main__':
	print(str(part1()))
	print(str(part2()))
