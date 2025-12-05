from advent_day import AdventDay
from collections import Counter
from copy import deepcopy

class Advent2020Day11(AdventDay):
    FLOOR = '.'
    EMPTY = 'L'
    OCCUPIED = '#'

    def _generate_next_seating(self, seating: list[str]) -> list[str]:
        next_seating = deepcopy(seating)
        rows = len(seating)
        cols = len(seating[0])
        for r in range(rows):
            for c in range(cols):
                if seating[r][c] == self.FLOOR:
                    continue
                neighbors = self._num_neighbors(seating, r, c)
                if self._is_occupied(seating, r, c):
                    if neighbors >= 4:
                        next_seating[r] = self._set_seat(
                            next_seating[r],
                            c,
                            self.EMPTY
                        )
                else:
                    if neighbors == 0:
                        next_seating[r] = self._set_seat(
                            next_seating[r],
                            c,
                            self.OCCUPIED
                        )
        return next_seating

    def _generate_next_seating_2(self, seating: list[str]) -> list[str]:
        next_seating = deepcopy(seating)
        rows = len(seating)
        cols = len(seating[0])
        for r in range(rows):
            for c in range(cols):
                if seating[r][c] == self.FLOOR:
                    continue

                neighbors = self._num_neighbors_in_eyeline(seating, r, c)
                if self._is_occupied(seating, r, c):
                    if neighbors >= 5:
                        next_seating[r] = self._set_seat(
                            next_seating[r],
                            c,
                            self.EMPTY
                        )
                else:
                    if neighbors == 0:
                        next_seating[r] = self._set_seat(
                            next_seating[r],
                            c,
                            self.OCCUPIED
                        )
        return next_seating

    def _set_seat(self, seating_row: str, col: int, state: str) -> str:
        return seating_row[:col] + state + seating_row[col+1:]

    def _is_occupied(self, seating: list[str], row: int, col: int) -> bool:
        if 0 <= row < len(seating) and 0 <= col < len(seating[0]):
            return seating[row][col] == self.OCCUPIED
        return False

    def _sees_occupied(
        self,
        seating: list[str],
        row: int,
        col: int,
        rise: int,
        run: int,
    ) -> bool:
        sees_occupied = False
        row += rise
        col += run
        while (
            0 <= row < len(seating)
            and 0 <= col < len(seating[0])
            and not sees_occupied
        ):
            if seating[row][col] != self.FLOOR:
                return seating[row][col] == self.OCCUPIED
            row += rise
            col += run
        return sees_occupied

    def _num_neighbors(self, seating: list[str], row: int, col: int) -> int:
        neighbors = 0
        neighbor_coords = [
            (row-1, col-1),
            (row-1, col),
            (row-1, col+1),
            (row, col-1),
            (row, col+1),
            (row+1, col-1),
            (row+1, col),
            (row+1, col+1),
        ]
        for row, col in neighbor_coords:
            if self._is_occupied(seating, row, col):
                neighbors += 1
        return neighbors

    def _num_neighbors_in_eyeline(
        self,
        seating: list[str],
        row: int,
        col: int
    ) -> int:
        neighbors = 0
        slopes = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, +1),
        ]
        for rise, run in slopes:
            if self._sees_occupied(seating, row, col, rise, run):
                neighbors += 1
        return neighbors

    def _print_seating(self, seating: list[str]) -> None:
        print()
        for s in seating:
            print(s)
        print()

    def part_one(self) -> int:
        seating = deepcopy(self.input_str_array)
        next_seating = self._generate_next_seating(seating)
        occupied_seats = 0
        while seating != next_seating:
            seating = next_seating
            next_seating = self._generate_next_seating(seating)
        c = Counter()
        for s in seating:
            c.update(s)
        occupied_seats = c[self.OCCUPIED]
        return occupied_seats

    def part_two(self) -> int:
        seating = deepcopy(self.input_str_array)
        next_seating = self._generate_next_seating_2(seating)
        occupied_seats = 0
        while seating != next_seating:
            seating = next_seating
            next_seating = self._generate_next_seating_2(seating)
        c = Counter()
        for s in seating:
            c.update(s)
        occupied_seats = c[self.OCCUPIED]
        return occupied_seats


Advent2020Day11().run()