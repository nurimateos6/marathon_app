from flask import Flask, render_template, request, redirect, url_for, jsonify
from google_calendar.view_calendar import get_next_events, get_events_between_date
from google_calendar.create_event import create_event
from garmin.main import query_activities, insights_activities
from chat_gpt.chat_interaction import chat_with_gpt

app = Flask(__name__)

events = []


@app.route('/')
def index():
    return render_template('index.html', events=events)


@app.route('/task_planning', methods=['GET', 'POST'])
def task_planning():
    message = request.args.get('message', '')  # Get the message from the URL parameter

    if request.method == 'POST':
        event_date = request.form['event_date']
        event_description = request.form['event_description']

        # Add new event to the events list
        events.append({'date': event_date, 'description': event_description})

        message = "Event created successfully!"

        return redirect(url_for('index'), message=message)

    return render_template('task_planning.html', message=message)


@app.route('/submit_activity', methods=['POST'])
def submit_activity():
    from datetime import datetime
    try:
        if request.method == 'POST':
            # Get form data
            activity_type = request.form['activity_type']
            activity_date_str = request.form['activity_date']
            activity_description = request.form['activity_description']

            # Convert the activity_date string to a datetime object
            activity_date = datetime.strptime(activity_date_str, '%Y-%m-%d')

            # Call the create_event function
            create_event(activity_type=activity_type, activity_description=activity_description,
                         activity_date=activity_date)

            # Set a success message
            message = "Event created successfully!"

            # Redirect to the index route with the success message
            return redirect(url_for('task_planning', message=message))
    except Exception as e:
        # Set an error message
        message = f"Error creating event: {str(e)}"

        # Redirect to the index route with the error message
        return redirect(url_for('task_planning', message=message))


@app.route('/training_tracking', methods=['GET'])
def training_tracking():
    results_activities = insights_activities()
    return render_template('insights_activities.html', activities=results_activities)


@app.route('/api/get_activities', methods=['GET'])
def get_activities():
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')
    activity_type = 'running'  # TODO request.args.get('activity_type')

    activities_data = query_activities(activity_type, start_date, end_date)

    return jsonify(activities_data)


@app.route('/my_garmin_area')
def my_garmin_area():
    return render_template('garmin.html', activities_data=None)


@app.route('/view_calendar', methods=['GET', 'POST'])
def calendar():
    events = []  # Define events with a default value

    if request.method == 'POST':
        # Get the user input for timeMin and maxResults
        time_min = request.form.get('timeMin')
        max_results = int(request.form.get('maxResults', 10))

        # Fetch google_calendar events based on user input
        events = get_next_events(time_min, max_results)

        # Return events as JSON
        return jsonify(events)

    # Default rendering for the initial page load
    return render_template('calendar.html', events=events)


# Route for handling GET requests to fetch events
@app.route('/get_events', methods=['GET'])
def get_events():
    # Retrieve query parameters from the request
    time_min = request.args.get('timeMin')
    max_results = int(request.args.get('maxResults', 10))

    # Fetch google_calendar events based on the provided parameters
    events = get_events_between_date(time_min, max_results)
    # events = get_next_events(max_results)

    # Return events as JSON
    return jsonify(events)


@app.route('/call_chat', methods=['GET', 'POST'])
def call_chat():
    message = request.args.get('message', '')  # Get the message from the URL parameter

    if request.method == 'POST':
        user_input = request.form['user_input']

        chatbot_response = chat_with_gpt(user_input)
        events.append({'date': '', 'description': chatbot_response, 'is_chatbot': True})

        return render_template('chatbot.html', events=events)

    return render_template('chatbot.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
