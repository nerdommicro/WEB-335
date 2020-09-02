#============================================
#Title: nesbitt-user-update.py
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

db.users.update_one( 
    {"employee_id": "12345"},
    {
        "$set": {
            "email": "micnes@my.bellevue.edu"
        }
    }
)

pprint.pprint(db.users.find_one({"employee_id": "12345"}))