import unittest
from parse import parse, UNAVAILABLE, AVAILABLE
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

