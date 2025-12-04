from advent_day import AdventDay

class Advent2025Day04(AdventDay):

    def accessible_rolls(self, grid: list[str]) -> int:
        ar = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] != '@':
                    continue
                neighbors = 0
                for y_d in range(-1, 2):
                    for x_d in range(-1, 2):
                        if y_d == x_d == 0:
                            continue
                        if 0 <= x+x_d < len(grid[0]) and 0 <= y+y_d < len(grid):
                            neighbors += 1 if grid[y+y_d][x+x_d] == '@' else 0
                ar += 1 if neighbors < 4 else 0
        return ar

    def part_one(self) -> int:
        return self.accessible_rolls(self.input_str_array)

    def part_two(self) -> int:
        ...

Advent2025Day04().run()