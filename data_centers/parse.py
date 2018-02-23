# parse.py
from collections import namedtuple

UNAVAILABLE = -2
AVAILABLE = -1
Server = namedtuple('Server', 'id size capacity')


def parse(input_file):

    world = {}

    with open(file=input_file, mode='r') as f:
        num_rows, num_slots, num_unavailables, num_pools, num_servers = f.readline().split(" ")
        world['rows'] = []
        for x in range(int(num_rows)):
            world['rows'].append([AVAILABLE]*int(num_slots))

        for a in range(int(num_unavailables)):
            x, y = f.readline().split(" ")
            world['rows'][int(x)][int(y)] = UNAVAILABLE

        world['pool_counts'] = int(num_pools)

        world['servers'] = []
        for i, x in enumerate(range(int(num_servers[:-1]))):
            size, capacity = f.readline().split(" ")
            world['servers'].append(Server(id=i, size=int(size), capacity=int(capacity)))

    return world
