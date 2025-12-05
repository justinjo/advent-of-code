from advent_day import AdventDay
from collections import Counter

class Advent2020Day06(AdventDay):

    def part_one(self) -> int:
        arr = self.input_str_array
        answers = set()
        count_sum = i = 0
        while i < len(arr):
            if arr[i]:
                answers.update(arr[i])
            if not arr[i] or i == len(arr) -1:
                # wrap up
                count_sum += len(answers)
                answers = set()
            i += 1
        return count_sum

    def part_two(self) -> int:
        arr = self.input_str_array
        answers = Counter()
        num_ppl = count_sum = i = 0
        while i < len(arr):
            if arr[i]:
                num_ppl += 1
                answers.update(arr[i])
            if not arr[i] or i == len(arr) -1:
                # wrap up
                num_unanimous = 0
                for _, count in answers.items():
                    if count == num_ppl:
                        num_unanimous += 1
                count_sum += num_unanimous
                answers = Counter()
                num_ppl = 0
            i += 1
        return count_sum


Advent2020Day06().run()