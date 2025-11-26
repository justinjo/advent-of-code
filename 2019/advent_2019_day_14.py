from advent_day import AdventDay
from collections import defaultdict
from math import ceil

type ChemicalAmount = tuple[int, str]
type ReactionMap = dict[str, dict] # [str, int | list[ChemicalAmount]]

class Advent2019Day14(AdventDay):

    def build_reaction_map(self) -> ReactionMap:
        reaction_map = defaultdict(dict)
        for line in self.input_str_array:
            inputs_str, output = line.split(' => ')
            inputs = inputs_str.split(', ')
            out_amt, out_name = output.split(' ')
            reagants: list[tuple[int, str]] = []
            for reagant in inputs:
                amt, chemical = reagant.split(' ')
                reagants.append((int(amt), chemical) )
            reaction_map[out_name] = {
                'amount': int(out_amt),
                'reagants': reagants,
            }
        return reaction_map

    def part_one(self) -> int:
        ore = 0
        reaction_map = self.build_reaction_map()
        reaction_stack: list[ChemicalAmount] = [(1, 'FUEL')]
        chemical_bank = defaultdict(int)
        while reaction_stack:
            chem_amt, chemical = reaction_stack.pop()
            if chemical == 'ORE':
                ore += chem_amt
                continue
            if chemical_bank[chemical]:
                if chem_amt > chemical_bank[chemical]:
                    chem_amt -= chemical_bank[chemical]
                    chemical_bank[chemical] = 0
                else:
                    chemical_bank[chemical] -= chem_amt
                    chem_amt = 0
            if chem_amt > 0:
                reaction_amt = reaction_map[chemical]['amount']
                num_reactions = ceil(chem_amt / reaction_amt)
                for rg_amt, reagant in reaction_map[chemical]['reagants']:
                    reaction_stack.append((rg_amt * num_reactions, reagant))
                chemical_bank[chemical] += (reaction_amt * num_reactions) - chem_amt
        return ore

    def part_two(self) -> int:
        ...


Advent2019Day14().run()