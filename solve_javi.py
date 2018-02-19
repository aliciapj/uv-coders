from collections import defaultdict

from parse import UNAVAILABLE
from utils import servers_in_row


# solve.py
def solve_simple(world):
    world['rows'] = [
        [UNAVAILABLE, 0, 0, 0, 3],
        [1, 1, 1, 2, 2]
    ]
    world['pools'] = servers_into_pools(world)
    return world


def servers_into_pools(world):
    servers_by_rows = [
        list(servers_in_row(world, row))
        for row in world['rows']
    ]

    for r in servers_by_rows:
        print(r)

    pools = defaultdict(list)
    next_pool = 0
    next_row = 0
    row_count = len(world['rows'])
    pool_count = world['pool_counts']
    remaining_servers = sum(len(servers_in_row) for servers_in_row in servers_by_rows)

    while remaining_servers:
        while not servers_by_rows[next_row]:
            next_row = (next_row + 1) % row_count
        next_server = servers_by_rows[next_row].pop(0)
        pools[next_pool].append(next_server.id)
        next_pool = (next_pool + 1) % pool_count
        remaining_servers -= 1

    return pools

solve = solve_simple
