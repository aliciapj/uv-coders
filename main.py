import os
import sys
from parse import parse
from utils import get_output_file, calculate_score
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
    score = calculate_score(world, solution)
    print("SCORE: %d" % score)
    write(solution, output_file)
    return score


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        print("python3 needed")
        sys.exit(1)

    total_score = 0
    for input_file in config['input_files']:
        total_score += process_file(config['solve'], input_file)

    print('TOTAL SCORE: %d' % total_score)
