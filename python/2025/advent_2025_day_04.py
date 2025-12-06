NEIGHBOR_COORDS = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))

def get_accessible_rolls(grid: list[str]) -> set[tuple[int, int]]:
    rolls = set()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] != '@':
                continue
            neighbors = 0
            for xd, yd in NEIGHBOR_COORDS:
                if 0 <= x + xd < len(grid[0]) and 0 <= y + yd < len(grid):
                    neighbors += 1 if grid[y+yd][x+xd] == '@' else 0
            if neighbors < 4:
                rolls.add((x, y))
    return rolls

def remove_rolls(grid: list[str], rolls: set[tuple[int, int]]) -> list[str]:
    new_grid = []
    for y in range(len(grid)):
        new_line = ''
        for x in range(len(grid[0])):
            new_line += 'x' if (x, y) in rolls else grid[y][x]
        new_grid.append(new_line)
    return new_grid

def part_one(input_arr: list[str]) -> int:
    return len(get_accessible_rolls(input_arr))

def part_two(input_arr: list[str]) -> int:
    removed = 0
    grid = input_arr
    accessible_rolls = get_accessible_rolls(grid)
    while accessible_rolls:
        grid = remove_rolls(grid, accessible_rolls)
        removed += len(accessible_rolls)
        accessible_rolls = get_accessible_rolls(grid)
    return removed

input_arr: list[str] = open('advent_2025_day_04.txt').read().splitlines()

print('Advent of Code 2025 - Day 04')
print(f'Part One: {part_one(input_arr)}')
print(f'Part Two: {part_two(input_arr)}')