from advent_day import AdventDay

class Advent2025Day05(AdventDay):

    def part_one(self) -> int:
        ranges = []
        i = fresh = 0
        while self.input_str_array[i]:
            ranges.append(tuple([int(x) for x in self.input_str_array[i].split('-')]))
            i += 1
        i += 1
        for i in range(i, self.input_length):
            fresh += 1 if any([lo <= int(self.input_str_array[i]) <= hi for lo, hi in ranges]) else 0
        return fresh

    def part_two(self) -> int:
        ranges = []
        i = 0
        while self.input_str_array[i]:
            ranges.append(tuple([int(x) for x in self.input_str_array[i].split('-')]))
            i += 1
        ranges.sort()
        merged_ranges = []
        curr_range = ()
        for lo, hi in ranges:
            if not curr_range:
                curr_range = (lo, hi)
            elif curr_range[1] < lo:
                merged_ranges.append(curr_range)
                curr_range = (lo, hi)
            else:
                curr_range = (curr_range[0], max(curr_range[1], hi))
        merged_ranges.append(curr_range)
        return sum([(hi - lo + 1) for lo, hi in merged_ranges])


Advent2025Day05().run()