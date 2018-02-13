# solve.py
from operator import itemgetter, attrgetter

from collections import defaultdict, namedtuple


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

SavingsTuple = namedtuple('SavingsTuple', 'cache_id video_id video_size savings')


def calculate_savings(world):
    savings = defaultdict(dict)
    savings_tuples = []
    for request in world['requests']:
        video_id = request['video']
        endpoint = world['endpoints'][request['endpoint']]
        for cache_id, cache_latency in endpoint['cache_latency'].items():
            savings[cache_id][video_id] = (endpoint['datacenter_latency'] - endpoint['cache_latency'][cache_id]) * request['count']
            video_size = world['videos'][video_id]
            savings_tuples.append( SavingsTuple(cache_id, video_id, video_size, (endpoint['datacenter_latency'] - endpoint['cache_latency'][cache_id]) * request['count']))
    return savings, savings_tuples


def solve_videos_per_cache_using_size_count_and_latency(world):
    videos_in_cache = videos_per_cache(world)
    savings, _ = calculate_savings(world)

    solution = {}
    for cache_id in range(0, len(world['caches'])):
        video_tuples_in_this_cache = [(video_id, world['videos'][video_id]) for video_id in videos_in_cache[cache_id]]
        video_tuples_in_this_cache = [(video_id, video_size, savings[cache_id][video_id]) for video_id, video_size in video_tuples_in_this_cache]
        videos_by_size = sorted(
            video_tuples_in_this_cache,
            key=lambda t: t[2] / t[1],
            reverse=True
        )

        size = 0
        videos = set()
        for video_id, video_size, video_savings in videos_by_size:
            if size + video_size > world['cache_size']:
                break
            size += video_size
            videos.add(video_id)

        solution[cache_id] = videos
    return solution


def solve_videos_by_savings(world):
    # videos_in_cache = videos_per_cache(world)
    _, savings_tuples = calculate_savings(world)

    savings_tuples = sorted(savings_tuples, key=attrgetter('savings'), reverse=True)

    solution = defaultdict(set)
    available_space = list(world['caches'])  # copy list
    print(len(savings_tuples))
    for i, t in enumerate(savings_tuples):
        if available_space[t.cache_id] >= t.video_size:
            solution[t.cache_id].add(t.video_id)
            available_space[t.cache_id] -= t.video_size
        if i % 1000 == 0:
            print('.', end='')

    return solution


# solve = solve_small_videos
# solve = solve_small_videos_per_cache
# solve = solve_videos_per_cache_using_size_count_and_latency
solve = solve_videos_by_savings
