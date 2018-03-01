# utils.py
import os
from _ast import keyword


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
            bonus_finish = ride['duration'] if ride['real_finish'] < ride['latest_finish'] else 0
            bonus_start = world['bonus'] if ride['real_start'] == ride['earliest_start'] else 0
            score += (bonus_finish + bonus_start)

    return score


def distance(start, finish):
    return abs(start.r - finish.r) + abs(start.c - finish.c)


def get_ride_by_start_bonus(world, t, vehicle, rides):

    if not rides:
        return None

    result_rides = []

    for ride in rides:

        # calculo la duracion
        duration = distance(start=vehicle.pos, finish=ride['start'])

        # miro si con esa distancia llego al earlier_start
        is_bonus_start = t + duration <= ride['earliest_start']
        bonus_start = world['bonus'] if is_bonus_start else 0

        # miro si con esa distancia llego antes de latest_start
        is_bonus_end = t + duration < ride['latest_start']
        bonus_end = ride['duration'] if is_bonus_end else 0

        ride['score'] = bonus_start + bonus_end

        result_rides.append(ride)

    # ordeno por las que tienen más duración primero, puesto que si llego en el earliest_start,
    sorted_rides = sorted(result_rides, key=lambda ride: ride['score'], reverse=True)
    ride = sorted_rides[0]

    return ride


def get_ride_by_start_bonus_apj(world, t, car, rides):

    if not rides:
        return None

    result_rides = []

    for ride in rides:

        # calculo la duracion
        ride['to_start_duration'] = distance(start=car['pos'], finish=ride['start'])

        # miro si con esa distancia llego al earlier_start
        is_bonus_start = t + ride['to_start_duration'] <= ride['earliest_start']
        bonus_start = world['bonus'] if is_bonus_start else 0

        # miro si con esa distancia llego antes de latest_start
        is_bonus_end = t + ride['to_start_duration'] < ride['latest_start']
        bonus_end = ride['duration'] if is_bonus_end else 0

        ride['score'] = bonus_start + bonus_end


        result_rides.append(ride)

    # ordeno por las que tienen más duración primero, puesto que si llego en el earliest_start,
    sorted_score_rides = sorted(result_rides, key=lambda ride: ride['score'], reverse=True)
    best_score_ride = sorted_score_rides[0]
    best_scores = [ride for ride in sorted_score_rides if ride['score'] == best_score_ride['score']]
    sorted_to_start_rides = sorted(best_scores, key=lambda ride: ride['to_start_duration'])
    ride = sorted_to_start_rides[0]

    return ride
