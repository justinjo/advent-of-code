from advent_day import AdventDay

class BingoBoard:
    ROWS = 5
    COLS = 5

    def __init__(self) -> None:
        self.row_counts: list[int] = [0] * self.ROWS
        self.col_counts: list[int] = [0] * self.COLS
        self.rows: list[list[int]] = []
        self.numbers_found: set[int] = set()

    def add_row(self, row_str: str) -> None:
        row_int_arr = []
        row_str_arr = row_str.split(' ')
        for r in row_str_arr:
            if r.isnumeric():
                row_int_arr.append(int(r))
        self.rows.append(row_int_arr)

    def add_num(self, num: int) -> bool:
        # returns true if bingo is created, else false
        if num in self.numbers_found:
            return False

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.rows[r][c] == num:
                    self.numbers_found.add(num)
                    self.row_counts[r] += 1
                    self.col_counts[c] += 1

        return self.has_bingo()

    def has_bingo(self) -> bool:
        for rc in self.row_counts:
            if rc == self.COLS: # row count must add to number of cols for bingo
                return True
        for cc in self.col_counts:
            if cc == self.ROWS: # col count must add ot number of rows for bingo
                return True
        return False

    def get_score(self, num: int) -> int:
        value = 0
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if self.rows[r][c] not in self.numbers_found:
                    value += self.rows[r][c]
        return value * num

    def print(self) -> None:
        for r in range(self.ROWS):
            print_str = ''
            for c in range(self.COLS):
                print_str += str(self.rows[r][c]).zfill(2) + ' '
            print(print_str)
        print()


class Advent2021Day04(AdventDay):

    def part_one(self) -> int:
        numbers_to_call: list[int] = [int(s) for s in self.input_str_array[0].split(',')]
        boards: list[BingoBoard] = []
        i = 2
        while i < self.input_length:
            board = BingoBoard()
            boards.append(board)
            while i < self.input_length and self.input_str_array[i]:
                board.add_row(self.input_str_array[i])
                i += 1
            i += 1

        for num in numbers_to_call:
            for board in boards:
                if board.add_num(num):
                    return board.get_score(num)
        return -1

    def part_two(self) -> int:
        ...


Advent2021Day04().run()