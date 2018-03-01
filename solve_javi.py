# solve.py
from collections import namedtuple, defaultdict
from operator import itemgetter

from parse import Position
from utils import distance
import heapq

Car = namedtuple('Car', 'busy_until id pos')

def solve(world):


    cars = [Car(-1, i, Position(0, 0)) for i in range(world['n_cars'])]  # coches ordenados por tiempo en el que se van a quedar libres
    rides = sorted(world['rides'], key=itemgetter('latest_start'))  # rides ordenadas por latest_start
    solution = defaultdict(list)

    t = 0
    while t < world['steps'] and len(rides):
        # mirar los coches que están libres
        while cars[0].busy_until < t:
            # para cada coche mirar los rides que podría atender, asignarle uno
            for ride_pos, ride in enumerate(rides):
                car = cars[0]
                car_to_start = distance(car.pos, ride['start'])
                if t + car_to_start <= ride['latest_start']:   # TODO: < o <= ?
                    # asignar la ride al coche
                    car = heapq.heappop(cars)
                    del rides[ride_pos]

                    ride['real_start'] = t + car_to_start
                    ride['real_finish'] = t + car_to_start
                    solution[car.id].append(ride)

                    # devolverlo a la lista
                    car_after = Car(busy_until=t + car_to_start + ride['duration'], id=car.id, pos=ride['finish'])
                    heapq.heappush(cars, car_after)

        t = cars[0].busy_until+1  # avanzo la simulación hasta que el próximo coche se quede libre

    return solution
