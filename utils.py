# utils.py
import os


def get_output_file(input_file):
    output_file = os.path.basename(os.path.splitext(input_file)[0]) + '_solution.txt'
    output_file = os.path.join('./output_files', output_file)
    return output_file


def analyze_world(world):
    print("total capacity: %d" % sum(world['caches']))
    print("total video size: %d" % sum(world['videos']))


TOO_BIG_LATENCY = 1000000


def calculate_score(world, solution):
    score = 0
    total_requests = 0
    for request in world['requests']:
        endpoint = world['endpoints'][request['endpoint']]
        caches_containing_video = [cache_id for (cache_id, videos) in solution.items() if request['video'] in videos]
        min_latency = min((endpoint['cache_latency'].get(cache, TOO_BIG_LATENCY) for cache in caches_containing_video),
                          default=None)
        latency_to_data_center = endpoint['datacenter_latency']

        if min_latency and min_latency < latency_to_data_center:
            time_saved = latency_to_data_center - min_latency
            score += time_saved * request['count']

        total_requests += request['count']

    return score * 1000 / total_requests
