from collections import namedtuple

Slice = namedtuple('Slice', 'row_init col_init row_end col_end')


def write(solution, output_file):
    print('writing to', output_file)
    
    # parse Slices tuples to lines
    lines = []
    lines.append(str(len(solution)))
    for slice in solution:
        line = [str(slice[0]), str(slice[1]), str(slice[2]), str(slice[3])]
        lines.append(' '.join(line))
    # write file
    f = open(output_file, 'w')
    f.write('\n'.join(lines))
    f.close()