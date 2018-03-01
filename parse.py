# parse.py
import os
from collections import namedtuple

import utils

Position = namedtuple('Position', 'r c')


def parse(input_file):
    world = {}

    input_file = os.path.join('./input_files', 'a_example.in')

    with open(file=input_file, mode='r') as f:
        n_rows, n_columns, n_fleet, n_rides, bonus, steps = f.readline().split(" ")

        world['grid'] = [[0]*int(n_columns)]*int(n_rows)
        world['n_cars'] = int(n_fleet)
        world['rides'] = []
        world['bonus'] = int(bonus)
        world['steps'] = int(steps)

        for n in range(int(n_rides)):
            # ride from [0, 0] to [1, 3], earliest start 2, latest finish 9
            from_r, from_c, to_r, to_c, earliest_start, latest_finish = f.readline().split(" ")
            start = Position(r=int(from_r), c=int(from_c))
            finish = Position(r=int(to_r), c=int(to_c))
            duration = utils.duration(start=start, finish=finish)
            ride = dict(
                id=n,
                start=start,
                finish=finish,
                earliest_start=int(earliest_start),
                latest_finish=int(latest_finish),
                latest_start=int(latest_finish)-duration,
                duration=duration
            )
            world['rides'].append(ride)

    return world
