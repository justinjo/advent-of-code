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
        password = 0
        dial = 50
        for rotation in self.input_str_array:
            delta = int(rotation[1:]) if rotation[0] == 'R' else -int(rotation[1:])
            if rotation[0] == 'R':
                password += (dial + delta) // 100
            else:
                password += -((dial + delta) // 100)
                password -= 1 if dial == 0 else 0
                password += 1 if (dial + delta) % 100 == 0 else 0
            dial = (dial + delta) % 100
        return password


Advent2025Day01().run()