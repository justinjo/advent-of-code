from advent_day import AdventDay

class Advent2025Day04(AdventDay):

    def list_accessible_rolls(self, grid: list[str]) -> list[tuple[int, int]]:
        ar = []
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
                if neighbors < 4:
                    ar.append((x, y))
        return ar

    def remove_rolls(self, grid: list[str], rolls: list[tuple[int, int]]):
        new_grid = []
        roll_set = set(rolls)
        for y in range(len(grid)):
            new_line = ''
            for x in range(len(grid[0])):
                new_line += 'x' if (x, y) in roll_set else grid[y][x]
            new_grid.append(new_line)
        return new_grid

    def count_accessible_rolls(self, grid: list[str]) -> int:
        return len(self.list_accessible_rolls(grid))

    def part_one(self) -> int:
        return self.count_accessible_rolls(self.input_str_array)

    def part_two(self) -> int:
        removed = 0
        grid = self.input_str_array
        accessible_rolls = self.list_accessible_rolls(grid)
        while accessible_rolls:
            grid = self.remove_rolls(grid, accessible_rolls)
            removed += len(accessible_rolls)
            accessible_rolls = self.list_accessible_rolls(grid)
        return removed


Advent2025Day04().run()