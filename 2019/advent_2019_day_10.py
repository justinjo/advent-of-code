from advent_day import AdventDay
import math

class AsteroidMap:
    ASTEROID = '#'

    def __init__(self, asteroid_map: list[str]) -> None:
        self.map = asteroid_map
        self.rows = len(asteroid_map)
        self.cols = len(asteroid_map[0])
        self._generate_slopes()

    def _generate_slopes(self) -> None:
        # does not include (0, 1) or (1, 0)
        self.slope_set = set([0.0])
        self.slopes = [] # list[tuple[int, int]]
        for r in range(1, self.rows):
            for c in range(1, self.cols):
                slope = r / c
                if slope in self.slope_set:
                    continue
                self.slope_set.add(slope)
                common_divisor = math.gcd(r, c)
                self.slopes.append((r // common_divisor, c // common_divisor))

    def _sees_asteroid(self, row: int, col: int, rise: int, run: int) -> bool:
        r = row + rise
        c = col + run
        sees_asteroid = False
        while 0 <= r < self.rows and 0 <= c < self.cols:
            if self.map[r][c] == self.ASTEROID:
                sees_asteroid = True
            r += rise
            c += run
        return sees_asteroid

    def asteroids_seen(self, row: int, col: int) -> int:
        seen = 0
        if self._sees_asteroid(row, col, 0, 1):
            seen += 1
        if self._sees_asteroid(row, col, 0, -1):
            seen += 1
        if self._sees_asteroid(row, col, 1, 0):
            seen += 1
        if self._sees_asteroid(row, col, -1, 0):
            seen += 1
        for rise, run in self.slopes:
            if self._sees_asteroid(row, col, rise, run):
                seen += 1
            if self._sees_asteroid(row, col, rise, -run):
                seen += 1
            if self._sees_asteroid(row, col, -rise, run):
                seen += 1
            if self._sees_asteroid(row, col, -rise, -run):
                seen += 1
        return seen

    def best_station_placement(self) -> tuple[int, int]:
        best_row = best_col = max_asteroids = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.map[row][col] != self.ASTEROID:
                    continue
                num_asteroids = self.asteroids_seen(row, col)
                if num_asteroids > max_asteroids:
                    best_row = row
                    best_col = col
                    max_asteroids = num_asteroids
        return (best_row, best_col)

    def print_seen(self) -> None:
        strings = []
        for row in range(self.rows):
            row_str = ''
            for col in range(self.cols):
                if self.map[row][col] != self.ASTEROID:
                    row_str += 'XX '
                    continue
                num_asteroids = self.asteroids_seen(row, col)
                row_str += str(num_asteroids).zfill(2) + ' '
            row_str += '\n'
            strings.append(row_str)
        for s in strings:
            print(s)



class Advent2019Day10(AdventDay):

    def part_one(self) -> int:
        am = AsteroidMap(self.input_str_array)
        row, col = am.best_station_placement()
        return am.asteroids_seen(row, col)

    def part_two(self) -> int:
        ...


Advent2019Day10().run()