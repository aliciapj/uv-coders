from collections import namedtuple

Slice = namedtuple('Slice', 'row_init col_init row_end col_end')


def write(solution, output_file):
    print('writing to', output_file)

    with open(output_file, 'w') as f:
        f.write('%d\n' % (len(solution),))
        for slice in solution:
            f.write('%d %d %d %d\n' % (slice.row_init, slice.col_init, slice.row_end, slice.col_end))
