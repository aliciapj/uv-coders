# utils.py
import os


def get_output_file(input_file):
    output_file = os.path.basename(os.path.splitext(input_file)[0]) + '.out'
    output_file = os.path.join('./output_files', output_file)
    return output_file


def analyze_world(world):
    pass


def calculate_score(world, solution):
    score = 0
    return score


def duration(start, finish):
    return abs(start.r - finish.r) + abs(start.c - finish.c)
