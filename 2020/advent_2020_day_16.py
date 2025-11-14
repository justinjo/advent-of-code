from advent_day import AdventDay

class Advent2020Day16(AdventDay):

    def _parse_input(self) -> None:
        i = 0
        self.ticket_ranges = {}
        while self.input_str_array[i]:
            field, ranges_str = self.input_str_array[i].split(': ')
            range_1_str, range_2_str = ranges_str.split(' or ')
            range_1 = [int(r) for r in range_1_str.split('-')]
            range_2 = [int(r) for r in range_2_str.split('-')]
            self.ticket_ranges[field] = [range_1, range_2] # [[A, B], [C, D]]
            i += 1

        self.my_ticket = self._read_ticket(self.input_str_array[i+2])
        i += 5

        self.nearby_tickets = []
        while i < len(self.input_str_array):
            self.nearby_tickets.append(self._read_ticket(self.input_str_array[i]))
            i += 1

    def _read_ticket(self, ticket: str) -> list[int]:
        return [int(n) for n in ticket.split(',')]

    def _check_value_validity(self, value: int) -> bool:
        for ranges in self.ticket_ranges.values():
            for lo, hi in ranges:
                if lo <= value <= hi:
                    return True
        return False

    def _calculate_ticket_validity(self, ticket: list[int]) -> int:
        error_value = 0
        for t in ticket:
            if not self._check_value_validity(t):
                error_value += t
        return error_value

    def _calculate_ticket_validities(self) -> int:
        error_value = 0
        for ticket in self.nearby_tickets:
            error_value += self._calculate_ticket_validity(ticket)
        return error_value

    def part_one(self) -> int:
        self._parse_input()
        return self._calculate_ticket_validities()

    def part_two(self) -> int:
        ...


Advent2020Day16().run()