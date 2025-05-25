from pymongo import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os



# this will run inside render, so i need to get an environment variable from that
load_dotenv()  # Load environment variables from .env file if it exists
mongo_db_pw = os.getenv('MONGO_DB_PW', '')  # Default password if not set


# This is a MongoDB connection setup script.
# It connects to a MongoDB Atlas cluster and returns a database object.

uri = f"mongodb+srv://gardner761:{mongo_db_pw}@cluster0.l3sqckj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

def get_mongo_db(db_name='games_2025'):
    """
    Connects to the MongoDB database and returns the database object.
    :param db_name: Name of the database to connect to.
    :return: Database object.
    """
    # Create a MongoDB client with the provided URI and server API version
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client[db_name]

# Example usage:
if __name__ == "__main__":
    try:
        db = get_mongo_db()
        print(f"Connected to database: {db.name}")
    except Exception as e:
        print(f"An error occurred while connecting to the database: {e}")
