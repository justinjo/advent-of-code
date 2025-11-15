from advent_day import AdventDay
from collections import defaultdict

class Worker:

    def __init__(self, id: int, task_id: str = '.') -> None:
        self.id = id
        self.give_task(task_id)

    def give_task(self, task_id: str) -> None:
        self.task = Task(task_id)
        self.time_worked = 0

    def work(self) -> None:
        self.time_worked += 1

    def is_done(self) -> bool:
        return self.time_worked >= self.task.time

    def get_current_task(self) -> Task:
        return self.task


class Task:

    def __init__(self, id: str, base_time: int = 60) -> None:
        self.id = id
        self.time = base_time + (ord(id) - ord('A')) + 1


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

    def _construct(
        self,
        step_order: defaultdict[str, list[str]],
        blocking_order: defaultdict[str, list[str]],
        step_queue: list[str],
        num_workers: int = 5
    ) -> int:
        time: int = -1 # increment time at start of loop

        completed: set[str] = set()
        final_steps: set[str] = set()
        blocked_steps: set[str] = set()

        available_workers: list[int] = [i for i in range(num_workers)]
        busy_workers: list[int] = []
        workers: list[Worker] = []
        for i in available_workers:
            workers.append(Worker(i))

        # loop until all steps are completed
        while len(completed) + len(final_steps) < len(step_order):
            time += 1

            # free up any workers
            for i in range(num_workers):
                if not (i in busy_workers and workers[i].is_done()):
                    continue
                completed_task = workers[i].get_current_task()
                completed.add(completed_task.id)
                busy_workers.remove(i)
                available_workers.append(i)
                for maybe_unblocked in step_order[completed_task.id]:
                    if not step_order[maybe_unblocked]:
                        final_steps.add(maybe_unblocked)
                        continue
                    if not set(blocking_order[maybe_unblocked]) - completed:
                        step_queue.append(maybe_unblocked)
                        blocked_steps -= set([maybe_unblocked])
                    else:
                        blocked_steps.add(maybe_unblocked)

            # if we've done all the non-final steps, queue up final steps
            if len(completed) == len(step_order) - len(final_steps):
                step_queue = list(final_steps)
                final_steps = set()

            # always pick the earliest letter available
            step_queue.sort(reverse=True)

            # assign any available work
            while available_workers and step_queue:
                worker_id = available_workers.pop()
                workers[worker_id].give_task(step_queue.pop())
                busy_workers.append(worker_id)

            # all workers perform a unit of work
            for worker_id in busy_workers:
                workers[worker_id].work()

        return time

    def part_one(self) -> str:
        step_order = self._get_step_order()
        blocking_order = self._get_blocking_order()
        first_steps = self._first_steps(step_order)
        return self._get_order(step_order, blocking_order, first_steps)

    def part_two(self) -> int:
        step_order = self._get_step_order()
        blocking_order = self._get_blocking_order()
        first_steps = self._first_steps(step_order)
        return self._construct(step_order, blocking_order, first_steps)

Advent2018Day07().run()