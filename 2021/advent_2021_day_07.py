from advent_day import AdventDay

class Advent2021Day07(AdventDay):

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
        ...


Advent2021Day07().run()