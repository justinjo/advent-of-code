from advent_day import AdventDay

class Advent2017Day01(AdventDay):

    def part_one(self) -> int:
        captcha_sum = 0
        input_str = self.input_str_array[0]
        for i in range(len(input_str)):
            if input_str[i-1] == input_str[i]:
                captcha_sum += int(input_str[i])
        return captcha_sum

    def part_two(self) -> int:
        captcha_sum = 0
        input_str = self.input_str_array[0]
        for i in range(len(input_str)):
            index = (i + len(input_str) // 2) % len(input_str)
            if input_str[index] == input_str[i]:
                captcha_sum += int(input_str[i])
        return captcha_sum


Advent2017Day01().run()