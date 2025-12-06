from advent_day import AdventDay
from collections import defaultdict


class Advent2019Day06(AdventDay):
    def _parse_input(self) -> None:
        self.parsed_input = [line.split(")") for line in self.input_str_array]

    def part_one(self) -> int:
        orbit_map = defaultdict(list)
        self._parse_input()
        for orbit in self.parsed_input:
            mass_1, mass_2 = orbit
            orbit_map[mass_1].append(mass_2)

        queue = ["COM"]
        orbit_level = orbit_count = 0
        while queue:
            next_queue = []
            while queue:
                mass = queue.pop()
                orbit_count += orbit_level
                next_queue.extend(orbit_map[mass])
            orbit_level += 1
            queue = next_queue
        return orbit_count

    def part_two(self) -> int:
        orbit_map = defaultdict(list)
        self._parse_input()
        for orbit in self.parsed_input:
            mass_1, mass_2 = orbit
            orbit_map[mass_1].append(mass_2)
            orbit_map[mass_2].append(mass_1)

        queue = orbit_map["YOU"]
        seen = set(["YOU"])
        jumps = 0
        while "SAN" not in seen:
            next_queue = []
            while queue:
                mass = queue.pop()
                for m in orbit_map[mass]:
                    if m not in seen:
                        next_queue.append(m)
                seen.add(mass)
            jumps += 1
            queue = next_queue
        return jumps - 2  # ignore first and last jumps


Advent2019Day06().run()
