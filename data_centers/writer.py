# writer.py
def write(solution, output_file):
    print('writing to', output_file)

    with open(output_file, 'w') as f:

        for server_index, server_info in enumerate(solution['servers']):
            out_server = {}

            for row_index, row_info in enumerate(solution['rows']):
                try:
                    location_in_row = row_info.index(server_index)
                    out_server['row'] = row_index
                    out_server['slot'] = location_in_row
                except:
                    pass

            for pool_index, pool_info in enumerate(solution['pools']):
                if server_index in pool_info:
                    out_server['pool'] = pool_index

            if out_server:
                f.write('%d %d %d\n' % (out_server['row'], out_server['slot'], out_server['pool']))
            else:
                f.write('x\n')
