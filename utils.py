

def print_pizza(world):
    print('-')
    for row in world['pizza']:
        print(''.join(row))


def get_slice_len(slice):
    return (slice.row_end - slice.row_init) * (slice.column_end - slice.column_init)