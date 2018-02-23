from operator import itemgetter, attrgetter

from parse import UNAVAILABLE, AVAILABLE
from utils import servers_in_row, analyze_capacity_per_row, analyze_capacity_per_pool
from heapq import heappop, heappush

# solve.py
def solve_simple(world):
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
    # search a row with available space... rows are stored in a heap (priority queue) sorted by allocated capacity so far
    # we try to place a server first in the row with less allocated capacity... the goal is to have capacity as evenly
    # distributed as possible

    # maybe the first row we look at does not have enough space available for the server we want to place... we remove
    # these rows from the 'rows' heap, but we need to keep them, because maybe other smaller servers will fit in... we
    # keep them in 'rows_without_space' and we return them to the heap before exiting this function
    rows_without_space = []

    while rows:
        # lets take the row with less allocated capacity so far
        capacity, row = heappop(rows)

        # does our server fit in this row?
        slot = find_space(row, slots)
        if slot is not None:
            # put all previously examined rows back into the heap before returning
            for r in rows_without_space:
                heappush(rows, r)
            # return the row,slot and the current allocated capacity in the row
            return row, slot, capacity
        else:
            # the server does not fit in this row... let's put the row aside and examine next (with regard to allocated capacity) row
            rows_without_space.append((capacity, row))

    # we examined all rows and our server didn't fit in any of them... it was too large
    # let's put all previously examined rows back into the heap before returning
    for r in rows_without_space:
        heappush(rows, r)

    # server can't be placed
    return None, None, None


def servers_into_rows(world):
    # try to allocate servers into rows, the most powerful ones first
    servers = sorted(world['servers'], key=lambda s: s.capacity / s.size, reverse=True)

    # rows is a heapq sorted by allocated capacity
    rows = [(0, row) for row in world['rows']]
    while servers:
        # take next server
        next_server = servers.pop(0)

        # try to find a place for it, starting by the rows with less allocated capacity so far
        row, slot, capacity = find_row_with_space(rows, next_server.size)

        if row:
            # place the server in the row
            row[slot:slot + next_server.size] = [next_server.id] * next_server.size

            # place the row back into the heapq, with it's new allocated capacity
            heappush(rows, (capacity + next_server.capacity, row))


def servers_into_pools(world):
    # for each row, make a list of servers in the row, sorted by decreasing capacity
    servers_by_rows = [
        sorted(list(servers_in_row(world, row)), key=attrgetter('capacity'), reverse=True)
        for row in world['rows']
    ]

    for r in servers_by_rows:
        print(r)

    next_row = 0
    row_count = len(world['rows'])
    pool_count = world['pool_counts']
    remaining_servers = sum(len(servers_in_row) for servers_in_row in servers_by_rows)
    pools = [(0, []) for _ in range(pool_count)]

    # distribute all servers across pools
    while remaining_servers:
        while not servers_by_rows[next_row]:                # find the next row with any remaining servers
            next_row = (next_row + 1) % row_count
        next_server = servers_by_rows[next_row].pop(0)      # take the most powerful server available in the row
        capacity, next_pool = heappop(pools)                # take the pool with less allocated capacity so far
        next_pool.append(next_server.id)                    # add the server to the pool
        capacity += next_server.capacity
        heappush(pools, (capacity, next_pool))              # put the pool back into the heapq with the updated capacity
        remaining_servers -= 1

    return [pool[1] for pool in pools]          # take the second item of the tuple (the list of servers) for each pool


solve = solve_simple
