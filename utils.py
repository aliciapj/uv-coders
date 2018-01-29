

def print_pizza(world):
    print('-')
    for row in world['pizza']:
        print(''.join(row))


def is_valid_slice(world, slice):
    m_count = 0
    t_count = 0
    cell_count = (slice.row_end - slice.row_init + 1) * (slice.col_end - slice.col_init + 1)
    for row in range(slice.row_init, slice.row_end + 1):
        for col in range(slice.col_init, slice.col_end + 1):
            cell = world['pizza'][row][col]
            if cell == 'T':
                t_count += 1
            if cell == 'M':
                m_count += 1
    return m_count >= world['min_of_each_ingredients'] and \
           t_count >= world['min_of_each_ingredients'] and \
           cell_count <= world['max_cells']


