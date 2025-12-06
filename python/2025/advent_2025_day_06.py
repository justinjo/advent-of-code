def array_product(arr: list[str]) -> int:
    return eval("*".join(map(str, arr)))


def part_one(input_arr: list[str]) -> int:
    arr = [[x for x in l.split(" ") if x] for l in input_arr]  # trim whitespace
    total = 0
    for col in range(len(arr[0])):
        operands = [arr[row][col] for row in range(len(arr) - 1)]
        if arr[-1][col] == "+":
            total += sum([int(op) for op in operands])
        elif arr[-1][col] == "*":
            total += array_product(operands)
    return total


def part_two(input_arr: list[str]) -> int:
    operator_i = operand_i = len(input_arr[0]) - 1  # read right to left
    total = 0
    while operator_i >= 0 and operand_i >= 0:
        # get operator
        while operator_i >= 0 and input_arr[-1][operator_i] == " ":
            operator_i -= 1
        operator = input_arr[-1][operator_i]
        operator_i -= 1

        # get operands, looping until the operator column
        operands = []
        while operand_i > operator_i:
            operand = 0
            for row in range(len(input_arr) - 1):
                if input_arr[row][operand_i] != " ":
                    operand = int(input_arr[row][operand_i]) + operand * 10
            operands.append(operand)
            operand_i -= 1
        operand_i -= 1  # skip column of all whitespace

        if operator == "+":
            total += sum(operands)
        elif operator == "*":
            total += array_product(operands)
    return total


input_arr: list[str] = open("advent_2025_day_06.txt").read().splitlines()

print("Advent of Code 2025 - Day 06")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
