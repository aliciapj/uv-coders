from utils import print_pizza, is_valid_slice, expand_slice
from writer import Slice


def find_slice(world, row, col):
    slices = [Slice(row, col, row, col)]

    while slices:
        slice = slices.pop()
        if is_valid_slice(world, slice):
            return slice
        else:
            slices += expand_slice(world, slice)

    return None


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
