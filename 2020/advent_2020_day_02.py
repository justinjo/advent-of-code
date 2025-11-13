from advent_day import AdventDay
from collections import Counter

class Advent2020Day02(AdventDay):

    def _format_input(self, string: str) -> tuple[int, int, str, str]:
        min_count, l = string.split("-")
        max_count, letter, password = l.split(" ")
        password = password.splitlines()
        return (
            int(min_count),
            int(max_count),
            letter[0],
            password[0]
        )

    def _is_valid_password(
        self,
        min_count: int,
        max_count: int,
        letter: str,
        password: str
    ) -> bool:
        c = Counter(password)
        return min_count <= c[letter] <= max_count

    def _is_valid_password_2(
        self,
        index_1: int,
        index_2: int,
        letter: str,
        password: str
    ) -> bool:
        return (password[index_1 - 1] == letter) ^ (password[index_2 - 1] == letter)

    def part_one(self) -> int:
        valid_passwords = 0
        for s in self.input_str_array:
            if self._is_valid_password(*self._format_input(s)):
                valid_passwords += 1
        return valid_passwords

    def part_two(self) -> int:
        valid_passwords = 0
        for s in self.input_str_array:
            if self._is_valid_password_2(*self._format_input(s)):
                valid_passwords += 1
        return valid_passwords


Advent2020Day02().run()