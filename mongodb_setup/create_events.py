from get_mongo_client import get_mongo_db

db = get_mongo_db('games_2025')


# create json race object with type, letter and event_id
knoxville_nationals_saturday_night_2024 = {
    "name": "Knoxville Nationals",
    "date": "2024-08-10",
    "location": "Knoxville, Iowa",
}

# create events collection if it doesn't exist
if 'events' not in db.list_collection_names():
    db.create_collection('events')
    db.events.create_index([("name",1),( "date",1)], unique=True)

db.events.insert_one(knoxville_nationals_saturday_night_2024)
print("Knoxville Nationals event added to the database.")