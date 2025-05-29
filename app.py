from flask import Flask, jsonify, request
from flask_cors import CORS
from get_mongo_client import get_mongo_db

import pandas as pd
import time
import logging
logging.basicConfig(level=logging.INFO)

from bson import ObjectId

def serialize_doc(doc):
    if isinstance(doc, list):
        return [serialize_doc(item) for item in doc]
    elif isinstance(doc, dict):
        return {
            key: serialize_doc(value)
            for key, value in doc.items()
        }
    elif isinstance(doc, ObjectId):
        return str(doc)
    else:
        return doc


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


@app.route('/api/events/<string:event_id>')
def serve_event(event_id: str):
    doc = db.events.find_one({'_id': ObjectId(event_id)})
    if doc is None:
        return jsonify({'error': 'Event not found'}), 404
    return jsonify({'data': serialize_doc(doc)})

@app.route('/api/events')
def serve_events():
    raw_data = db.events.find()
    data = [serialize_doc(data) for data in raw_data]
    return jsonify({'data': data})

@app.route('/api/create_event', methods=['POST'])
def create_or_update_event():
    event_data = request.get_json()
    
    if event_data['_id'] != '':
        # Update existing event
        event_id = ObjectId(event_data['_id'])
        del event_data['_id']  # Remove _id from update data
        result = db.events.update_one(
            {'_id': event_id},
            {'$set': event_data}
        )
        if result.matched_count == 0:
            return jsonify({'error': 'Event not found'}), 404
        return jsonify({'message': 'Event updated successfully'})
    else:
        # Create new event
        if '_id' in event_data:
            del event_data['_id']
        result = db.events.insert_one(event_data)
        return jsonify({'message': 'Event created successfully', 'id': str(result.inserted_id)})


@app.route('/api/games/<string:game_id>')
def serve_game(game_id: str):
    doc = db.games.find_one({'_id': ObjectId(game_id)})
    if doc is None:
        return jsonify({'error': 'Game not found'}), 404
    return jsonify({'data': serialize_doc(doc)})

@app.route('/api/games')
def serve_games():
    raw_games = db.games.find()
    games = [serialize_doc(game) for game in raw_games]
    return jsonify({'data': games})

@app.route('/api/games/event/<string:event_id>')
def serve_games_by_event(event_id: str):
    doc = db.games.find({'event_id': ObjectId(event_id)})
    if doc is None or doc.retrieved == 0:
        #return jsonify({'error': 'Game not found'}), 404
        return jsonify({'data': []})
    return jsonify({'data': serialize_doc(doc)})


@app.route('/api/create_game', methods=['POST'])
def create_or_update_game():
    game_data = request.get_json()
    
    if game_data['_id'] != '':
        # Update existing game
        game_id = ObjectId(game_data['_id'])
        del game_data['_id']  # Remove _id from update data
        result = db.games.update_one(
            {'_id': game_id},
            {'$set': game_data}
        )
        if result.matched_count == 0:
            return jsonify({'error': 'Game not found'}), 404
        return jsonify({'message': 'Game updated successfully'})
    else:
        # Create new game
        if '_id' in game_data:
            del game_data['_id']
        result = db.games.insert_one(game_data)
        return jsonify({'message': 'Game created successfully', 'id': str(result.inserted_id)})


@app.route('/api/races/<string:race_id>')
def serve_race(race_id: str):
    doc = db.races.find_one({'_id': ObjectId(race_id)})
    if doc is None:
        return jsonify({'error': 'Race not found'}), 404
    return jsonify({'data': serialize_doc(doc)})

@app.route('/api/racers/<string:race_id>')
def serve_racers_of_race(race_id: str):
    doc = db.racers.find({'race_id': ObjectId(race_id)})
    prepped_racers = []
    for racer in doc:
        prepped_racers.append(serialize_doc(racer))

    return jsonify({'data': prepped_racers})
    

@app.route('/api/racers-with-drivers/<string:race_id>')
def serve_racers_with_drivers_of_race(race_id: str):
    if 'racers' not in db.list_collection_names():
        return jsonify({'error': 'Racers collection not found'}), 404
    doc_racers = db.racers.find()#({'race_id': ObjectId(race_id)})
    if doc_racers.retrieved > 0 or True:
        doc_drivers = []
        prepped_racers = []
        for racer in doc_racers:
            driver = None
            driver = db.drivers.find_one({'_id': racer['driver_id']})
            if driver is None:
                logging.warning(f"Driver with ID {racer['driver_id']} not found for racer {racer['_id']}")
                return jsonify({'error': f'Driver with ID {racer["driver_id"]} not found'}), 404
            
            prepped_racers.append(serialize_doc(racer))
            doc_drivers.append(serialize_doc(driver))
    else:
        return jsonify({'racers':[],'drivers': []})
    prepped_drivers = doc_drivers
    return jsonify({'racers':prepped_racers,'drivers': prepped_drivers})



@app.route('/api/races')
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



@app.route('/api/races/event/<string:event_id>')
def serve_races_by_event(event_id):
    raw_races = db.races.find({"event_id": ObjectId(event_id)})
    races = [serialize_doc(race) for race in raw_races]
    return jsonify({'data': races})


@app.route('/api/create_race', methods=['POST'])
def create_or_update_race():
    race_data = request.get_json()
    
    if race_data.get('_id'):
        # Update existing race
        race_id = ObjectId(race_data['_id'])
        del race_data['_id']
        result = db.races.update_one(
            {'_id': race_id},
            {'$set': race_data}
        )
        if result.matched_count == 0:
            return jsonify({'error': 'Race not found'}), 404
        return jsonify({'message': 'Race updated successfully'})
    else:
        # Create new race
        if '_id' in race_data:
            del race_data['_id']
        if 'event_id' in race_data:
            if type(race_data['event_id']) is str:
                object_id = ObjectId(race_data['event_id'])
                race_data['event_id'] = object_id
                
        result = db.races.insert_one(race_data)
        return jsonify({'message': 'Race created successfully', 'id': str(result.inserted_id)})

@app.route('/api/create_racer', methods=['POST'])
def create_or_update_racer():
    racer_data = request.get_json()
    
    if racer_data.get('_id') and racer_data['_id'] != '':
        # Update existing racer
        racer_id = ObjectId(racer_data['_id'])
        del racer_data['_id']
        result = db.racers.update_one(
            {'_id': racer_id},
            {'$set': racer_data}
        )
        if result.matched_count == 0:
            return jsonify({'error': 'Racer not found'}), 404
        return jsonify({'message': 'Racer updated successfully'})
    else:
        # Create new racer
        if '_id' in racer_data:
            del racer_data['_id']
        if 'driver_id' in racer_data:
            racer_data['driver_id'] = ObjectId(racer_data['driver_id']) 
        if 'race_id' in racer_data:
            racer_data['race_id'] = ObjectId(racer_data['race_id']) 
        else: 
            return jsonify({'error': 'Driver not found'}), 404
        result = db.racers.insert_one(racer_data)
        return jsonify({'message': 'Racer created successfully', 'id': str(result.inserted_id)})

@app.route('/api/drivers')
def serve_drivers():
    raw_drivers = db.drivers.find()
    drivers = [serialize_doc(driver) for driver in raw_drivers]
    return jsonify({'data': drivers})

@app.route('/api/create_driver', methods=['POST'])
def create_or_update_driver():
    driver_data = request.get_json()
    
    if driver_data.get('_id'):
        # Update existing driver
        driver_id = ObjectId(driver_data['_id'])
        del driver_data['_id']
        result = db.drivers.update_one(
            {'_id': driver_id},
            {'$set': driver_data}
        )
        if result.matched_count == 0:
            return jsonify({'error': 'Driver not found'}), 404
        return jsonify({'message': 'Driver updated successfully'})
    else:
        # Create new driver
        if '_id' in driver_data:
            del driver_data['_id']
        result = db.drivers.insert_one(driver_data)
        return jsonify({'message': 'Driver created successfully', 'id': str(result.inserted_id)})

if __name__ == '__main__':
    logging.info("Starting entry result scheduler...")
    #update_entry_results()  # Optional: preload on startup

    logging.info("Starting Flask app...")
    app.run(debug=True,port=8080)# The above code initializes a Flask web application and defines a single route that returns a simple greeting message.
    print("Starting Flask app...")