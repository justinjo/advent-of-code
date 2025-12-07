from collections import defaultdict

type Coord = tuple[int, int]


INVALID_COORD = (-1, -1)


def parse_input(input_arr: list[str]) -> list[Coord]:
    coords = []
    for line in input_arr:
        col, row = [int(l) for l in line.split(", ")]
        coords.append((col, row))
    return coords


def max_coord(coords: list[Coord]) -> Coord:
    max_col = max_row = 0
    for col, row in coords:
        max_col = max(max_col, col)
        max_row = max(max_row, row)
    return (max_col, max_row)


def get_distances(
    coords: list[Coord],
    col: int,
    row: int,
) -> dict[int, list[Coord]]:
    # map of manhattan distances to a list of tuple coords
    distances_coords_map = defaultdict(list)
    for coord in coords:
        distance = manhattan_distance((col, row), coord)
        distances_coords_map[distance].append(coord)
    return distances_coords_map


def manhattan_distance(c_1: Coord, c_2: Coord) -> int:
    return abs(c_1[0] - c_2[0]) + abs(c_1[1] - c_2[1])


def get_closest(distances_coords_map: dict[int, list[Coord]]) -> Coord:
    min_distance = min(distances_coords_map.keys())
    num_closest = len(distances_coords_map[min_distance])
    return distances_coords_map[min_distance][0] if num_closest == 1 else INVALID_COORD


def within_distance(
    distances_coords_map: dict[int, list[Coord]],
    max_distance: int = 10000,
) -> bool:
    distance = 0
    for d in distances_coords_map:
        distance += d * len(distances_coords_map[d])
    return distance < max_distance


def part_one(input_arr: list[str]) -> int:
    coords = parse_input(input_arr)
    max_col, max_row = max_coord(coords)
    coord_area_map = defaultdict(int)
    border_coords = set()

    for r in range(max_row + 1):
        for c in range(max_col + 1):
            distances_coords_map = get_distances(coords, c, r)
            closest_coord = get_closest(distances_coords_map)
            if closest_coord != INVALID_COORD:
                # ignore coords with area extending past the border
                if c == 0 or c == max_col or r == 0 or r == max_row:
                    border_coords.add(closest_coord)
                coord_area_map[closest_coord] += 1

    max_area = 0
    for coord in coord_area_map:
        if coord not in border_coords and coord_area_map[coord] > max_area:
            max_area = coord_area_map[coord]
    return max_area


def part_two(input_arr: list[str]) -> int:
    coords = parse_input(input_arr)
    max_col, max_row = max_coord(coords)
    safe_area = 0

    for r in range(max_row):
        for c in range(max_col):
            distances_coords_map = get_distances(coords, c, r)
            if within_distance(distances_coords_map):
                safe_area += 1

    return safe_area


input_arr: list[str] = open("advent_2018_day_06.txt").read().splitlines()

print("Advent of Code 2018 - Day 06")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
