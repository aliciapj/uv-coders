# solve.py
from collections import OrderedDict


def is_video_in_caches(video, caches, caches_info):
    return any([video in cache_info['videos'] for i, cache_info in enumerate(caches_info) if i in caches])


def solve(world):

    solution = []
    caches_info = [{'data_remain': world['cache_size'], 'videos': []} for cache in world['caches']]

    # recorrer los endpoints
    for endpoint_id, endpoint in enumerate(world['endpoints']):

        # filtrar los videos del endpoint
        requests = [request for request in world['requests'] if request['endpoint'] == endpoint_id]
        videos = sorted(requests, key=lambda t: t['count'])

        most_requested = videos[-1]
        caches = endpoint['cache_latency'].keys()

        video_in_cache = is_video_in_caches(most_requested['video'], caches, caches_info)

        if not video_in_cache:
            # añadir
            for cache in caches:
                video_size = world['videos'][most_requested['video']]
                remaining_in_cache = caches_info[cache]['data_remain']
                if video_size <= remaining_in_cache:
                    caches_info[cache]['data_remain'] -= video_size
                    caches_info[cache]['videos'].append(most_requested['video'])
                    break
        else:
            # todo optimizar luego
            pass

    solution = {i: set(cache['videos']) for i, cache in enumerate(caches_info)}

    return solution
