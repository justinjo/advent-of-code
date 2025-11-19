from advent_day import AdventDay

class Advent2023Day01(AdventDay):

    def part_one(self) -> int:
        calibration_sum = 0
        for s in self.input_str_array:
            first_digit = ''
            last_digit = ''
            for c in s:
                if c.isnumeric():
                    if not first_digit:
                        first_digit = c
                    last_digit = c
            calibration_sum += int(first_digit + last_digit)
        return calibration_sum

    def part_two(self) -> int:
        ...


Advent2023Day01().run()