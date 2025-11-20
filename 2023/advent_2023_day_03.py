from advent_day import AdventDay
from collections import defaultdict

class Advent2023Day03(AdventDay):

    NOT_FOUND_TUPLE = (-1, -1)

    def get_adjacent_symbol_coord(
        self,
        row: int,
        col: int,
        search_gear: bool = False
    ) -> tuple[int, int]:
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
                if search_gear:
                    if char == '*':
                        return (r, c)
                elif (char != '.' and not char.isnumeric()):
                    return (r, c)
        return self.NOT_FOUND_TUPLE

    def part_one(self) -> int:
        part_numbers = []
        for row in range(self.input_length):
            num_str = ''
            is_adjacent = False
            for col in range(len(self.input_str_array[0])):
                char = self.input_str_array[row][col]
                if char.isnumeric():
                    num_str += char
                    is_adjacent |= self.get_adjacent_symbol_coord(row, col) != self.NOT_FOUND_TUPLE
                else:
                    if num_str and is_adjacent:
                        part_numbers.append(int(num_str))
                    num_str = ''
                    is_adjacent = False
            if num_str and is_adjacent:
                part_numbers.append(int(num_str))
        return sum(part_numbers)

    def part_two(self) -> int:
        gear_ratios = []
        gear_number_map = defaultdict(list)
        for row in range(self.input_length):
            num_str = ''
            adjacent_gear_coords = set()
            for col in range(len(self.input_str_array[0])):
                char = self.input_str_array[row][col]
                if char.isnumeric():
                    num_str += char
                    maybe_gear_coord = self.get_adjacent_symbol_coord(
                        row,
                        col,
                        search_gear=True
                    )
                    if maybe_gear_coord != self.NOT_FOUND_TUPLE:
                        adjacent_gear_coords.add(maybe_gear_coord)
                else:
                    if num_str:
                        for coord in adjacent_gear_coords:
                            gear_number_map[coord].append(int(num_str))
                    num_str = ''
                    adjacent_gear_coords = set()
            if num_str:
                for coord in adjacent_gear_coords:
                    gear_number_map[coord].append(int(num_str))
        for geared_num_list in gear_number_map.values():
            if len(geared_num_list) == 2:
                gear_ratios.append(geared_num_list[0] * geared_num_list[1])
        return sum(gear_ratios)


Advent2023Day03().run()