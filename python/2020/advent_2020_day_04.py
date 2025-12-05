from advent_day import AdventDay

class Advent2020Day04(AdventDay):
    fields = {
        'byr': {
            'required': True,
            'min': 1920,
            'max': 2002,
        },
        'iyr': {
            'required': True,
            'min': 2010,
            'max': 2020,
        },
        'eyr': {
            'required': True,
            'numeric': True,
            'min': 2020,
            'max': 2030,
        },
        'hgt': {
            'required': True,
        },
        'hcl': {
            'required': True,
        },
        'ecl': {
            'required': True,
            'values': set([
                'amb',
                'blu',
                'brn',
                'gry',
                'grn',
                'hzl',
                'oth',
            ])
        },
        'pid': {
            'required': True,
            'length': 9,
        },
        'cid': {
            'required': False,
        },
    }

    def _validate_field(self, field: str, requirements: dict, passport: dict) -> bool:
        if requirements[field]['required'] and field not in passport:
            return False
        if 'min' in requirements[field]:
            return requirements[field]['min'] <= int(passport[field]) <= requirements[field]['max']
        if 'values' in requirements[field]:
            return passport[field] in requirements[field]['values']
        if 'length' in requirements[field]:
            return passport[field].isnumeric() and len(passport[field]) == requirements[field]['length']
        if field == 'hgt':
            unit = passport[field][-2:]
            value = passport[field][:-2]
            if not value.isnumeric():
                return False
            value = int(value)
            if unit == 'cm':
                return 150 <= value <= 193
            elif unit == 'in':
                return 59 <= value <= 76
            else:
                return False
        if field == 'hcl':
            for i in range(len(passport[field])):
                if i == 0:
                    if passport[field][i] != '#':
                        return False
                elif i >= 7:
                    return False
                elif not (
                    (passport[field][i].isalpha() and passport[field][i].islower())
                    or passport[field][i].isnumeric()
                ):
                    return False
        return True

    def _fill_passport(self, passport: dict, index: int) -> int:
        # returns index
        while index < self.input_length and self.input_str_array[index]:
            for elem in self.input_str_array[index].split(' '):
                key, val = elem.split(':')
                passport[key] = val
            index += 1
        return index + 1

    def _is_valid_passport(self, passport: dict) -> bool:
        is_valid = True
        for f in self.fields:
            if not self._validate_field(f, self.fields, passport):
                is_valid = False
        return is_valid

    def part_one(self) -> int:
        valid_passports = index = 0
        while index < self.input_length:
            passport = {}
            index = self._fill_passport(passport, index)

            is_valid = True
            for f in self.fields:
                if self.fields[f]['required'] and f not in passport:
                    is_valid = False
            valid_passports += 1 if is_valid else 0
        return valid_passports

    def part_two(self) -> int:
        valid_passports = index = 0
        while index < self.input_length:
            passport = {}
            index = self._fill_passport(passport, index)
            valid_passports += 1 if self._is_valid_passport(passport) else 0
        return valid_passports


Advent2020Day04().run()