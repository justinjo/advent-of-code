def react(polymer: str, ignore_unit: str = "") -> int:
    ignore_units = set()
    if ignore_unit:
        ignore_units.update([ignore_unit, ignore_unit.upper()])
    stack = []
    for i in range(len(polymer)):
        p = polymer[i]
        if p in ignore_units:
            continue
        if stack and stack[-1] != p and stack[-1].lower() == p.lower():
            stack.pop()
        else:
            stack.append(p)
    return len(stack)


def part_one(input_arr: list[str]) -> int:
    return react(input_arr[0])


def part_two(input_arr: list[str]) -> int:
    polymer = input_arr[0]
    chars = [chr(ord("a") + i) for i in range(26)]
    min_length = float("inf")
    for c in chars:
        min_length = min(min_length, react(polymer, c))
    return int(min_length)


input_arr: list[str] = open("advent_2018_day_05.txt").read().splitlines()

print("Advent of Code 2018 - Day 05")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
