from advent_day import AdventDay
from collections import Counter

class Advent2020Day9(AdventDay):

    def part_one(self, preamble_length: int = 25) -> int:
        self._convert_input_to_int()
        arr = self.input_int_array
        counter = Counter()
        for i in range(preamble_length):
            for j in range(i):
                counter[arr[i] + arr[j]] += 1
        for i in range(preamble_length, len(arr)):
            if counter[arr[i]] == 0:
                return arr[i]
            for j in range(i-preamble_length, i):
                counter[arr[i] + arr[j]] += 1
            for k in range(i-preamble_length, i):
                counter[arr[i-preamble_length-1] + arr[k]] -= 1
        return -1

    def part_two(self):
        arr = self.input_int_array
        lo = 0
        hi = 1
        cont_sum = arr[lo] + arr[hi]
        target = 25918798
        while cont_sum != target:
            if cont_sum < target:
                hi += 1
                cont_sum += arr[hi]
            else:
                cont_sum -= arr[lo]
                lo += 1
        return min(arr[lo:hi+1]) + max(arr[lo:hi+1])


Advent2020Day9().run()