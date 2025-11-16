from advent_day import AdventDay
from collections import Counter

class Advent2021Day06(AdventDay):

    def _parse_input(self) -> Counter:
        c = Counter([int(n) for n in self.input_str_array[0].split(',')])
        return c

    def spawn(self, fish: Counter, days: int) -> int:
        for _ in range(days):
            spawned = fish[0]
            for i in range(8):
                fish[i] = fish[i+1]
            fish[6] += spawned
            fish[8] = spawned
        return sum(fish.values())

    def part_one(self) -> int:
        fish_counter = self._parse_input()
        return self.spawn(fish_counter, 80)

    def part_two(self) -> int:
        fish_counter = self._parse_input()
        return self.spawn(fish_counter, 256)


Advent2021Day06().run()