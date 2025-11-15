from advent_day import AdventDay
from datetime import datetime, timedelta
from collections import Counter

class Guard:

    def __init__(self, id: int = 0) -> None:
        self.id = id
        self.minutes_asleep = 0
        self.time_awake = 0
        self.on_duty = False
        self.is_asleep = False
        self.shift_start = datetime(1, 1, 1)
        self.sleep_start = datetime(1, 1, 1)
        self.sleep_minutes = Counter()

    def begin_shift(self, dt: datetime) -> None:
        self.shift_start = dt
        self.on_duty = True

    def end_shift(self, dt: datetime) -> None:
        self.wake_up(dt)
        self.shift_end = dt
        self.on_duty = False

    def fall_asleep(self, dt: datetime) -> None:
        self.sleep_start = dt
        self.is_asleep = True

    def wake_up(self, dt: datetime) -> None:
        sleep_delta = dt - self.sleep_start
        minutes_slept = int(sleep_delta.total_seconds()) // 60
        self.minutes_asleep += minutes_slept
        for minute in range(
            self.sleep_start.minute,
            self.sleep_start.minute + minutes_slept
        ):
            self.sleep_minutes[minute] += 1
        self.is_asleep = False

    def sleepiest_minute(self) -> int:
        return self.sleep_minutes.most_common(1)[0][0]


class Scheduler:
    STARTS = 'Guard begins shift'
    SLEEPS = 'falls asleep'
    WAKES = 'wakes up'
    BASE_DATETIME = datetime(1, 1, 1)

    def __init__(self, events: list[dict[str, int | str | datetime]]) -> None:
        self.events: list[dict[str, int | str | datetime]] = events
        self.guards: dict[int, Guard] = {}
        self.guard_on_watch: Guard = Guard()
        self.is_guard_on_watch: bool = False
        self.previous_event_time: datetime = self.BASE_DATETIME

    def run_schedule(self) -> None:
        for event in self.events:
            self._process_event(event)

    def _process_event(self, event: dict[str, int | str | datetime]) -> None:
        dt: datetime = event['datetime'] # type: ignore
        if event['action'] == self.STARTS:
            guard_id: int = event['guard'] # type: ignore
            if guard_id not in self.guards:
                self.guards[guard_id] = Guard(guard_id)

            self.guard_on_watch = self.guards[guard_id]
            self.guard_on_watch.begin_shift(dt)
            self.is_guard_on_watch = True

        elif event['action'] == self.SLEEPS:
            self.guard_on_watch.fall_asleep(dt)

        elif event['action'] == self.WAKES:
            self.guard_on_watch.wake_up(dt)

    def get_sleepiest_guard(self) -> Guard:
        sleepiest = Guard()
        for guard in self.guards.values():
            if guard.minutes_asleep > sleepiest.minutes_asleep:
                sleepiest = guard
        return sleepiest


class Advent2018Day04(AdventDay):

    def _parse_input(self) -> None:
        self.events = []
        for line in self.input_str_array:
            guard = 0
            timestamp, action = line[1:].split('] ')
            dt = datetime.fromisoformat(timestamp)
            if action.split(' ')[0] == 'Guard':
                guard = int(action.split(' ')[1][1:])
                action = Scheduler.STARTS
            event = {
                'timestamp': timestamp,
                'datetime': dt,
                'action': action,
                'guard': guard, # 0 is empty
            }
            self.events.append(event)
        self.events.sort(key=lambda e: e['timestamp'])

    def part_one(self) -> int:
        self._parse_input()
        scheduler = Scheduler(self.events)
        scheduler.run_schedule()
        guard = scheduler.get_sleepiest_guard()
        return guard.id * guard.sleepiest_minute()

    def part_two(self) -> int:
        ...


Advent2018Day04().run()