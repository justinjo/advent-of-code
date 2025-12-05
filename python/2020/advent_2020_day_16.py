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

    def _is_valid_value(self, value: int) -> bool:
        for ranges in self.ticket_ranges.values():
            for lo, hi in ranges:
                if lo <= value <= hi:
                    return True
        return False

    def _is_valid_ticket(self, ticket: list[int]) -> bool:
        for t in ticket:
            if not self._is_valid_value(t):
                return False
        return True

    def _calculate_ticket_validity(self, ticket: list[int]) -> int:
        error_value = 0
        for t in ticket:
            if not self._is_valid_value(t):
                error_value += t
        return error_value

    def _calculate_ticket_validities(self) -> int:
        self.valid_tickets = []
        error_value = 0
        for ticket in self.nearby_tickets:
            error_value += self._calculate_ticket_validity(ticket)
            if self._is_valid_ticket(ticket):
                self.valid_tickets.append(ticket)
        return error_value

    def _determine_possible_field_names(self, index: int) -> list[str]:
        fields = []
        tickets = self.valid_tickets + [self.my_ticket]
        values = [ticket[index] for ticket in tickets]
        for field in self.ticket_ranges:
            r1, r2 = self.ticket_ranges[field]
            is_valid_field = True
            i = 0
            while i < len(values) and is_valid_field:
                is_valid_field = (
                    r1[0] <= values[i] <= r1[1] or r2[0] <= values[i] <= r2[1]
                )
                i += 1
            if is_valid_field:
                fields.append(field)
        return fields

    def _determine_field_order(self, fields: list[list[str]]) -> list[str]:
        ordered_fields = [''] * len(fields)
        determined_fields_set = set()
        next_size = 1
        while next_size < len(fields):
            i = 0
            while len(fields[i]) != next_size:
                i += 1
            for field in fields[i]:
                if field not in determined_fields_set:
                    ordered_fields[i] = field
                    determined_fields_set.add(field)
            next_size += 1
        return ordered_fields

    def part_one(self) -> int:
        self._parse_input()
        return self._calculate_ticket_validities()

    def part_two(self) -> int:
        self._parse_input()
        self._calculate_ticket_validities()
        possible_fields = [
            self._determine_possible_field_names(i)
            for i in range(len(self.my_ticket))
        ]
        actual_fields = self._determine_field_order(possible_fields)
        result = 1
        for i, field in enumerate(actual_fields):
            if 'departure' in field:
                result *= self.my_ticket[i]
        return result


Advent2020Day16().run()