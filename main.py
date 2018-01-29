import parse from parse
import write from writer


def solve(world):
    return "SOLVED!"


if __name__ == '__main__':
    world = parse('input_files/input1.txt')

    solution = solve(world)

    write(solution,'solution.txt')
