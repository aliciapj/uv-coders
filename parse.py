# parse.py
from collections import namedtuple


def parse(input_file):
    with open(file=input_file, mode='r') as f:
        world = {}

    server = namedtuple('Server', ['size', 'capacity'])

    world = dict(
        rows=[[-2, -1, -1, -1, -1],
              [-1, -1, -1, -1, -1]],
        servers=[server(size=3, capacity=10),
                 server(size=3, capacity=10),
                 server(size=2, capacity=5),
                 server(size=1, capacity=5),
                 server(size=1, capacity=1)],
        pool_counts=2
    )

    return world
