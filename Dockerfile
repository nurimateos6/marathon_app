FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ../marathon_app%20copy /app

# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install poetry
RUN poetry install
RUN pip install streamlit
RUN pip install garminconnect==0.1.55

# Make port 8501 available to the world outside this container
EXPOSE 8501


# Define environment variable
ENV STREAMLIT_SERVER_PORT 8501

# Run app.py when the container launches
CMD ["streamlit", "run", "main.py"]
