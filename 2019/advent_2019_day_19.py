from advent_day import AdventDay
from .intcode import Intcode
from collections import deque

class Advent2019Day19(AdventDay):

    def part_one(self) -> int:
        self._convert_input_to_int()
        q_out = deque()
        for x in range(50):
            for y in range(50):
                Intcode(memory=self.input_int_array, queue_in=deque([x, y]), queue_out=q_out).execute()
        return sum(q_out)

    def part_two(self) -> int:
        ...


Advent2019Day19().run()