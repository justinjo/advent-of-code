from advent_day import AdventDay
from collections import Counter

class Advent2021Day06(AdventDay):

    def _parse_input(self) -> Counter:
        c = Counter([int(n) for n in self.input_str_array[0].split(',')])
        return c

    def part_one(self) -> int:
        fish_counter = self._parse_input()
        for _ in range(80):
            spawned = fish_counter[0]
            for i in range(8):
                fish_counter[i] = fish_counter[i+1]
            fish_counter[6] += spawned
            fish_counter[8] = spawned
        return sum(fish_counter.values())

    def part_two(self) -> int:
        ...


Advent2021Day06().run()