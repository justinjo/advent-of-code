from advent_day import AdventDay
from collections import Counter

class Diagnostic:

    def __init__(self, bits: int = 12) -> None:
        self.bit_counts: list[Counter] = []
        for _ in range(bits):
            self.bit_counts.append(Counter())

    def intake_binary_string(self, num: str) -> None:
        for i, c in enumerate(num):
            self.bit_counts[i][c] += 1

    def get_gamma_rate(self) -> int:
        # amma rate has most common bit in each position
        gamma_rate = ''
        for c in self.bit_counts:
            gamma_rate += c.most_common(1)[0][0]
        return int(gamma_rate, 2)

    def get_epsilon_rate(self) -> int:
        # epsilon rate is least common bit in each position
        epsilon_rate = ''
        for c in self.bit_counts:
            epsilon_rate += '0' if c['0'] < c['1'] else '1'
        return int(epsilon_rate, 2)


class Advent2021Day03(AdventDay):

    def part_one(self) -> int:
        diagnostic = Diagnostic()
        for num in self.input_str_array:
            diagnostic.intake_binary_string(num)
        gamma_rate = diagnostic.get_gamma_rate()
        epsilon_rate = diagnostic.get_epsilon_rate()
        return gamma_rate * epsilon_rate

    def part_two(self) -> int:
        ...


Advent2021Day03().run()