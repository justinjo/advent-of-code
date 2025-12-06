from copy import deepcopy


def format_input(arr: list[int], noun: int = 12, verb: int = 2) -> None:
    arr[1] = noun
    arr[2] = verb


def execute(arr: list[int]) -> None:
    i = 0
    while True:
        opcode = arr[i]
        if opcode == 99:
            break
        input_1 = arr[i + 1]
        input_2 = arr[i + 2]
        location = arr[i + 3]
        if opcode == 1:
            arr[location] = arr[input_1] + arr[input_2]
        elif opcode == 2:
            arr[location] = arr[input_1] * arr[input_2]
        i += 4


def part_one(input_arr: list[str]) -> int:
    arr = [int(x) for x in input_arr[0].split(",")]
    format_input(arr)
    execute(arr)
    return arr[0]


def part_two(input_arr: list[str]) -> int:
    arr = [int(x) for x in input_arr[0].split(",")]
    for noun in range(0, 100):
        for verb in range(0, 100):
            memory = deepcopy(arr)
            format_input(memory, noun, verb)
            execute(memory)
            if memory[0] == 19690720:
                return 100 * noun + verb
    return -1


input_arr: list[str] = open("advent_2019_day_02.txt").read().splitlines()

print("Advent of Code 2019 - Day 02")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
