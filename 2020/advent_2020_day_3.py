from advent_day import AdventDay

class Advent2020Day3(AdventDay):
    TREE = "#"

    def _calc_trees(self, rise: int, fall: int) -> int:
        arr = self.input_str_array
        rows = self.input_length
        cols = len(arr[0])
        r = c = trees = 0
        while r < rows:
            if arr[r][c] == self.TREE:
                trees += 1
            r += fall
            c = (c + rise) % cols
        return trees

    def part_one(self) -> int:
        return self._calc_trees(3, 1)

    def part_two(self) -> int:
        return (
            self._calc_trees(1, 1) *
            self._calc_trees(3, 1) *
            self._calc_trees(5, 1) *
            self._calc_trees(7, 1) *
            self._calc_trees(1, 2)
        )


Advent2020Day3().run()