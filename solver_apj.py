import itertools
import math
import copy

from collections import Counter
from main import world
from writer import Slice


def get_first_appearance(pizza, ingredient):
    for i, row in enumerate(pizza):
        for j, ing in enumerate(row):
            if ing == ingredient:
                return i, j
    return -1, -1


def get_slice_len(slice):
    return (slice.row_end - slice.row_init) * (slice.column_end - slice.column_init)


def expand(slice, pizza):
    # strategy: right - left - down - up
    candidate_index = slice.col_end + 1
    if candidate_index >= 0 and candidate_index < len(pizza[0]):  # if index is inside the pizza
         pass


def solve(world):
    # counting number of ingredients
    pizza = world['pizza']
    plain_pizza = list(itertools.chain.from_iterable(pizza))
    # get the less common
    less_common_ing = Counter(plain_pizza).most_common()[-1]

    # number of slices = round_down(less_common_ing.value / min_ing)
    number_slices = math.floor(less_common_ing[1]/world['min_of_each_ingredient'])

    first_ingredient = get_first_appearance(pizza, less_common_ing[0])

    tmp_pizza = copy.deepcopy(pizza)

    # first slice with only this ingredient
    slice = Slice(first_ingredient[0], first_ingredient[0], first_ingredient[1], first_ingredient[1])
    tmp_pizza[first_ingredient[0]][first_ingredient[1]] = 'X'

    while get_slice_len(slice) < world['max_cells']:
        expand(slice, tmp_pizza)






    return first_slice

print(solve(world))
