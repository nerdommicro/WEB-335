#============================================
#Title: nesbitt-user-service.py
#Author: Richard Krasso
#Date: 25 Aug 2020
#Modified By: Michelle Nesbitt
#Description: Demonstrates Python functions
# #==============================================

import pymongo
import datetime
import pprint

from pymongo import MongoClient

client = MongoClient('localhost', 27017) 
db = client.web335
print(client)
user = {
    "first_name": "Michelle",
    "last_name": "Jones",
    "employee_id": "12345",
    "email": "mn@test123.com",
    "date_create": datetime.datetime.utcnow()
}
user_id = db.users.insert_one(user).inserted_id
print(user_id)
pprint.pprint(db.users.find_one({"employee_id": "12345"}))