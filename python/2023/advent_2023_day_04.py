from advent_day import AdventDay
from collections import Counter

class Card:

    def __init__(self, card: str) -> None:
        card_id_str, card_values = card.split(': ')
        self.id = int(card_id_str.split(' ')[-1])
        winning_nums_str, hand_str = card_values.split(' | ')
        self.winning_nums = set([int(n) for n in winning_nums_str.split(' ') if n.isnumeric()])
        self.hand_nums = set([int(n) for n in hand_str.split(' ') if n.isnumeric()])
        self.score = 0

    def get_score(self) -> int:
        return 2 * self.get_num_matches()

    def get_num_matches(self) -> int:
        matches = 0
        for num in self.hand_nums:
            matches += 1 if num in self.winning_nums else 0
        return matches


class Advent2023Day04(AdventDay):

    def part_one(self) -> int:
        return sum([Card(card).get_score() for card in self.input_str_array])

    def part_two(self) -> int:
        cards = [Card(card) for card in self.input_str_array]
        card_ids = sorted([card.id for card in cards])
        card_count = Counter(card_ids)
        total_cards = 0
        for id in card_ids:
            num_cards = card_count[id]
            num_matches = cards[id - 1].get_num_matches()
            card_count.update(list(range(id + 1, id + num_matches + 1)) * num_cards)
            total_cards += num_cards

        return total_cards


Advent2023Day04().run()