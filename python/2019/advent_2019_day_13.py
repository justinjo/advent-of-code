from intcode import Intcode
from enum import IntEnum
from collections import defaultdict, deque
import os


class TileType(IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


TILE_TO_CHAR = {
    TileType.EMPTY: " ",
    TileType.WALL: "W",
    TileType.BLOCK: "B",
    TileType.PADDLE: "P",
    TileType.BALL: "O",
}


def print_board(tiles: dict[int, set[tuple[int, int]]], score: int) -> None:
    os.system("clear")
    board = f"score: {score}\n"
    max_x = max_y = 0
    for coord_set in tiles.values():
        if not coord_set:
            continue
        max_x = max(max(coord_set)[0], max_x)
        max_y = max(max(coord_set, key=lambda c: c[1])[1], max_y)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            for t in tiles:
                if (x, y) in tiles[t]:
                    board += TILE_TO_CHAR[t]  # type: ignore
        board += "\n"
    print(board)


def play_game(memory: list[int], silenced: bool = True) -> int:
    q_in = deque()
    q_out = deque()
    ic = Intcode(memory=memory, queue_in=q_in, queue_out=q_out)
    tiles = defaultdict(set)

    ic.execute()
    while q_out:
        x = q_out.popleft()
        y = q_out.popleft()
        tile_id = q_out.popleft()
        tiles[tile_id].add((x, y))

    score = 0
    while not ic.finished_execution():
        if not silenced:
            print_board(tiles, score)
        ic.execute()
        while q_out:
            x = q_out.popleft()
            y = q_out.popleft()
            tile_id = q_out.popleft()
            if x == -1 and y == 0:
                score = tile_id
                continue
            for coord_set in tiles.values():  # remove previous tile at (x, y)
                coord_set.discard((x, y))
            tiles[tile_id].add((x, y))

        if list(tiles[TileType.BALL])[0][0] < list(tiles[TileType.PADDLE])[0][0]:
            q_in.append(-1)
        elif list(tiles[TileType.BALL])[0][0] == list(tiles[TileType.PADDLE])[0][0]:
            q_in.append(0)
        else:
            q_in.append(1)

    if not silenced:
        print_board(tiles, score)
    return score


def part_one(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    q_out = deque()
    Intcode(memory=memory, queue_out=q_out).execute()
    tiles = defaultdict(set)
    while q_out:
        x = q_out.popleft()
        y = q_out.popleft()
        tile_id = q_out.popleft()
        tiles[tile_id].add((x, y))
    return len(tiles[TileType.BLOCK])


def part_two(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    return play_game([2] + memory[1:], silenced=True)


input_arr: list[str] = open("advent_2019_day_13.txt").read().splitlines()

print("Advent of Code 2019 - Day 13")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
