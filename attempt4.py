'''
workout tracker, stored locally in a csv file

Garrett Rogers
'''

import csv
from datetime import datetime

def log_workout(workout_data):
    file_name = f'{day}_workout_data.csv'
    with open(file_name, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(workout_data)

categories = ['leg', 'push', 'pull', 'cardio']

data = [
    {'squats': {'weight': 0, 'sets': 0, 'reps': 0},
    'Hack Squats': {'weight': 0, 'sets': 0, 'reps': 0},
    'Goblin Squats': {'weight': 0, 'sets': 0, 'reps': 0},
    'Hip Abductor (out)': {'weight': 0, 'sets': 0, 'reps': 0},
    'Hip Abductor (in)': {'weight': 0, 'sets': 0, 'reps': 0},
    'Hamstring Curls': {'weight': 0, 'sets': 0, 'reps': 0},
    'Leg Extensions': {'weight': 0, 'sets': 0, 'reps': 0}},
    
    {'Decline Bench': {'weight': 0, 'sets': 0, 'reps': 0},
    'Bench press': {'weight': 0, 'sets': 0, 'reps': 0},
    'Shoulder press': {'weight': 0, 'sets': 0, 'reps': 0},
    'Tricep dips': {'weight': 0, 'sets': 0, 'reps': 0}},
    
    {'Pull-ups': {'weight': 0, 'sets': 0, 'reps': 0},
    'Bent-over rows': {'weight': 0, 'sets': 0, 'reps': 0},
    'Bicep curls': {'weight': 0, 'sets': 0, 'reps': 0},
    'Rows': {'weight': 0, 'sets': 0, 'reps': 0},
    'Lat Pulldowns': {'weight': 0, 'sets': 0, 'reps': 0}},

    {'Elliptical': {'time': 0},
    'Arc-Trainer': {'time': 0}}
]


day = input('What kind of day was it? (push, pull, leg, or cardio) ').lower().strip()

if day in categories:
    for exercise, exercise_data in data[categories.index(day)].items():
        workout_data = []
        done = input(f'Did you do {exercise} today?(1 for yes, 0 for no) ')
        if done == '1':
            date = datetime.now().strftime('%Y-%m-%d')
            weight = int(input(f'How much weight for {exercise}? '))
            sets = int(input(f'How many sets for {exercise}? '))
            reps = int(input('How many reps for each set? '))
            workout_data = [date, exercise, weight, sets, reps]
            log_workout(workout_data)
        elif done == '0':
            workout_data[datetime.now().strftime('%Y-%m-%d'), exercise, 0, 0, 0]
            log_workout(workout_data)
        else:
            input('not a valid input. type "1" for yes, or "0" for no: ')

else:
    print('That wasn\'t a valid input')