from collections import defaultdict

class Intcode:
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2
    MASK_1 = 100
    MASK_2 = 1000
    MASK_3 = 10000

    def __init__(
        self,
        memory: list[int],
        args: list[int] = [],
        silence_output: bool = False,
        input_from_args_only: bool = False,
    ) -> None:
        self.memory = self._generate_memory_map(memory)
        self.index = 0
        self.relative_base = 0
        self.args = args
        self.silence_output = silence_output
        self.input_from_args_only = input_from_args_only
        self.output_values = []

    def _generate_memory_map(self, memory: list[int]) -> dict[int, int]:
        memory_map = defaultdict(int)
        for i in range(len(memory)):
            memory_map[i] = memory[i]
        return memory_map

    def _get_opcode(self, value: int) -> int:
        return value % 100

    def _get_mode(self, value: int, mask: int) -> int:
        return value % (mask * 10) // mask

    def _get_index(self, index: int, mode: int) -> int:
        if mode == self.POSITION:
            return self.memory[index]
        elif mode == self.IMMEDIATE:
            return index
        elif mode == self.RELATIVE:
            return self.memory[index] + self.relative_base
        raise Exception('Mode not supported')

    def _get_value(self, index: int, mode: int) -> int:
        return self.memory[self._get_index(index, mode)]

    def _allocate_memory(self, new_size: int) -> None:
        new_memory = [0] * new_size
        for i in range(len(self.memory)):
            new_memory[i] = self.memory[i]
        self.memory = new_memory

    def _add(self) -> None:
        mode_1 = self._get_mode(self.memory[self.index], self.MASK_1)
        mode_2 = self._get_mode(self.memory[self.index], self.MASK_2)
        mode_3 = self._get_mode(self.memory[self.index], self.MASK_3)
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        index_3 = self._get_index(self.index+3, mode_3)
        self.memory[index_3] = val_1 + val_2
        self.index += 4

    def _multiply(self) -> None:
        mode_1 = self._get_mode(self.memory[self.index], self.MASK_1)
        mode_2 = self._get_mode(self.memory[self.index], self.MASK_2)
        mode_3 = self._get_mode(self.memory[self.index], self.MASK_3)
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        index_3 = self._get_index(self.index+3, mode_3)
        self.memory[index_3] = val_1 * val_2
        self.index += 4

    def _input(self) -> None:
        mode = self._get_mode(self.memory[self.index], self.MASK_1)
        index = self._get_index(self.index+1, mode)
        val = 0
        if self.args:
            val = self.args.pop(0)
        elif self.input_from_args_only:
            # wait for next input
            self.halt = True
            return
        else:
            val = input("Input: ")
        self.memory[index] = int(val)
        self.index += 2

    def _output(self) -> None:
        mode = self._get_mode(self.memory[self.index], self.MASK_1)
        val = self._get_value(self.index+1, mode)
        if not self.silence_output:
            print(val)
        self.output_values.append(val)
        self.index += 2

    def _jump_if_true(self) -> None:
        mode_1 = self._get_mode(self.memory[self.index], self.MASK_1)
        mode_2 = self._get_mode(self.memory[self.index], self.MASK_2)
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        self.index = val_2 if val_1 else self.index + 3

    def _jump_if_false(self) -> None:
        mode_1 = self._get_mode(self.memory[self.index], self.MASK_1)
        mode_2 = self._get_mode(self.memory[self.index], self.MASK_2)
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        self.index = val_2 if val_1 == 0 else self.index + 3

    def _less_than(self) -> None:
        mode_1 = self._get_mode(self.memory[self.index], self.MASK_1)
        mode_2 = self._get_mode(self.memory[self.index], self.MASK_2)
        mode_3 = self._get_mode(self.memory[self.index], self.MASK_3)
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        index_3 = self._get_index(self.index+3, mode_3)
        self.memory[index_3] = 1 if val_1 < val_2 else 0
        self.index += 4

    def _equal_to(self) -> None:
        mode_1 = self._get_mode(self.memory[self.index], self.MASK_1)
        mode_2 = self._get_mode(self.memory[self.index], self.MASK_2)
        mode_3 = self._get_mode(self.memory[self.index], self.MASK_3)
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        index_3 = self._get_index(self.index+3, mode_3)
        self.memory[index_3] = 1 if val_1 == val_2 else 0
        self.index += 4

    def _adjust_relative_base(self) -> None:
        mode_1 = self._get_mode(self.memory[self.index], self.MASK_1)
        val_1 = self._get_value(self.index+1, mode_1)
        self.relative_base += val_1
        self.index += 2

    def _execute_instruction(self) -> None:
        if self.index < 0:
            raise Exception(f'Index cannot be negative: {self.index}')
        opcode = self._get_opcode(self.memory[self.index])
        if opcode == 99:
            return
        elif opcode == 1:
            self._add()
        elif opcode == 2:
            self._multiply()
        elif opcode == 3:
            self._input()
        elif opcode == 4:
            self._output()
        elif opcode == 5:
            self._jump_if_true()
        elif opcode == 6:
            self._jump_if_false()
        elif opcode == 7:
            self._less_than()
        elif opcode == 8:
            self._equal_to()
        elif opcode == 9:
            self._adjust_relative_base()
        else:
            raise Exception

    def execute(self) -> None:
        self.halt = False
        while self.memory[self.index] != 99 and not self.halt:
            self._execute_instruction()

    def get_most_recent_output_value(self) -> int:
        return self.output_values[-1]

    def add_args(self, args: list[int]) -> None:
        self.args.extend(args)

    def popleft_output_value(self) -> int:
        return self.output_values.pop(0)

    def finished_execution(self) -> bool:
        return self.memory[self.index] == 99