from abc import ABC, abstractmethod

class AdventDay(ABC):
    """
    self.year: int
    self.day: int
    self.pretty_name: str  # Advent of Code YYYY - Day DD"
    self.input_length: int
    self.input_str_array: List[str]
    self.input_int_array: List[int] # if self._convert_input_to_int() is called
    """

    def __init__(self) -> None:
        """
        Class name must be of form AdventYYYYDayDD (e.g. Advent2019Day1)
        """
        self.year = int(self.__class__.__name__[6:10])
        self.day = int(self.__class__.__name__[13:])
        self.pretty_name = f'Advent of Code {self.year} - Day {self.day}'
        self._read_input()
        self.input_length = len(self.input_str_array)

    def _get_input_file_name(self) -> str:
        """
        Input file names are of the form 'advent_YYYY_day_DD.txt'
        (e.g. advent_2019_day_01.txt)
        They exist in the same directory as the class
        """
        return f'{self.year}/advent_{self.year}_day_{self.day}.txt'
    
    def _read_input(self) -> None:
        self.input_str_array = open(self._get_input_file_name()).read().splitlines()

    def _convert_input_to_int(self) -> None:
        # Most common int input types are one-line csv or newline delineated
        if self.input_length == 1:
            self.input_int_array = [int(elem) for elem in self.input_str_array[0].split(',')]
        else:
            self.input_int_array = [int(elem) for elem in self.input_str_array]

    @abstractmethod
    def part_one(self) -> int | str:
        pass

    @abstractmethod
    def part_two(self) -> int | str:
        pass

    def run(self) -> None:
        print(self.pretty_name)
        print(f'Part One: {self.part_one()}')
        print(f'Part Two: {self.part_two()}')
        print()