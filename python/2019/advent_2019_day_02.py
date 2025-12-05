from advent_day import AdventDay
from copy import deepcopy

class Advent2019Day02(AdventDay):

    def _format_input(self, arr: list[int], noun: int = 12, verb: int = 2) -> None:
        arr[1] = noun
        arr[2] = verb

    def _execute(self, arr: list[int]) -> None:
        i = 0
        while True:
            opcode = arr[i]
            if opcode == 99:
                break
            input_1 = arr[i+1]
            input_2 = arr[i+2]
            location = arr[i+3]
            if opcode == 1:
                arr[location] = arr[input_1] + arr[input_2]
            elif opcode == 2:
                arr[location] = arr[input_1] * arr[input_2]
            i += 4

    def part_one(self, arr: list[int] = []) -> int:
        self._convert_input_to_int()
        arr = deepcopy(self.input_int_array)
        self._format_input(arr)
        self._execute(arr)
        return arr[0]

    def part_two(self) -> int:
        self._convert_input_to_int()
        for n in range(0, 100):
            for v in range(0, 100):
                arr = deepcopy(self.input_int_array)
                self._format_input(arr, n, v)
                self._execute(arr)
                if arr[0] == 19690720:
                    return 100 * n + v
        return -1


Advent2019Day02().run()