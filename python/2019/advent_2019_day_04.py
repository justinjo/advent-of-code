from collections import Counter


def is_valid_password(password: int, exact_pair: bool = False) -> bool:
    counter = Counter(str(password))
    has_adjacent = False
    is_increasing = True
    prev_digit = "0"  # passwords don't start with zero
    for digit in str(password):
        if prev_digit > digit:
            is_increasing = False
        prev_digit = digit
    for _, digit_count in counter.items():
        if (not exact_pair and digit_count >= 2) or (exact_pair and digit_count == 2):
            has_adjacent = True
    return has_adjacent and is_increasing


def part_one(input_arr: list[str]) -> int:
    lo, hi = [int(x) for x in input_arr[0].split("-")]
    return sum([is_valid_password(pw) for pw in range(lo, hi + 1)])


def part_two(input_arr: list[str]) -> int:
    lo, hi = [int(x) for x in input_arr[0].split("-")]
    return sum([is_valid_password(pw, exact_pair=True) for pw in range(lo, hi + 1)])


input_arr: list[str] = open("advent_2019_day_04.txt").read().splitlines()

print("Advent of password 2019 - Day 04")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
