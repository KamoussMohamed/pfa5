import os
import json
from pymongo import MongoClient

imageList = os.listdir("images/")
namesList = []
currentName = []
all_data = []
client = MongoClient('mongodb://localhost:27017')
db = client['presenceAI']
collections = ["studentsCollection", "presentCollection", "absentCollection"]

def storeStudents():
    
    for imageName in imageList:
        nameWithoutExtension = imageName.replace('.png', '')
        nameParts = nameWithoutExtension.split()

        if len(nameParts) > 1:
            namesList.append(' '.join(nameParts))
        else:
            currentName.append(nameParts[0])
            if len(currentName) >= 2:
                namesList.append(' '.join(currentName))
                currentName = []

    for name in namesList:
        frag = name.split(" ")
        firstName = frag[0]
        middleAndLastNames = ' '.join(frag[1:])
        person_data = {
            "firstName": firstName,
            "lastName": middleAndLastNames
        }
        all_data.append(person_data)

    with open("data.json", "w") as file:
        json.dump(all_data, file, indent=4)

    collection = db[collections[0]]
    existing_records = list(collection.find({}, {"_id": 0}))

    new_records = []
    for person in all_data:
        if person not in existing_records:
            new_records.append(person)

    if new_records:
        collection.insert_many(new_records)
        print(f"Added {len(new_records)} new records to the database")
    else:
        print("No new records to add")

storeStudents()