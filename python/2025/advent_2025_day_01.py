def part_one(input_arr: list[str]) -> int:
    password = 0
    dial = 50
    for rotation in input_arr:
        dial += int(rotation[1:]) if rotation[0] == "R" else -int(rotation[1:])
        password += 1 if dial % 100 == 0 else 0
    return password


def part_two(input_arr: list[str]) -> int:
    password = 0
    dial = 50
    for rotation in input_arr:
        delta = int(rotation[1:]) if rotation[0] == "R" else -int(rotation[1:])
        password += abs((dial + delta) // 100)
        if delta < 0:
            password -= 1 if dial == 0 else 0
            password += 1 if (dial + delta) % 100 == 0 else 0
        dial = (dial + delta) % 100
    return password


input_arr: list[str] = open("advent_2025_day_01.txt").read().splitlines()

print("Advent of Code 2025 - Day 01")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
