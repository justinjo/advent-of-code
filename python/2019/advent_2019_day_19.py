from intcode import Intcode
from collections import deque


def print_beam(memory: list[int], rows: int, cols: int) -> None:
    q_out = deque()
    beamed = set()
    for y in range(cols):
        for x in range(rows):
            Intcode(memory=memory, queue_in=deque([x, y]), queue_out=q_out).execute()
            if q_out.popleft():
                beamed.add((x, y))
    max_x, max_y = sorted(list(beamed))[-1]
    beam = ""
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            beam += "#" if (x, y) in beamed else "."
        beam += "\n"
    print(beam)


def part_one(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    q_out = deque()
    for x in range(50):
        for y in range(50):
            Intcode(memory=memory, queue_in=deque([x, y]), queue_out=q_out).execute()
    return sum(q_out)


def part_two(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    q_out = deque()
    x = val = 0
    y = 50  # start past 0, where the beam is contiguous
    while not val:
        # find first column (x) in row (y) affected by beam
        Intcode(memory=memory, queue_in=deque([x, y]), queue_out=q_out).execute()
        while not q_out[-1]:
            x += 1
            Intcode(memory=memory, queue_in=deque([x, y]), queue_out=q_out).execute()

        # check square corners on right side
        Intcode(memory=memory, queue_in=deque([x + 99, y]), queue_out=q_out).execute()
        Intcode(
            memory=memory, queue_in=deque([x + 99, y - 99]), queue_out=q_out
        ).execute()
        if q_out[-2] == q_out[-1] == 1:
            val = (x * 10000) + (y - 99)
        y += 1
    return val


input_arr: list[str] = open("advent_2019_day_19.txt").read().splitlines()

print("Advent of Code 2019 - Day 19")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
