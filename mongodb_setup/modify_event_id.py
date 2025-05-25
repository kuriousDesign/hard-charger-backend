from get_mongo_client import get_mongo_db

db = get_mongo_db('games_2025')

db.races 

# I want to update look up knoxville nationals events from events collection, then add a race to the races collection called b main

"""
Current Position
Positions Gained
Driver

1
0
Brad Sweet

2
0
Justin Peck

3
+3
David Gravel

4
-1
James McFadden

5
+4
Brock Zearfoss

6
+2
Dusty Zomer

7
-3
Cory Eliason

8
+7
Buddy Kofoid

9
+4
Spencer Bayston

10
+2
Cole Macedo

11
-6
Matt Juhl

12
+6
Parker Price-Miller

13
-6
Garet Williamson

14
+3
Skylar Gee

15
+4
Hunter Schuerenberg

16
+6
Danny Dietrich

17
+7
Chris Windom

18
+3
Brenham Crouch

19
-9
Cap Henry

20
+3
Ayrton Gennetten

21
-5
Tanner Holmes

22
-2
Kasey Kahne

23
-12
Lynton Jeffrey

24
-10
Kaleb Johnson
"""

b_main = {
    "type": "Main",
    "letter": "B",
    "event_id": 1,
    "num_cars": 24,
    "laps": 22,
    "num_transfers": 4,
    "first_transfer_position": 21,
    "intermission_lap": 0,
    "racers": [
        # use this commented list above to create the racers list
        {"car_number": "49", "driver_fullname": "Brad Sweet", "starting_position": 1, "current_position": 1},
        {"car_number": "26", "driver_fullname": "Justin Peck", "starting_position": 2, "current_position": 2},
        {"car_number": "2", "driver_fullname": "David Gravel", "starting_position": 6, "current_position": 3},
        {"car_number": "41", "driver_fullname": "James McFadden", "starting_position": 3, "current_position": 4},
        {"car_number": "70", "driver_fullname": "Brock Zearfoss", "starting_position": 9, "current_position": 5},
        {"car_number": "1S", "driver_fullname": "Dusty Zomer", "starting_position": 8, "current_position": 6},
        {"car_number": "26R", "driver_fullname": "Cory Eliason", "starting_position": 4, "current_position": 7},
        {"car_number": "83", "driver_fullname": "Buddy Kofoid", "starting_position": 15, "current_position": 8},
        {"car_number": "14", "driver_fullname": "Spencer Bayston", "starting_position": 13, "current_position": 9},
        {"car_number": "2C", "driver_fullname": "Cole Macedo", "starting_position": 12, "current_position": 10},
        {"car_number": "", "driver_fullname": "Matt Juhl", "starting_position": 5, "current_position": 11},
        {"car_number": "9", "driver_fullname": "Parker Price-Miller", "starting_position": 18, "current_position": 12},
        {"car_number": "23", "driver_fullname": "Garet Williamson", "starting_position": 7, "current_position": 13},
        {"car_number": "99", "driver_fullname": "Skylar Gee", "starting_position": 17, "current_position": 14},
        {"car_number": "55", "driver_fullname": "Hunter Schuerenberg", "starting_position": 19, "current_position": 15},
        {"car_number": "", "driver_fullname": "Danny Dietrich", "starting_position": 22, "current_position": 16},
        {"car_number": "", "driver_fullname": "Chris Windom", "starting_position": 24, "current_position": 17},
        {"car_number": "", "driver_fullname": "Brenham Crouch", "starting_position": 21, "current_position": 18},
        {"car_number": "", "driver_fullname": "Cap Henry", "starting_position": 10, "current_position": 19},
        {"car_number": "", "driver_fullname": "Ayrton Gennetten", "starting_position": 23, "current_position": 20},
        {"car_number": "", "driver_fullname": "Tanner Holmes", "starting_position": 16, "current_position": 21},
        {"car_number": "", "driver_fullname": "Kasey Kahne", "starting_position": 20, "current_position": 22},
        {"car_number": "", "driver_fullname": "Lynton Jeffrey", "starting_position": 11, "current_position": 23},
        {"car_number": "", "driver_fullname": "Kaleb Johnson", "starting_position": 14, "current_position": 24}
    ]
}


knoxville_nationals_event = db.events.find_one({"name": "Knoxville Nationals", "date": "2024-08-10"})
if knoxville_nationals_event:
    #
    # create b main 
    b_main["event_id"] = knoxville_nationals_event["_id"]
    #db.races.insert_one(b_main)
else:
    print("Knoxville Nationals event not found in the database")



# i want to modify the a main race so that its event_id is the same as b main
if knoxville_nationals_event:
    a_main_event_id = knoxville_nationals_event["_id"]
    db.races.update_one(
        {"type": "Main", "letter": "A", "event_id": 1},
        {"$set": {"event_id": a_main_event_id}}
    )
    print(f"Updating A Main event_id to {a_main_event_id}")
