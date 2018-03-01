import os
import sys
import time

from parse import parse
from utils import get_output_file, calculate_score, analyze_world
from writer import write

from solve_javi import solve as solve_javi

config = {
    'solve': solve_javi,
    'input_files': [
        'a_example.in',
        'b_should_be_easy.in',
        'c_no_hurry.in',
        'd_metropolis.in',
        'e_high_bonus.in',
    ]
}


def process_file(solve, input_file):
    print("processing %s" % (input_file,))
    output_file = get_output_file(input_file)

    world = parse(input_file=os.path.join('./input_files', input_file))
    analyze_world(world)
    t0 = time.time()
    solution = solve(world)
    t1 = time.time()
    print("solution took %.1f sec" % (t1 - t0,))
    score = calculate_score(world, solution)
    t2 = time.time()
    print("calculate score took %.1f sec" % (t2 - t1,))
    print("SCORE: %d" % score)
    write(solution, output_file)
    return score


if __name__ == '__main__':
    if sys.version_info < (3, 0):
        print("python3 needed")
        sys.exit(1)

    t0 = time.time()
    total_score = 0
    for input_file in config['input_files']:
        total_score += process_file(config['solve'], input_file)

    print('TOTAL SCORE: %d' % total_score)
    t1 = time.time()
    print("TOTAL TIME: %.1f sec" % (t1 - t0,))
