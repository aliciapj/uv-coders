from pathlib import Path

import os

from parse import parse
from solve_javi import solve
from writer import write

from solve_javi import solve

if __name__ == '__main__':
    ROOT_DIR = Path(os.path.abspath(__file__)).parent
    filename = os.path.join(ROOT_DIR, "input_files", "input1.txt")

    world = parse(input_file=filename)

    solution = solve(world)

    write(solution, 'solution.txt')
