from advent_day import AdventDay
from collections import Counter

class Advent2018Day02(AdventDay):

    def part_one(self) -> int:
        twos = 0
        threes = 0
        for s in self.input_str_array:
            c = Counter(s)
            add_two = False
            add_three = False
            for _, count in c.items():
                if count == 2:
                    add_two = True
                elif count == 3:
                    add_three = True
            twos += 1 if add_two else 0
            threes += 1 if add_three else 0
        return twos * threes

    def part_two(self) -> str:
        return_str = ''
        for i in range(self.input_length):
            for j in range(i+1, self.input_length):
                str_i = self.input_str_array[i]
                str_j = self.input_str_array[j]
                c_i = Counter(str_i)
                c_j = Counter(str_j)
                c_diff = (c_i - c_j) + (c_j - c_i)
                if len(c_diff) == 2:
                    chars = ''
                    for k in range(len(str_i)):
                        if str_i[k] != str_j[k]:
                            if str_i[k] not in c_diff:
                                break
                        else:
                            chars += str_i[k]
                    return_str = chars if len(chars) == len(str_i) - 1 else return_str
        return return_str


Advent2018Day02().run()