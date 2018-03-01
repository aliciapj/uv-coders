# writer.py
def write(solution, output_file):
    print('writing to', output_file)

    with open(output_file, 'w') as f:

        for vehicle in solution['vehicles']:
            rides = [str(ride['id']) for ride in vehicle['rides']]
            f.write('{} {}\n'.format(len(vehicle['rides']), ' '.join(rides)))

if __name__ == '__main__':

    w = {
        'vehicles': [
            {'rides': [{'id': 0}]},
            {'rides': [{'id': 1},{'id': 2}]}
        ]
    }

    write(w, '/home/alicia/workspace/uv-coders/output.txt')