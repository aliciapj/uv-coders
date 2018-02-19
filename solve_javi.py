from parse import UNAVAILABLE, AVAILABLE
from utils import servers_in_row, analyze_capacity_per_row, analyze_capacity_per_pool
from heapq import heappop, heappush

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


def find_row_with_space(rows, slots):
    rows_without_space = []
    while rows:
        capacity, row = heappop(rows)
        slot = find_space(row, slots)
        if slot is not None:
            for r in rows_without_space:
                heappush(rows, r)
            return row, slot, capacity
        else:
            rows_without_space.append((capacity, row))

    for r in rows_without_space:
        heappush(rows, r)

    return None, None, None


def servers_into_rows(world):
    servers = sorted(world['servers'], key=lambda s: s.capacity / s.size, reverse=True)

    rows = [(0, row) for row in world['rows']]
    while servers:
        next_server = servers.pop(0)
        row, slot, capacity = find_row_with_space(rows, next_server.size)
        if row:
            row[slot:slot + next_server.size] = [next_server.id] * next_server.size
            heappush(rows, (capacity + next_server.capacity, row))


def servers_into_pools(world):
    servers_by_rows = [
        list(servers_in_row(world, row))
        for row in world['rows']
    ]

    for r in servers_by_rows:
        print(r)

    next_row = 0
    row_count = len(world['rows'])
    pool_count = world['pool_counts']
    remaining_servers = sum(len(servers_in_row) for servers_in_row in servers_by_rows)
    pools = [(0, []) for _ in range(pool_count)]

    while remaining_servers:
        while not servers_by_rows[next_row]:
            next_row = (next_row + 1) % row_count
        next_server = servers_by_rows[next_row].pop(0)
        capacity, next_pool = heappop(pools)
        next_pool.append(next_server.id)
        capacity += next_server.capacity
        heappush(pools, (capacity, next_pool))
        remaining_servers -= 1

    return [pool[1] for pool in pools]

solve = solve_simple
