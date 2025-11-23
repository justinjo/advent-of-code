from advent_day import AdventDay
import re

type Coord3D = tuple[int, int, int]
type Moon = dict # [str, Coord3D | list[int]
type MoonsMap = dict[str, Moon]

class Advent2019Day12(AdventDay):

    REGEX_PATTERN = r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>'
    DEFAULT_COORD: Coord3D = (0, 0, 0)
    MOONS = ('io', 'europa', 'ganymede', 'callisto')

    def match_regex(self, string: str) -> Coord3D:
        match = re.match(self.REGEX_PATTERN, string)
        if match:
            x, y, z = [int(m) for m in match.groups()]
            return (x, y, z)
        return self.DEFAULT_COORD

    def get_moon_coords(self) -> MoonsMap:
        moons = {}
        for i in range(self.input_length):
            moons[self.MOONS[i]] = {
                'pos': self.match_regex(self.input_str_array[i]),
                'vel': self.DEFAULT_COORD,
                'acc': [0, 0, 0],
            }
        return moons

    def calculate_acceleration(self, moon_1: Moon, moon_2: Moon) -> Coord3D:
        a_x = a_y = a_z = 0
        if moon_1['pos'][0] != moon_2['pos'][0]:
            a_x = 1 if moon_1['pos'][0] < moon_2['pos'][0] else -1
        if moon_1['pos'][1] != moon_2['pos'][1]:
            a_y = 1 if moon_1['pos'][1] < moon_2['pos'][1] else -1
        if moon_1['pos'][2] != moon_2['pos'][2]:
            a_z = 1 if moon_1['pos'][2] < moon_2['pos'][2] else -1
        return (a_x, a_y, a_z)

    def simulate_motion(self, moons: MoonsMap, steps: int = 1) -> None:
        for _ in range(steps):
            for i in range(len(moons)):
                moon_i = moons[self.MOONS[i]]
                for j in range(i + 1, len(moons)):
                    moon_j = moons[self.MOONS[j]]
                    a_x, a_y, a_z = self.calculate_acceleration(moon_i, moon_j)
                    moon_i['acc'][0] += a_x
                    moon_i['acc'][1] += a_y
                    moon_i['acc'][2] += a_z
                    moon_j['acc'][0] -= a_x
                    moon_j['acc'][1] -= a_y
                    moon_j['acc'][2] -= a_z
            for moon in moons.values():
                p_x, p_y, p_z = moon['pos']
                v_x, v_y, v_z = moon['vel']
                a_x, a_y, a_z = moon['acc']
                v_x += a_x
                v_y += a_y
                v_z += a_z
                moon['vel'] = (v_x, v_y, v_z)
                moon['pos'] = (p_x + v_x, p_y + v_y, p_z + v_z)
                moon['acc'] = [0, 0, 0]

    def calculate_total_energy(self, moons: MoonsMap) -> int:
        total_energy = 0
        for moon in moons.values():
            potential_energy = sum([abs(p) for p in moon['pos']])
            kinetic_energy = sum([abs(i) for i in moon['vel']])
            total_energy += potential_energy * kinetic_energy
        return total_energy

    def print_moons(self, moons: MoonsMap, step: str = '') -> None:
        if step:
            print(f'after step: {step}')
        for id in moons:
            moon = moons[id]
            p_x, p_y, p_z = moon['pos']
            v_x, v_y, v_z = moon['vel']
            a_x, a_y, a_z = moon['acc']
            pos = f'pos=<x={p_x:3}, y={p_y:2}, z={p_z:2}>'
            vel = f'vel=<x={v_x:3}, y={v_y:2}, z={v_z:2}>'
            acc = f'delta=<x={a_x:3}, y={a_y:2}, z={a_z:2}>'
            print(f'moon: {id} ' + pos + ', ' + vel + ', ' + acc)
        print()

    def part_one(self) -> int:
        moons = self.get_moon_coords()
        self.simulate_motion(moons, 1000)
        return self.calculate_total_energy(moons)

    def part_two(self) -> str:
        ...


Advent2019Day12().run()