from advent_day import AdventDay

class Advent2020Day01(AdventDay):

    def _two_sum(self, array: list, target: int) -> tuple[int, int]:
        entries = {}
        for i, value in enumerate(array):
            if value in entries:
                return (entries[value], i)
            entries[target - value] = i
        return (-1, -1)

    def part_one(self) -> int:
        self._convert_input_to_int()
        i, j = self._two_sum(self.input_int_array, 2020)
        return self.input_int_array[i] * self.input_int_array[j]

    def part_two(self) -> int:
        target = 2020
        sorted_array = sorted(self.input_int_array)
        for i in range(self.input_length):
            j = i + 1
            k = self.input_length - 1
            while j < k:
                tri_sum = sorted_array[i] + sorted_array[j] + sorted_array[k]
                if tri_sum < target:
                    j += 1
                elif tri_sum > target:
                    k -= 1
                else:
                    return sorted_array[i] * sorted_array[j] * sorted_array[k]
        return -1


Advent2020Day01().run()