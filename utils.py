# utils.py
import os


def get_output_file(input_file):
    output_file = os.path.basename(os.path.splitext(input_file)[0]) + '.out'
    output_file = os.path.join('./output_files', output_file)
    return output_file


def analyze_world(world):
    pass


def calculate_score(world, solution):
    # Earns points: (distance) + (bonus)
    # Each ride completed before its latest finish earns the number of points equal
    # to the distance between the start intersection and the finish intersection.
    # Additionally, each ride which started exactly in its earliest allowed start step
    # gets an additional timeliness bonus of B.

    score = 0
    for ride in solution['rides']:
        distance = ride['duration']

        bonus_finish = ride['finish'] - ride['real_finish'] if ride['real_finish'] < ride['finish'] else 0
        bonus_start = solution['bonus'] if ride['real_start'] == ride['start'] else 0

        score += distance + bonus_finish + bonus_start

    return score


def distance(start, finish):
    return abs(start.r - finish.r) + abs(start.c - finish.c)
