'''
I am so lost, this has become spaghetti code. none of it makes any sense. I have been working on this for quite some time to get it
to work again, but to no avail.

I had it working at some point, but I tried to make it more efficient, but in the end I just killed it.

so sad. I was finished with it, but I ruined my creation.
'''

import os.path
from datetime import datetime
import json
import os

from dataclasses import dataclass
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

script_directory = os.path.dirname(os.path.abspath(__file__))
credentials_path = os.path.join(script_directory, ".gitignore", "credentials2.json")

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)

SPREADSHEET_ID = '1uUJN2HeYXJ1NdPFD4BGXK3XYwPjT2SWt--rgfUTJ_VU'

#import exercise dictionaries
with open('data.json', 'r') as file:
    data = json.load(file)


# @dataclass
# class Exercise():
#     weight: int = 0
#     sets: int = 0
#     reps: int = 0

# data = {'squats' : Exercise(),
#     'hack squats' : Exercise(),}

selected_dict = []

#letters, to increment in the track_fitness() function
let1 = 'B'
let3 = 'D'

#gets the next available row in sheets to update
def get_next_available_row(sheet_name, service):
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=f'{sheet_name}!A1:A').execute()
    values = result.get('values', [])
    return len(values) + 1

def update_sheet(service, sheets_name, next_row, exercise_data):
    global let1, let3
    range_name = f'{sheets_name}!{let1}{next_row}:{let3}{next_row}'
    values = [[exercise_data['weight'], exercise_data['sets'], exercise_data['reps']]]

    body = {'values': values}
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=range_name,
        valueInputOption='RAW', body=body).execute()
    print(f'{result.get('updatedCells')} cells updated.')

def update_date(service, sheets_name, next_row):
    range_name = f'{sheets_name}!A{next_row}:A{next_row}'
    date = [[datetime.now().strftime('%Y-%m-%d')]]

    body = {'values': date}
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID, range=range_name,
        valueInputOption='RAW', body=body).execute()
    print(f'Date updated. {result.get('date')}')

def track_fitness():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    while True:
        global let1, let3
        dumb = {'leg': 0, 'push': 1, 'pull': 2, 'cardio': 3}
        category = input('What kind of day was it? ').lower().strip()
        if any(category in day for day in dumb.keys()):
            selected_dict = next(day for day in data if category in day)
            print(f"Selected dictionary for {category}: {selected_dict}")
            service = build('sheets', 'v4', credentials=creds)
            next_row = get_next_available_row(category, service)
            update_date(service, category, next_row)
            for exercise, details in selected_dict.items():
                done = input(f'Did you do {exercise} today? (1 for yes, 0 for no): ')
                if done == '1':
                    details.weight = int(input(f'How much weight for {exercise}? '))
                    details.sets = int(input(f'How many sets for {exercise}? '))
                    details.reps = int(input(f'How many reps per set for {exercise}? '))
                    service = build('sheets', 'v4', credentials=creds)
                    update_sheet(service, category, next_row, details)
                    let1 = chr(ord(let1) + 3)
                    let3 = chr(ord(let3) + 3)
                else:
                    details.weight = 0
                    details.sets = 0
                    details.reps = 0
                    service = build('sheets', 'v4', credentials=creds)
                    next_row = get_next_available_row(category, service)
                    update_sheet(service, category, next_row, details)
                    let1 = chr(ord(let1) + 3)
                    let3 = chr(ord(let3) + 3)
            break
        else:
            print('not a valid input. please type either "leg", "push", "pull", or "cardio"')



def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_path, SCOPES
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

track_fitness()