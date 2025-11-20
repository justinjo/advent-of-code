from advent_day import AdventDay

class Card:

    def __init__(self, card: str) -> None:
        card_id_str, card_values = card.split(': ')
        self.id = int(card_id_str.split(' ')[-1])
        winning_nums_str, hand_str = card_values.split(' | ')
        self.winning_nums = set([int(n) for n in winning_nums_str.split(' ') if n.isnumeric()])
        self.hand_nums = set([int(n) for n in hand_str.split(' ') if n.isnumeric()])
        self.score = 0

    def get_score(self) -> int:
        score = 0
        for num in self.hand_nums:
            if num in self.winning_nums:
                score = score * 2 if score else 1
        return score


class Advent2023Day04(AdventDay):

    def part_one(self) -> int:
        return sum([Card(card).get_score() for card in self.input_str_array])

    def part_two(self) -> int:
        ...


Advent2023Day04().run()