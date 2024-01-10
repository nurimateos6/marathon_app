import streamlit as st
from google.oauth2 import service_account
import googleapiclient.discovery
from datetime import datetime

# Define the Google Calendar API scope and credentials
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'credentials.json'


# Function to create an event in Google Calendar
def create_event(summary: str, location: str, description: str, start_time: datetime, end_time: datetime):
    try:
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES
        )
    except Exception as e:
        print(f"Authentication error: {e}")

    service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    event = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Your-Timezone',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Your-Timezone',
        },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    return event


# Streamlit UI
st.title('Marathon Training App')

# Create a reminder for a run
st.subheader('Create a Run Reminder')

run_summary = st.text_input('Run Summary')
run_location = st.text_input('Run Location')
run_description = st.text_input('Run Description')
run_start_time = st.text_input('Run Start Time (YYYY-MM-DD HH:MM)')
run_end_time = st.text_input('Run End Time (YYYY-MM-DD HH:MM)')

if st.button('Create Reminder'):
    try:
        start_time = datetime.strptime(run_start_time, '%Y-%m-%d %H:%M').isoformat()
        end_time = datetime.strptime(run_end_time, '%Y-%m-%d %H:%M').isoformat()
        create_event(run_summary, run_location, run_description, start_time, end_time)
        st.success('Reminder created successfully!')
    except Exception as e:
        st.error(f'Error creating reminder: {e}')

# View google_calendar events
st.subheader('View Calendar Events')

# Authenticate and retrieve google_calendar events here using Google Calendar API
# Display the events in the Streamlit app


if __name__ == '__main__':
    summary = 'test'
    location = 'Barcelona'
    description = 'test from my new app'
    now = datetime.utcnow().isoformat() + 'Z'
    start_time = now
    end_time = now
    create_event(summary, location, description, start_time, end_time)

