#!/usr/bin/env python3
'''
	Advent of code 2016 day 7
	http://adventofcode.com/2016/day/7
'''

with open('inputs/7.txt') as f:
	addresses = [line for line in f]

def part1():
	tls_addresses = []
	for address in addresses:
		is_tls = False
		in_brackets = False
		for i in range(len(address) - 4):
			if address[i] == '[':
				in_brackets = True
			elif address[i] == ']':
				in_brackets = False
			elif address[i] == address[i+3] and address[i+1] == address[i+2] and address[i] != address[i+1]:
				if in_brackets:
					is_tls = False
					break
				else:
					is_tls = True
		if is_tls:
			tls_addresses.append(address)

	return len(tls_addresses)

def part2():
	ssl_addresses = []
	for address in addresses:
		in_brackets = False
		combos = {True: [], False: []}
		for i in range(len(address) - 3):
			if address[i] == '[':
				in_brackets = True
			elif address[i] == ']':
				in_brackets = False
			else:
				if address[i] == address[i+2] and address[i] != address[i+1]:
					if (address[i+1] + address[i] + address[i+1]) in combos[not in_brackets]:
						ssl_addresses.append(address)
						break
					combos[in_brackets].append(address[i:i+3])

	return len(ssl_addresses)

if __name__ == '__main__':
	print(str(part1()))
	print(str(part2()))
