#!/usr/bin/env python3
'''
    Advent of Code 2016 Day 1
    http://adventofcode.com/2016/day/1
    A little better this time
'''

from collections import deque
from operator import add

matrices = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
with open('../inputs/1.txt') as f:
    steps = f.readline().split(', ')

def part1():
    pos = (0, 0)
    for step in steps:
        moves = get_moves(step)
        while len(moves):
            pos = move(pos, moves.pop())
    return get_distance(pos)

def part2():
    pos = (0, 0)
    history = []
    for step in steps:
        moves = get_moves(step)
        while len(moves):
            pos = move(pos, moves.pop())
            if pos in history:
                return get_distance(pos)
            history.append(pos)

def get_moves(step):
    turn = step[:1]
    dist = int(step[1:])
    matrices.rotate(1 if turn == 'R' else -1)
    return [matrices[0] for x in range(dist)]

def move(pos, matrix):
    return tuple(map(add, pos, matrix))

def get_distance(pos):
    print(str(pos))
    return sum(tuple(map(abs, pos)))

if __name__ == '__main__':
    print(str(part1()))
    print(str(part2()))
