from collections import defaultdict
from math import sqrt

type Coord = tuple[int, int, int]


def get_distance(c1: Coord, c2: Coord) -> float:
    return sqrt(sum([(c1[i] - c2[i]) ** 2 for i in range(3)]))


def part_one(input_arr: list[str]) -> int:
    coords = [(int(x), int(y), int(z)) for x, y, z in [s.split(",") for s in input_arr]]

    # calculate and sort distances
    distance_coord_pairs = []
    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            distance = get_distance(coords[i], coords[j])
            distance_coord_pairs.append((distance, coords[i], coords[j]))
    distance_coord_pairs.sort()

    # create graph
    coord_graph = {}
    for c in coords:
        coord_graph[c] = set()
    for distance, c1, c2 in distance_coord_pairs[:1000]:
        coord_graph[c1].add(c2)
        coord_graph[c2].add(c1)

    # traverse graph to create circuits
    circuits = []
    visited = set()
    for coord in coords:
        if coord in visited:
            continue
        circuit = set()
        queue = [coord]
        while queue:
            c = queue.pop()
            if c in visited:
                continue
            circuit.add(c)
            visited.add(c)
            queue.extend(list(coord_graph[c]))
        circuits.append(circuit)

    # return product of 3 largest circuit sizes
    circuit_sizes = sorted([len(cir) for cir in circuits], reverse=True)
    return circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2]


def part_two(input_arr: list[str]) -> int: ...


input_arr: list[str] = open("advent_2025_day_08.txt").read().splitlines()

print("Advent of Code 2025 - Day 08")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
