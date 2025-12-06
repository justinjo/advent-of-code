from advent_day import AdventDay
from .intcode import Intcode
from collections import deque


class Advent2019Day09(AdventDay):

    def part_one(self) -> int:
        self._convert_input_to_int()
        queue_out = deque()
        Intcode(
            memory=self.input_int_array,
            queue_in=deque([1]),
            queue_out=queue_out,
        ).execute()
        return queue_out[-1]

    def part_two(self) -> int:
        self._convert_input_to_int()
        queue_out = deque()
        Intcode(
            memory=self.input_int_array,
            queue_in=deque([2]),
            queue_out=queue_out,
        ).execute()
        return queue_out[-1]


Advent2019Day09().run()
