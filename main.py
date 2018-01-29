import parse from parse
import write from writer

world = {
    min_cells: 1,
    max_cells: 6,
    pizza: [
        ['T','T','T','T','T'],
        ['T','M','M','M','T'],
        ['T','T','T','T','T'],
    ],
}


def solve(world):
    return "SOLVED!"


if __name__ == '__main__':
    # world = parse('input_files/input1.txt')

    solution = solve(world)

    write(solution,'solution.txt')
