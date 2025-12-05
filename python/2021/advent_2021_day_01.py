from advent_day import AdventDay

class Advent2021Day01(AdventDay):

    def part_one(self) -> int:
        self._convert_input_to_int()
        increases = 0
        for i in range(1, self.input_length):
            if self.input_int_array[i-1] <  self.input_int_array[i]:
                increases += 1
        return increases

    def part_two(self) -> int:
        # self._convert_input_to_int()
        increases = prev_sum = 0
        for i in range(3, self.input_length):
            if self.input_int_array[i-3] <  self.input_int_array[i]:
                increases += 1
        return increases

Advent2021Day01().run()