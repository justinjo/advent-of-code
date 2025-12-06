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
        total_sum += n
    return total_sum

def part_two(input_arr: list[str]) -> int:
    operator_i = operand_i = total = 0
    is_calculating = True
    while is_calculating:
        # get operator
        while input_arr[-1][operator_i] == ' ':
            operator_i += 1
        operator = input_arr[-1][operator_i]
        operator_i += 1

        # get operands
        operands = []
        digit_found = True
        while digit_found:
            operand = 0
            digit_found = False
            for i in range(len(input_arr) - 1):
                if operand_i >= len(input_arr[0]):
                    continue
                digit = input_arr[i][operand_i]
                if digit == ' ':
                    continue
                digit_found = True
                operand = int(input_arr[i][operand_i]) + operand * 10
            if digit_found:
                operands.append(operand)
            operand_i += 1

        # calculate
        if operator == '+':
            total += sum(operands)
        elif operator == '*':
            product = 1
            for x in operands:
                product *= x
            total += product

        # calc until end reached
        is_calculating = operator_i < len(input_arr[0]) and operand_i < len(input_arr[-1])
    return total

input_arr: list[str] = open('advent_2025_day_06.txt').read().splitlines()

print('Advent of Code 2025 - Day 06')
print(f'Part One: {part_one(input_arr)}')
print(f'Part Two: {part_two(input_arr)}')