from advent_day import AdventDay

class Advent2025Day02(AdventDay):

    def parse_input(self) -> list[tuple[int, int]]:
        ranges = []
        input_str = self.input_str_array[0]
        range_strings = input_str.split(',')
        for rs in range_strings:
            lo, hi = rs.split('-')
            ranges.append((int(lo), int(hi)))
        return ranges

    def get_next_invalid_id(self, id: int) -> int:
        # input must be invalid id: even # digits, pattern repeated twice
        id_str = str(id)
        sequence = int(id_str[:len(id_str) // 2])
        return int(str(sequence + 1) * 2)

    def get_lowest_invalid_id_gte_length(self, length: int) -> int:
        if length % 2:
            length += 1 # invalid ids must be even
        sequence = '1' + '0' * ((length // 2) - 1)
        return int(sequence * 2)

    def part_one(self) -> int:
        invalid_ids = []
        ranges = self.parse_input()
        for lo, hi in ranges:
            id = self.get_lowest_invalid_id_gte_length(len(str(lo)))
            while id <= hi:
                if id >= lo:
                    invalid_ids.append(id)
                id = self.get_next_invalid_id(id)
        return sum([int(i) for i in invalid_ids])

    def part_two(self) -> int:
        ...


Advent2025Day02().run()