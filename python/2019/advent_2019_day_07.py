from intcode import Intcode
from collections import deque
import itertools


def part_one(input_arr: list[str]) -> int:
    # 1st input: phase setting (0,1,2,3,4)
    # 2nd input: input signal
    memory = [int(x) for x in input_arr[0].split(",")]
    phase_settings = [0, 1, 2, 3, 4]
    phase_combos = itertools.permutations(phase_settings, 5)
    max_output = 0

    for a, b, c, d, e in phase_combos:
        q_out_a = deque()
        q_out_b = deque()
        q_out_c = deque()
        q_out_d = deque()
        q_out_e = deque()

        Intcode(
            memory=memory,
            queue_in=deque([a, 0]),
            queue_out=q_out_a,
        ).execute()

        Intcode(
            memory=memory,
            queue_in=deque([b, q_out_a[-1]]),
            queue_out=q_out_b,
        ).execute()

        Intcode(
            memory=memory,
            queue_in=deque([c, q_out_b[-1]]),
            queue_out=q_out_c,
        ).execute()

        Intcode(
            memory=memory,
            queue_in=deque([d, q_out_c[-1]]),
            queue_out=q_out_d,
        ).execute()

        Intcode(
            memory=memory,
            queue_in=deque([e, q_out_d[-1]]),
            queue_out=q_out_e,
        ).execute()

        max_output = max(q_out_e[-1], max_output)

    return max_output


def part_two(input_arr: list[str]) -> int:
    memory = [int(x) for x in input_arr[0].split(",")]
    phase_settings = [5, 6, 7, 8, 9]
    num_settings = len(phase_settings)
    phase_combos = itertools.permutations(phase_settings, num_settings)
    max_output = 0

    for phase_setting in phase_combos:
        ic_map = {}
        for i in range(num_settings):
            queue_in = deque([phase_setting[i]])
            if i == 0:
                queue_in.append(0)
            queue_out = deque()
            intcode = Intcode(
                memory=memory,
                queue_in=queue_in,
                queue_out=queue_out,
            )
            ic_map[i] = {
                "queue_in": queue_in,
                "queue_out": queue_out,
                "intcode": intcode,
            }
        ic_map[0]["intcode"].execute()

        i = 0
        while not ic_map[num_settings - 1]["intcode"].finished_execution():
            next_i = (i + 1) % 5
            output = ic_map[i]["queue_out"].popleft()

            ic_map[next_i]["queue_in"].append(output)
            ic_map[next_i]["intcode"].execute()

            i = next_i

        max_output = max(ic_map[num_settings - 1]["queue_out"][-1], max_output)

    return max_output


input_arr: list[str] = open("advent_2019_day_07.txt").read().splitlines()

print("Advent of Code 2019 - Day 07")
print(f"Part One: {part_one(input_arr)}")
print(f"Part Two: {part_two(input_arr)}")
