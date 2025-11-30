from advent_day import AdventDay
from .intcode import Intcode
from collections import deque

class Advent2019Day17(AdventDay):

    INTERSECTION_NEIGHBORS = ((0, -1), (0, 1), (-1, 0), (1, 0))

    def is_intersection(self, arr: list[list[str]], row: int, col: int) -> bool:
        neighbors = 0
        if arr[row][col] != '#':
            return False
        for r_d, c_d in self.INTERSECTION_NEIGHBORS:
            if 0 <= row + r_d < len(arr) and 0 <= col + c_d < len(arr[0]):
                neighbors += 1 if arr[row + r_d][col + c_d] == '#' else 0
        return neighbors == 4

    def part_one(self) -> int:
        self._convert_input_to_int()
        q_out = deque()
        Intcode(memory=self.input_int_array, queue_out=q_out).execute()
        lines = []
        line = ''
        alignment_sum = 0
        for val in q_out:
            if val == 10 and line:
                lines.append(line)
                line = ''
            else:
                line += chr(val)
        for r in range(len(lines)):
            for c in range(len(lines[0])):
                if self.is_intersection(lines, r, c):
                    alignment_sum += r * c
        return alignment_sum

    def part_two(self) -> int:
        ...


Advent2019Day17().run()