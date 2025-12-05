from advent_day import AdventDay
from .intcode import Intcode
from enum import IntEnum
from collections import defaultdict, deque
import os

class TileType(IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


class Advent2019Day13(AdventDay):

    TILE_TO_CHAR = {
        TileType.EMPTY: ' ',
        TileType.WALL: 'W',
        TileType.BLOCK: 'B',
        TileType.PADDLE: 'P',
        TileType.BALL: 'O',
    }

    def print_board(self, tiles: dict[int, set[tuple[int, int]]], score: int) -> None:
        os.system('clear')
        print(f'score: {score}')
        max_x = max_y = 0
        for li in tiles.values():
            if not li:
                continue
            max_x = max(sorted(li, key=lambda l: l[0])[-1][0], max_x)
            max_y = max(sorted(li, key=lambda l: l[1])[-1][1], max_y)
        for y in range(max_y + 1):
            tube = '' # CRT
            for x in range(max_x + 1):
                for t in tiles:
                    if (x, y) in tiles[t]:
                        tube += self.TILE_TO_CHAR[t] # type: ignore
            print(tube)

    def remove_tile(self, tiles: dict[int, set[tuple[int, int]]], x: int, y: int) -> None:
        for li in tiles.values():
            if (x, y) in li:
                li.remove((x, y))

    def part_one(self) -> int:
        self._convert_input_to_int()
        q_in = deque()
        q_out = deque()
        ic = Intcode(
            memory=self.input_int_array,
            queue_in=q_in,
            queue_out=q_out,
        )
        ic.execute()
        block_set = set()
        while q_out:
            x = q_out.popleft()
            y = q_out.popleft()
            tile_id = q_out.popleft()
            if tile_id == TileType.BLOCK:
                block_set.add((x, y))
        return len(block_set)

    def part_two(self) -> int:
        self._convert_input_to_int()
        q_in = deque()
        q_out = deque()
        ic = Intcode(
            memory=[2] + self.input_int_array[1:], # quarter hack
            queue_in=q_in,
            queue_out=q_out,
        )
        tiles = defaultdict(set)

        ic.execute()
        while q_out:
            x = q_out.popleft()
            y = q_out.popleft()
            tile_id = q_out.popleft()
            tiles[tile_id].add((x, y))

        score = 0
        while not ic.finished_execution():
            self.print_board(tiles, score)
            ic.execute()
            while q_out:
                x = q_out.popleft()
                y = q_out.popleft()
                tile_id = q_out.popleft()
                if x == -1 and y == 0:
                    score = tile_id
                    continue
                self.remove_tile(tiles, x, y)
                if tile_id == TileType.BALL or tile_id == TileType.PADDLE:
                    tiles[tile_id] = set([(x, y)])
                else:
                    tiles[tile_id].add((x, y))

            if list(tiles[TileType.BALL])[0][0] < list(tiles[TileType.PADDLE])[0][0]:
                q_in.append(-1)
            elif list(tiles[TileType.BALL])[0][0] == list(tiles[TileType.PADDLE])[0][0]:
                q_in.append(0)
            else:
                q_in.append(1)
        self.print_board(tiles, score)
        return score


Advent2019Day13().run()