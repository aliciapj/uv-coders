# solve.py
from collections import namedtuple, defaultdict
from operator import itemgetter

from parse import Position
from utils import distance
import heapq

Car = namedtuple('Car', 'busy_until id pos')

DEBUG = False

def solve(world):
    cars = [Car(-1, i, Position(0, 0)) for i in range(world['n_cars'])]  # coches ordenados por tiempo en el que se van a quedar libres
    rides = sorted(world['rides'], key=itemgetter('latest_start'))  # rides ordenadas por latest_start
    solution = defaultdict(list)

    t = 0
    while t < world['steps'] and len(rides):
        # mirar los coches que están libres
        if DEBUG:
            print('instante %d' % (t,))
        first_car = cars[0]
        if cars[0].busy_until < t:
            # para cada coche mirar los rides que podría atender, asignarle uno
            for ride_pos, ride in enumerate(rides):
                car = cars[0]
                car_to_start = distance(car.pos, ride['start'])
                if ride['earliest_start'] <= t + car_to_start <= ride['latest_start']:   # TODO: < o <= ?
                    # asignar la ride al coche
                    car = heapq.heappop(cars)
                    del rides[ride_pos]

                    if DEBUG:
                        print('asignando ride', ride)
                        print('a', car)
                        print('quedan %d rides por asignar' % (len(rides),))

                    ride['real_start'] = t + car_to_start
                    ride['real_finish'] = t + car_to_start + ride['duration']
                    solution[car.id].append(ride)

                    # devolverlo a la lista
                    car_after = Car(busy_until=ride['real_finish'], id=car.id, pos=ride['finish'])
                    heapq.heappush(cars, car_after)

        if first_car == cars[0]:  # couldn't assign anything to this car... get rid of it
            if DEBUG:
                print("getting rid of car %d" % (cars[0].id,))
            heapq.heappop(cars)

        t += cars[0].busy_until + 1  # avanzo la simulación hasta que el próximo coche se quede libre

    solution = dict(solution)  # freeze defaultdict()
    print('SOLUTION')
    print(solution)
    return solution
