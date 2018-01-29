from pathlib import Path

import os

from parse import parse
from solve_javi import solve
from utils import is_valid_slice
from writer import write, Slice

from solve_javi import solve

if __name__ == '__main__':
    ROOT_DIR = Path(os.path.abspath(__file__)).parent
    filename = os.path.join(ROOT_DIR, "input_files", "input1.txt")

    world = parse(input_file=filename)

    # assert not is_valid_slice(world, Slice(0, 0, 0, 0))
    # assert is_valid_slice(world, Slice(0, 0, 1, 1))

    solution = solve(world)

    write(solution, 'solution.txt')
