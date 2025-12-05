from advent_day import AdventDay
from collections import Counter

class DiagnosticReport:

    def __init__(self, bits: int = 12) -> None:
        self.values: list[str] = []
        self.bits = bits

    def intake_binary_string(self, num: str) -> None:
        self.values.append(num)
        if len(num) != self.bits:
            self.bits = len(num)

    def _get_bit_counts(self, arr: list[str]) -> list[Counter]:
        bit_counts: list[Counter] = []
        for _ in range(self.bits):
            bit_counts.append(Counter())
        for bin_str in arr:
            for i, c in enumerate(bin_str):
                bit_counts[i][c] += 1
        return bit_counts

    def get_gamma_rate(self, arr: list[str] = []) -> str:
        # amma rate has most common bit in each position
        if not arr:
            arr = self.values
        gamma_rate = ''
        bit_counts = self._get_bit_counts(arr)
        for c in bit_counts:
            gamma_rate += c.most_common(1)[0][0]
        return gamma_rate

    def get_epsilon_rate(self, arr: list[str] = []) -> str:
        # epsilon rate is least common bit in each position
        if not arr:
            arr = self.values
        epsilon_rate = ''
        bit_counts = self._get_bit_counts(arr)
        for c in bit_counts:
            epsilon_rate += '0' if c['0'] < c['1'] else '1'
        return epsilon_rate

    def get_power_consumption(self) -> int:
        gamma_rate = int(self.get_gamma_rate(), 2)
        epsilon_rate = int(self.get_epsilon_rate(), 2)
        return gamma_rate * epsilon_rate

    def get_oxygen_generator_rating(self) -> str:
        # oxygen generator rating is most common bit with sequential elimination
        values = self.values
        for i in range(self.bits):
            next_values = []
            bit_counts = self._get_bit_counts(values)
            bit = '0' if bit_counts[i]['0'] > bit_counts[i]['1'] else '1'
            for val in values:
                if val[i] == bit:
                    next_values.append(val)
            values = next_values
            # stop process if only one value remains
            if len(values) == 1:
                return values[0]
        return values[0]

    def get_co2_scrubber_rating(self) -> str:
        # co2 scrubber rating is least common bit with sequential elimination
        values = self.values
        for i in range(self.bits):
            next_values = []
            bit_counts = self._get_bit_counts(values)
            bit = '0' if bit_counts[i]['0'] <= bit_counts[i]['1'] else '1'
            for val in values:
                if val[i] == bit:
                    next_values.append(val)
            values = next_values
            # stop process if only one value remains
            if len(values) == 1:
                return values[0]
        return values[0]

    def get_life_support_rating(self) -> int:
        oxygen_generator_rating = int(self.get_oxygen_generator_rating(), 2)
        co2_scrubber_rating = int(self.get_co2_scrubber_rating(), 2)
        return oxygen_generator_rating * co2_scrubber_rating


class Advent2021Day03(AdventDay):

    def part_one(self) -> int:
        dr = DiagnosticReport()
        for num in self.input_str_array:
            dr.intake_binary_string(num)
        return dr.get_power_consumption()

    def part_two(self) -> int:
        dr = DiagnosticReport()
        for num in self.input_str_array:
            dr.intake_binary_string(num)
        return dr.get_life_support_rating()


Advent2021Day03().run()