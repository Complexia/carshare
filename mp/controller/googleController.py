import datetime
import pickle
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class GoogleController:
    def __init__(self):
        self.__creds = None
        self.__scope = ['https://www.googleapis.com/auth/calendar']
        self.__service = None

    def authenticateGoogleUser(self):
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                self.__creds = pickle.load(token)
        # if the user has not logged in on this device before, they will be asked to login through Google in their browser
        if not self.__creds or not self.__creds.valid:
            if self.__creds and self.__creds.expired and self.__creds.refresh_token:
                self.__creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.__scope)
                self.__creds = flow.run_local_server(port=0)
            # since the user has provided a valid login combination, their details will be saved for prior runs
            with open('token.pickle', 'wb') as token:
                pickle.dump(self.__creds, token)

    def fetchCalendar(self):
        self.__service = build('calendar', 'v3', credentials=self.__creds)

    def addBookingToCalendar(self, title, location, description, startTime, endTime):
        event = {
            'summary': title,
            'location': location,
            'description': description,
            'start': {
                'dateTime': startTime,
                'timeZone': 'Australia/Melbourne'
            },
            'end': {
                'dateTime': endTime,
                'timeZone': 'Australia/Melbourne'
            },
            'reminders': {
                'useDefault': True
            }
        }
        event = self.__service.events().insert(calendarId='primary', body=event).execute()
        
    def isUserAuthenticated(self):
        return self.__creds != None

googleController = GoogleController()