from advent_day import AdventDay

class Ship:
    NORTH = 'N'
    EAST = 'E'
    SOUTH = 'S'
    WEST = 'W'
    LEFT = 'L'
    RIGHT = 'R'
    FORWARD = 'F'
    DIRECTIONS = [NORTH, EAST, SOUTH, WEST]
    MOVE = set([NORTH, EAST, SOUTH, WEST, FORWARD])
    TURN = set([LEFT, RIGHT])

    def __init__(
        self,
        direction: str = EAST,
        ship_x: int = 0,
        ship_y: int = 0,
        use_waypoint: bool = False,
        wp_x: int = 0,
        wp_y: int = 0,
    ) -> None:
        self.direction_index = self.DIRECTIONS.index(direction)
        self.start_x = self.x = ship_x
        self.start_y = self.y = ship_y
        self.wp_x = wp_x
        self.wp_y = wp_y
        self.use_waypoint = use_waypoint

    def _move(self, direction: str, value: int) -> None:
        if direction == self.FORWARD:
            direction = self.DIRECTIONS[self.direction_index]
        if direction == self.NORTH:
            self.y += value
        elif direction == self.EAST:
            self.x += value
        elif direction == self.SOUTH:
            self.y -= value
        elif direction == self.WEST:
            self.x -= value
        else:
            raise Exception ('Invalid direction')

    def _move_ship_with_waypoint(self, value: int) -> None:
        self.x += self.wp_x * value
        self.y += self.wp_y * value

    def _move_with_waypoint(self, direction: str, value: int) -> None:
        if direction == self.FORWARD:
            self._move_ship_with_waypoint(value)
        elif direction == self.NORTH:
            self.wp_y += value
        elif direction == self.EAST:
            self.wp_x += value
        elif direction == self.SOUTH:
            self.wp_y -= value
        elif direction == self.WEST:
            self.wp_x -= value
        else:
            raise Exception ('Invalid direction')

    def _turn(self, direction: str, value: int) -> None:
        num_turns = value // 90
        if direction == self.LEFT:
            self.direction_index = (self.direction_index - num_turns) % len(self.DIRECTIONS)
        elif direction == self.RIGHT:
            self.direction_index = (self.direction_index + num_turns) % len(self.DIRECTIONS)

    def _turn_with_waypoint(self, direction: str, value: int) -> None:
        num_clockwise_turns = (value // 90) % 4
        if direction == self.LEFT:
            num_clockwise_turns = (4 - num_clockwise_turns) % 4
        if num_clockwise_turns == 1:
            tmp = self.wp_x
            self.wp_x = self.wp_y
            self.wp_y = -tmp
        elif num_clockwise_turns == 2:
            self.wp_x = -self.wp_x
            self.wp_y = -self.wp_y
        elif num_clockwise_turns == 3:
            tmp = self.wp_x
            self.wp_x = -self.wp_y
            self.wp_y = tmp

    def command(self, action: str, value: int) -> None:
        if action in self.MOVE:
            if self.use_waypoint:
                self._move_with_waypoint(action, value)
            else:
                self._move(action, value)
        elif action in self.TURN:
            if self.use_waypoint:
                self._turn_with_waypoint(action, value)
            else:
                self._turn(action, value)
        else:
            raise Exception('Invalid action')

    def get_direction(self) -> str:
        return self.DIRECTIONS[self.direction_index]

    def get_manhattan_distance_from_start(self) -> int:
        return abs (self.x - self.start_x) + abs(self.y - self.start_y)

    def print_location(self) -> None:
        print(f'N/S: {self.y}, E/W: {self.x}, dir: {self.DIRECTIONS[self.direction_index]}')


class Advent2020Day12(AdventDay):

    def _get_action(self, instruction: str) -> str:
        return instruction[0]

    def _get_value(self, instruction: str) -> int:
        return int(instruction[1:])

    def part_one(self) -> int:
        ship = Ship()
        for command in self.input_str_array:
            action = self._get_action(command)
            value = self._get_value(command)
            ship.command(action, value)
        return ship.get_manhattan_distance_from_start()

    def part_two(self) -> int:
        ship = Ship(use_waypoint=True, wp_x=10, wp_y=1)
        for command in self.input_str_array:
            action = self._get_action(command)
            value = self._get_value(command)
            ship.command(action, value)
        return ship.get_manhattan_distance_from_start()


Advent2020Day12().run()