# utils.py
import os


def get_output_file(input_file):
    output_file = os.path.basename(os.path.splitext(input_file)[0]) + '.out'
    output_file = os.path.join('./output_files', output_file)
    return output_file


def analyze_world(world):
    # print interesting things about our world
    pass


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
