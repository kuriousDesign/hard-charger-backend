from get_mongo_client import get_mongo_db

db = get_mongo_db('games_2025')


# create json race object with type, letter and event_id
a_main = {
    "type": "Main",
    "letter": "A",
    "event_id": 1,
    "num_cars": 24,
    "laps": 50,
    "num_transfers": 4,
    "first_transfer_position": 17,
    "intermission_lap": 25,
    "racers": [
        {"car_number": "2C", "driver_fullname": "Kyle Larson", "starting_position": 1, "current_position": 1},
        {"car_number": "2", "driver_fullname": "David Gravel", "starting_position": 2, "current_position": 2},
        {"car_number": "15", "driver_fullname": "Donny Schatz", "starting_position": 3, "current_position": 3},
        {"car_number": "1S", "driver_fullname": "Logan Schuchart", "starting_position": 4, "current_position": 4},
        {"car_number": "23", "driver_fullname": "Garet Williamson", "starting_position": 5, "current_position": 5},
        {"car_number": "17B", "driver_fullname": "Bill Balog", "starting_position": 6, "current_position": 6},
        {"car_number": "7S", "driver_fullname": "Chris Windom", "starting_position": 7, "current_position": 7},
        {"car_number": "17", "driver_fullname": "Sheldon Haudenschild", "starting_position": 8, "current_position": 8},
        {"car_number": "41", "driver_fullname": "Carson Macedo", "starting_position": 9, "current_position": 9},
        {"car_number": "18", "driver_fullname": "Gio Scelzi", "starting_position": 10, "current_position": 10},
        {"car_number": "83", "driver_fullname": "Buddy Kofoid", "starting_position": 11, "current_position": 11},
    ]
}

db.races.create_index([("type", 1), ("letter", 1), ("event_id", 1)], unique=True)
db.races.insert_one(a_main)

