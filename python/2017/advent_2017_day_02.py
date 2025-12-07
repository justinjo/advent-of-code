def parse_input(input_arr: list[str]) -> list[list[int]]:
    parsed_input = []
    for line in input_arr:
        parsed_input.append([int(l) for l in line.split("\t")])
    return parsed_input


def part_one(input_arr: list[str]) -> int:
    checksum = 0
    for arr in parse_input(input_arr):
        checksum += max(arr) - min(arr)
    return checksum


def part_two(input_arr: list[str]) -> int:
    prodsum = 0
    for arr in parse_input(input_arr):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] % arr[j] == 0:
                    prodsum += arr[i] // arr[j]
                elif arr[j] % arr[i] == 0:
                    prodsum += arr[j] // arr[i]
    return prodsum


input_arr: list[str] = open("advent_2017_day_02.txt").read().splitlines()

print("Advent of Code 2017 - Day 02")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
