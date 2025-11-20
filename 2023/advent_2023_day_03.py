from advent_day import AdventDay

class Advent2023Day03(AdventDay):

    def char_is_adjacent(self, row: int, col: int) -> bool:
        adjacent_cells = (
            (row-1, col-1),
            (row-1, col),
            (row-1, col+1),
            (row, col-1),
            (row, col+1),
            (row+1, col-1),
            (row+1, col),
            (row+1, col+1),
        )
        for r, c in adjacent_cells:
            if 0 <= r < self.input_length and 0 <= c < len(self.input_str_array[0]):
                char = self.input_str_array[r][c]
                if char != '.' and not char.isnumeric():
                    return True
        return False


    def part_one(self) -> int:
        part_numbers = []
        for row in range(self.input_length):
            num_str = ''
            is_adjacent = False
            for col in range(len(self.input_str_array[0])):
                char = self.input_str_array[row][col]
                if char.isnumeric():
                    num_str += char
                    is_adjacent |= self.char_is_adjacent(row, col)
                else:
                    if num_str and is_adjacent:
                        part_numbers.append(int(num_str))
                    num_str = ''
                    is_adjacent = False
            if num_str and is_adjacent:
                part_numbers.append(int(num_str))
        return sum(part_numbers)

    def part_two(self) -> int:
        ...


Advent2023Day03().run()