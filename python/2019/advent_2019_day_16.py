PATTERN = [0, 1, 0, -1]


def fft(arr: list[int]) -> list[int]:
    next_phase = [0] * len(arr)
    for next_i in range(len(arr)):
        for arr_i in range(len(arr)):
            pattern_i = ((arr_i + 1) // (next_i + 1)) % len(PATTERN)
            next_phase[next_i] += arr[arr_i] * PATTERN[pattern_i]
        if next_phase[next_i] >= 0 or next_phase[next_i] % 10 == 0:
            next_phase[next_i] %= 10
        else:
            next_phase[next_i] = 10 - (next_phase[next_i] % 10)
    return next_phase


def part_one(input_arr: list[str]) -> str:
    arr = [int(x) for x in input_arr[0]]
    for _ in range(100):  # ~3 seconds
        arr = fft(arr)
    return "".join(str(a) for a in arr[:8])


def part_two(input_arr: list[str]) -> str: ...


input_arr: list[str] = open("advent_2019_day_16.txt").read().splitlines()

print("Advent of Code 2019 - Day 16")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
