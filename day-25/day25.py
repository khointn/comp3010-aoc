### day 25

import re
from functools import reduce


def coord_to_count(row, col):
    # calculate the ordinal of the given coordinates, counting from 1
    return ((col + row - 2) * (col + row - 1) // 2) + col


def calculate_code(row, col):
    count = coord_to_count(row, col)
    return reduce(lambda c, i: c * 252533 % 33554393, range(count - 1), 20151125)


if __name__ == '__main__':
    import sys
    filename = r'C:\Users\nguye\comp3010-aoc\day-25\day25input.txt'
    with open(filename) as f:
        line = next(f)
        row, col = map(int, re.search(r'row (\d+), column (\d+)', line).groups())

    print('Part 1:', calculate_code(row, col))