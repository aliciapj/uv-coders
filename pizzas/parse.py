def parse(input_file):
    with open(file=input_file, mode='r') as f:
        rows, cols, min_of_each_ingredient, max_cells = map(int, f.readline().strip().split(' '))
        pizza = [list(f.readline().strip()) for _ in range(rows)]

        world = {
            'min_of_each_ingredient': min_of_each_ingredient,
            'max_cells': max_cells,
            'pizza': pizza
        }

    return world
