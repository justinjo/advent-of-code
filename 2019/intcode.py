class Intcode:
    POSITION = 0
    IMMEDIATE = 1
    MASK_1 = 100
    MASK_2 = 1000
    MASK_3 = 10000

    def __init__(self, memory: list[int]) -> None:
        self.memory = memory
        self.index = 0

    def _get_opcode(self, value: int) -> int:
        return value % 100
    
    def _get_mode(self, value: int, mask: int) -> int:
        return value % (mask * 10) // mask
    
    def _get_value(self, index: int, mode: int) -> int:
        if mode == self.IMMEDIATE:
            return self.memory[index]
        return self.memory[self.memory[index]]
    
    def _add(self) -> None:
        mode_1 = self._get_mode(self.memory[self.index], self.MASK_1)
        mode_2 = self._get_mode(self.memory[self.index], self.MASK_2)
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        self.memory[self.memory[self.index+3]] = val_1 + val_2
        self.index += 4
    
    def _multiply(self) -> None:
        mode_1 = self._get_mode(self.memory[self.index], self.MASK_1)
        mode_2 = self._get_mode(self.memory[self.index], self.MASK_2)
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        self.memory[self.memory[self.index+3]] = val_1 * val_2
        self.index += 4

    def _input(self) -> None:
        val = input("Input: ")
        self.memory[self.memory[self.index+1]] = int(val)
        self.index += 2

    def _output(self) -> None:
        mode = self._get_mode(self.memory[self.index], self.MASK_1)
        i = self.index+1 if mode == self.IMMEDIATE else self.memory[self.index+1]
        print(self.memory[i])
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
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        val_3 = self._get_value(self.index+3, self.IMMEDIATE)
        self.memory[val_3] = 1 if val_1 < val_2 else 0
        self.index += 4
    
    def _equal_to(self) -> None:
        mode_1 = self._get_mode(self.memory[self.index], self.MASK_1)
        mode_2 = self._get_mode(self.memory[self.index], self.MASK_2)
        val_1 = self._get_value(self.index+1, mode_1)
        val_2 = self._get_value(self.index+2, mode_2)
        val_3 = self._get_value(self.index+3, self.IMMEDIATE)
        self.memory[val_3] = 1 if val_1 == val_2 else 0
        self.index += 4

    def _execute_instruction(self) -> None:
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
        else:
            raise Exception

    def execute(self) -> None:
        self.index = 0
        while self.memory[self.index] != 99:
            self._execute_instruction()