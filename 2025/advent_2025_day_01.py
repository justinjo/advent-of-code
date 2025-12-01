from advent_day import AdventDay

class Advent2025Day01(AdventDay):

    def part_one(self) -> int:
        password = 0
        dial = 50
        for rotation in self.input_str_array:
            dial += int(rotation[1:]) if rotation[0] == 'R' else -int(rotation[1:])
            password += 1 if dial % 100 == 0 else 0
        return password


    def part_two(self) -> int:
        ...


Advent2025Day01().run()