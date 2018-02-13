# solve.py
from collections import OrderedDict


def is_video_in_caches(video, caches, caches_info):
    return any([video in cache_info['videos'] for i, cache_info in enumerate(caches_info) if i in caches])


def solve(world):

    caches_info = [{'data_remain': world['cache_size'], 'videos': []} for cache in world['caches']]
    old_len_cache = -1
    new_len_cache = sum([len(cache['videos']) for cache in caches_info])
    i = 0

    while new_len_cache != old_len_cache and i < 10:

        old_len_cache = new_len_cache
        # recorrer los endpoints
        for endpoint_id, endpoint in enumerate(world['endpoints']):

            # filtrar los videos del endpoint
            requests = [request for request in world['requests'] if request['endpoint'] == endpoint_id]
            videos = sorted(requests, key=lambda t: t['count'], reverse = True)

            caches = endpoint['cache_latency'].keys()

            most_requested = None
            for video in videos:
                if not is_video_in_caches(video['video'], caches, caches_info):
                    most_requested = video
                    break

            if most_requested:
                sorted_caches = sorted(endpoint['cache_latency'].items(), key=lambda t: t[1])

                # añadir
                for cache in sorted_caches:
                    video_size = world['videos'][most_requested['video']]
                    cache_id = cache[0]
                    remaining_in_cache = caches_info[cache_id]['data_remain']
                    if video_size <= remaining_in_cache:
                        caches_info[cache_id]['data_remain'] -= video_size
                        caches_info[cache_id]['videos'].append(most_requested['video'])
                        break

        new_len_cache = sum([len(cache['videos']) for cache in caches_info])
        i += 1

    solution = {i: set(cache['videos']) for i, cache in enumerate(caches_info)}

    return solution
