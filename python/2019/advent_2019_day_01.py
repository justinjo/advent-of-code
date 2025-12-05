from advent_day import AdventDay

class Advent2019Day01(AdventDay):

    def _fuel_calc(self, mass: int) -> int:
        return mass//3 - 2

    def part_one(self) -> int:
        self._convert_input_to_int()
        return sum([self._fuel_calc(mass) for mass in self.input_int_array])

    def part_two(self) -> int:
        self._convert_input_to_int()
        total_fuel = 0
        mass_fuel = 0
        incremental_fuel = 0
        for mass in self.input_int_array:
            incremental_fuel = self._fuel_calc(mass)
            while incremental_fuel > 0:
                mass_fuel += incremental_fuel
                incremental_fuel = self._fuel_calc(incremental_fuel)
            total_fuel += mass_fuel
            incremental_fuel = mass_fuel = 0
        return total_fuel


Advent2019Day01().run()