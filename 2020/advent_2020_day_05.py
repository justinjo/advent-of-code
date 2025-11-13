from advent_day import AdventDay
from collections import defaultdict
from copy import deepcopy

class Advent2020Day05(AdventDay):
    ROWS = 128
    COLS = 8
    BASE_TICKET = {
        'ticket': '.',
        'row': -1,
        'col': -1,
        'seat_id': -1,
    }

    def _calc_row(self, ticket: str, end_i: int = 7) -> int:
        lo = 0
        hi = self.ROWS
        for i in range(end_i):
            if ticket[i] == 'F':
                hi = hi - ((hi-lo)+1)//2
            elif ticket[i] == 'B':
                lo = hi - ((hi-lo)+1)//2
        if ticket[end_i-1] == 'F':
            return lo
        elif ticket[end_i-1] == 'B':
            return hi - 1
        return -1

    def _calc_col(self, ticket: str, start_i: int = 7) -> int:
        lo = 0
        hi = self.COLS
        for i in range(start_i, len(ticket) - 1):
            if ticket[i] == 'L':
                hi = hi - ((hi-lo)+1)//2
            elif ticket[i] == 'R':
                lo = hi - ((hi-lo)+1)//2
        if ticket[-1] == 'L':
            return lo
        elif ticket[-1] == 'R':
            return hi - 1
        return -1

    def _get_seat_id(self, row: int, col: int, row_mult: int = 8, col_mult: int = 1) -> int:
        return row * row_mult + col * col_mult

    def _print_pass(self, ticket: str, row: int, col: int, seat_id: int) -> None:
        print(f'{ticket}: row {row}, column: {col}, seat ID {seat_id}.')

    def part_one(self) -> int:
        max_ticket = deepcopy(self.BASE_TICKET)
        for ticket in self.input_str_array:
            row = self._calc_row(ticket)
            col = self._calc_col(ticket)
            seat_id = self._get_seat_id(row, col)
            if seat_id > max_ticket['seat_id']:
                max_ticket = {
                    'ticket': ticket,
                    'row': row,
                    'col': col,
                    'seat_id': seat_id,
                }
        return max_ticket['seat_id']

    def part_two(self):
        boarding_dict = defaultdict(set)
        for ticket in self.input_str_array:
            boarding_dict[self._calc_row(ticket)].add(self._calc_col(ticket))
        for row in range(1, self.ROWS - 2):
            if (
                len(boarding_dict[row]) == self.COLS
                and len(boarding_dict[row+1]) == self.COLS - 1
                and len(boarding_dict[row+2]) == self.COLS
            ):
                for col in range(8):
                    if col not in boarding_dict[row+1]:
                        return self._get_seat_id(row+1, col)
        return -1


Advent2020Day05().run()