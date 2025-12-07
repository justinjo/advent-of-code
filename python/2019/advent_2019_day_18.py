from collections import defaultdict
from dataclasses import dataclass

type Coord = tuple[int, int]


@dataclass
class Tile:
    coord: Coord
    value: str
    doors: list


MOVES = ((0, -1), (0, 1), (-1, 0), (1, 0))
# TILE_ORDER = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
TILE_ORDER = "abcdefghijklmnopqrstuvwxyz"


def get_tile_coords(board: list[str]) -> dict[str, set[Coord]]:
    tile_coord_map = defaultdict(set)
    for r in range(len(board)):
        for c in range(len(board[0])):
            tile_coord_map[board[r][c]].add((r, c))
    return tile_coord_map


def unlock_door(tile_map: dict[str, set[Coord]], tile) -> None:
    key = tile_map[tile].pop()
    door = tile_map[tile.upper()].pop()
    tile_map["."].update([key, door])


def blocked_keys(
    board: list[str],
    # tile_map: dict[str, set[Coord]],
    row: int,
    col: int,
) -> dict:
    steps = num_doors = 0
    queue = [((row, col), "@", [])]
    door_map: dict[Coord, Tile] = {}
    # find all keys not blocked by doors
    # remove
    while queue:
        next_queue = []
        while queue:
            coord, val, doors = queue.pop()
            tile = Tile(coord, val, doors)
            if coord in door_map:
                if door_map[coord] != tile.doors:
                    door_map[coord].doors.extend(doors)
                continue
            else:
                door_map[coord] = tile
            r, c = coord
            for r_d, c_d in MOVES:
                if 0 <= r + r_d < len(board) and 0 <= c + c_d < len(board[0]):
                    next_coord = (r + r_d, c + c_d)
                    char = board[r + r_d][c + c_d]
                    door = []
                    if char.isalpha() and char.isupper():
                        door.append(char)
                    next_queue.append((next_coord, char, door_map[coord].doors + door))
        queue = next_queue
        steps += 1
    return door_map


def find_tile(
    self, tile_map: dict[str, set[Coord]], tile: str, row: int, col: int
) -> int:
    steps = 0
    queue = [(row, col)]
    visited = set()
    found_tile = False
    while not found_tile:
        next_queue = []
        while queue:
            r, c = queue.pop()
            visited.add((r, c))
            for r_d, c_d in self.MOVES:
                next_coord = (r + r_d, c + c_d)
                if next_coord in tile_map[tile]:
                    found_tile = True
                elif next_coord not in visited and next_coord not in tile_map["#"]:
                    next_queue.append(next_coord)
        queue = next_queue
        steps += 1
    return steps


def part_one(input_arr: list[str]) -> int:
    tile_coord_map = get_tile_coords(input_arr)
    r, c = next(iter(tile_coord_map["@"]))
    steps = 0
    door_map = blocked_keys(input_arr, r, c)
    for coord in sorted(door_map):
        if (
            door_map[coord].value not in ("#", ".", "@")
            and door_map[coord].value.islower()
        ):
            print(
                f"coord: {coord}, val: {door_map[coord].value}, doors: {door_map[coord].doors}"
            )

    # for tile in self.TILE_ORDER:
    #     steps += self.find_tile(tile_coord_map, tile, r, c)
    #     # print(steps)
    #     r, c = next(iter(tile_coord_map[tile]))
    return steps


def part_two(input_arr: list[str]) -> int: ...


input_arr: list[str] = open("advent_2019_day_18.txt").read().splitlines()

print("Advent of Code 2019 - Day 18")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
