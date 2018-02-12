import os
import sys
from parse import parse
from utils import get_output_file
from writer import write

from solve_javi import solve as solve_javi

config = {
    'solve': solve_javi,
    'input_files': [
        'me_at_the_zoo.in',
        'videos_worth_spreading.in',
        'trending_today.in',
        'kittens.in',
    ]
}


def process_file(solve, input_file):
    print("processing %s" % (input_file,))
    output_file = get_output_file(input_file)

    world = parse(input_file=os.path.join('./input_files', input_file))
    solution = solve(world)
    write(solution, output_file)


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        print("python3 needed")
        sys.exit(1)

    for input_file in config['input_files']:
        process_file(config['solve'], input_file)
