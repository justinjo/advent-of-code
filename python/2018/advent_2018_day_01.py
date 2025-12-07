def part_one(input_arr: list[str]) -> int:
    return sum([int(x) for x in input_arr])


def part_two(input_arr: list[str]) -> int:
    seen = set()
    freq = i = 0
    arr = [int(x) for x in input_arr]
    while freq not in seen:
        seen.add(freq)
        freq += arr[i]
        i = (i + 1) % len(arr)
    return freq


input_arr: list[str] = open("advent_2018_day_01.txt").read().splitlines()

print("Advent of Code 2018 - Day 01")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
