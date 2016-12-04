'''
	Advent of Code 2016 day 4
	http://adventofcode.com/2016/day/4

	For part 2, need to manually look in output for the room involving
	"North Pole object storage", name was "northpole object storage" for me.
	Unsure if it's always that or what.
'''

from collections import OrderedDict

with open('inputs/4.txt') as f:
	rooms = [line for line in f]

alphabet = [letter for letter in 'abcdefghijklmnopqrstuvwxyz']

def part1():
	sector_ids = []
	for room in rooms:
		letter_map = OrderedDict()
		for piece in room.split('-'):
			if '[' in piece:
				sector_id = int(piece.split('[')[0])
				checksum = piece.split('[')[1][:-2]
			else:
				for letter in piece:
					try:
						letter_map[letter] += 1
					except:
						letter_map[letter] = 1

		letter_map = OrderedDict(sorted(letter_map.items()))

		valid = True
		for i in range(5):
			next_max = max(letter_map.keys(), key=(lambda key: letter_map[key]))
			del letter_map[next_max]
			if checksum[i] != next_max:
				valid = False
		if valid:
			sector_ids.append(sector_id)

	return sum(sector_ids)

def part2():
	real_rooms = []
	for room in rooms:
		letter_map = OrderedDict()
		for piece in room.split('-'):
			if '[' in piece:
				sector_id = int(piece.split('[')[0])
				checksum = piece.split('[')[1][:-2]
			else:
				for letter in piece:
					try:
						letter_map[letter] += 1
					except:
						letter_map[letter] = 1

		letter_map = OrderedDict(sorted(letter_map.items()))

		valid = True
		for i in range(5):
			next_max = max(letter_map.keys(), key=(lambda key: letter_map[key]))
			del letter_map[next_max]
			if checksum[i] != next_max:
				valid = False
		if valid:
			real_rooms.append(room)

	for room in real_rooms:
		name = []
		for piece in room.split('-'):
			if '[' in piece:
				sector_id = int(piece.split('[')[0])
				checksum = piece.split('[')[1][:-2]
			else:
				name.append(piece)
		array_name = []
		for word in name:
			array_name.append([letter for letter in word])

		for word in array_name:
			for word_index in range(len(word)):
				letter_index = alphabet.index(word[word_index])
				for i in range(sector_id):
					letter_index = 0 if letter_index == len(alphabet) - 1 else letter_index + 1
				word[word_index] = alphabet[letter_index]

		str_name = ''
		for word in array_name:
			str_name += ''.join(word) + ' '

		print(str_name + ': ' + str(sector_id))


if __name__ == '__main__':
	print(str(part1()))
	part2()
