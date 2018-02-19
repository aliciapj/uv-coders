import unittest

import os

from parse import parse, Server, UNAVAILABLE, AVAILABLE
from utils import calculate_score, next_row
from solve_javi import find_row_with_space, find_space

class TestCalculateScore(unittest.TestCase):

    def test_calculate_score(self):
        world = parse('input_files/example.in')
        print(world)

        # sample solution
        world['rows'] = [
            [UNAVAILABLE, 0, 0, 0, 3],
            [1, 1, 1, 2, 2]
        ]
        world['pools'] = [
            [0, 2],
            [1, 3]
        ]
        self.assertEqual(calculate_score(world, None), 5, 'ha fallado el test!')

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

    def test_find_row_with_space(self):
        rows = [
            [AVAILABLE, AVAILABLE, AVAILABLE, AVAILABLE, AVAILABLE],
            [AVAILABLE, AVAILABLE, AVAILABLE, AVAILABLE, AVAILABLE],
            [AVAILABLE, AVAILABLE, AVAILABLE, AVAILABLE, AVAILABLE],
        ]
        self.assertEqual((0, 0), find_row_with_space(rows, 0, 1))
        self.assertEqual((1, 0), find_row_with_space(rows, 1, 1))

        self.assertEqual((0, 0), find_row_with_space(rows, 0, 3))
        self.assertEqual((2, 0), find_row_with_space(rows, 2, 3))

        self.assertEqual((0, 0), find_row_with_space(rows, 0, 5))
        self.assertEqual((2, 0), find_row_with_space(rows, 2, 5))

        self.assertEqual((0, None), find_row_with_space(rows, 0, 6))
        self.assertEqual((1, None), find_row_with_space(rows, 1, 6))

        rows = [
            [UNAVAILABLE, AVAILABLE, UNAVAILABLE, AVAILABLE, AVAILABLE],
            [AVAILABLE, AVAILABLE, AVAILABLE, UNAVAILABLE, AVAILABLE],
            [AVAILABLE, AVAILABLE, UNAVAILABLE, AVAILABLE, AVAILABLE],
        ]
        self.assertEqual((0, 1), find_row_with_space(rows, 0, 1))
        self.assertEqual((1, 0), find_row_with_space(rows, 1, 1))

        self.assertEqual((0, 3), find_row_with_space(rows, 0, 2))
        self.assertEqual((1, 0), find_row_with_space(rows, 1, 2))
        self.assertEqual((2, 0), find_row_with_space(rows, 2, 2))

        self.assertEqual((1, 0), find_row_with_space(rows, 0, 3))
        self.assertEqual((1, 0), find_row_with_space(rows, 2, 3))

    def test_next_row1(self):
        world = parse(input_file=os.path.join('./input_files', 'example.in'))
        new_row, new_up_down = next_row(world=world, current_row=0, up_down=1)
        self.assertEqual(new_row, 1)
        self.assertEqual(new_up_down, 1)

    def test_next_row2(self):
        world = parse(input_file=os.path.join('./input_files', 'example.in'))
        new_row, new_up_down = next_row(world=world, current_row=1, up_down=1)
        self.assertEqual(new_row, 1)
        self.assertEqual(new_up_down, -1)

    def test_next_row3(self):
        world = parse(input_file=os.path.join('./input_files', 'example.in'))
        new_row, new_up_down = next_row(world=world, current_row=1, up_down=-1)
        self.assertEqual(new_row, 0)
        self.assertEqual(new_up_down, -1)

    def test_next_row4(self):
        world = parse(input_file=os.path.join('./input_files', 'example.in'))
        new_row, new_up_down = next_row(world=world, current_row=0, up_down=-1)
        self.assertEqual(new_row, 0)
        self.assertEqual(new_up_down, 1)
