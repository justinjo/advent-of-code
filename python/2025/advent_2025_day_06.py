

def part_one(input_arr: list[str]) -> int:
    arr = []
    total_sum = 0
    for l in input_arr:
        row = []
        for op in l.split(' '):
            if op:
                row.append(op)
        arr.append(row)
    for i in range(len(arr[0])):
        n = 0
        if arr[len(arr)-1][i] == '+':
            n = 0
            for j in range(len(arr)-1):
                n += int(arr[j][i])
        else:
            n = 1
            for j in range(len(arr)-1):
                n *= int(arr[j][i])
        print(n)
        total_sum += n
    return total_sum

def part_two(input_arr: list[str]) -> int:
    ...

input_arr: list[str] = open('advent_2025_day_06.txt').read().splitlines()

print('Advent of Code 2025 - Day 06')
print(f'Part One: {part_one(input_arr)}')
print(f'Part Two: {part_two(input_arr)}')