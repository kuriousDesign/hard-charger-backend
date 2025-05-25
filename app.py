from flask import Flask, jsonify
from flask_cors import CORS
from get_mongo_client import get_mongo_db

import pandas as pd
import time
import logging
logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
db = get_mongo_db('games_2025')

entry_results = []  # Global variable to store entry results
race_results = []

@app.route('/')
def index():
    # insert clickable linke to the Google Form and link to entries
    return f"""
    <h1>Welcome to the Entry Results Page</h1>
    <p>Click <a href="/races">here</a> to view all races.</p>
    <p>Click <a href="/drivers">here</a> to view all drivers.</p>
    """

@app.route('/api/drivers')
def serve_drivers():
    # get list of drivers from drivers collection
    # get all documents in drivers collection
    drivers = db.drivers.find({}, {'_id': 0})
    # Convert cursor to list of driver names
    driver_names = [driver['first_name'] + ' ' + driver['last_name'] + ' ' + driver['suffix'] + ' - ' + driver["car_number"] for driver in drivers]
    
    return jsonify({'drivers': driver_names})

@app.route('/races')
def serve_races():
    # get list of races from races collection
    
    # i want list of all names of races by concatenating type, letter and event_id
    # get all documents in races collection
    races = db.races.find({}, {'_id': 0})
    events = db.events.find({}, {'_id': 0, 'name': 1, 'date': 1})
    # Convert cursor to list of races with concatenated names

    races_display = []
    for race in races:
        event = db.events.find_one(race["event_id"])
        races_display.append( race["letter"] + ' ' + race["type"] + " - " + event["name"] + " - " + event["date"])

    return jsonify(races_display)

if __name__ == '__main__':
    logging.info("Starting entry result scheduler...")
    #update_entry_results()  # Optional: preload on startup

    logging.info("Starting Flask app...")
    app.run(debug=True,port=8080)# The above code initializes a Flask web application and defines a single route that returns a simple greeting message.
    print("Starting Flask app...")