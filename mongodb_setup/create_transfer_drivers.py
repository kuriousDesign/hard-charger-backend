from get_mongo_client import get_mongo_db

db = get_mongo_db('games_2025')


# create json race object with type, letter and event_id
transfer_driver = {
    "first_name": "B Main #1",
    "last_name": "Transfer Driver",
    "suffix": "",
    "car_number": "T1-B",
}

list_of_mains = [
    "A",
    "B",
    "C",
    "D",
    "E",
]

# create events collection if it doesn't exist
for main in list_of_mains:
    for index in range(1, 5):
        # create a transfer driver for each main

        driver = transfer_driver.copy()
        driver["car_number"] = f"T{index}-{main}"
        driver["first_name"] = f"{main} Main #{index}"
        #db.drivers.insert_one(driver)
        db.drivers.update_one(
            {"car_number": driver["car_number"]},
            {"$set": {"suffix": ""}}
        )
