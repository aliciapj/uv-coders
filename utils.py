# utils.py
import os
from itertools import groupby
from parse import AVAILABLE, UNAVAILABLE


def get_output_file(input_file):
    output_file = os.path.basename(os.path.splitext(input_file)[0]) + '.out'
    output_file = os.path.join('./output_files', output_file)
    return output_file


def analyze_world(world):
    total_available_space = sum(row.count(AVAILABLE) for row in world['rows'])
    total_servers_size = sum(server.size for server in world['servers'])
    print('Total Available Space: %d' % (total_available_space,))
    print('Total Servers Size: %d' % (total_servers_size,))
    print('Total Servers Capacity: %d' % (sum(server.capacity for server in world['servers']),))


def servers_in_row(world, row):
    # group[0] is the server_id
    return (world['servers'][group[0]] for group in groupby(row) if group[0] not in (UNAVAILABLE, AVAILABLE))


def analyze_capacity_per_row(world):
    for row_id, row in enumerate(world['rows']):
        row_capacity = sum(server.capacity for server in servers_in_row(world, row))
        print('row %d, capacity: %d', row_id, row_capacity)


def calculate_pool_capacity(world, pool, row_down):
    capacity = 0
    for server_id in pool:
        if server_id not in row_down:
            capacity += world['servers'][server_id].capacity
    return capacity


def calculate_score(world, solution):
    capacities = []
    for row_index, row in enumerate(world['rows']):
        # suponemos que se viene abajo esta row
        for pool_id, pool in enumerate(world['pools']):
            capacities.append(calculate_pool_capacity(world, pool, row_down=row))

    return min(capacities)


def next_row(world, current_row, up_down):
    num_rows = len(world['rows'])

    new_row = current_row + up_down
    new_up_down = up_down

    if new_row == -1 or new_row >= num_rows:
        new_row = current_row
        new_up_down = -up_down

    return new_row, new_up_down
