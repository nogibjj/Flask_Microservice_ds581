import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my flight data microservice!"

@app.route("/api/v1/flight_data", methods=["GET"])
def flight_data():
    flight_number = request.args.get("flight_number")
    app_id = "YOUR_API_ID"
    api_key = "YOUR_API_KEY"
    url = f"https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/{flight_number}?appId={app_id}&appKey={api_key}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    app.run(debug=True)