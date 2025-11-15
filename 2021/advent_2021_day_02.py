from advent_day import AdventDay

class Submarine:

    def __init__(self) -> None:
        self.horiz = 0
        self.depth = 0

    def move(self, instruction: str) -> None:
        direction, value = instruction.split(' ')
        if direction == 'forward':
            self.horiz += int(value)
        elif direction == 'down':
            self.depth += int(value)
        elif direction == 'up':
            self.depth -= int(value)


class Advent2021Day02(AdventDay):

    def part_one(self) -> int:
        sub = Submarine()
        for instr in self.input_str_array:
            sub.move(instr)
        return sub.horiz * sub.depth


    def part_two(self) -> int:
        ...


Advent2021Day02().run()