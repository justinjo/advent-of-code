from advent_day import AdventDay

class Advent2018Day05(AdventDay):

    def part_one(self) -> int:
        polymer = self.input_str_array[0]
        stack = []
        for i in range(len(polymer)):
            p = polymer[i]
            if stack and stack[-1] != p and stack[-1].lower() == p.lower():
                stack.pop()
            else:
                stack.append(p)
        return len(stack)

    def part_two(self) -> int:
        ...


Advent2018Day05().run()