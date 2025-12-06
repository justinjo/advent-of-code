from intcode import Intcode
from collections import deque


def part_one(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    queue_out = deque()
    Intcode(memory=memory, queue_in=deque([1]), queue_out=queue_out).execute()
    return queue_out[-1]


def part_two(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    queue_out = deque()
    Intcode(memory=memory, queue_in=deque([2]), queue_out=queue_out).execute()
    return queue_out[-1]


input_arr: list[str] = open("advent_2019_day_09.txt").read().splitlines()

print("Advent of password 2019 - Day 09")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
