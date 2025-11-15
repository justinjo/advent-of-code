from advent_day import AdventDay

class Submarine:

    def __init__(self) -> None:
        self.horiz = 0
        self.depth = 0
        self.aim = 0

    def _move_without_aim(self, direction: str, value: int) -> None:
        if direction == 'forward':
            self.horiz += value
        elif direction == 'down':
            self.depth += value
        elif direction == 'up':
            self.depth -= value

    def _move_with_aim(self, direction: str, value: int) -> None:
        if direction == 'forward':
            self.horiz += value
            self.depth += self.aim * value
        elif direction == 'down':
            self.aim += value
        elif direction == 'up':
            self.aim -= value


    def move(self, instruction: str, should_aim: bool = False) -> None:
        direction, value = instruction.split(' ')
        if should_aim:
            self._move_with_aim(direction, int(value))
        else:
            self._move_without_aim(direction, int(value))


class Advent2021Day02(AdventDay):

    def part_one(self) -> int:
        sub = Submarine()
        for instr in self.input_str_array:
            sub.move(instr)
        return sub.horiz * sub.depth

    def part_two(self) -> int:
        sub = Submarine()
        for instr in self.input_str_array:
            sub.move(instr, should_aim=True)
        return sub.horiz * sub.depth


Advent2021Day02().run()