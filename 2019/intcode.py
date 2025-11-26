from collections import defaultdict, deque
from enum import IntEnum

class Mode(IntEnum):
    POSITION = 0
    IMMEDIATE = 1
    RELATIVE = 2


class Intcode:

    def __init__(
        self,
        memory: list[int],
        use_cli_io: bool = False,
        queue_in: deque = deque(),
        queue_out: deque = deque(),
    ) -> None:
        self._create_memory_map(memory)
        self.index = self.relative_base = 0
        self.use_cli_io = use_cli_io
        self.queue_in = queue_in
        self.queue_out = queue_out
        self.opcode_to_func_map = {
            1: self._add,
            2: self._multiply,
            3: self._input,
            4: self._output,
            5: self._jump_if_true,
            6: self._jump_if_false,
            7: self._less_than,
            8: self._equal_to,
            9: self._adjust_relative_base,
        }

    def _create_memory_map(self, memory: list[int]) -> None:
        self.memory: dict[int, int] = defaultdict(int)
        for i in range(len(memory)):
            self.memory[i] = memory[i]

    def _get_opcode(self, value: int) -> int:
        return value % 100

    def _get_mode(self, value: int, mask: int) -> int:
        return value % (mask * 10) // mask

    def _get_modes(self, value: int) -> tuple[int, int, int]:
        mode_1 = self._get_mode(value, 100)
        mode_2 = self._get_mode(value, 1000)
        mode_3 = self._get_mode(value, 10000)
        return (mode_1, mode_2, mode_3)

    def _get_index(self, index: int, mode: int) -> int:
        if mode == Mode.POSITION:
            return self.memory[index]
        elif mode == Mode.IMMEDIATE:
            return index
        elif mode == Mode.RELATIVE:
            return self.memory[index] + self.relative_base
        raise Exception('Mode not supported')

    def _get_value(self, index: int, mode: int) -> int:
        return self.memory[self._get_index(index, mode)]

    def _set_value(self, index: int, mode: int, value: int) -> None:
        self.memory[self._get_index(index, mode)] = value

    def _add(self) -> None:
        mode_1, mode_2, mode_3 = self._get_modes(self.memory[self.index])
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        self._set_value(self.index+3, mode_3, val_1 + val_2)
        self.index += 4

    def _multiply(self) -> None:
        mode_1, mode_2, mode_3 = self._get_modes(self.memory[self.index])
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        self._set_value(self.index+3, mode_3, val_1 * val_2)
        self.index += 4

    def _input(self) -> None:
        mode, _, _ = self._get_modes(self.memory[self.index])
        val = 0
        if self.use_cli_io:
            val = input("Input: ")
        elif self.queue_in:
            val = self.queue_in.popleft()
        else:
            self.halt = True # wait for next input from self.queue_in
            return
        self._set_value(self.index+1, mode, int(val))
        self.index += 2

    def _output(self) -> None:
        mode, _, _ = self._get_modes(self.memory[self.index])
        val = self._get_value(self.index+1, mode)
        if self.use_cli_io:
            print(val)
        self.queue_out.append(val)
        self.index += 2

    def _jump_if_true(self) -> None:
        mode_1, mode_2, _ = self._get_modes(self.memory[self.index])
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        self.index = val_2 if val_1 else self.index + 3

    def _jump_if_false(self) -> None:
        mode_1, mode_2, _ = self._get_modes(self.memory[self.index])
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        self.index = val_2 if val_1 == 0 else self.index + 3

    def _less_than(self) -> None:
        mode_1, mode_2, mode_3 = self._get_modes(self.memory[self.index])
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        self._set_value(self.index+3, mode_3, 1 if val_1 < val_2 else 0)
        self.index += 4

    def _equal_to(self) -> None:
        mode_1, mode_2, mode_3 = self._get_modes(self.memory[self.index])
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        self._set_value(self.index+3, mode_3, 1 if val_1 == val_2 else 0)
        self.index += 4

    def _adjust_relative_base(self) -> None:
        mode, _, _ = self._get_modes(self.memory[self.index])
        val = self._get_value(self.index+1, mode)
        self.relative_base += val
        self.index += 2

    def _execute_instruction(self) -> None:
        if self.index < 0:
            raise Exception(f'Index cannot be negative: {self.index}')
        opcode = self._get_opcode(self.memory[self.index])
        if opcode == 99:
            return
        self.opcode_to_func_map[opcode]()

    def execute(self) -> None:
        self.halt = False
        while self.memory[self.index] != 99 and not self.halt:
            self._execute_instruction()

    def finished_execution(self) -> bool:
        return self.memory[self.index] == 99