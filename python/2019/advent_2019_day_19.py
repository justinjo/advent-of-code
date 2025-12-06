from advent_day import AdventDay
from .intcode import Intcode
from collections import deque


class Advent2019Day19(AdventDay):

    def print(self, beamed: set) -> None:
        max_x, max_y = sorted(list(beamed))[-1]
        for y in range(max_y + 1):
            line = ""
            for x in range(max_x + 1):
                line += "#" if (x, y) in beamed else "."
            print(line)

    def part_one(self) -> int:
        self._convert_input_to_int()
        q_out = deque()
        for x in range(50):
            for y in range(50):
                Intcode(
                    memory=self.input_int_array, queue_in=deque([x, y]), queue_out=q_out
                ).execute()
        return sum(q_out)

    def part_two(self) -> int:
        # ~30 second runtime
        self._convert_input_to_int()
        q_out = deque()
        beamed = set()
        # seed beamed coords
        for y in range(50):
            for x in range(50):
                Intcode(
                    memory=self.input_int_array, queue_in=deque([x, y]), queue_out=q_out
                ).execute()
                if q_out.popleft():
                    beamed.add((x, y))
        # seed x, y with first contiguous values from beam
        min_x = max_x = 9
        y = 11
        val = 0
        while not val:
            next_min = next_max = 0
            for x in range(min_x, max_x + 2):
                if (x - 1, y) not in beamed and (x, y - 1) not in beamed:
                    continue
                Intcode(
                    memory=self.input_int_array, queue_in=deque([x, y]), queue_out=q_out
                ).execute()
                if q_out.popleft():
                    if not next_min:
                        next_min = x
                    next_max = x
                    beamed.add((x, y))
                    if (x - 99, y) in beamed and (x, y - 99) in beamed:
                        val = (x - 99) * 10000 + (y - 99)
            min_x = next_min
            max_x = next_max
            y += 1
        return val


Advent2019Day19().run()
