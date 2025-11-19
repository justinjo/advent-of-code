from advent_day import AdventDay

class Advent2023Day01(AdventDay):
    number_strs = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    def get_number_str(self, s: str, i: int) -> str:
        for num in self.number_strs:
            if num == s[i:i+len(num)]:
                return self.number_strs[num]
        return ''

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
        calibration_sum = 0
        for s in self.input_str_array:
            first_digit = ''
            last_digit = ''
            for i in range(len(s)):
                digit = s[i] if s[i].isnumeric() else self.get_number_str(s, i)
                if digit:
                    if not first_digit:
                        first_digit = digit
                    last_digit = digit
            calibration_sum += int(first_digit + last_digit)
        return calibration_sum


Advent2023Day01().run()