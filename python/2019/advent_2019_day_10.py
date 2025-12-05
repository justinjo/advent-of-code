from advent_day import AdventDay
import math

class AsteroidMap:
    ASTEROID = '#'
    SPACE = '.'

    def __init__(self, asteroid_map: list[str]) -> None:
        self.map = asteroid_map
        self.rows = len(asteroid_map)
        self.cols = len(asteroid_map[0])
        self._generate_slopes()
        self.strings = []

    def _generate_slopes(self) -> None:
        # does not include (0, 1) or (1, 0)
        self.slope_set = set([0.0])
        self.slopes = [] # list[tuple[int, int]]
        self.slopes_dict = {}
        for r in range(1, self.rows):
            for c in range(1, self.cols):
                slope = r / c
                if slope in self.slope_set:
                    continue
                self.slope_set.add(slope)
                common_divisor = math.gcd(r, c)
                slope_tuple = (r // common_divisor, c // common_divisor)
                self.slopes.append(slope_tuple)
                self.slopes_dict[slope] = slope_tuple
        self.slope_set.remove(0.0)
        self.sorted_slopes = sorted(list(self.slope_set))
        self.reverse_sorted_slopes = self.sorted_slopes[::-1]

    def _sees_asteroid(
        self,
        row: int,
        col: int,
        rise: int,
        run: int,
    ) -> tuple[int, int] | None:
        r = row + rise
        c = col + run
        seen_row = seen_col = 0
        sees_asteroid = False
        while 0 <= r < self.rows and 0 <= c < self.cols and not sees_asteroid:
            if self.map[r][c] == self.ASTEROID:
                sees_asteroid = True
                seen_row = r
                seen_col = c
            r += rise
            c += run
        return (seen_row, seen_col) if sees_asteroid else None

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

    def _destroy_asteroid(
        self,
        row: int,
        col: int,
        rise: int,
        run: int,
    ) -> tuple[int, int] | None:
        # returns coord of asteroid that was destroyed if it exists
        coords = self._sees_asteroid(row, col, rise, run)
        if coords:
            r, c = coords
            self.map[r] = self.map[r][:c] + self.SPACE + self.map[r][c+1:]
            if self.strings:
                self.strings[r] = self.strings[r][:8*c] + 'DESTROY ' + self.strings[r][8*c+8:]
        return coords

    def _get_slope_order(self) -> list[tuple[int, int]]:
        # generate all slope tuples in clockwise order
        ordered_slopes = []

        # top right quadrant
        ordered_slopes.append((-1, 0))
        for slope in self.reverse_sorted_slopes:
            rise, run = self.slopes_dict[slope]
            ordered_slopes.append((-rise, run))

        # bottom right quadrant
        ordered_slopes.append((0, 1))
        for slope in self.sorted_slopes:
            rise, run = self.slopes_dict[slope]
            ordered_slopes.append((rise, run))

        # bottom left quadrant
        ordered_slopes.append((1, 0))
        for slope in self.reverse_sorted_slopes:
            rise, run = self.slopes_dict[slope]
            ordered_slopes.append((rise, -run))

        # top left quadrant
        ordered_slopes.append((0, -1))
        for slope in self.sorted_slopes:
            rise, run = self.slopes_dict[slope]
            ordered_slopes.append((-rise, -run))

        return ordered_slopes

    def destroy_asteroids(
        self,
        row: int,
        col: int,
        num_to_destroy: int,
        should_print_map: bool = False
    ) -> tuple[int, int]:
        # returns the coordinates of the final destroyed astroid
        destroyed_row = destroyed_col = num_destroyed = 0
        slopes = self._get_slope_order()
        i = 0
        while num_destroyed < num_to_destroy:
            rise, run = slopes[i]
            destroyed_coords = self._destroy_asteroid(row, col, rise, run)
            if destroyed_coords:
                if should_print_map:
                    self.print_map(row, col)
                num_destroyed += 1
                destroyed_row, destroyed_col = destroyed_coords
            i = (i + 1) % len(slopes)

        return (destroyed_row, destroyed_col)

    def _generate_print_map(self, row: int, col: int) -> None:
        for r in range(self.rows):
            row_str = ''
            for c in range(self.cols):
                if self.map[r][c] != self.ASTEROID:
                    row_str += '....... '
                    continue
                elif (r == row and c == col):
                    row_str += '_BASE__ '
                    continue
                if -0.001 < row - r < 0.001:
                    row_str += '0.00000 '
                elif -0.001 < col - c < 0.001:
                    row_str += 'INFINIT '
                else:
                    if 0 < ((row-r)/(col-c)) < 10:
                        row_str += f'{((row-r)/(col-c)):.5f}' + ' '
                    elif 10 <= ((row-r)/(col-c)):
                        row_str += f'{((row-r)/(col-c)):.4f}' + ' '
                    elif -10 < ((row-r)/(col-c)) < 0:
                        row_str += f'{((row-r)/(col-c)):.4f}' + ' '
                    else:
                        row_str += f'{((row-r)/(col-c)):.3f}' + ' '
            row_str += '\n'
            self.strings.append(row_str)

    def print_map(self, row: int, col: int) -> None:
        if not self.strings:
            self._generate_print_map(row, col)
        for s in self.strings:
            print(s)


class Advent2019Day10(AdventDay):

    def part_one(self) -> int:
        am = AsteroidMap(self.input_str_array)
        row, col = am.best_station_placement()
        return am.asteroids_seen(row, col)

    def part_two(self) -> int:
        am = AsteroidMap(self.input_str_array)
        r, c = am.best_station_placement()
        row, col = am.destroy_asteroids(r, c, 200)
        # i did this whole thing x=row, y=col
        # problem statement has it the other way around...
        return 100 * col + row


Advent2019Day10().run()