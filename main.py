from parse import parse
from solve_javi import solve
from writer import write

if __name__ == '__main__':
    world = parse(input_file='./input_files/input1.txt')

    solution = solve(world)

    write(solution, 'solution.txt')
