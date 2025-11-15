from advent_day import AdventDay
from collections import defaultdict

class Advent2018Day07(AdventDay):

    def _get_step_order(self) -> defaultdict[str, list[str]]:
        step_order = defaultdict(list)
        for s in self.input_str_array:
            words = s[5:-11].split(' ')
            blocking_step = words[0]
            next_step = words[-1]
            step_order[blocking_step].append(next_step)
        return step_order

    def _get_blocking_order(self) -> defaultdict[str, list[str]]:
        step_order = defaultdict(list)
        for s in self.input_str_array:
            words = s[5:-11].split(' ')
            blocking_step = words[0]
            next_step = words[-1]
            step_order[next_step].append(blocking_step)
        return step_order

    def _first_steps(self, step_order: defaultdict[str, list[str]]) -> list[str]:
        first_steps = []
        for blocking_step in step_order:
            step_found = False
            for next_steps in step_order.values():
                if blocking_step in next_steps:
                    step_found = True
            if not step_found:
                first_steps.append(blocking_step)
        return first_steps

    def _get_order(
        self,
        step_order: defaultdict[str, list[str]],
        blocking_order: defaultdict[str, list[str]],
        next_steps: list[str],
    ) -> str:
        order = ''
        completed = set()
        final_steps = set()
        while next_steps:
            # always pick the earliest letter available
            next_steps.sort(reverse=True)
            next_step = next_steps.pop()
            if next_step in completed:
                continue
            if not step_order[next_step]:
                final_steps.add(next_step)
                continue
            completed.add(next_step)
            order += next_step
            for maybe_unblocked in step_order[next_step]:
                # check that all blocking steps are complete
                if not set(blocking_order[maybe_unblocked]) - completed:
                    next_steps.append(maybe_unblocked)
        order += ''.join(sorted(final_steps))
        return order

    def part_one(self) -> str:
        step_order = self._get_step_order()
        blocking_order = self._get_blocking_order()
        first_steps = self._first_steps(step_order)
        return self._get_order(step_order, blocking_order, first_steps)

    def part_two(self) -> int:
        ...


Advent2018Day07().run()