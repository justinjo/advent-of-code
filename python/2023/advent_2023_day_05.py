from advent_day import AdventDay

class Advent2023Day05(AdventDay):

    def translate(self, val: int, translation_ranges: list[tuple[int, int, int]]) -> int:
        new_val = val
        for dest, src, range_len in translation_ranges:
            if src <= val < src + range_len:
                new_val = dest + (val - src)
        return new_val

    def _parse_input(self) -> None:
        self.seeds = [int(s) for s in self.input_str_array[0].split(' ') if s.isnumeric()]
        self.seed_soil_ranges = []
        self.soil_fertilizer_ranges = []
        self.fertilizer_water_ranges = []
        self.water_light_ranges = []
        self.light_temp_ranges = []
        self.temp_humidity_ranges = []
        self.humidity_location_ranges = []
        i = 2
        while i < self.input_length:
            curr_arr = []
            while i < self.input_length and self.input_str_array[i]:
                line = self.input_str_array[i]
                if line == 'seed-to-soil map:':
                    curr_arr = self.seed_soil_ranges
                elif line == 'soil-to-fertilizer map:':
                    curr_arr = self.soil_fertilizer_ranges
                elif line == 'fertilizer-to-water map:':
                    curr_arr = self.fertilizer_water_ranges
                elif line == 'water-to-light map:':
                    curr_arr = self.water_light_ranges
                elif line == 'light-to-temperature map:':
                    curr_arr = self.light_temp_ranges
                elif line == 'temperature-to-humidity map:':
                    curr_arr = self.temp_humidity_ranges
                elif line == 'humidity-to-location map:':
                    curr_arr = self.humidity_location_ranges
                else:
                    dest_start, src_start, range_len = [int(l) for l in line.split(' ')]
                    curr_arr.append((dest_start, src_start, range_len))
                i += 1
            i += 1

    def part_one(self) -> int:
        self._parse_input()
        min_loc = float('inf')
        for seed in self.seeds:
            soil = self.translate(seed, self.seed_soil_ranges)
            fert = self.translate(soil, self.soil_fertilizer_ranges)
            water = self.translate(fert, self.fertilizer_water_ranges)
            light = self.translate(water, self.water_light_ranges)
            temp = self.translate(light, self.light_temp_ranges)
            hum = self.translate(temp, self.temp_humidity_ranges)
            loc = self.translate(hum, self.humidity_location_ranges)
            min_loc = min(loc, min_loc)
        return int(min_loc)

    def part_two(self) -> int:
        ...


Advent2023Day05().run()