def get_steps(turn: str) -> int:
    return int(turn[1:])


def get_coord(origin: tuple[int, int], cardinality: str, steps: int) -> tuple[int, int]:
    x, y = origin
    if cardinality == "R":
        return (x + steps, y)
    elif cardinality == "U":
        return (x, y + steps)
    elif cardinality == "L":
        return (x - steps, y)
    else:  # cardinality == "D":
        return (x, y - steps)


def manhattan_distance(coord: tuple[int, int]) -> int:
    return abs(coord[0]) + abs(coord[1])


def part_one(input_arr: list[str]) -> int:
    wire_1, wire_2 = [l.split(",") for l in input_arr]
    visited_coords = set()
    coord = (0, 0)
    min_distance = float("inf")

    # map out wire_1's path
    for turn in wire_1:
        steps = get_steps(turn)
        cardinality = turn[0]
        for step in range(1, steps + 1):
            visited_coords.add(get_coord(coord, cardinality, step))
        coord = get_coord(coord, cardinality, steps)

    # map out wire_2's path
    coord = (0, 0)
    for turn in wire_2:
        steps = get_steps(turn)
        cardinality = turn[0]
        for _ in range(steps):
            coord = get_coord(coord, cardinality, 1)
            if coord in visited_coords:
                min_distance = min(min_distance, manhattan_distance(coord))

    return int(min_distance)


def part_two(input_arr: list[str]) -> int:
    wire_1, wire_2 = [l.split(",") for l in input_arr]
    # maps coord tuple to # of steps wire_1 took to arrive there
    visited_coords = {}
    total_steps = 0
    coord = (0, 0)
    min_steps = float("inf")

    # map out wire_1's path
    for turn in wire_1:
        steps = get_steps(turn)
        cardinality = turn[0]
        for _ in range(steps):
            coord = get_coord(coord, cardinality, 1)
            total_steps += 1
            if coord not in visited_coords:
                visited_coords[coord] = total_steps

    # map out wire_2's path
    coord = (0, 0)
    total_steps = 0
    for turn in wire_2:
        steps = get_steps(turn)
        cardinality = turn[0]
        for _ in range(steps):
            coord = get_coord(coord, cardinality, 1)
            total_steps += 1
            if coord in visited_coords:
                min_steps = min(total_steps + visited_coords[coord], min_steps)

    return int(min_steps)


input_arr: list[str] = open("advent_2019_day_03.txt").read().splitlines()

print("Advent of Code 2019 - Day 03")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
