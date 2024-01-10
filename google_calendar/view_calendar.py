from datetime import datetime
from googleapiclient.errors import HttpError

from googleapiclient.discovery import build
from google_calendar.logging_gc import get_credentials


def get_next_events(maxResults: int):
    try:
        # Google API credentials
        credentials = get_credentials()

        # Create a Calendar API service
        service = build('calendar', 'v3', credentials=credentials)

        # Call the Calendar API
        now = datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
        print("Getting the upcoming 10 events")
        events_result = (
            service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=maxResults,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
            return

        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            print(start, event["summary"])

    except HttpError as error:
        print(f"An error occurred: {error}")


def get_events_between_date(time_min: datetime, maxResults: int):
    # Google API credentials
    credentials = get_credentials()

    # Create a Calendar API service
    service = build('calendar', 'v3', credentials=credentials)

    # Fetch google_calendar events
    events_result = service.events().list(
        calendarId='primary', timeMin=time_min, maxResults=maxResults, singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    # Display google_calendar events
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(f'{start} - {event["summary"]}')
    return events


if __name__ == '__main__':
    get_next_events(10)
    get_events_between_date('2023-09-01T00:00:00Z', 10)
