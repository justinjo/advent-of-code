from advent_day import AdventDay

class Advent2020Day13(AdventDay):

    def _parse_input(self, s: list[str]) -> tuple[int, list[tuple[int, int]]]:
        arrival_time = int(s[0])
        buses = s[1].split(',')
        active_buses = []
        for i, b in enumerate(buses):
            if b.isnumeric():
                active_buses.append((i, int(b)))
        return (arrival_time, active_buses)

    def _get_closest_bus_time(self, arrival_time: int, bus: int) -> int:
        return (arrival_time // bus + 1) * bus

    def _product(self, arr: list[int]) -> int:
        product = 1
        for elem in arr:
            product *= elem
        return product

    def _chinese_remainder_theorem(self, buses: list[tuple[int, int]]) -> int:
        """
        NOTE: well, this doesn't work - it finds a timestamp that satisfies
        the requirements, but not the earliest one that does.

        this doesn't strictly use the chinese remainder theorem but:

        we have buses: [b_0, b_1, ... b_i, ... b_N-1, b_N]

        and a timestamp t such that for i=[0,N]: t mod b_i != 0
        (this is a slight simplification, there's an edge case where b_i < i)

        we can construct a series of N products that add up to t:
            t = p_0 + p_1 + ... p_i ... + p_N-1 + p_N

        according to the problem statement, for products p_i where i=[0,N]:
            p_i mod b_0 = 0
            p_i mod b_i != 0 (NOTE: same edge case as above)
        conversely: p_i mod b_x = 0 for all x != i

        if all b are coprime, this product satisfies those requirements:
            p_i = b_0 * b_1 * ... b_i-1 * b_i+1 ... * b_N-1 * b_N
                = product(b for b in buses) // b_i
        dividing b_i from the total product allows p_i to be the only
        term from t to be nonzero in (t mod b_i)

        now we want to find c_i satisfying: (c_i * p_i) mod b_i = i
        to do so, we take the inverse modulo power of p_i:
            (imp_i * p_i) mod b_i = 1
            i * (imp_i * p_i) mod b_i = i
            c_i = i * imp_i
        """
        total_product = self._product([b[1] for b in buses])
        products = [total_product] * len(buses)
        for p_index, bus_tuple in enumerate(buses):
            # products = [p_0, ... p_i, ... p_N]
            # p_i: products[p_index]
            # i: b_index
            # b_i: bus

            # First bus must have a modulo of 0
            if p_index == 0:
                continue

            b_index, bus = bus_tuple
            products[p_index] //= bus

            # need to solve for case where i > b_i
            # target = bus_index if bus_index < bus else bus_index % bus
            modulo = bus if bus > b_index else ((b_index // bus) + 1) * bus
            products[p_index] *= pow(products[p_index], -1, modulo) * b_index

        return sum(products)

    def _get_earliest_timestamp(self, buses: list[tuple[int, int]]) -> int:
        timestamp = 0
        increment = 1
        for index, bus in buses:
            # in order for a timestamp to satisfy the requirement for bus_i,
            # timestamp + index must be a multiple of bus_i's departure frequency
            while (timestamp + index) % bus != 0:
                timestamp += increment
            # increase the increment to shorten search times
            # the increment can be multiplied by the bus we just found a solution
            # for- this preserves the relationship of timestamp + i being a
            # multiple of bus_i's frequency
            increment *= bus
        return timestamp

    def part_one(self) -> int:
        arrival_time, active_buses = self._parse_input(self.input_str_array)
        min_departure_time = float('inf')
        min_bus = 0
        for _, bus in active_buses:
            departure_time = self._get_closest_bus_time(arrival_time, bus)
            if min_departure_time > departure_time:
                min_departure_time = departure_time
                min_bus = bus
        return (int(min_departure_time) - arrival_time) * min_bus

    def part_two(self) -> int:
        _, active_buses = self._parse_input(self.input_str_array)
        return self._get_earliest_timestamp(active_buses)


Advent2020Day13().run()