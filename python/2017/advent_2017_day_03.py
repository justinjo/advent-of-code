def get_distance(target: int) -> int:
    base = 1
    while base**2 < target:
        base += 2
    curr = base**2
    distance = base - 1
    toggle = (base - 1) // 2
    offset = -1
    counter = 0
    while curr != target:
        distance += offset
        curr -= 1
        counter += 1
        if counter % toggle == 0:
            offset *= -1
    return distance


def part_one(input_arr: list[str]) -> int:
    return get_distance(int(input_arr[0]))


def part_two(input_arr: list[str]) -> int: ...


input_arr: list[str] = open("advent_2017_day_03.txt").read().splitlines()

print("Advent of Code 2017 - Day 03")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")


"""
part 1 notes

37 36  35  34  33  32 31
38 17  16  15  14  13 30
39 18   5   4   3  12 29
40 19   6   1   2  11 28
41 20   7   8   9  10 27
42 21  22  23  24  25 26
43 44  45  46  47  48 49

1 - 1^2
0

2 3 4 5 6 7 8 9 - 3^2
1 2 1 2 1 2 1 2

10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 - 5^2
 3  2  3  4  3  2  3  4  3  2  3  4  3  2  3  4

26                                           49 - 7^2
 5  4  3  4  5  6  5  4  3  4  5  6 ... 4  5  6

distance from odd squares: base - 1
decrementing until next odd square has this loop behavior:
    distance -= 1 ((base-1)/2 times)
    distance += 1 ((base-1)/2 times)
"""
