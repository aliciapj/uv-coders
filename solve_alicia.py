# solve.py
from collections import defaultdict
from operator import itemgetter

import utils
from parse import Position
from utils import distance


def solve(world):
    cars = [{'busy_until' :-1, 'id': i, 'pos': Position(0, 0)} for i in range(world['n_cars'])]  # coches ordenados por tiempo en el que se van a quedar libres
    rides = sorted(world['rides'], key=itemgetter('latest_start'))  # rides ordenadas por latest_start
    solution = defaultdict(list)

    t = 0
    while t < world['steps'] and len(rides):
        # mirar los coches que están libres
        for car in cars:
            if car['busy_until'] < t:
                # para cada coche mirar los rides que podría atender, asignarle uno
                ride = utils.get_ride_by_start_bonus_apj(world, t, car, rides)
                if not ride:
                    continue

                rides = [r for r in rides if r['id'] != ride['id']]

                car_to_start = distance(start=car['pos'], finish=ride['start'])
                ride['real_start'] = t + car_to_start
                ride['real_finish'] = t + car_to_start + ride['duration']
                solution[car['id']].append(ride)

                car['busy_until'] = ride['real_finish']

        sorted_rides = sorted(cars, key=lambda car: car['busy_until'])
        t += sorted_rides[0]['busy_until'] + 1  # avanzo la simulación hasta que el próximo coche se quede libre

    solution = dict(solution)  # freeze defaultdict()
    print('SOLUTION')
    print(solution)
    return solution
