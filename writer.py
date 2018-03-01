# writer.py
def write(world, solution, output_file):
    print('writing to', output_file)

    with open(output_file, 'w') as f:

        for car_id in range(world['n_cars']):
            rides = solution.get(car_id, [])
            f.write('{} {}\n'.format(len(rides), ' '.join(str(ride['id']) for ride in rides)))

# if __name__ == '__main__':
#
#     w = {
#         'vehicles': [
#             {'rides': [{'id': 0}]},
#             {'rides': [{'id': 1},{'id': 2}]}
#         ]
#     }
#
#     write(w, '/home/alicia/workspace/uv-coders/output.txt')
