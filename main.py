from parse import parse
from solve_javi import solve
from utils import is_valid_slice
from writer import write, Slice

from solve_javi import solve

if __name__ == '__main__':
    world = parse(input_file='./input_files/input1.txt')

    # assert not is_valid_slice(world, Slice(0, 0, 0, 0))
    # assert is_valid_slice(world, Slice(0, 0, 1, 1))

    solution = solve(world)

    write(solution, 'solution.txt')
