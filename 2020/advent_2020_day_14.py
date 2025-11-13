from advent_day import AdventDay
from collections import defaultdict

class BitmaskSystem:
    MASK_INSTR = 'mask'
    BITS = 36
    BIT_FORMAT = '0' + str(BITS) + 'b'

    def __init__(self) -> None:
        self.memory = defaultdict(int)

    def _calculate_masked_value(self, value: int) -> int:
        masked_value = ''
        binary_value = format(value, self.BIT_FORMAT)
        # build up masked_value in reverse
        for i in range(self.BITS):
            if self.mask[i] == 'X':
                masked_value += binary_value[i]
            else:
                masked_value += self.mask[i]
        return int(masked_value, 2)

    def _generate_binary_permutations(self, length: int) -> list[list[int]]:
        # Thank you google - itertools.permutations was timing out
        results = []
        def backtrack(current_permutation: list[int]) -> list[int] | None:
            if len(current_permutation) == length:
                results.append(current_permutation)
                return
            # Try adding 0
            backtrack(current_permutation + [0])
            # Try adding 1
            backtrack(current_permutation + [1])
        backtrack([])
        return results

    def _calculate_masked_addresses(self, value: int) -> list[int]:
        masked_addresses = []
        binary_value = format(value, self.BIT_FORMAT)
        x_indices = [i for i, char in enumerate(self.mask) if char == 'X']
        bits_to_order = self._generate_binary_permutations(len(x_indices))

        # build up masked_value in reverse
        for ordering in bits_to_order:
            masked_address = ''
            x_i = 0
            for i in range(self.BITS):
                if self.mask[i] == '0':
                    masked_address += binary_value[i]
                elif self.mask[i] == '1':
                    masked_address += '1'
                else: # 'X'
                    masked_address += str(ordering[x_i])
                    x_i += 1
            masked_addresses.append(masked_address)
        return [int(val, 2) for val in masked_addresses]

    def set_mask(self, mask: str) -> None:
        self.mask = mask

    def set_value(self, address: int, value: int) -> None:
        self.memory[address] = self._calculate_masked_value(value)

    def set_values(self, addresses: list[int], value: int) -> None:
        for address in addresses:
            self.memory[address] = value

    def process_instruction(self, instruction: str, version: int = 1) -> None:
        target, value = instruction.split(" = ")
        if target == self.MASK_INSTR:
            self.set_mask(value)
        else: # Write value to memory
            memory_index = target[4:-1]
            if version == 1:
                self.set_value(int(memory_index), int(value))
            elif version == 2:
                masked_addresses = self._calculate_masked_addresses(int(memory_index))
                self.set_values(masked_addresses, int(value))

    def get_value_sum(self) -> int:
        return sum(self.memory.values())


class Advent2020Day14(AdventDay):

    def part_one(self) -> int:
        bms = BitmaskSystem()
        for instr in self.input_str_array:
            bms.process_instruction(instr)
        return bms.get_value_sum()

    def part_two(self) -> int:
        bms = BitmaskSystem()
        for instr in self.input_str_array:
            bms.process_instruction(instr, version=2)
        return bms.get_value_sum()


Advent2020Day14().run()