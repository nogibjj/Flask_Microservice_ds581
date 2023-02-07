# Use an official Python runtime as the base image
FROM python:3.7-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the API key as an environment variable
ARG API_KEY
ENV API_KEY=$API_KEY
ENV FLASK_APP=app.py

# Expose the application's port
EXPOSE 5000

# Set the entry point to run the flask application
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]

# docker build --build-arg API_KEY=YOUR_API_KEY .
