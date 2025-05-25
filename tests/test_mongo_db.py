from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://gardner761:YrC9Xu8H1HEds8kf@cluster0.l3sqckj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def create_collections_and_indexes():
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client['games_2025']

    # Create collections explicitly (optional, since MongoDB creates on insert)
    collections = ['games', 'races', 'entries', 'drivers']
    for coll_name in collections:
        if coll_name not in db.list_collection_names():
            db.create_collection(coll_name)
            print(f"Created collection: {coll_name}")
        else:
            print(f"Collection {coll_name} already exists")

    # Indexes for drivers
    db.drivers.create_index("car_number", unique=True)
    db.drivers.create_index([("last_name", 1), ("first_name", 1)])

    # Indexes for games
    db.games.create_index("name", unique=True)

    # Indexes for races
    db.races.create_index("game_id")
    db.races.create_index("race_name")

    # Indexes for entries
    db.entries.create_index("game_id")
    db.entries.create_index("player_id")  # Assuming you track player_id in entries

    print("Indexes created.")


try:
    create_collections_and_indexes()
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command('ping')
    print("✅ Connected to MongoDB Atlas!")
    db = client['test_db']  # Replace with your database name
    collection = db['test_collection']  # Replace with your collection name
    print("Database and collection are ready for use.")
    # Example operation: Insert a document
    collection.insert_one({"test_key": "test_value"})
    print("✅ Document inserted successfully.")     

    # Example operation: Find a document
    result = collection.find_one({"test_key": "test_value"})
    if result:
        print("✅ Document found:", result)
    else:
        print("❌ Document not found.")


    
except Exception as e:
    print("❌ Connection failed:", e)
