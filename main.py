import os
import sys
from parse import parse
from writer import write

from solve_javi import solve as solve_javi

config = {
    'solve': solve_javi,
    'input_files': [
        'input1.txt',
        'small.txt',
        'medium.txt',
        'large.txt',
    ]
}


def process_file(solve, input_file):
    world = parse(input_file=os.path.join('./input_files', input_file))

    solution = solve(world)

    output_file = os.path.basename(os.path.splitext(input_file)[0]) + '_solution.txt'
    output_file = os.path.join('./output_files', output_file)
    write(solution, output_file)


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        print("python3 needed")
        sys.exit(1)

    for input_file in config['input_files']:
        print("processing %s" % (input_file,))
        process_file(config['solve'], input_file)
