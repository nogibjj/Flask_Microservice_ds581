from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to my deck of cards microservice!"

@app.route("/deck", methods=["GET"])
def get_deck():
    print("1")
    deck_api_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
    print("2")
    response = requests.get(deck_api_url)
    print("3")
    deck = response.json()
    print("4")
    print(deck)
    return jsonify(deck)

@app.route("/deck/<deck_id>/draw", methods=["GET"])
def draw_card(deck_id):
    count = request.args.get("count", default=1, type=int)
    draw_api_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={count}"
    response = requests.get(draw_api_url)
    cards = response.json()
    return jsonify(cards)

@app.route("/deck/<deck_id>/shuffle", methods=["GET"])
def shuffle_deck(deck_id):
    shuffle_api_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/shuffle/"
    response = requests.get(shuffle_api_url)
    deck = response.json()
    return jsonify(deck)

if __name__ == "__main__":
    app.run(debug=True)