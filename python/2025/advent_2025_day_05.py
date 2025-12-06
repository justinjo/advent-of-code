def part_one(input_arr: list[str]) -> int:
    ranges = []
    i = fresh = 0
    while input_arr[i]:
        ranges.append(tuple([int(x) for x in input_arr[i].split("-")]))
        i += 1
    for i in range(i + 1, len(input_arr)):  # i+1 skips empty line
        fresh += int(any([lo <= int(input_arr[i]) <= hi for lo, hi in ranges]))
    return fresh


def part_two(input_arr: list[str]) -> int:
    ranges = []
    i = 0
    while input_arr[i]:
        ranges.append(tuple([int(x) for x in input_arr[i].split("-")]))
        i += 1
    ranges.sort()
    merged_ranges = []
    curr_range = ranges[0]
    for lo, hi in ranges:
        if curr_range[1] < lo:
            merged_ranges.append(curr_range)
            curr_range = (lo, hi)
        elif curr_range[1] < hi:
            curr_range = (curr_range[0], hi)
    merged_ranges.append(curr_range)
    return sum([(hi - lo + 1) for lo, hi in merged_ranges])


input_arr: list[str] = open("advent_2025_day_05.txt").read().splitlines()

print("Advent of Code 2025 - Day 05")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
