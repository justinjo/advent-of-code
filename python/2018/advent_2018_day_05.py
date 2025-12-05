from advent_day import AdventDay

class Advent2018Day05(AdventDay):

    def _react(self, polymer: str, ignore_unit: str = '') -> int:
        ignore_units = set()
        if ignore_unit:
            ignore_units.update([ignore_unit, ignore_unit.upper()])
        stack = []
        for i in range(len(polymer)):
            p = polymer[i]
            if p in ignore_units:
                continue
            if stack and stack[-1] != p and stack[-1].lower() == p.lower():
                stack.pop()
            else:
                stack.append(p)
        return len(stack)

    def part_one(self) -> int:
        polymer = self.input_str_array[0]
        return self._react(polymer)

    def part_two(self) -> int:
        polymer = self.input_str_array[0]
        chars = [chr(ord('a') + i) for i in range(26)]
        min_length = float('inf')
        for c in chars:
            min_length = min(min_length, self._react(polymer, c))
        return int(min_length)


Advent2018Day05().run()