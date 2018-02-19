from parse import UNAVAILABLE, AVAILABLE
from utils import servers_in_row, analyze_capacity_per_row, analyze_capacity_per_pool


# solve.py
def solve_simple(world):
    # world['rows'] = [
    #     [UNAVAILABLE, 0, 0, 0, 3],
    #     [1, 1, 1, 2, 2]
    # ]
    servers_into_rows(world)
    analyze_capacity_per_row(world)
    world['pools'] = servers_into_pools(world)
    analyze_capacity_per_pool(world)
    return world


def find_space(row, slots):
    for s in range(len(row)-slots+1):
        slot = row[s:s+slots]
        if slot.count(AVAILABLE) == slots:
            return s
    return None


def find_row_with_space(rows, next_row, slots):
    row_count = len(rows)
    first_row = next_row
    while True:
        slot = find_space(rows[next_row], slots)
        if not slot is None:
            return next_row, slot
        next_row = (next_row + 1) % row_count
        if next_row == first_row:
            return next_row, None


def servers_into_rows(world):
    servers = sorted(world['servers'], key=lambda s: s.capacity / s.size, reverse=True)

    row_count = len(world['rows'])
    next_row = 0
    while servers:
        next_server = servers.pop(0)
        next_row, slot = find_row_with_space(world['rows'], next_row, next_server.size)
        if not slot is None:
            world['rows'][next_row][slot:slot + next_server.size] = [next_server.id] * next_server.size



def servers_into_pools(world):
    servers_by_rows = [
        list(servers_in_row(world, row))
        for row in world['rows']
    ]

    for r in servers_by_rows:
        print(r)

    next_pool = 0
    next_row = 0
    row_count = len(world['rows'])
    pool_count = world['pool_counts']
    remaining_servers = sum(len(servers_in_row) for servers_in_row in servers_by_rows)
    pools = [[] for _ in range(pool_count)] # defaultdict(list)

    while remaining_servers:
        while not servers_by_rows[next_row]:
            next_row = (next_row + 1) % row_count
        next_server = servers_by_rows[next_row].pop(0)
        pools[next_pool].append(next_server.id)
        next_pool = (next_pool + 1) % pool_count
        remaining_servers -= 1

    return pools

solve = solve_simple
