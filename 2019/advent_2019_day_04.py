from advent_day import AdventDay
from collections import Counter

class Advent2019Day04(AdventDay):

    def _valid_code(self, code: int):
        has_adjacent = False
        is_increasing = True
        prev_digit = float('inf')
        while code:
            digit = code % 10
            if prev_digit == digit:
                has_adjacent = True
            if prev_digit < digit:
                is_increasing = False
                break
            code //= 10
            prev_digit = digit
        return has_adjacent and is_increasing

    def _valid_code_2(self, code: int):
        c = Counter()
        has_adjacent = False
        is_increasing = True
        prev_digit = float('inf')
        while code:
            digit = code % 10
            c.update([digit])
            if prev_digit < digit:
                is_increasing = False
                break
            code //= 10
            prev_digit = digit
        for _, count in c.items():
            if count == 2:
                has_adjacent = True
        return has_adjacent and is_increasing

    def _parse_input(self) -> tuple[int, int]:
        low, hi = self.input_str_array[0].split('-')
        return (int(low), int(hi))

    def part_one(self) -> int:
        num = 0
        low, hi = self._parse_input()
        for i in range(low, hi+1):
            if self._valid_code(i):
                num += 1
        return num

    def part_two(self) -> int:
        num = 0
        low, hi = self._parse_input()
        for i in range(low, hi+1):
            if self._valid_code_2(i):
                num += 1
        return num


Advent2019Day04().run()