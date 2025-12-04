from advent_day import AdventDay

class Advent2025Day03(AdventDay):

    def part_one(self) -> int:
        joltage = 0
        for s in self.input_str_array:
            arr = [int(x) for x in list(s)]
            b1 = max(arr[:-1])
            i1 = arr.index(b1)
            b2 = max(arr[i1+1:])
            joltage += b1 * 10 + b2
        return joltage

    def part_two(self) -> int:
        ...

Advent2025Day03().run()