from advent_day import AdventDay
from .intcode import Intcode
from copy import deepcopy

class Advent2019Day09(AdventDay):

    def part_one(self) -> int:
        self._convert_input_to_int()
        ic = Intcode(deepcopy(self.input_int_array))
        ic.execute()
        return ic.get_most_recent_output_value()

    def part_two(self) -> int:
        ic = Intcode(deepcopy(self.input_int_array))
        ic.execute()
        return ic.get_most_recent_output_value()


Advent2019Day09().run()