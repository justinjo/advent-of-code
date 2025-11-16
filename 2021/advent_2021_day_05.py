from advent_day import AdventDay
from collections import Counter

class Line:

    def __init__(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def is_vertical(self) -> bool:
        return self.x1 == self.x2

    def is_horizontal(self) -> bool:
        return self.y1 == self.y2

    def get_points(self) -> list[tuple[int, int]]:
        points = []
        if self.is_vertical():
            ys = [self.y1, self.y2]
            for y in range(min(ys), max(ys) + 1):
                points.append((self.x1, y))
        elif self.is_horizontal():
            xs = [self.x1, self.x2]
            for x in range(min(xs), max(xs) + 1):
                points.append((x, self.y1))
        else:
            # sloped
            pass
        return points


class Advent2021Day05(AdventDay):

    def _parse_input(self) -> list[Line]:
        lines = []
        for s in self.input_str_array:
            c1, c2 = s.split(' -> ')
            x1, y1 = c1.split(',')
            x2, y2 = c2.split(',')
            lines.append(Line(int(x1), int(y1), int(x2), int(y2)))
        return lines

    def part_one(self) -> int:
        lines = self._parse_input()
        point_counter = Counter()
        for line in lines:
            if line.is_vertical() or line.is_horizontal():
                points = line.get_points()
                point_counter.update(points)

        overlaps = 0
        for point in point_counter:
            if point_counter[point] >= 2:
                overlaps += 1
        return overlaps

    def part_two(self) -> int:
        ...


Advent2021Day05().run()