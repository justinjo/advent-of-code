type Coord = tuple[int, int]


def get_rectangle_size(c1: Coord, c2: Coord) -> int:
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)


def get_size_coord_pairs(coords: list[Coord]) -> list[tuple[int, Coord, Coord]]:
    size_coord_pairs = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            size = get_rectangle_size(coords[i], coords[j])
            size_coord_pairs.append((size, coords[i], coords[j]))
    return size_coord_pairs


def line_intersects_rectangle(line_1, line_2, rect_1, rect_2):
    l1, l2 = sorted([line_1, line_2])
    r1 = (min(rect_1[0], rect_2[0]), min(rect_1[1], rect_2[1]))  # bot left of rect
    r2 = (max(rect_1[0], rect_2[0]), max(rect_1[1], rect_2[1]))  # bot right of rect
    if (
        l1[0] == l2[0]  # vertical line
        and r1[0] < l1[0] < r2[0]  # line is between rectangle x coords
        and not (l1[1] >= r2[1] or l2[1] <= r1[1])  # line in rectangle
    ):
        return True
    if (
        l1[1] == l2[1]  # horizontal line
        and r1[1] < l1[1] < r2[1]  # line is between rectangle y coords
        and not (l1[0] >= r2[0] or l2[0] <= r1[0])  # line in rectangle
    ):
        return True
    return False


def part_one(input_arr: list[str]) -> int:
    coords = [(int(x), int(y)) for x, y in [s.split(",") for s in input_arr]]
    size_coord_pairs = get_size_coord_pairs(coords)
    return sorted(size_coord_pairs)[-1][0]


def part_two(input_arr: list[str]) -> int:
    coords = [(int(x), int(y)) for x, y in [s.split(",") for s in input_arr]]
    size_coord_pairs = sorted(get_size_coord_pairs(coords), reverse=True)
    max_size = scp_i = 0
    while not max_size:
        size, rect_1, rect_2 = size_coord_pairs[scp_i]
        scp_i += 1
        is_intersected = False
        c_i = -1
        while not is_intersected and c_i < len(coords) - 1:
            line_1, line_2 = coords[c_i], coords[c_i + 1]  # points on line
            c_i += 1
            if len(set([line_1, line_2, rect_1, rect_2])) != 4:
                continue
            is_intersected = line_intersects_rectangle(line_1, line_2, rect_1, rect_2)
        max_size = size if not is_intersected else 0
    return max_size


input_arr: list[str] = open("advent_2025_day_09.txt").read().splitlines()

print("Advent of Code 2025 - Day 09")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
