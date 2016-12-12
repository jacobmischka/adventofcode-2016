#!/usr/bin/env python3
'''

'''
from copy import deepcopy
from itertools import combinations
from multiprocessing import JoinableQueue, Lock, Process
from time import sleep

NUM_THREADS = 4

def move_things(start_state, things, new_floor):
	state = deepcopy(start_state)

	for item in things:
		state['floors'][state['elevator_floor']].remove(item)
		state['floors'][new_floor].append(item)

	state['elevator_floor']	= new_floor
	state['count'] += 1

	return state


def is_valid(state, prev_state):
	if prev_state and state['floors'][state['elevator_floor']] == prev_state['floors'][state['elevator_floor']]:
		return False

	for floor in state['floors']:
		chips = []
		generators = []
		for item in floor:
			(element, kind) = item.split(' ')
			if kind == 'generator':
				generators.append(element)
			elif kind == 'microchip':
				chips.append(element)

		if len(generators) > 0:
			for element in chips:
				if element not in generators:
					return False

	return True


def worker(q, l):
	while True:
		if q.empty():
			sleep(1)
			continue
		(state, prev_state) = q.get()

		current_floor = state['elevator_floor']
		if len(state['floors'][-1]) == num_things:
			l.acquire()
			print('*****************{}****************'.format(state['count']))
			print(str(state))
			l.release()

		else:
			combos = list(combinations(state['floors'][current_floor], 2))
			for item in state['floors'][current_floor]:
				combos.append([item])

			for combo in combos:
				reason_to_go_down = False
				lower_floor = current_floor - 1
				while lower_floor >= 0:
					if len(state['floors'][lower_floor]) > 0:
						reason_to_go_down = True
					lower_floor -= 1

				if reason_to_go_down:
					low_state = move_things(state, combo, current_floor - 1)
					if is_valid(low_state, prev_state):
						q.put((low_state, state))
				if current_floor < len(state['floors']) - 1:
					high_state = move_things(state, combo, current_floor + 1)
					if is_valid(high_state, prev_state):
						q.put((high_state, state))

		q.task_done()

if __name__ == '__main__':
	num_things = 0
	initial_state = {
		'count': 0,
		'elevator_floor': 0,
		'floors': []
	}

	with open('inputs/11.txt') as f:
		for line in f:
			line = line.strip()
			if 'contains nothing relevant' in line:
				initial_state['floors'].append([])
				continue
			things_str = line[line.find('contains') + len('contains'):]
			floor_things = things_str.split(', ')
			floor_things = [thing.strip('and .').replace('-compatible', '') for thing in floor_things]
			floor = []
			for thing in floor_things:
				num_things += 1
				floor.append(thing)
			initial_state['floors'].append(floor)

	lock = Lock()
	queue = JoinableQueue()
	queue.put((initial_state, False))

	workers = []
	for _ in range(NUM_THREADS):
		p = Process(target=worker, args=(queue,lock))
		workers.append(p)
		p.start()

	print(str(initial_state))
	print(str(num_things))

	queue.join()
