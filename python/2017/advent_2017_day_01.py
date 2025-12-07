def part_one(input_arr: list[str]) -> int:
    captcha_sum = 0
    input_str = input_arr[0]
    for i in range(len(input_str)):
        if input_str[i - 1] == input_str[i]:
            captcha_sum += int(input_str[i])
    return captcha_sum


def part_two(input_arr: list[str]) -> int:
    captcha_sum = 0
    input_str = input_arr[0]
    for i in range(len(input_str)):
        index = (i + len(input_str) // 2) % len(input_str)
        if input_str[index] == input_str[i]:
            captcha_sum += int(input_str[i])
    return captcha_sum


input_arr: list[str] = open("advent_2017_day_01.txt").read().splitlines()

print("Advent of Code 2017 - Day 01")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
