from advent_day import AdventDay
from collections import defaultdict

type Coord = tuple[int, int]

class Advent2018Day06(AdventDay):

    INVALID_COORD = (-1, -1)

    def _parse_input(self) -> list[Coord]:
        coords = []
        for line in self.input_str_array:
            col, row = [int(l) for l in line.split(', ')]
            coords.append((col, row))
        return coords

    def _max_coord(self, coords: list[Coord]) -> Coord:
        max_col = max_row = 0
        for col, row in coords:
            max_col = max(max_col, col)
            max_row = max(max_row, row)
        return (max_col, max_row)

    def _get_distances(
        self,
        coords: list[Coord],
        col: int,
        row: int,
    ) -> dict[int, list[Coord]]:
        # map of manhattan distances to a list of tuple coords
        distances_coords_map = defaultdict(list)
        for coord in coords:
            distance = self._manhattan_distance((col, row), coord)
            distances_coords_map[distance].append(coord)
        return distances_coords_map

    def _manhattan_distance(self, c_1: Coord, c_2: Coord) -> int:
        return abs(c_1[0] - c_2[0]) + abs(c_1[1] - c_2[1])

    def _get_closest(self, distances_coords_map: dict[int, list[Coord]]) -> Coord:
        min_distance = min(distances_coords_map.keys())
        num_closest = len(distances_coords_map[min_distance])
        return distances_coords_map[min_distance][0] if num_closest == 1 else self.INVALID_COORD

    def part_one(self) -> int:
        coords = self._parse_input()
        max_col, max_row = self._max_coord(coords)
        coord_area_map = defaultdict(int)
        border_coords = set()

        for r in range(max_row + 1):
            for c in range(max_col + 1):
                distances_coords_map = self._get_distances(coords, c, r)
                closest_coord = self._get_closest(distances_coords_map)
                if closest_coord != self.INVALID_COORD:
                    # ignore coords with area extending past the border
                    if c == 0 or c == max_col or r == 0 or r == max_row:
                        border_coords.add(closest_coord)
                    coord_area_map[closest_coord] += 1

        max_area = 0
        for coord in coord_area_map:
            if coord not in border_coords and coord_area_map[coord] > max_area:
                max_area = coord_area_map[coord]
        return max_area

    def part_two(self) -> int:
        ...


Advent2018Day06().run()