from advent_day import AdventDay
from .intcode import Intcode
from copy import deepcopy

class Advent2019Day05(AdventDay):

    def part_one(self) -> str:
        self._convert_input_to_int()
        Intcode(deepcopy(self.input_int_array)).execute()
        return 'Program Terminated'

    def part_two(self) -> str:
        self._convert_input_to_int()
        Intcode(deepcopy(self.input_int_array)).execute()
        return 'Program Terminated'


Advent2019Day05().run()