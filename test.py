import unittest

import os

from parse import parse, Server, UNAVAILABLE
from utils import calculate_score


class TestCalculateScore(unittest.TestCase):
    def setUp(self):
        self.world = parse('input_files/example.in')

    def test_calculate_score(self):
        print(self.world)

        # sample solution
        self.world['rows'] = [
            [UNAVAILABLE, 0, 0, 0, 3],
            [1, 1, 1, 2, 2]
        ]
        self.world['pools'] = [
            [0, 2],
            [1, 3]
        ]
        self.assertEqual(calculate_score(self.world, None), 5, 'ha fallado el test!')

    def test_parser(self):
        world = parse(input_file=os.path.join('./input_files', 'example.in'))
        expected = dict(
            rows=[[-2, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1]],
            servers=[Server(0, 3, 10),
                     Server(1, 3, 10),
                     Server(2, 2, 5),
                     Server(3, 1, 5),
                     Server(4, 1, 1)],
            pool_counts=2
        )
        self.assertDictEqual(world, expected)
