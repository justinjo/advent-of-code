from advent_day import AdventDay
from collections import defaultdict

class Advent2020Day15(AdventDay):

    def _play_game_until(self, final_turn: int) -> int:
        most_recent = defaultdict(list)
        turn = 1
        i = curr_num = prev_num = 0

        while turn <= final_turn:
            if i < len(self.input_int_array):
                curr_num = self.input_int_array[i]
                i += 1
            else:
                if prev_num in most_recent and len(most_recent[prev_num]) >= 2:
                    curr_num = most_recent[prev_num][-1] - most_recent[prev_num][-2]
                else:
                    curr_num = 0

            most_recent[curr_num].append(turn)
            prev_num = curr_num
            turn += 1

        return curr_num

    def _play_game_until_with_optimization(self, final_turn: int) -> int:
        most_recent = defaultdict(int)
        turn = 1
        i = curr_num = prev_num = 0

        while turn <= final_turn:
            if i < len(self.input_int_array):
                curr_num = self.input_int_array[i]
                i += 1
            else:
                if prev_num in most_recent:
                    curr_num = (turn - 1) - most_recent[prev_num]
                else:
                    curr_num = 0

            most_recent[prev_num] = turn - 1
            prev_num = curr_num
            turn += 1

        return curr_num

    def part_one(self) -> int:
        self._convert_input_to_int()
        return self._play_game_until(2020)

    def part_two(self) -> int:
        # takes a bit under 15 seconds to run
        # return self._play_game_until(30000000)

        # takes ~7 seconds to run
        return self._play_game_until_with_optimization(30000000)


Advent2020Day15().run()