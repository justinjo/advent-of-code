from intcode import Intcode
from collections import defaultdict, deque

DIRECTIONS: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
BLACK = 0
WHITE = 1


def paint_tiles(
    memory: list[int],
    start_color: int = BLACK,
) -> dict[tuple[int, int], int]:
    dir_i = 0
    coord = (0, 0)
    tile_map: dict[tuple[int, int], int] = defaultdict(int)
    tile_map[coord] = start_color

    q_in = deque([start_color])
    q_out = deque()
    ic = Intcode(memory=memory, queue_in=q_in, queue_out=q_out)
    while not ic.finished_execution():
        ic.execute()
        tile_map[coord] = q_out.popleft()  # color painted
        dir_i += 1 if q_out.popleft() else -1  # direction change
        dir_i %= len(DIRECTIONS)
        coord = (coord[0] + DIRECTIONS[dir_i][0], coord[1] + DIRECTIONS[dir_i][1])
        q_in.append(tile_map[coord])  # color seen
    return tile_map


def print_tile_map(tile_map: dict[tuple[int, int], int]) -> None:
    min_x = min(tile_map)[0]
    max_x = max(tile_map)[0]
    min_y = min(tile_map, key=lambda c: c[1])[1]
    max_y = max(tile_map, key=lambda c: c[1])[1]
    print_str = "\n"
    for y in range(max_y, min_y - 1, -1):
        for x in range(min_x, max_x + 1):
            print_str += "#" if tile_map[(x, y)] == WHITE else " "
        print_str += "\n"
    print(print_str)


def part_one(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    return len(paint_tiles(memory))


def part_two(input_arr: list[str]) -> str:
    memory = [int(x) for x in input_arr[0].split(",")]
    print_tile_map(paint_tiles(memory, start_color=WHITE))
    return "See above"


input_arr: list[str] = open("advent_2019_day_11.txt").read().splitlines()

print("Advent of Code 2019 - Day 11")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
