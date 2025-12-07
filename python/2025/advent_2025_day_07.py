def part_one(input_arr: list[str]) -> int:
    grid = {}
    for row in range(len(input_arr)):
        for col in range(len(input_arr[0])):
            grid[(row, col)] = input_arr[row][col]
    beams = [(0, input_arr[0].find("S"))]
    splits = 0
    visited = set()
    while beams:
        next_level = []
        while beams:
            r, c = beams.pop()
            if (r, c) in visited or r >= len(input_arr):
                continue
            visited.add((r, c))
            if input_arr[r][c] == "^":
                splits += 1
                next_level.append((r + 1, c - 1))
                next_level.append((r + 1, c + 1))
            else:
                next_level.append((r + 1, c))
        beams = next_level
    return splits


def part_two(input_arr: list[str]) -> int: ...


input_arr: list[str] = open("advent_2025_day_07.txt").read().splitlines()

print("Advent of Code 2025 - Day 07")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
