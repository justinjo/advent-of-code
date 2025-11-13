from advent_day import AdventDay

class Advent2019Day03(AdventDay):

    def _get_steps(self, direction: str) -> int:
        return int(direction[1:])

    def _get_coord(
        self,
        cardinality: str,
        steps: int,
        origin_x: int,
        origin_y: int,
    ) -> tuple[int, int]:
        if cardinality == "R":
            return (origin_x + steps, origin_y)
        elif cardinality == "U":
            return (origin_x, origin_y + steps)
        elif cardinality == "L":
            return (origin_x - steps, origin_y)
        else: # cardinality == "D":
            return (origin_x, origin_y - steps)

    def _manhattan_distance(self, coord: tuple[int, int]) -> int:
        return abs(coord[0]) + abs(coord[1])

    def _closest_coord_to_origin(self, coord_1: tuple, coord_2: tuple) -> tuple:
        return coord_1 if self._manhattan_distance(coord_1) > self._manhattan_distance(coord_2) else coord_2

    def part_one(self) -> int:
        wire_1 = self.input_str_array[0]
        wire_2 = self.input_str_array[1]
        visited_coords = set()
        current_coord = (0, 0)
        min_distance = float('inf')

        # map out wire_1's path
        for direction in wire_1.split(','):
            steps = self._get_steps(direction)
            cardinality = direction[0]
            for i in range(1, steps+1):
                coord = self._get_coord(
                    cardinality,
                    i,
                    current_coord[0],
                    current_coord[1],
                )
                visited_coords.add(coord)
            current_coord = self._get_coord(
                    cardinality,
                    steps,
                    current_coord[0],
                    current_coord[1],
            )

        # map out wire_2's path
        current_coord = (0, 0)
        for direction in wire_2.split(','):
            steps = self._get_steps(direction)
            cardinality = direction[0]
            for i in range(1, steps+1):
                coord = self._get_coord(
                    cardinality,
                    i,
                    current_coord[0],
                    current_coord[1],
                )
                if coord in visited_coords:
                    min_distance = min(
                        min_distance,
                        self._manhattan_distance(coord)
                    )
            current_coord = self._get_coord(
                    cardinality,
                    steps,
                    current_coord[0],
                    current_coord[1],
            )

        return int(min_distance)

    def part_two(self) -> int:
        wire_1 = self.input_str_array[0]
        wire_2 = self.input_str_array[1]
        # maps coord tuple to # of steps wire_1 took to arrive there
        visited_coords = {}
        total_steps = 0
        current_coord = (0, 0)
        min_steps = float('inf')

        # map out wire_1's path
        for direction in wire_1.split(','):
            steps = self._get_steps(direction)
            cardinality = direction[0]
            for i in range(1, steps+1):
                coord = self._get_coord(
                    cardinality,
                    i,
                    current_coord[0],
                    current_coord[1],
                )
                if coord not in visited_coords:
                    visited_coords[coord] = total_steps+i
            current_coord = self._get_coord(
                    cardinality,
                    steps,
                    current_coord[0],
                    current_coord[1],
            )
            total_steps += steps

        # map out wire_2's path
        current_coord = (0, 0)
        total_steps = 0
        for direction in wire_2.split(','):
            steps = self._get_steps(direction)
            cardinality = direction[0]
            for i in range(1, steps+1):
                coord = self._get_coord(
                    cardinality,
                    i,
                    current_coord[0],
                    current_coord[1],
                )
                if coord in visited_coords:
                    min_steps = min(
                        min_steps,
                        total_steps + i + visited_coords[coord]
                    )
            current_coord = self._get_coord(
                    cardinality,
                    steps,
                    current_coord[0],
                    current_coord[1],
            )
            total_steps += steps

        return int(min_steps)


Advent2019Day03().run()