from collections import defaultdict


def part_one(input_arr: list[str]) -> int:
    orbits = [line.split(")") for line in input_arr]
    orbit_map = defaultdict(list)
    for mass_1, mass_2 in orbits:
        orbit_map[mass_1].append(mass_2)

    queue = ["COM"]
    orbit_level = orbit_count = 0
    while queue:
        next_queue = []
        while queue:
            mass = queue.pop()
            orbit_count += orbit_level
            next_queue.extend(orbit_map[mass])
        orbit_level += 1
        queue = next_queue
    return orbit_count


def part_two(input_arr: list[str]) -> int:
    orbits = [line.split(")") for line in input_arr]
    orbit_map = defaultdict(list)
    for mass_1, mass_2 in orbits:
        orbit_map[mass_1].append(mass_2)
        orbit_map[mass_2].append(mass_1)

    queue = orbit_map["YOU"]
    seen = set(["YOU"])
    jumps = 0
    while "SAN" not in seen:
        next_queue = []
        while queue:
            mass = queue.pop()
            next_queue.extend([m for m in orbit_map[mass] if m not in seen])
            seen.add(mass)
        jumps += 1
        queue = next_queue
    return jumps - 2  # ignore first and last jumps


input_arr: list[str] = open("advent_2019_day_06.txt").read().splitlines()

print("Advent of password 2019 - Day 06")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
