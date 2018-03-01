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
    for ride in solution['rides']:

        bonus_finish = ride['duration'] if ride['real_finish'] < ride['finish'] else 0
        bonus_start = solution['bonus'] if ride['real_start'] == ride['start'] else 0

        score += bonus_finish + bonus_finish + bonus_start

    return score


def distance(start, finish):
    return abs(start.r - finish.r) + abs(start.c - finish.c)


def get_ride_by_start_bonus(t, vehicle_position, rides):

    rides = []

    for ride in rides:

        # calculo la duracion
        duration = distance(start=vehicle_position, finish=ride['start'])

        # miro si con esa distancia llego al earlier_start
        is_bonus = t + duration <= ride['earliest_start']

        # si si, la meto en la lista de resultados
        if is_bonus:
            rides.append(ride)

    ride = rides[0] if rides else None

    return ride
