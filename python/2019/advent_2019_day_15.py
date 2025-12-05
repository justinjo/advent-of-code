from advent_day import AdventDay
from .intcode import Intcode
from collections import deque
from enum import Enum, IntEnum
from dataclasses import dataclass
from copy import deepcopy
import os
import time

type CoordType = tuple[int, int] | tuple

class TileDisplay(Enum):
    UNVISITED = '?'
    EMPTY = ' '
    WALL = '#'

class TileType(IntEnum):
    WALL = 0
    EMPTY = 1
    OXYGEN = 2

class Movement(IntEnum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4

@dataclass
class Coord:
    coord: CoordType
    distance: int
    tile: TileType


class Droid:

    MOVEMENT_TO_COORD_MAP = {
        Movement.NORTH: (0, 1),
        Movement.SOUTH: (0, -1),
        Movement.WEST: (-1, 0),
        Movement.EAST: (1, 0),
    }

    OPPOSING_MOVEMENT_MAP = {
        Movement.NORTH: Movement.SOUTH,
        Movement.SOUTH: Movement.NORTH,
        Movement.EAST: Movement.WEST,
        Movement.WEST: Movement.EAST,
    }

    def __init__(self, ic_program: list[int], silenced: bool = True) -> None:
        self.queue_in = deque()
        self.queue_out = deque()
        self.ic = Intcode(
            memory=ic_program,
            queue_in=self.queue_in,
            queue_out=self.queue_out,
        )
        self.current_coord: CoordType = (0, 0)
        self.coord_map: dict[CoordType, Coord] = {
            self.current_coord: Coord(self.current_coord, 0, TileType.EMPTY)
        }
        self.silenced = silenced
        self.oxygen_coords: CoordType = ()
        self.unexplored_coord_state_map = {}

    def print(self) -> None:
        x_lo = y_lo = -25
        x_hi = y_hi = 25
        os.system('clear')
        print('map')
        for y in range(y_hi, y_lo - 1, -1):
            line = ''
            for x in range(x_lo, x_hi + 1):
                if (x, y) == self.current_coord:
                    line += 'X'
                elif y in (y_lo, y_hi) or x in (x_lo, x_hi):
                    line += '+'
                elif (x, y) in self.coord_map:
                    line += '#' if self.coord_map[(x, y)].tile == TileType.WALL else '.'
                else:
                    line += ' '
            print(line)
        time.sleep(.01)
        print()

    def move(self, direction: Movement) -> bool:
        moved = False
        x, y = self.current_coord
        x_d, y_d = self.MOVEMENT_TO_COORD_MAP[direction]
        travel_coord = (x + x_d, y + y_d)
        self.queue_in.append(direction)
        self.ic.execute()
        output = self.queue_out.popleft()

        if travel_coord not in self.coord_map:
            self.coord_map[travel_coord] = Coord(
                travel_coord,
                self.coord_map[(x, y)].distance + 1, # will never be used for calc if wall
                output,
            )
        else:
            self.coord_map[travel_coord].distance = min(
                self.coord_map[(x, y)].distance + 1,
                self.coord_map[travel_coord].distance,
            )

        if output in (1, 2):
            self.current_coord = travel_coord
            moved = True
            if output == 2:
                self.oxygen_coords = travel_coord
        if not self.silenced:
            self.print()
        return moved

    def search_one(self, prev_movement: Movement | None = None) -> Movement | None:
        successful_move = None
        for direction in Movement:
            if direction == prev_movement:
                continue
            if self.move(direction):
                self.move(self.OPPOSING_MOVEMENT_MAP[direction])
                if not successful_move:
                    successful_move = direction
                else:
                    self.unexplored_coord_state_map[self.current_coord] = {
                        'direction': direction,
                        'memory': deepcopy(self.ic.memory),
                    }
        return successful_move

    def search(self) -> None:
        prev_move = next_move = None
        while not self.oxygen_coords or self.unexplored_coord_state_map:
            next_move = self.search_one(prev_move)
            if not next_move:
                next_coord = next(iter(self.unexplored_coord_state_map))
                self.current_coord = next_coord
                self.ic.memory = self.unexplored_coord_state_map[next_coord]['memory']
                next_move = self.unexplored_coord_state_map[next_coord]['direction']
                del self.unexplored_coord_state_map[next_coord]
            self.move(next_move)
            prev_move = self.OPPOSING_MOVEMENT_MAP[next_move] if next_move else None

    def oxygen_distance(self) -> int:
        return self.coord_map[self.oxygen_coords].distance

    def fill_oxygen(self) -> int:
        fill_coords = [self.oxygen_coords]
        visited = set()
        minutes = -1
        while fill_coords:
            next_layer = []
            while fill_coords:
                x, y = fill_coords.pop()
                for x_d, y_d in self.MOVEMENT_TO_COORD_MAP.values():
                    next_coord = (x + x_d, y + y_d)
                    if (
                        next_coord not in visited
                        and next_coord in self.coord_map
                        and self.coord_map[next_coord].tile == TileType.EMPTY
                    ):
                        next_layer.append(next_coord)
                        visited.add(next_coord)
            fill_coords = next_layer
            minutes += 1
        return minutes


class Advent2019Day15(AdventDay):

    def part_one(self) -> int:
        self._convert_input_to_int()
        droid = Droid(ic_program=self.input_int_array)
        droid.search()
        return droid.oxygen_distance()

    def part_two(self) -> int:
        self._convert_input_to_int()
        droid = Droid(ic_program=self.input_int_array)
        droid.search()
        return droid.fill_oxygen()


Advent2019Day15().run()