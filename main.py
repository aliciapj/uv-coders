from parse import parse
from writer import write, Slice


world = {
    'min_of_each_ingredient': 1,
    'max_cells': 6,
    'pizza': [
        ['T', 'T', 'T', 'T', 'T'],
        ['T', 'M', 'M', 'M', 'T'],
        ['T', 'T', 'T', 'T', 'T'],
    ],
}





def solve(world):

    # search for first available ingredient

    # try to find a suitable slice

    # add to list of slices
    return solution


if __name__ == '__main__':
    # world = parse('input_files/input1.txt')

    solution = solve(world)

    write(solution, 'solution.txt')
