from advent_day import AdventDay

class Advent2020Day08(AdventDay):

    def _parse_input(self) -> list[tuple[str, int]]:
        res = []
        for a in self.input_str_array:
            op, val = a.split(' ')
            val = int(val[1:]) if val[0] == '+' else int(val)
            res.append((op, val))
        return res

    def part_one(self) -> int:
        arr = self._parse_input()
        accumulator = pointer = 0
        visited = set()
        while pointer not in visited:
            visited.add(pointer)
            op, val = arr[pointer]
            if op == 'nop':
                pointer += 1
            elif op == 'acc':
                accumulator += val
                pointer += 1
            elif op == 'jmp':
                pointer += val
        return accumulator

    def part_two(self) -> int:
        arr = self._parse_input()
        for i in range(len(arr)):
            if arr[i][0] == 'jmp':
                arr[i] = ('nop', arr[i][1])
            elif arr[i][0] == 'nop':
                arr[i] = ('jmp', arr[i][1])
            else:
                continue
            pointer = 0
            accumulator = 0
            visited = set()
            while pointer not in visited:
                if pointer == len(arr):
                    return accumulator
                visited.add(pointer)
                op, val = arr[pointer]
                if op == 'nop':
                    pointer += 1
                elif op == 'acc':
                    accumulator += val
                    pointer += 1
                elif op == 'jmp':
                    pointer += val
            if arr[i][0] == 'jmp':
                arr[i] = ('nop', arr[i][1])
            elif arr[i][0] == 'nop':
                arr[i] = ('jmp', arr[i][1])
        return -1


Advent2020Day08().run()