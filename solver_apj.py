import itertools
import math
import copy

from collections import Counter
from writer import Slice
from utils import print_pizza, is_valid_slice, expand_slice, un_eat_slice, eat_slice


def get_first_appearance(pizza, ingredient):
    for i, row in enumerate(pizza):
        for j, ing in enumerate(row):
            if ing == ingredient:
                return i, j
    return -1, -1


def solve(world):

    # counting number of ingredients
    pizza = world['pizza']
    plain_pizza = list(itertools.chain.from_iterable(pizza))
    # get the less common
    less_common_ing = Counter(plain_pizza).most_common()[-1]

    # number of slices = round_down(less_common_ing.value / min_ing)
    number_slices = math.floor(less_common_ing[1]/world['min_of_each_ingredient'])

    tmp_world = copy.deepcopy(world)

    # generate number_slices initial portions
    slices = []
    for i in range(number_slices):
        first_ingredient = get_first_appearance(tmp_world['pizza'], less_common_ing[0])
        slice = Slice(first_ingredient[0], first_ingredient[1], first_ingredient[0], first_ingredient[1])
        slices.append(slice)
        tmp_world['pizza'][slice.row_init][slice.col_init] = 'X'

    result = []
    new_slices = copy.deepcopy(slices)
    valid_result = all([is_valid_slice(world, slice) for slice in slices])
    keep_expanding = True

    while len(new_slices) > 0 and keep_expanding:
        keep_expanding = False
        result = copy.deepcopy(new_slices)
        slices = copy.deepcopy(new_slices)
        new_slices = []
        for slice in slices:
            un_eat_slice(world, tmp_world, slice)
            candidates = expand_slice(tmp_world, slice)
            if candidates:
                # TODO explore all candidates instead 1
                new_slices.append(candidates[0])
                eat_slice(tmp_world, candidates[0])
                keep_expanding = True
            else:
                eat_slice(tmp_world, slice)
                new_slices.append(slice)

            print_pizza(tmp_world)

    valid_result = all([is_valid_slice(world, slice) for slice in new_slices])
    print(result)

    print_pizza(tmp_world)

    return result




