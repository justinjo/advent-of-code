def fuel_calc(mass: int) -> int:
    return mass // 3 - 2

def part_one(input_arr: list[str]) -> int:
    arr = [int(x) for x in input_arr]
    return sum([fuel_calc(mass) for mass in arr])

def part_two(input_arr: list[str]) -> int:
    arr = [int(x) for x in input_arr]
    total_fuel = 0
    for mass in arr:
        mass_fuel = 0
        incremental_fuel = fuel_calc(mass)
        while incremental_fuel > 0:
            mass_fuel += incremental_fuel
            incremental_fuel = fuel_calc(incremental_fuel)
        total_fuel += mass_fuel
    return total_fuel

input_arr: list[str] = open('advent_2019_day_01.txt').read().splitlines()

print('Advent of Code 2019 - Day 01')
print(f'Part One: {part_one(input_arr)}')
print(f'Part Two: {part_two(input_arr)}')