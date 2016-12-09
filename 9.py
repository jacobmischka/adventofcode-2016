#!/usr/bin/env python3
'''
	Advent of code 2016 day 9
	http://adventofcode.com/2016/day/9
'''

with open('inputs/9.txt') as f:
	contents = f.readline().strip()

def part1():
	return len(decompress_chunk_v1(contents))

def part2():
	return compute_chunk_length_v2(contents)

def decompress_chunk_v1(chunk):
	output = ''
	num_chars = -1
	times = 1
	repeat_substr = ''
	i = 0
	while i < len(chunk):
		if num_chars > 0:
			repeat_substr += chunk[i]
			num_chars -= 1
		else:
			if len(repeat_substr) > 0:
				for _ in range(times):
					output += repeat_substr
				repeat_substr = ''
			char = chunk[i]
			if char != '(':
				output += char
			else:
				marker = ''
				i += 1
				char = chunk[i]
				while char != ')':
					marker += char
					i += 1
					char = chunk[i]
				(num_chars, times) = marker.split('x')
				num_chars = int(num_chars)
				times = int(times)
		i += 1
	if len(repeat_substr) > 0:
		for _ in range(times):
			output += repeat_substr

	return output

def compute_chunk_length_v2(chunk):
	length = 0
	num_chars = -1
	times = 1
	repeat_substr = ''
	i = 0
	while i < len(chunk):
		if num_chars > 0:
			repeat_substr += chunk[i]
			num_chars -= 1
		else:
			if len(repeat_substr) > 0:
				if '(' in repeat_substr:
					repeat_substr_length = compute_chunk_length_v2(repeat_substr)
				else:
					repeat_substr_length = len(repeat_substr)
				length += repeat_substr_length * times
				repeat_substr = ''
			char = chunk[i]
			if char != '(':
				length += 1
			else:
				marker = ''
				i += 1
				char = chunk[i]
				while char != ')':
					marker += char
					i += 1
					char = chunk[i]
				(num_chars, times) = marker.split('x')
				num_chars = int(num_chars)
				times = int(times)
		i += 1
	if len(repeat_substr) > 0:
		if '(' in repeat_substr:
			repeat_substr_length = compute_chunk_length_v2(repeat_substr)
		else:
			repeat_substr_length = len(repeat_substr)
		length += repeat_substr_length * times
		repeat_substr = ''

	return length


if __name__ == '__main__':
	print(str(part1()))
	print(str(part2()))
