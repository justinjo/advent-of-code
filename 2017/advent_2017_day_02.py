from advent_day import AdventDay

class Advent2017Day02(AdventDay):

    def _parse_input(self) -> None:
        self.parsed_input = []
        for line in self.input_str_array:
            self.parsed_input.append([int(l) for l in line.split('\t')])

    def part_one(self) -> int:
        checksum = 0
        self._parse_input()
        for arr in self.parsed_input:
            checksum += max(arr) - min(arr)
        return checksum

    def part_two(self) -> int:
        prodsum = 0
        for arr in self.parsed_input:
            for i in range(len(arr)):
                for j in range(i+1, len(arr)):
                    if arr[i] % arr[j] == 0:
                        prodsum += arr[i] // arr[j]
                    elif arr[j] % arr[i] == 0:
                        prodsum += arr[j] // arr[i]
        return prodsum


Advent2017Day02().run()