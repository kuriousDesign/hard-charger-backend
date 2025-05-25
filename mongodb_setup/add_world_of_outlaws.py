from get_mongo_client import get_mongo_db

db = get_mongo_db('games_2025')

if 'drivers' not in db.list_collection_names():
    db.create_collection('drivers')
    db.drivers.create_index([("last_name", 1), ("first_name", 1),("suffix", 1)], unique=True)

drivers = [
    {"first_name": "Cole", "last_name": "Macedo", "car_number": "2C", "suffix": ""},
    {"first_name": "David", "last_name": "Gravel", "car_number": "2", "suffix": ""},
    {"first_name": "Donny", "last_name": "Schatz", "car_number": "15", "suffix": ""},
    {"first_name": "Logan", "last_name": "Schuchart", "car_number": "1S", "suffix": ""},
    {"first_name": "Garet", "last_name": "Williamson", "car_number": "23", "suffix": ""},
    {"first_name": "Bill", "last_name": "Balog", "car_number": "17B", "suffix": ""},
    {"first_name": "Chris", "last_name": "Windom", "car_number": "7S", "suffix": ""},
    {"first_name": "Sheldon", "last_name": "Haudenschild", "car_number": "17", "suffix": ""},
    {"first_name": "Carson", "last_name": "Macedo", "car_number": "41", "suffix": ""},
    {"first_name": "Gio", "last_name": "Scelzi", "car_number": "18", "suffix": ""},
    {"first_name": "Buddy", "last_name": "Kofoid", "car_number": "83", "suffix": ""},
    {"first_name": "Skylar", "last_name": "Gee", "car_number": "99", "suffix": ""},
    {"first_name": "Zack", "last_name": "Hampton", "car_number": "6R", "suffix": ""},
    {"first_name": "Hunter", "last_name": "Shruenberg", "car_number": "55", "suffix": ""},
    {"first_name": "Daison", "last_name": "Pursley", "car_number": "13", "suffix": ""},
    {"first_name": "Spencer", "last_name": "Bayston", "car_number": "14", "suffix": ""},
    {"first_name": "Brad", "last_name": "Sweet", "car_number": "49", "suffix": ""},
    {"first_name": "Justin", "last_name": "Peck", "car_number": "26", "suffix": ""},
    {"first_name": "Aaron", "last_name": "Reutzel", "car_number": "87", "suffix": ""},
    {"first_name": "Rico", "last_name": "Abreu", "car_number": "24", "suffix": ""},
    {"first_name": "Tyler", "last_name": "Courtney", "car_number": "7BC", "suffix": ""},
    {"first_name": "Tanner", "last_name": "Thorson", "car_number": "88", "suffix": ""},
    {"first_name": "Brent", "last_name": "Marks", "car_number": "19M", "suffix": ""},
    {"first_name": "Kasey", "last_name": "Kahne", "car_number": "9", "suffix": ""},
    {"first_name": "Brenham", "last_name": "Crouch", "car_number": "5", "suffix": ""},
    {"first_name": "Sye", "last_name": "Lynch", "car_number": "42", "suffix": ""},
    {"first_name": "Danny", "last_name": "Sams", "car_number": "24D", "suffix": ""},
    {"first_name": "Chase", "last_name": "Randall", "car_number": "9", "suffix": ""}
]

# Insert drivers into the 'drivers' collection
for driver in drivers:
    db.drivers.insert_one(driver)


print("World of Outlaws drivers added to the database.")