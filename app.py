import os
import logging
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)

@app.route("/")
def index():
    return "Welcome to my flight data microservice!"

@app.route('/flights', methods=['GET'])
def get_flights():
    api_key = os.getenv("API_KEY")
    flight_number = request.args.get('flight_number')
    url = f'https://app.goflightlabs.com/flights?access_key={api_key}&flightIata={flight_number}'
    response = requests.get(url)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)