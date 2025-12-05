from advent_day import AdventDay
from collections import Counter

class Advent2024Day01(AdventDay):

    def parse_input(self) -> tuple[list[int], list[int]]:
        left = []
        right = []
        for l in self.input_str_array:
            l, r = l.split('   ')
            left.append(int(l))
            right.append(int(r))
        return (left, right)

    def part_one(self) -> int:
        left, right = self.parse_input()
        distance = 0
        for l, r in zip(sorted(left), sorted(right)):
            distance += abs(r - l)
        return distance

    def part_two(self) -> int:
        left, right = self.parse_input()
        c = Counter(right)
        similarity = 0
        for l in left:
            similarity += l * c[l]
        return similarity


Advent2024Day01().run()