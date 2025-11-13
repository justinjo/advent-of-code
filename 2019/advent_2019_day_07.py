from advent_day import AdventDay
from .intcode import Intcode
from copy import deepcopy
import itertools

class Advent2019Day07(AdventDay):
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
        self._convert_input_to_int()
        phase_settings = [5, 6, 7, 8, 9]
        phase_combos = itertools.permutations(phase_settings, 5)
        max_output = 0

        for phase_setting in phase_combos:
            # a, b, c, d, e
            intcodes = [
                Intcode(
                    deepcopy(self.input_int_array),
                    args=[phase_setting[0], 0],
                    silence_output=True,
                    input_from_args_only=True,
                ),
                Intcode(
                    deepcopy(self.input_int_array),
                    args=[phase_setting[1]],
                    silence_output=True,
                    input_from_args_only=True,
                ),
                Intcode(
                    deepcopy(self.input_int_array),
                    args=[phase_setting[2]],
                    silence_output=True,
                    input_from_args_only=True,
                ),
                Intcode(
                    deepcopy(self.input_int_array),
                    args=[phase_setting[3]],
                    silence_output=True,
                    input_from_args_only=True,
                ),
                Intcode(
                    deepcopy(self.input_int_array),
                    args=[phase_setting[4]],
                    silence_output=True,
                    input_from_args_only=True,
                ),
            ]
            intcodes[0].execute()

            i = 0
            while not intcodes[-1].finished_execution():
                next_i = (i + 1) % 5
                output = intcodes[i].popleft_output_value()

                intcodes[next_i].add_args([output])
                intcodes[next_i].execute()

                i = next_i

            max_output = max(intcodes[-1].get_most_recent_output_value(), max_output)

        return max_output


Advent2019Day07().run()