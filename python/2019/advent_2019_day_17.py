from intcode import Intcode
from collections import deque

DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))  # (row, col)
SHIP_TO_DIRECTION = {
    "^": 0,
    ">": 1,
    "v": 2,
    "<": 3,
}


def get_scaffold_map(ic_program: list[int]) -> list[str]:
    q_out = deque()
    Intcode(memory=ic_program, queue_out=q_out).execute()
    map_string = "".join([chr(val) for val in q_out])
    return [line for line in map_string.split("\n") if line]


def is_intersection(arr: list[str], row: int, col: int) -> bool:
    num_neighbors = 0
    for r, c in DIRECTIONS:
        if 0 <= row + r < len(arr) and 0 <= col + c < len(arr[0]):
            num_neighbors += 1 if arr[row + r][col + c] == "#" else 0
    return arr[row][col] == "#" and num_neighbors == 4


def get_scaffold_set(scaffold_map: list[str]) -> set[tuple[int, int]]:
    scaffold_set = set()
    for row in range(len(scaffold_map)):
        for col in range(len(scaffold_map[0])):
            if scaffold_map[row][col] == "#":
                scaffold_set.add((row, col))
    return scaffold_set


def get_starting_coord(arr: list[str]) -> tuple[int, int]:
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            if arr[row][col] in ("^", ">", "v", "<"):
                return (row, col)
    return (-1, -1)


def get_next_turn(
    scaffold_set: set[tuple[int, int]], row: int, col: int, direction_index: int
) -> str:
    next_turn = "END"
    left_r, left_c = DIRECTIONS[(direction_index - 1) % len(DIRECTIONS)]
    right_r, right_c = DIRECTIONS[(direction_index + 1) % len(DIRECTIONS)]
    if (row + left_r, col + left_c) in scaffold_set:
        next_turn = "L"
    if (row + right_r, col + right_c) in scaffold_set:
        next_turn = "R"
    return next_turn


def get_path(arr: list[str]) -> str:
    path = ""
    row, col = get_starting_coord(arr)
    dir_i = SHIP_TO_DIRECTION[arr[row][col]]
    scaffold_set = get_scaffold_set(arr)
    next_turn = get_next_turn(scaffold_set, row, col, dir_i)
    while next_turn != "END":
        path += next_turn
        if next_turn == "R":
            dir_i = (dir_i + 1) % len(DIRECTIONS)
        else:  # next_turn == "L"
            dir_i = (dir_i - 1) % len(DIRECTIONS)
        r, c = DIRECTIONS[dir_i]
        steps = 0
        while (row + r, col + c) in scaffold_set:
            steps += 1
            row += r
            col += c
        path += str(steps) + ","
        next_turn = get_next_turn(scaffold_set, row, col, dir_i)

    return path[:-1]  # trim final comma


def part_one(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    scaffold_map = get_scaffold_map(memory)
    alignment_sum = 0
    for row in range(len(scaffold_map)):
        for col in range(len(scaffold_map[0])):
            if is_intersection(scaffold_map, row, col):
                alignment_sum += row * col
    return alignment_sum


def part_two(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    scaffold_map = get_scaffold_map(memory)
    path = get_path(scaffold_map)

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
