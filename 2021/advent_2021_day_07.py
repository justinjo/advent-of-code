from advent_day import AdventDay
from collections import Counter

class Advent2021Day07(AdventDay):

    sigma_arr = [0]

    def get_sigma(self, val: int) -> int:
        if val >= len(self.sigma_arr):
            for i in range(len(self.sigma_arr), val + 1):
                self.sigma_arr.append(self.sigma_arr[-1] + i)
        return self.sigma_arr[val]

    def calculate_fuel(self, fewer: Counter, greater: Counter) -> int:
        fuel = 0
        for pos in fewer:
            fuel += self.get_sigma(pos) * fewer[pos]
        for pos in greater:
            fuel += self.get_sigma(pos) * greater[pos]
        return fuel


    def part_one(self) -> int:
        self._convert_input_to_int()
        sorted_arr = sorted(self.input_int_array)
        fuel = sum(sorted_arr)
        fewer = 0 # num crabs with position less than pos
        greater = len(sorted_arr) # num crabs with position greater than pos
        min_fuel = fuel
        i = 0
        # pos is position checked against all crabs
        for pos in range(sorted_arr[-1] + 1):
            while i < len(sorted_arr) and sorted_arr[i] <= pos:
                fewer += 1
                greater -= 1
                i += 1
            fuel += fewer - greater
            min_fuel = min(fuel, min_fuel)
        return min_fuel

    def part_two(self) -> int:
        # self._convert_input_to_int()
        max_val = max(sorted(self.input_int_array))
        fewer = Counter() # num crabs n positions less than pos
        greater = Counter(self.input_int_array) # num crabs n positions greater than pos
        min_fuel = float('inf')
        # pos is position checked against all crabs
        for _ in range(max_val + 1):
            fewer[0] = greater[0]
            for pos in range(max(sorted(greater)) + 1):
                greater[pos] = greater[pos+1]
            for pos in reversed(range(max(sorted(fewer)) + 2)):
                fewer[pos] = fewer[pos-1]
            min_fuel = min(self.calculate_fuel(fewer, greater), min_fuel)
        return int(min_fuel)


Advent2021Day07().run()