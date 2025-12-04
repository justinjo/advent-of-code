from advent_day import AdventDay

class Advent2025Day03(AdventDay):

    def sum_joltage(self, digits: int = 2) -> int:
        joltage = 0 # should be doing monotonic stacks but lazy
        for s in self.input_str_array:
            i = j = 0
            arr = [int(x) for x in list(s)]
            for t in range(digits-1,-1,-1):
                subarr = arr[i:len(arr)-t] # use len to prevent arr[x:0]
                b = max(subarr)
                i += subarr.index(b) + 1
                j = j * 10 + b
            joltage += j
        return joltage

    def part_one(self) -> int:
        return self.sum_joltage()

    def part_two(self) -> int:
        return self.sum_joltage(12)

Advent2025Day03().run()