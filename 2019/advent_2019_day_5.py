from advent_day import AdventDay
from copy import deepcopy

class Advent2019Day5(AdventDay):
    POSITION = 0
    IMMEDIATE = 1
    MASK_1 = 100
    MASK_2 = 1000
    MASK_3 = 10000

    def _get_opcode(self, value: int) -> int:
        return value % 100
    
    def _get_mode(self, value: int, mask: int) -> int:
        return value % (mask * 10) // mask
    
    def _get_value(self, memory: list, index: int, mode: int) -> int:
        return memory[index] if mode == self.IMMEDIATE else memory[memory[index]]
    
    def _add(self, memory: list[int], index: int) -> int:
        mode_1 = self._get_mode(memory[index], self.MASK_1)
        mode_2 = self._get_mode(memory[index], self.MASK_2)
        val_1 = self._get_value(memory, index+1, mode_1)
        val_2 = self._get_value(memory, index+2, mode_2)
        memory[memory[index+3]] = val_1 + val_2
        return index + 4
    
    def _multiply(self, memory: list[int], index: int) -> int:
        mode_1 = self._get_mode(memory[index], self.MASK_1)
        mode_2 = self._get_mode(memory[index], self.MASK_2)
        val_1 = self._get_value(memory, index+1, mode_1)
        val_2 = self._get_value(memory, index+2, mode_2)
        memory[memory[index+3]] = val_1 * val_2
        return index + 4
    
    def _input(self, memory: list[int], index: int) -> int:
        val = input("Input: ")
        memory[memory[index+1]] = int(val)
        return index + 2

    def _output(self, memory: list[int], index: int) -> int:
        mode = self._get_mode(memory[index], self.MASK_1)
        i = index+1 if mode == self.IMMEDIATE else memory[index+1]
        print(memory[i])
        return index + 2
    
    def _jump_if_true(self, memory: list[int], index: int) -> int:
        mode_1 = self._get_mode(memory[index], self.MASK_1)
        mode_2 = self._get_mode(memory[index], self.MASK_2)
        val_1 = self._get_value(memory, index+1, mode_1)
        val_2 = self._get_value(memory, index+2, mode_2)
        return val_2 if val_1 else index + 3
    
    def _jump_if_false(self, memory: list[int], index: int) -> int:
        mode_1 = self._get_mode(memory[index], self.MASK_1)
        mode_2 = self._get_mode(memory[index], self.MASK_2)
        val_1 = self._get_value(memory, index+1, mode_1)
        val_2 = self._get_value(memory, index+2, mode_2)
        return val_2 if val_1 == 0 else index + 3
    
    def _less_than(self, memory: list[int], index: int) -> int:
        mode_1 = self._get_mode(memory[index], self.MASK_1)
        mode_2 = self._get_mode(memory[index], self.MASK_2)
        val_1 = self._get_value(memory, index+1, mode_1)
        val_2 = self._get_value(memory, index+2, mode_2)
        val_3 = self._get_value(memory, index+3, self.IMMEDIATE)
        memory[val_3] = 1 if val_1 < val_2 else 0
        return index + 4
    
    def _equal_to(self, memory: list[int], index: int) -> int:
        mode_1 = self._get_mode(memory[index], self.MASK_1)
        mode_2 = self._get_mode(memory[index], self.MASK_2)
        val_1 = self._get_value(memory, index+1, mode_1)
        val_2 = self._get_value(memory, index+2, mode_2)
        val_3 = self._get_value(memory, index+3, self.IMMEDIATE)
        memory[val_3] = 1 if val_1 == val_2 else 0
        return index + 4

    # returns index of next instruction, -1 if done, -2 if unexpected opcode
    def _execute_instruction(self, memory: list[int], index: int) -> int:
        opcode = self._get_opcode(memory[index])
        if opcode == 99:
            return -1
        elif opcode == 1:
            return self._add(memory, index)
        elif opcode == 2:
            return self._multiply(memory, index)
        elif opcode == 3:
            return self._input(memory, index)
        elif opcode == 4:
            return self._output(memory, index)
        elif opcode == 5:
            return self._jump_if_true(memory, index)
        elif opcode == 6:
            return self._jump_if_false(memory, index)
        elif opcode == 7:
            return self._less_than(memory, index)
        elif opcode == 8:
            return self._equal_to(memory, index)
        return -2

    def _execute(self, memory: list) -> None:
        i = 0
        while i != -1:
            i = self._execute_instruction(memory, i)
            if i == -2:
                raise Exception

    def part_one(self) -> str:
        self._convert_input_to_int()
        self._execute(deepcopy(self.input_int_array))
        return 'Program Terminated'

    def part_two(self) -> str:
        self._convert_input_to_int()
        self._execute(deepcopy(self.input_int_array))
        return 'Program Terminated'


Advent2019Day5().run()