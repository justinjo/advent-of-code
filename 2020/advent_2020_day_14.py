from advent_day import AdventDay
from collections import defaultdict

class BitmaskSystem:
    MASK_INSTR = 'mask'
    MEM_INSTR = 'mem'
    BITS = 36
    BIT_FORMAT = '0' + str(BITS) + 'b'
    MASK_PASSTHROUGH = 'X'

    def __init__(self) -> None:
        self.memory = defaultdict(int)

    def _calculate_masked_value(self, value: int) -> int:
        masked_value = ''
        binary_value = format(value, self.BIT_FORMAT)
        # build up masked_value in reverse
        for i in range(self.BITS):
            if self.mask[i] == self.MASK_PASSTHROUGH:
                masked_value += binary_value[i]
            else:
                masked_value += self.mask[i]
        return int(masked_value, 2)

    def set_mask(self, mask: str) -> None:
        self.mask = mask

    def set_value(self, address: int, value: int) -> None:
        self.memory[address] = self._calculate_masked_value(value)


    def process_instruction(self, instruction: str) -> None:
        target, value = instruction.split(" = ")
        if target == self.MASK_INSTR:
            self.set_mask(value)
        else:
            memory_index = target[4:-1]
            self.set_value(int(memory_index), int(value))

    def get_value_sum(self) -> int:
        return sum(self.memory.values())

class Advent2020Day14(AdventDay):



    def part_one(self) -> int:
        bms = BitmaskSystem()
        for instr in self.input_str_array:
            bms.process_instruction(instr)
        return bms.get_value_sum()

    def part_two(self) -> int:
        ...


Advent2020Day14().run()