# utils.py
import os


def get_output_file(input_file):
    output_file = os.path.basename(os.path.splitext(input_file)[0]) + '.out'
    output_file = os.path.join('./output_files', output_file)
    return output_file


def analyze_world(world):
    pass


def calculate_score(world, solution):
    # Earns points: (distance) + (bonus)
    # Each ride completed before its latest finish earns the number of points equal
    # to the distance between the start intersection and the finish intersection.
    # Additionally, each ride which started exactly in its earliest allowed start step
    # gets an additional timeliness bonus of B.

    score = 0
    for car_id, rides in solution.items():
        for ride in rides:
            bonus_finish = ride['duration'] if ride['real_finish'] <= ride['latest_finish'] else 0
            bonus_start = world['bonus'] if ride['real_start'] == ride['earliest_start'] else 0

        score += bonus_finish + bonus_finish + bonus_start

    return score


def distance(start, finish):
    return abs(start.r - finish.r) + abs(start.c - finish.c)


def get_ride_by_start_bonus(t, vehicle, rides):

    result_rides = []
    ride = None

    for ride in rides:

        # calculo la duracion
        duration = distance(start=vehicle.pos, finish=ride['start'])

        # miro si con esa distancia llego al earlier_start
        is_bonus = t + duration <= ride['earliest_start']

        # si si, la meto en la lista de resultados
        if is_bonus:
            rides.append(ride)

    if result_rides:
        # ordeno por las que tienen más duración primero, puesto que si llego en el earliest_start,
        sorted_rides = sorted(result_rides.items, lambda ride: ride['duration'], reverse=True)
        ride = sorted_rides[0]

    return ride
