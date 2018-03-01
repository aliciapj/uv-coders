# solve.py
from collections import namedtuple
from parse import Position
from utils import distance
import heapq

Car = namedtuple('Car', 'busy_until id pos')

def solve(world):

    t = 0

    cars = [Car(0, i, Position(0,0)) for i in range(world['n_cars'])] # coches ordenados por tiempo en el que se van a quedar libres
    rides = [] # rides ordenadas por latest_start
    assignments = []
    while t < world['T']:
        # mirar los coches que están libres
        while cars[0].busy_until < t:
            # para cada coche mirar los rides que podría atender, asignarle uno
            for ride_pos, ride in enumerate(rides):
                car_to_start = distance(car.pos, ride.start)
                if t + car_to_start < ride.latest_start:   # TODO: < o <= ?
                    # asignar la ride al coche
                    car = heapq.heappop(cars)
                    del rides[ride_pos]

                    # donde me guardo la asignación

                    # devolverlo a la lista
                    car_after = Car(busy_until=t + car_to_start + ride.duration, id=car.id, pos=ride.finish)
                    heapq.heappush(cars, car_after)

    solution = []
    return solution
