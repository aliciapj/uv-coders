import unittest

import os

from parse import parse
from utils import calculate_score


class TestCalculateScore(unittest.TestCase):

    def test_calculate_score(self):
        world = parse('input_files/example.in')
        # print(world)
        #
        # # sample solution
        # world['rows'] = [
        #     [UNAVAILABLE, 0, 0, 0, 3],
        #     [1, 1, 1, 2, 2]
        # ]
        # world['pools'] = [
        #     [0, 2],
        #     [1, 3]
        # ]
        self.assertEqual(calculate_score(world, None), 5, 'ha fallado el test!')

    def test_parser(self):
        world = parse(input_file=os.path.join('./input_files', 'example.in'))
        expected = {
            'rows': [
                [-2, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1]
            ],
            'servers': [
                Server(0, 3, 10),
                Server(1, 3, 10),
                Server(2, 2, 5),
                Server(3, 1, 5),
                Server(4, 1, 1)
            ],
            'pool_counts': 2
        }
        self.assertDictEqual(world, expected)
