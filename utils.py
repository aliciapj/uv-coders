from writer import Slice


def print_pizza(world):
    print('-')
    for row in world['pizza']:
        print(''.join(row))


def is_valid_slice(world, slice):
    m_count = 0
    t_count = 0
    cell_count = get_slice_len(slice)
    for row in range(slice.row_init, slice.row_end + 1):
        for col in range(slice.col_init, slice.col_end + 1):
            cell = world['pizza'][row][col]
            if cell == 'T':
                t_count += 1
            if cell == 'M':
                m_count += 1
    return m_count >= world['min_of_each_ingredient'] and \
           t_count >= world['min_of_each_ingredient'] and \
           cell_count <= world['max_cells']


def get_slice_len(slice):
    return (slice.row_end - slice.row_init + 1) * (slice.col_end - slice.col_init + 1)


def is_available_slice(world, slice):
    for row in range(slice.row_init, slice.row_end + 1):
        for col in range(slice.col_init, slice.col_end + 1):
            if world['pizza'][row][col] == 'X':
                return False
    return True


def expand_slice(world, slice):
    row_count = len(world['pizza'])
    col_count = len(world['pizza'][0])

    slices = []

    # expand up
    if slice.row_init != 0:
        new_slice = Slice(slice.row_init - 1, slice.col_init, slice.row_end, slice.col_end)
        if is_available_slice(world, new_slice) and get_slice_len(new_slice) <= world['max_cells']:
            slices.append(new_slice)

    # expand down
    if slice.row_end != row_count-1:
        new_slice = Slice(slice.row_init, slice.col_init, slice.row_end+1, slice.col_end)
        if is_available_slice(world, new_slice) and get_slice_len(new_slice) <= world['max_cells']:
            slices.append(new_slice)

    # expand left
    if slice.col_init != 0:
        new_slice = Slice(slice.row_init, slice.col_init-1, slice.row_end, slice.col_end)
        if is_available_slice(world, new_slice) and get_slice_len(new_slice) <= world['max_cells']:
            slices.append(new_slice)

    # expand right
    if slice.col_init != col_count-1:
        new_slice = Slice(slice.row_init, slice.col_init, slice.row_end, slice.col_end+1)
        if is_available_slice(world, new_slice) and get_slice_len(new_slice) <= world['max_cells']:
            slices.append(new_slice)

    return slices

