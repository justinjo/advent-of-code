from collections import defaultdict
from math import ceil

type ChemicalAmount = tuple[int, str]
type ReactionMap = dict[str, dict]  # [str, int | list[ChemicalAmount]]


def build_reaction_map(input_arr: list[str]) -> ReactionMap:
    reaction_map = defaultdict(dict)
    for line in input_arr:
        inputs, output = line.split(" => ")
        out_amt, out_name = output.split(" ")
        reagants: list[tuple[int, str]] = []
        for reagant in inputs.split(", "):
            amt, chemical = reagant.split(" ")
            reagants.append((int(amt), chemical))
        reaction_map[out_name] = {
            "amount": int(out_amt),
            "reagants": reagants,
        }
    return reaction_map


def get_ore_for_fuel(input_arr: list[str], fuel_amt: int = 1) -> int:
    ore = 0
    reaction_map = build_reaction_map(input_arr)
    reaction_stack: list[ChemicalAmount] = [(fuel_amt, "FUEL")]
    chemical_bank = defaultdict(int)
    while reaction_stack:
        chem_amt, chemical = reaction_stack.pop()
        if chemical == "ORE":
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
            reaction_amt = reaction_map[chemical]["amount"]
            num_reactions = ceil(chem_amt / reaction_amt)
            for reag_amt, reagant in reaction_map[chemical]["reagants"]:
                reaction_stack.append((reag_amt * num_reactions, reagant))
            chemical_bank[chemical] += (reaction_amt * num_reactions) - chem_amt
    return ore


def part_one(input_arr: list[str]) -> int:
    return get_ore_for_fuel(input_arr)


def part_two(input_arr: list[str]) -> int:
    ore_limit = 1000000000000
    fuel_amt = 1
    for _ in range(100):  # zip zap zoom
        sub_amt = 1
        while get_ore_for_fuel(input_arr, fuel_amt) > ore_limit:
            fuel_amt -= sub_amt
            sub_amt *= 2
        add_amt = 1
        while get_ore_for_fuel(input_arr, fuel_amt) < ore_limit:
            fuel_amt += add_amt
            add_amt *= 2
    while get_ore_for_fuel(input_arr, fuel_amt) > ore_limit:
        fuel_amt -= 1
    return fuel_amt


input_arr: list[str] = open("advent_2019_day_14.txt").read().splitlines()

print("Advent of Code 2019 - Day 14")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
