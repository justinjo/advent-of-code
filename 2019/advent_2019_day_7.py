from advent_day import AdventDay
from .intcode import Intcode
from copy import deepcopy
import itertools

class Advent2019Day7(AdventDay):
    NUM_AMPS = 5

    def part_one(self) -> int:
        # 1st input: phase setting (0,1,2,3,4)
        # 2nd input: input signal
        self._convert_input_to_int()
        phase_settings = [0, 1, 2, 3, 4]
        phase_combos = itertools.permutations(phase_settings, 5)
        max_output = 0
        
        for a, b, c, d, e in phase_combos:
            intcode_a = Intcode(
                deepcopy(self.input_int_array),
                args=[a, 0],
                silence_output=True,
            )
            intcode_a.execute()

            intcode_b = Intcode(
                deepcopy(self.input_int_array),
                args=[b, intcode_a.get_most_recent_output_value()],
                silence_output=True,
            )
            intcode_b.execute()

            intcode_c = Intcode(
                deepcopy(self.input_int_array),
                args=[c, intcode_b.get_most_recent_output_value()],
                silence_output=True,
            )
            intcode_c.execute()

            intcode_d = Intcode(
                deepcopy(self.input_int_array),
                args=[d, intcode_c.get_most_recent_output_value()],
                silence_output=True,
            )
            intcode_d.execute()

            intcode_e = Intcode(
                deepcopy(self.input_int_array),
                args=[e, intcode_d.get_most_recent_output_value()],
                silence_output=True,
            )
            intcode_e.execute()

            max_output = max(intcode_e.get_most_recent_output_value(), max_output)

        return max_output

    def part_two(self) -> int:
        ...


Advent2019Day7().run()