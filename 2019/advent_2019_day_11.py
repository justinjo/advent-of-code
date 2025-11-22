from advent_day import AdventDay
from .intcode import Intcode
from collections import defaultdict

class Tile:
    BLACK = 0
    WHITE = 1

    def __init__(self, color: int = BLACK) -> None:
        self.color = color
        self.history = []

    def paint(self, color: int) -> None:
        self.history.append(self.color)
        self.color = color

    def was_painted(self) -> bool:
        return bool(self.history)


class Advent2019Day11(AdventDay):
    DIRECTIONS: list[tuple[int, int]] = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    def paint_tiles(self, start_color: int = Tile.BLACK) -> dict[tuple[int, int], Tile]:
        x = y = dir_i = 0
        tile_map = defaultdict(Tile)
        tile_map[(x, y)] = Tile(start_color)
        ic = Intcode(
            memory=self.input_int_array,
            args=[start_color],
            silence_output=True,
            input_from_args_only=True,
        )
        while not ic.finished_execution():
            ic.execute()
            color = ic.popleft_output_value()
            tile = tile_map[(x, y)]
            tile.paint(color)
            # change directions and add args
            dir_change = 1 if ic.popleft_output_value() else -1
            dir_i = (dir_i + dir_change) % len(self.DIRECTIONS)
            x += self.DIRECTIONS[dir_i][0]
            y += self.DIRECTIONS[dir_i][1]
            ic.add_args([tile_map[(x, y)].color])
        return tile_map

    def part_one(self) -> int:
        self._convert_input_to_int()
        return len([t for t in self.paint_tiles().values() if t.was_painted()])

    def part_two(self) -> str:
        ...


Advent2019Day11().run()