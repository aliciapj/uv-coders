# writer.py
def write(solution, output_file):
    print('writing to', output_file)

    with open(output_file, 'w') as f:
        f.write('%d\n' % (len(solution),))
        for cache_id, video_ids in solution.items():
            f.write('%s %s\n' % (cache_id, ' '.join(str(video_id) for video_id in video_ids)))
        pass


# write(solution_test, 'test1.txt')