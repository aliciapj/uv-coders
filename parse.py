# parse.py
def parse(input_file):
    with open(file=input_file, mode='r') as f:
        rows, cols, min_of_each_ingredient, max_cells = map(int, f.readline().strip().split(' '))
        # pizza = [list(f.readline().strip()) for _ in range(rows)]

        world = {
            'cache_size': 100,
            'caches': [100, 100, 100],
            'videos': [50, 50, 80, 30, 110],  # array de MBs
            'endpoints': [   # datacenter_latency: number, cache_latency: {id_cache: latency}
                {'datacenter_latency': 1000,
                 'cache_latency': [
                     {0: 100},
                     {2: 200},
                     {1: 300}
                 ]},
                {'datacenter_latency': 500,
                 'cache_latency': []}
            ],
            'requests': [  # video_id, endpoint_id, count
                {'endpoint': 0,
                 'video': 3,
                 'count': 1500},
                {'endpoint': 1,
                 'video': 0,
                 'count': 1000},
                {'endpoint': 0,
                 'video': 4,
                 'count': 500},
                {'endpoint': 0,
                 'video': 1,
                 'count': 1000}
            ],
        }

    return world
