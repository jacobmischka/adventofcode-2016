#!/usr/bin/env python3
'''
	Advent of code 2016 day 10
	http://adventofcode.com/2016/day/10

	Gotta just read the output and use your noggin and ctrl+f to find the answers
'''

class ChipHolder:
	type = 'output'

	def __init__(self, name):
		self.name = name
		self.chips = []

	def take(self, chip):
		self.chips.append(chip)
		self.chips.sort()

class Bot(ChipHolder):
	type = 'bot'

	def __init__(self, name):
		super().__init__(name)
		self.low_dest = None
		self.high_dest = None

	def receive_instructions(self, low_dest, high_dest):
		self.low_dest = low_dest
		self.high_dest = high_dest
		self.do_job()

	def take(self, chip):
		super().take(chip)
		self.do_job()

	def do_job(self):
		if len(self.chips) == 2 and self.low_dest and self.high_dest:
			print('bot {} giving {} to {} {} and {} to {} {}'.format(
				self.name,
				self.chips[0],
				self.low_dest.type,
				self.low_dest.name,
				self.chips[1],
				self.high_dest.type,
				self.high_dest.name
			))
			self.low_dest.take(self.chips[0])
			self.high_dest.take(self.chips[1])
			self.chips = []


with open('inputs/10.txt') as f:
	instructions = [line.strip() for line in f]

def main():
	destinations = {'bot': {}, 'output': {}}

	for instruction in instructions:
		args = instruction.split(' ')
		if args[0] == 'value':
			dest_type = args[4]
			dest_name = args[5]
			if dest_type == 'bot':
				destinations = init_holder(destinations, dest_type, dest_name)
				destinations['bot'][dest_name].take(int(args[1]))

		elif args[0] == 'bot':
			bot_name = args[1]
			low_type = args[5]
			low_name = args[6]
			high_type = args[10]
			high_name = args[11]
			destinations = init_holder(destinations, 'bot', bot_name)
			destinations = init_holder(destinations, low_type, low_name)
			destinations = init_holder(destinations, high_type, high_name)
			destinations['bot'][bot_name].receive_instructions(
				destinations[low_type][low_name],
				destinations[high_type][high_name])

def init_holder(holders, holder_type, name):
	if name not in holders[holder_type].keys():
		if holder_type == 'bot':
			holders[holder_type][name] = Bot(name)
		else:
			holders[holder_type][name] = ChipHolder(name)
	return holders

if __name__ == '__main__':
	main()
