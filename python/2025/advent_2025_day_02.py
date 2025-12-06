def parse_input(input_arr: list[str]) -> list[tuple[int, int]]:
    return [
        (int(lo), int(hi)) for lo, hi in [s.split('-') for s in input_arr[0].split(',')]
    ]

def get_next_invalid_id(id: int, repeats: int) -> int:
    # input must be invalid id: pattern repeated x times
    id_str = str(id)
    sequence = int(id_str[:len(id_str) // repeats])
    return int(str(sequence + 1) * repeats)

def get_lowest_invalid_id_leq_length(id_len: int, repeats: int) -> int:
    while id_len % repeats:
        id_len -= 1
    sequence = '1' + '0' * ((id_len // repeats) - 1)
    return int(sequence * repeats)

def sum_invalid_ids(ranges: list[tuple[int, int]], lock_repeats: bool = True) -> int:
    invalid_ids = set()
    for lo, hi in ranges:
        max_repeats = 2 if lock_repeats else len(str(hi))
        for repetitions in range(2, max_repeats + 1):
            id = get_lowest_invalid_id_leq_length(len(str(lo)), repetitions)
            while id <= hi:
                if id >= lo:
                    invalid_ids.add(id)
                id = get_next_invalid_id(id, repetitions)
    return sum([int(i) for i in invalid_ids])

def part_one(input_arr: list[str]) -> int:
    return sum_invalid_ids(parse_input(input_arr))

def part_two(input_arr: list[str]) -> int:
    return sum_invalid_ids(parse_input(input_arr), lock_repeats=False)

input_arr: list[str] = open('advent_2025_day_02.txt').read().splitlines()

print('Advent of Code 2025 - Day 02')
print(f'Part One: {part_one(input_arr)}')
print(f'Part Two: {part_two(input_arr)}')