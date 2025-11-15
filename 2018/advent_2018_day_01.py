from advent_day import AdventDay

class Advent2018Day01(AdventDay):

    def part_one(self) -> int:
        self._convert_input_to_int()
        return sum(self.input_int_array)

    def part_two(self) -> int:
        seen = set()
        freq = i = 0
        while freq not in seen:
            seen.add(freq)
            freq += self.input_int_array[i]
            i = (i + 1) % self.input_length
        return freq


Advent2018Day01().run()