# solve.py
from operator import itemgetter

from collections import defaultdict


def solve_small_videos(world):
    # coloca siempre todos los videos pequeños en todas las caches

    videos_by_size = sorted(enumerate(world['videos']), key=itemgetter(1))

    size = 0
    videos = set()
    for video_id, video_size in videos_by_size:
        if size + video_size > world['cache_size']:
            break
        size += video_size
        videos.add(video_id)

    solution = {cache_id: videos for cache_id in range(0, len(world['caches']))}

    return solution



def endpoints_per_cache(world):
    result = defaultdict(set)

    for cache_id in range(0, len(world['caches'])):
        for endpoint_id, endpoint in enumerate(world['endpoints']):
            if cache_id in endpoint['cache_latency']:
                result[cache_id].add(endpoint_id)

    return result


def videos_per_endpoint(world):
    result = defaultdict(set)

    for request in world['requests']:
        result[request['endpoint']].add(request['video'])

    return result


def videos_per_cache(world):
    endpoints = endpoints_per_cache(world)
    videos = videos_per_endpoint(world)
    result = {}
    for cache_id in range(0, len(world['caches'])):
        result[cache_id] = set().union( *[videos[endpoint_id] for endpoint_id in endpoints[cache_id]])
    return result


def solve_small_videos_per_cache(world):

    videos_in_cache = videos_per_cache(world)

    #
    # solution = {cache_id: videos for cache_id in range(0, len(world['caches']))}
    #
    solution = {}
    for cache_id in range(0, len(world['caches'])):
        video_tuples_in_this_cache = [(video_id, world['videos'][video_id]) for video_id in videos_in_cache[cache_id]]
        videos_by_size = sorted(
            video_tuples_in_this_cache,
            key=itemgetter(1)
        )

        size = 0
        videos = set()
        for video_id, video_size in videos_by_size:
            if size + video_size > world['cache_size']:
                break
            size += video_size
            videos.add(video_id)

        solution[cache_id] = videos

    return solution


# solve = solve_small_videos
solve = solve_small_videos_per_cache
