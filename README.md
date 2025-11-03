# Advent of Code
https://adventofcode.com

## Table of Contents

- [Requirements](#requirements)
- [Usage](#usage)

## Requirements
Use Python version >=3.10

## Usage

Follow the steps below, given a year YYYY (e.g. 2019) and day DD (e.g. 1, 20)

#### 1. If it doesn't exist, create directory YYYY
#### 2. Create input file `advent_YYYY_day_DD.txt` in directory YYYY
#### 3. Paste input from the current day's problem to said text file

##### Example: 2019/advent_2019_day_1.txt
```
106001
131342
51187
87791
68636
109091
```

#### 3. Create python file `advent_YYYY_day_DD.py` in directory YYYY
#### 4. Create an AdventDay class for the current day's problem

The solution values should be returned by `part_one` and `part_two`. They will be printed to stdout.

##### Example: 2019/advent_2019_day_1.py
```python
from advent_day import AdventDay

Advent2019Day1(AdventDay):
    def _helper_func(self) -> None:
        ...

    def part_one(self) -> int | str:
        return 1

    def part_two(self) -> int | str:
        self._helper_func()
        return 2


Advent2019Day1().run()
```

#### 5. Run code

Run: `python3 -m YYYY.advent_YYYY_day_DD`

##### e.g.
```
python3 -m 2019.advent_2019_day_1
```