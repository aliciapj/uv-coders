# writer.py
from sets import Set

solution_test = { # cache_id -> video_ids
    0: Set([2]),
    1: Set([3, 1]),
    2: Set([0, 1]),
}

def write(solution, output_file):
    print('writing to', output_file)

    with open(output_file, 'w') as f:
        f.write('%d\n' % (len(solution),))
        for cache_id, video_ids in solution.iteritems():
            f.write('%s %s\n' % (cache_id, ' '.join(str(video_id) for video_id in video_ids)))
        pass


# write(solution_test, 'test1.txt')