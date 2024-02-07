FROM python:3.9-slim

WORKDIR /app

COPY ../marathon_app /app

RUN pip install poetry
RUN poetry install
RUN pip install streamlit
RUN pip install garminconnect==0.1.55

# Make port 8501 available to the world outside this container
EXPOSE 8501

ENV STREAMLIT_SERVER_PORT 8501

CMD ["streamlit", "run", "main.py"]
