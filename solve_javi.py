from utils import print_pizza
from writer import Slice


def is_valid_slice(world, slice):
    m_count = 0
    t_count = 0
    cell_count = (slice.row_end - slice.row_init + 1) * (slice.col_end - slice.col_init + 1)
    for row in range(slice.row_init, slice.row_end + 1):
        for col in range(slice.col_init, slice.col_end + 1):
            cell = world['pizza'][row][col]
            if cell == 'T':
                t_count += 1
            if cell == 'M':
                m_count += 1
    return m_count >= world['min_of_each_ingredients'] and t_count >= world['min_of_each_ingredients'] and cell_count <= \
           world['max_cells']


def find_slice(world, row, col):
    slice = Slice(row, col, row, col)
    m_count, t_count, cell_count = is_valid_slice(world, slice)

    return slice


def find_cell(world):
    row_count = len(world['pizza'])
    col_count = len(world['pizza'][0])
    for row in range(row_count):
        for col in range(col_count):
            if world['pizza'][row][col] != 'X':
                return row, col
    return None, None


def solve(world):
    solution = []

    while True:
        # search for first available cell
        row, col = find_cell(world)
        if row == None and col == None:
            # don't have any available cells
            return solution

        # try to find a suitable slice starting at row, col
        slice = find_slice(world, row, col)

        if slice:
            for row in range(slice.row_init, slice.row_end + 1):
                for col in range(slice.col_init, slice.col_end + 1):
                    world['pizza'][row][col] = 'X'
            # add to list of slices
            solution.append(slice)
        else:
            world['pizza'][row][col] = 'X'

        print_pizza(world)

    return solution
