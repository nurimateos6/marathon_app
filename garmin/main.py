import logging
import json
import requests
import datetime
import os

from garminconnect import (
    Garmin,
    GarminConnectAuthenticationError,
    GarminConnectConnectionError,
    GarminConnectTooManyRequestsError,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_credentials():
    """Get user credentials."""
    credentials_file_path = os.path.join(os.path.dirname(__file__), 'credentials.json')

    if os.path.exists(credentials_file_path):
        try:
            with open(credentials_file_path, 'r') as file:
                credentials = json.load(file)

            email = credentials.get('email')
            password = credentials.get('password')

            if email and password:
                return email, password
            else:
                print("Invalid credentials format in the JSON file.")
                return None

        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
    return None


def login():
    """Authenticate the user and return a session."""
    email, password = get_credentials()
    session = requests.Session()

    # login_url = session.get('https://sso.garmin.com/sso/signin')

    login_url = 'https://sso.garmin.com/sso/signin'
    payload = {
        'username': email,
        'password': password,
    }

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        response = session.post(login_url, data=payload, headers=headers)
        response.raise_for_status()

        print("Final URL:", response.url)
        print("Login successful!")
        return session

    except requests.exceptions.RequestException as e:
        print(f"Error during login: {e}")
        print("Response content:", response.text)
        return None


def init_api():
    """Initialize Garmin API with your credentials."""
    try:
        email, password = get_credentials()
        api = Garmin(email, password)
        api.login()
    except (
            GarminConnectConnectionError,
            GarminConnectAuthenticationError,
            GarminConnectTooManyRequestsError,
            requests.exceptions.HTTPError,
    ) as err:
        logger.error("Error occurred logging Garmin Connect: %s", err)
        return None
    return api


def display_json(api_call, output):
    """Format API output for better readability."""
    dashed = "-" * 20
    header = f"{dashed} {api_call} {dashed}"
    footer = "-" * len(header)
    print(header)
    print(json.dumps(output, indent=4))
    print(footer)


def query_activities(activity_type: str, start_date, end_date):
    api = init_api()
    # api = login()
    # Query activities using the Garmin API
    activities = api.get_activities_by_date(start_date, end_date, activity_type)

    activities_data = []

    for activity in activities:
        duration_seconds = activity.get('duration')
        if duration_seconds is not None:
            # Convert duration from seconds to minutes
            duration_minutes = duration_seconds / 60

        activity_data = {
            'date': activity.get('startTimeLocal'),
            'type': activity.get('activityType')['typeKey'],
            'distance': activity.get('activitySummary.sumDistance.value'),
            'duration': duration_minutes,
            'average_speed': activity.get('averageSpeed')
        }
        activities_data.append(activity_data)
    logging.info(activities_data)

    return activities_data


def insights_activities():
    details_to_retrieve = [
        'activityName',
        'distance',
        'duration',
        'movingDuration',
        'elapsedDuration',
        'elevationGain',
        'elevationLoss',
        'averageSpeed',
        'maxSpeed',
        'calories',
        'averageHR',
        'maxHR',
        'aerobicTrainingEffect',
        'anaerobicTrainingEffect',
        'splitSummaries'
    ]
    api = init_api()
    today = datetime.date.today()
    end_date = today
    activity_type = 'running'
    # display_json(f"api.get_stats('{today.isoformat()}')", api.get_stats(today.isoformat()))
    activities = api.get_activities_by_date(
        today.isoformat(),
        end_date.isoformat(),
        activity_type)

    activities_data = []
    for activity in activities:
        activity_data = {detail: activity.get(detail, None) for detail in details_to_retrieve}
        activities_data.append(activity_data)

    return activities_data


if __name__ == '__main__':
    init_api()
