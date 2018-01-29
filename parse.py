def parse(input_file):

    f = open(file=input_file, mode='r')

    first_line = f.readline()
    first_line = first_line.split(' ')
    pizza = []
    for line in f:
        pizza.append([ch for ch in line[:-1]])

    world = dict(
        min_of_each_ingredient=int(first_line[2]),
        max_cells=int(first_line[3][:-1]),
        pizza=pizza
    )

    return world
