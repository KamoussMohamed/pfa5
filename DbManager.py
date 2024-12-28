import os
#import json
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
    

    collection = db[collections[0]]
    for data in all_data:
        collection.insert_one(data)
        
    # with open("data.json", "w") as file:
    #     json.dump(all_data, file, indent=4)
