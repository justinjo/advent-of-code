from advent_day import AdventDay
from collections import defaultdict

class Advent2020Day7(AdventDay):
    TARGET_BAG = 'shiny gold bags'

    def _build_map_from_input(self) -> dict[str, set[tuple[int, str]]]:
        bag_map = defaultdict(set)
        for s in self.input_str_array:
            key, contains = self._split_input(s)
            for count, bag_type in contains:
                bag_map[key].add((count, bag_type))
        return bag_map

    def _split_input(self, string: str) -> tuple[str, list[tuple]]:
        contains = []
        key, value = string.split(' contain ')
        if value != 'no other bags.':
            values = value.split(', ')
            for i in range(len(values)):
                count, affect, color, _ = values[i].split(' ')
                contains.append((int(count), affect + ' ' + color + ' bags'))
        return (key, contains)

    def part_one(self) -> int:
        bag_map = self._build_map_from_input()
        golden_bag_set = set()
        bags = list(bag_map.keys())
        for outer_bag in bags:
            # value
            # {
            #   bag_type: count
            # }
            queue = [outer_bag]
            while queue:
                bag_type = queue.pop()
                if bag_type == self.TARGET_BAG:
                    golden_bag_set.add(outer_bag)
                    break
                for _, nested_bag_type in bag_map[bag_type]:
                    queue.append(nested_bag_type)
        return len(golden_bag_set) - 1

    def part_two(self):
        bag_map = self._build_map_from_input()
        queue = list(bag_map[self.TARGET_BAG])
        count = 0
        while queue:
            bag_count, bag_type = queue.pop()
            count += bag_count
            queue.extend(list(bag_map[bag_type]) * bag_count)

        return count


Advent2020Day7().run()