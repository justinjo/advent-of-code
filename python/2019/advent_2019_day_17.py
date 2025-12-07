from intcode import Intcode
from collections import deque


INTERSECTION_NEIGHBORS = ((0, -1), (0, 1), (-1, 0), (1, 0))


def is_intersection(arr: list[str], row: int, col: int) -> bool:
    neighbors = 0
    if arr[row][col] != "#":
        return False
    for r_d, c_d in INTERSECTION_NEIGHBORS:
        if 0 <= row + r_d < len(arr) and 0 <= col + c_d < len(arr[0]):
            neighbors += 1 if arr[row + r_d][col + c_d] == "#" else 0
    return neighbors == 4


def part_one(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    q_out = deque()
    Intcode(memory=memory, queue_out=q_out).execute()
    lines = []
    line = ""
    alignment_sum = 0
    for val in q_out:
        if val == 10 and line:
            lines.append(line)
            line = ""
        else:
            line += chr(val)
    for r in range(len(lines)):
        for c in range(len(lines[0])):
            if is_intersection(lines, r, c):
                alignment_sum += r * c
    return alignment_sum


def part_two(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    q_in = deque()
    q_out = deque()
    ic = Intcode(memory=[2] + memory[1:], queue_in=q_in, queue_out=q_out)
    routine = [ord(c) for c in list("A,B,A,C,B,C,A,B,A,C\n")]
    func_a = [ord(c) for c in list("R,6,L,10,R,8,R,8\n")]
    func_b = [ord(c) for c in list("R,12,L,8,L,10\n")]
    func_c = [ord(c) for c in list("R,12,L,10,R,6,L,10\n")]
    feed = [ord("n"), ord("\n")]
    q_in.extend(routine + func_a + func_b + func_c + feed)
    ic.execute()
    return q_out[-1]


input_arr: list[str] = open("advent_2019_day_17.txt").read().splitlines()

print("Advent of Code 2019 - Day 17")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
