from advent_day import AdventDay
from .intcode import Intcode
from collections import defaultdict, deque

class Tile:
    BLACK = 0
    WHITE = 1

    def __init__(self, color: int = BLACK) -> None:
        self.color = color
        self.history = []

    def paint(self, color: int) -> None:
        self.history.append(self.color)
        self.color = color

    def was_painted(self) -> bool:
        return bool(self.history)


class Advent2019Day11(AdventDay):
    DIRECTIONS: list[tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def paint_tiles(self, start_color: int = Tile.BLACK) -> dict[tuple[int, int], Tile]:
        x = y = dir_i = 0
        tile_map = defaultdict(Tile)
        tile_map[(x, y)] = Tile(start_color)
        queue_in=deque([start_color])
        queue_out = deque()
        ic = Intcode(
            memory=self.input_int_array,
            queue_in=queue_in,
            queue_out=queue_out,
        )
        while not ic.finished_execution():
            ic.execute()
            color = queue_out.popleft()
            tile = tile_map[(x, y)]
            tile.paint(color)
            # change directions and add args
            dir_change = 1 if queue_out.popleft() else -1
            dir_i = (dir_i + dir_change) % len(self.DIRECTIONS)
            x += self.DIRECTIONS[dir_i][0]
            y += self.DIRECTIONS[dir_i][1]
            queue_in.append(tile_map[(x, y)].color)
        return tile_map

    def print_tile_map(self, tile_map: dict[tuple[int, int], Tile]) -> None:
        # sort coords by y val
        coords = sorted(sorted(tile_map), key=lambda c: c[1], reverse=True)
        min_x = min(coords)[0]
        row = ''
        prev_y =  None
        for x, y in coords:
            if y != prev_y: # new line
                print(row)
                row = ''
                i = 0 # align all values when printing
                while min_x + i < x:
                    row += ' '
                    i += 1
            row += '#' if tile_map[(x, y)].color == Tile.WHITE else ' '
            prev_y = y
        print(row + '\n')

    def part_one(self) -> int:
        self._convert_input_to_int()
        return len([t for t in self.paint_tiles().values() if t.was_painted()])

    def part_two(self) -> str:
        self._convert_input_to_int()
        self.print_tile_map(self.paint_tiles(Tile.WHITE))
        return 'See above'


Advent2019Day11().run()