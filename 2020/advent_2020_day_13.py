from advent_day import AdventDay

class Advent2020Day13(AdventDay):

    def _parse_input(self, s: list[str]) -> tuple[int, list[int]]:
        arrival_time = int(s[0])
        busses = s[1].split(',')
        active_busses = []
        for b in busses:
            if b.isnumeric():
                active_busses.append(int(b))
        return (arrival_time, active_busses)

    def _get_closest_bus_time(self, arrival_time: int, bus: int) -> int:
        return (arrival_time // bus + 1) * bus

    def part_one(self) -> int:
        arrival_time, active_busses = self._parse_input(self.input_str_array)
        min_departure_time = float('inf')
        min_bus = 0
        for bus in active_busses:
            departure_time = self._get_closest_bus_time(arrival_time, bus)
            if min_departure_time > departure_time:
                min_departure_time = departure_time
                min_bus = bus
        return (int(min_departure_time) - arrival_time) * min_bus

    def part_two(self) -> int:
        ...


Advent2020Day13().run()