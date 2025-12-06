from collections import Counter

def parse_input(input_arr: list[str]) -> tuple[list[int], list[int]]:
    left = []
    right = []
    for l in input_arr:
        l, r = l.split('   ')
        left.append(int(l))
        right.append(int(r))
    return (left, right)

def part_one(input_arr: list[str]) -> int:
    left, right = parse_input(input_arr)
    distance = 0
    for l, r in zip(sorted(left), sorted(right)):
        distance += abs(r - l)
    return distance

def part_two(input_arr: list[str]) -> int:
    left, right = parse_input(input_arr)
    c = Counter(right)
    similarity = 0
    for l in left:
        similarity += l * c[l]
    return similarity

input_arr: list[str] = open('advent_2024_day_01.txt').read().splitlines()

print('Advent of Code 2024 - Day 01')
print(f'Part One: {part_one(input_arr)}')
print(f'Part Two: {part_two(input_arr)}')