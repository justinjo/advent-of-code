from advent_day import AdventDay
import re
import math

type Coord3D = tuple[int, int, int]
type CoordState = tuple[int, int, int, int, int, int, int, int]
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

    def get_state(self, moons: MoonsMap, vertex_i: int) -> CoordState:
        io, eur, gan, cal = moons.values()
        return (
            io['pos'][vertex_i],
            io['vel'][vertex_i],
            eur['pos'][vertex_i],
            eur['vel'][vertex_i],
            gan['pos'][vertex_i],
            gan['vel'][vertex_i],
            cal['pos'][vertex_i],
            cal['vel'][vertex_i],
        )

    def find_steps_in_loop(self, moons: MoonsMap) -> tuple[int, int, int]:
        x_map: dict[CoordState, int] = {}
        y_map: dict[CoordState, int] = {}
        z_map: dict[CoordState, int] = {}
        x_found = y_found = z_found = False
        step = x_steps = y_steps = z_steps = 0
        x_state = self.get_state(moons, 0)
        y_state = self.get_state(moons, 1)
        z_state = self.get_state(moons, 2)
        while not x_found or not y_found or not z_found:
            x_found |= x_state in x_map
            y_found |= y_state in y_map
            z_found |= z_state in z_map
            if not x_found:
                x_map[x_state] = step
            elif not x_steps:
                x_found = True
                x_steps = step
            if not y_found:
                y_map[y_state] = step
            elif not y_steps:
                y_found = True
                y_steps = step
            if not z_found:
                z_map[z_state] = step
            elif not z_steps:
                z_found = True
                z_steps = step
            self.simulate_motion(moons)
            x_state = self.get_state(moons, 0)
            y_state = self.get_state(moons, 1)
            z_state = self.get_state(moons, 2)
            step += 1
        return (x_steps, y_steps, z_steps)


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
            acc = f'acc=<x={a_x:3}, y={a_y:2}, z={a_z:2}>'
            print(f'moon: {id}\n' + pos + ', ' + vel + ', ' + acc)
        print()

    def part_one(self) -> int:
        moons = self.get_moon_coords()
        self.simulate_motion(moons, 1000)
        return self.calculate_total_energy(moons)

    def part_two(self) -> int:
        moons = self.get_moon_coords()
        x, y, z = self.find_steps_in_loop(moons)
        return math.lcm(x, y, z)


Advent2019Day12().run()