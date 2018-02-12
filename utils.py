# utils.py
import os


def get_output_file(input_file):
    output_file = os.path.basename(os.path.splitext(input_file)[0]) + '_solution.txt'
    output_file = os.path.join('./output_files', output_file)
    return output_file


def calculate_score(world, solution):
    return 0
