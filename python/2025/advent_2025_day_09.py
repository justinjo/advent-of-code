type Coord = tuple[int, int]


def get_size(c1: Coord, c2: Coord) -> int:
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)


def get_size_coord_pairs(coords: list[Coord]) -> list[tuple[int, Coord, Coord]]:
    distance_coord_pairs = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            distance = get_size(coords[i], coords[j])
            distance_coord_pairs.append((distance, coords[i], coords[j]))
    return sorted(distance_coord_pairs)


def part_one(input_arr: list[str]) -> int:
    coords = [(int(x), int(y)) for x, y in [s.split(",") for s in input_arr]]
    size_coord_pairs = get_size_coord_pairs(coords)
    return size_coord_pairs[-1][0]


def part_two(input_arr: list[str]) -> int: ...


input_arr: list[str] = open("advent_2025_day_09.txt").read().splitlines()

print("Advent of Code 2025 - Day 09")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
