from advent_day import AdventDay
from collections import Counter

class Advent2020Day10(AdventDay):

    def part_one(self) -> int:
        self._convert_input_to_int()
        sorted_input = sorted(self.input_int_array)
        jump_count = Counter()
        jump_count[sorted_input[0]] += 1 # jump from outlet (0) to adapter
        for i in range(self.input_length - 1):
            jump_count[sorted_input[i+1] - sorted_input[i]] += 1
        jump_count[3] += 1 # jump from last outlet to device's adapter
        return jump_count[1] * jump_count[3]

    def part_two(self) -> int:
        sorted_input = sorted(self.input_int_array)
        dp_arr = [0] * self.input_length
        for i in range(self.input_length - 1):
            if sorted_input[i] <= 3:
                dp_arr[i] += 1 # jump from the outlet
            j = i + 1
            while (
                j < self.input_length
                and 1 <= (sorted_input[j] - sorted_input[i]) <= 3
            ):
                dp_arr[j] += dp_arr[i]
                j += 1
        return dp_arr[-1]


Advent2020Day10().run()