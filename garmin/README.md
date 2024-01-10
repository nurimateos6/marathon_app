# Garmin Connect API


## Prerequisites

- A Garmin device. 
- Install garminconnect library.
- Obtain Garmin Connect credentials and save them in credentials.json. You can clone the `credentials_template.json`, rename the file and add your personal secrets.

## Getting Started

1. Clone the repository.
2. Install the required dependencies.
3. Run the `app.py` file to run the entire application, or directly run the python files under this module to use the Garmin functionalities.

## Functions
- get_credentials(): Get user credentials.
- login(): Authenticate the user and return a session.
- init_api(): Initialize Garmin API with credentials.
- display_json(api_call, output): Format API output for better readability.
- query_activities(activity_type: str, start_date, end_date): Query activities using the Garmin API.
- insights_activities(): Retrieve detailed activity insights.

