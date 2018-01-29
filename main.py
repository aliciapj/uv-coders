from parse import parse
from writer import write, Slice
from utils import print_pizza

world = {
    'min_of_each_ingredient': 1,
    'max_cells': 6,
    'pizza': [
        ['T', 'T', 'T', 'T', 'T'],
        ['T', 'M', 'M', 'M', 'T'],
        ['T', 'T', 'T', 'T', 'T'],
    ],
}


def find_slice(world, row, col):
    return Slice(row, col, row, col)


def solve(world):
    solution = []

    while True:
        # search for first available ingredient
        row_count = len(world['pizza'])
        col_count = len(world['pizza'][0])
        for row in range(row_count):
            for col in range(col_count):
                if world['pizza'][row][col] != 'X':
                    break
        if row == row_count and col == col_count:
            # don't have any available cells
            return solution

        # try to find a suitable slice starting at row, col
        slice = find_slice(world, row, col)

        if slice:
            for row in range(slice.row_init, slice.row_end+1):
                for col in range(slice.col_init, slice.col_end+1):
                    world['pizza'][row][col] = 'X'
            # add to list of slices
            solution.append(slice)
        else:
            world['pizza'][row][col] = 'X'

        print_pizza(world)

    return solution


if __name__ == '__main__':
    # world = parse('input_files/input1.txt')

    solution = solve(world)

    write(solution, 'solution.txt')
