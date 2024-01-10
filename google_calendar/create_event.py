from datetime import datetime, timedelta

from googleapiclient.discovery import build
from google_calendar.logging_gc import get_credentials


def check_calendars(service):
    # Get a list of calendars (return the last one, my Google calendar)
    calendar_list = service.calendarList().list().execute()

    # Print information about each calendar
    for calendar in calendar_list.get('items', []):
        calendar_id = calendar['id']
        summary = calendar['summary']
        primary_indicator = '(Primary)' if 'primary' in calendar and calendar['primary'] else ''
        print(f"Calendar ID: {calendar_id} {primary_indicator} - Summary: {summary}")

        if 'primary' in calendar and calendar['primary']:
            return calendar_id

    # Return the last calendar's ID if no primary calendar is found
    return calendar_id


def create_event(activity_type: str, activity_description: str, activity_date: datetime):
    # Google API credentials
    credentials = get_credentials()

    # Create a Calendar API service
    service = build('calendar', 'v3', credentials=credentials)

    # Create event
    event = {
        'summary': activity_type,
        'description': activity_description,
        'start': {
            'dateTime': activity_date.isoformat(),
            'timeZone': 'Europe/Madrid',
        },
        'end': {
            'dateTime': (activity_date + timedelta(days=1)).isoformat(),
            'timeZone': 'Europe/Madrid',
        },
    }

    # Check calendars and retrieve the primary one
    calendar_id = check_calendars(service)

    # Add event to the user's calendar
    service.events().insert(calendarId=calendar_id, body=event).execute()


if __name__ == '__main__':
    create_event(activity_type='running', activity_description='this is a test', activity_date=datetime(2023, 12, 1))
