from advent_day import AdventDay

class Advent2019Day16(AdventDay):

    sequence = [0, 1, 0, -1]

    def fft(self, arr: list[int]) -> list[int]:
        next_phase = [0] * len(arr)
        for next_i in range(len(arr)):
            arr_i = 0
            offsets = next_i + 1
            while arr_i < len(arr):
                seq_i = ((arr_i + 1) // offsets ) % len(self.sequence)
                next_phase[next_i] += arr[arr_i] * self.sequence[seq_i]
                arr_i += 1
            if next_phase[next_i] >= 0:
                next_phase[next_i] %= 10
            else:
                next_phase[next_i] = 10 - (next_phase[next_i] % 10)
        return next_phase

    def split_input(self) -> list[int]:
        split_arr = []
        num = self.input_int_array[0]
        while num:
            split_arr.append(num % 10)
            num //= 10
        return split_arr[::-1]

    def part_one(self) -> str:
        self._convert_input_to_int()
        arr = self.split_input()
        for _ in range(100):
            arr = self.fft(arr)
        return ''.join(str(a) for a in arr[:8])

    def part_two(self) -> int:
        ...


Advent2019Day16().run()