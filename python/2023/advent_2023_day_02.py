from advent_day import AdventDay

class Turn:

    def __init__(self, turn_str: str) -> None:
        self.color_count_map: dict[str, int] = {}
        for turn in turn_str.split(', '):
            num, color = turn.split(' ')
            self.color_count_map[color] = int(num)


class Advent2023Day02(AdventDay):

    def _parse_input(self) -> dict[int, list[Turn]]:
        game_turns_map = {}
        for s in self.input_str_array:
            game, turns_str = s.split(': ')
            game_id = int(game.split(' ')[-1])
            turns_str_arr = turns_str.split('; ')
            turns_arr = [Turn(t) for t in turns_str_arr]
            game_turns_map[game_id] = turns_arr
        return game_turns_map

    def is_valid_game(self, bag_map: dict[str, int], turns: list[Turn]) -> bool:
        for turn in turns:
            for color in turn.color_count_map:
                if bag_map[color] < turn.color_count_map[color]:
                    return False
        return True

    def get_min_power(self, turns: list[Turn]) -> int:
        min_count_map = {
            'red': 0,
            'green': 0,
            'blue': 0,
        }
        for turn in turns:
            for color in turn.color_count_map:
                min_count_map[color] = max(min_count_map[color], turn.color_count_map[color])
        return min_count_map['red'] * min_count_map['green'] * min_count_map['blue']

    def part_one(self) -> int:
        game_turns_map = self._parse_input()
        bag_count_map = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }
        games_sum = 0
        for game in game_turns_map:
            if self.is_valid_game(bag_count_map, game_turns_map[game]):
                games_sum += game
        return games_sum

    def part_two(self) -> int:
        game_turns_map = self._parse_input()
        powers_sum = 0
        for game in game_turns_map:
            powers_sum += self.get_min_power(game_turns_map[game])
        return powers_sum


Advent2023Day02().run()