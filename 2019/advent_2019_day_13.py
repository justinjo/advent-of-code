from advent_day import AdventDay
from .intcode import Intcode
from enum import Enum

class TileType(Enum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    HORIZONTAL_PADDLE = 3
    BALL = 4


class Advent2019Day13(AdventDay):


    def part_one(self) -> int:
        self._convert_input_to_int()
        ic = Intcode(memory=self.input_int_array, silence_output=True)
        ic.execute()
        block_set = set()
        while ic.output_values:
            x = ic.popleft_output_value()
            y = ic.popleft_output_value()
            tile_id = ic.popleft_output_value()
            if tile_id == TileType.BLOCK.value:
                block_set.add((x, y))
        return len(block_set)

    def part_two(self) -> int:
        ...


Advent2019Day13().run()