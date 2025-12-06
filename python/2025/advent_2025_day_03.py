def sum_joltage(input_arr: list[str], digits: int = 2) -> int:
    total_joltage = 0 # should be doing monotonic stacks but lazy
    for battery in input_arr:
        i = joltage = 0
        arr = [int(x) for x in list(battery)]
        for t in range(digits-1,-1,-1):
            subarr = arr[i:len(arr)-t] # use len to prevent arr[x:0]
            max_digit = max(subarr)
            i += subarr.index(max_digit) + 1
            joltage = joltage * 10 + max_digit
        total_joltage += joltage
    return total_joltage

def part_one(input_arr: list[str]) -> int:
    return sum_joltage(input_arr)

def part_two(input_arr: list[str]) -> int:
    return sum_joltage(input_arr, digits=12)

input_arr: list[str] = open('advent_2025_day_03.txt').read().splitlines()

print('Advent of Code 2025 - Day 03')
print(f'Part One: {part_one(input_arr)}')
print(f'Part Two: {part_two(input_arr)}')