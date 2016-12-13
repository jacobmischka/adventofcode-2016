#!/usr/bin/env python3
'''
	Advent of code 2016 day 12
	http://adventofcode.com/2016/day/12

	ᶠᵘᶜᵏ ᵈᵃʸ ¹¹
'''

with open('inputs/12.txt') as f:
	instructions = f.read().splitlines()

def part1():
	registers = {
		'instruction_count': 0,
		'a': 0,
		'b': 0,
		'c': 0,
		'd': 0
	}

	run_instructions(registers, instructions)

	return registers['a']

def part2():
	registers = {
		'instruction_count': 0,
		'a': 0,
		'b': 0,
		'c': 1,
		'd': 0
	}

	run_instructions(registers, instructions)

	return registers['a']

def run_instructions(registers, instructions):
	while registers['instruction_count'] < len(instructions):
		args = instructions[registers['instruction_count']].split(' ')
		command = args.pop(0)
		globals()[command](registers, *args)

	return registers

def cpy(registers, val, reg):
	if val in registers.keys():
		val = registers[val]

	registers[reg] = int(val)
	registers['instruction_count'] += 1

def inc(registers, reg):
	registers[reg] += 1
	registers['instruction_count'] += 1

def dec(registers, reg):
	registers[reg] -= 1
	registers['instruction_count'] += 1

def jnz(registers, val, distance):
	if val in registers.keys():
		val = registers[val]

	if val != 0:
		registers['instruction_count'] += int(distance)
	else:
		registers['instruction_count'] += 1


if __name__ == '__main__':
	print(str(part1()))
	print(str(part2()))
