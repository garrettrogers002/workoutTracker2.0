import os.path
from datetime import datetime
import json
from dataclasses import dataclass

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = '1uUJN2HeYXJ1NdPFD4BGXK3XYwPjT2SWt--rgfUTJ_VU'

let1 = 'B'
let2 = 'D'
'''
I have no idea what's happening, most of my attempts have been spent on attempt2.py
send help
'''
@dataclass
class Exercise():
    exerciseDay: str
    weight: int = 0
    sets: int = 0
    reps: int = 0

@dataclass
class Cardio():
    exerciseDay: str
    time: int = 0
    distance: int = 0

data = {'squats' : Exercise('leg'),
    'hack squats' : Exercise('leg'),
    'golin squats' : Exercise('leg'),
    'hamstring curls' : Exercise('leg'),
    'leg extensions' : Exercise('leg'),
    
    'bench press' : Exercise('push'),
    'decline bench press' : Exercise('push'),
    'chest flies' : Exercise('push'),
    
    'pull ups' : Exercise('pull'),
    'bent over rows' : Exercise('pull'),

    'elliptical' : Cardio('cardio'),
    'arc trainer' : Cardio('cardio') 
}




def get_next_available_row(sheet_name, service):
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=f'{sheet_name}!A1:A').execute()
    values = result.get('values', [])
    return len(values) + 1

def update_sheet(service, day, next_row, exercise_data):
    global let1, let2
    range_name = f'{day}!{let1}{next_row}:{let2}{next_row}'
    values = [[exercise_data['weight'], exercise_data['sets'], exercise_data['reps']]]

    body = {'values': values}
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=range_name,
        valueInputOption='RAW', body=body).execute()
    print(f'{result.get('updatedCells')} cells updated.')

def track_fitness(service, day, next_row):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials2.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    while True:
        day = input('What day was it? ').lower()
        if day == 'exit':
            break

        for exercise_name, exercise_data in data.items():
            print(f"Exercise: {exercise_name}")
            weight = int(input("Enter weight: "))
            sets = int(input("Enter sets: "))
            reps = int(input("Enter reps: "))

            exercise_data.weight = weight
            exercise_data.sets = sets
            exercise_data.reps = reps

            next_row = get_next_available_row(day, service)
            update_sheet(service, day, next_row, exercise_data)
            print(f"{exercise_name} data tracked for {day} at row {next_row}")


def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials2.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        print()

    except HttpError as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()