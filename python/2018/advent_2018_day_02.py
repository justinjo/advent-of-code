from collections import Counter


def part_one(input_arr: list[str]) -> int:
    twos = 0
    threes = 0
    for s in input_arr:
        c = Counter(s)
        add_two = False
        add_three = False
        for _, count in c.items():
            if count == 2:
                add_two = True
            elif count == 3:
                add_three = True
        twos += 1 if add_two else 0
        threes += 1 if add_three else 0
    return twos * threes


def part_two(input_arr: list[str]) -> str:
    return_str = ""
    for i in range(len(input_arr)):
        for j in range(i + 1, len(input_arr)):
            str_i = input_arr[i]
            str_j = input_arr[j]
            c_i = Counter(str_i)
            c_j = Counter(str_j)
            c_diff = (c_i - c_j) + (c_j - c_i)
            if len(c_diff) == 2:
                chars = ""
                for k in range(len(str_i)):
                    if str_i[k] != str_j[k]:
                        if str_i[k] not in c_diff:
                            break
                    else:
                        chars += str_i[k]
                return_str = chars if len(chars) == len(str_i) - 1 else return_str
    return return_str


input_arr: list[str] = open("advent_2018_day_02.txt").read().splitlines()

print("Advent of Code 2018 - Day 02")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
