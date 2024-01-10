# My Marathon App

My Marathon App is a web application that allows users to quickly create activities in their Google Calendar and sync their fitness data from Garmin Connect. The application utilizes the Google Calendar API and Garmin Connect API to interact with the user's calendar and fitness activities.

## Prerequisites

### Google Calendar API

Before using the application, you need to set up a project in the Google Cloud Console and obtain the necessary credentials to access the Google Calendar API. Follow these steps:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project.
3. Enable the Google Calendar API for your project.
4. Create API credentials (OAuth 2.0 client IDs) and download the credentials file as `credentials.json`.
5. Ensure that the API key associated with the credentials has the necessary permissions (read and write) to access the user's calendar.
6. In the Google Cloud Console, configure the redirect URL for OAuth consent screen to `http://localhost:5000/`.

### Garmin Connect API

To sync fitness data from Garmin Connect, you'll need Garmin credentials. Follow these steps:

1. Create a Garmin Connect account.
2. Save your Garmin Connect email and password in a file named `credentials.json` in the project root directory:

   ```json
   {
     "email": "your_garmin_email@example.com",
     "password": "your_garmin_password"
   }
## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/nurimateos6/my-marathon-app.git

2. Install the required dependencies:
 ```bash
   poetry install
   ```

3. Place both credentials.json files (Google Calendar and Garmin Connect) in the project root directory.
4. Run the application:
 ```bash
   python app.py
   ```
5. Open your web browser and go to http://localhost:5000 to access the application.


## Usage
### Creating Activities
Navigate to the "Task Planning" section of the app.
Fill in the details for the new activity.
Click the "Create Activity" button. This is going to create a new task or event in your Google Calendar.


### Viewing Next Events
Navigate to the "View Calendar" section. Specify the number of events and the start date to retrieve upcoming events.
 Then, select the list view or the calendar view.
Click the "Fetch Events" button. This is going to show your upcoming events that you have in your Google Calendar

### My Activity
Navigate to the "My activity" section. Select a start and end ddate, and click on the "Fetch Activities" button to recover the activities realized in this slot.
This is going to query your activity using Garmin Connect.

### My day
Navigate to  "My day" section. Then you are going to discover some insights about your runs. For that, is also using the Garmin Connect data.

## Running the project with Docker
1. Build the Docker image:
Open a terminal, navigate to the directory containing your Dockerfile, and run the following command to build a Docker image from the Dockerfile:
docker build -t marathon-app .

2. Run the Docker container
docker run -p 8501:8501 marathon-app
This command maps port 8501 from the container to the same port on your host system. You can access your Streamlit app in a web browser by navigating to http://localhost:8501.

