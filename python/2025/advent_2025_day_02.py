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

    def get_next_invalid_id(self, id: int, repeats: int) -> int:
        # input must be invalid id: pattern repeated x times
        id_str = str(id)
        sequence = int(id_str[:len(id_str) // repeats])
        return int(str(sequence + 1) * repeats)

    def get_lowest_invalid_id_leq_length(self, id_len: int, repeats: int) -> int:
        while id_len % repeats:
            id_len -= 1
        sequence = '1' + '0' * ((id_len // repeats) - 1)
        return int(sequence * repeats)

    def sum_invalid_ids(self, ranges: list[tuple[int, int]], lock_repeats: bool = True) -> int:
        invalid_ids = set()
        for lo, hi in ranges:
            max_repeats = 2 if lock_repeats else len(str(hi))
            for repetitions in range(2, max_repeats + 1):
                id = self.get_lowest_invalid_id_leq_length(len(str(lo)), repetitions)
                while id <= hi:
                    if id >= lo:
                        invalid_ids.add(id)
                    id = self.get_next_invalid_id(id, repetitions)
        return sum([int(i) for i in invalid_ids])

    def part_one(self) -> int:
        return self.sum_invalid_ids(self.parse_input())

    def part_two(self) -> int:
        return self.sum_invalid_ids(self.parse_input(), lock_repeats=False)


Advent2025Day02().run()