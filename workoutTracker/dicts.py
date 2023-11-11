import json

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
    'Rows': {'weight': 0, 'sets': 0, 'reps': 0}},

    {'Elliptical': {'time': 0},
    'Arc-Trainer': {'time': 0}}
]




questions = {'weight': 'How much weight were the reps?',
    'sets': 'How many sets did you do?',
    'reps': 'How many reps did you do?'
}

# megadict = {}

data = []

with open('data.json', 'w') as file: 
    json.dump(data, file)
