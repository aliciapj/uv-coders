# parse.py
def parse(input_file):
    with open(file=input_file, mode='r') as f:

        world = {}

        video_count, endpoint_count, request_count, cache_count, cache_size = \
            [int(data) for data in f.readline().strip().split(' ')]

        world['cache_size'] = cache_size
        world['caches'] = [cache_size for _ in range(cache_count)]

        # parsing videos
        world['videos'] = [int(size) for size in f.readline().strip().split(' ')]

        # parsing endpoints
        world['endpoints'] = []

        for _ in range(endpoint_count):
            datacenter_latency, caches = [int(data) for data in f.readline().strip().split(' ')]
            # read endpoint latency
            endpoint = {'datacenter_latency': datacenter_latency,
                        'cache_latency': {}}

            for _ in range(caches):
                cache_id, latency = [int(data) for data in f.readline().strip().split(' ')]
                endpoint['cache_latency'][cache_id] = latency

            world['endpoints'].append(endpoint)

        # parsing requests
        world['requests'] = []
        for _ in range(request_count):
            video_id, endpoint_id, request_count= [int(data) for data in f.readline().strip().split(' ')]
            world['requests'].append(
                {
                    'endpoint': endpoint_id,
                    'video': video_id,
                    'count': request_count,
                }
            )

        # world = {
        #     'cache_size': 100,
        #     'caches': [100, 100, 100],
        #     'videos': [50, 50, 80, 30, 110],  # array de MBs
        #     'endpoints': [   # datacenter_latency: number, cache_latency: {id_cache: latency}
        #         {'datacenter_latency': 1000,
        #          'cache_latency': {
        #              0: 100,
        #              2: 200,
        #              1: 300,
        #          }},
        #         {'datacenter_latency': 500,
        #          'cache_latency': {}}
        #     ],
        #     'requests': [  # video_id, endpoint_id, count
        #         {'endpoint': 0,
        #          'video': 3,
        #          'count': 1500},
        #         {'endpoint': 1,
        #          'video': 0,
        #          'count': 1000},
        #         {'endpoint': 0,
        #          'video': 4,
        #          'count': 500},
        #         {'endpoint': 0,
        #          'video': 1,
        #          'count': 1000}
        #     ],
        # }

    return world
