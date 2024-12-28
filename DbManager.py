import os

imageList = os.listdir("images/")

namesList = []

currentName = []

for imageName in imageList:
    nameWithoutExtension = imageName.replace('.png', '')

    nameParts = nameWithoutExtension.split()

    if len(nameParts) > 1:
        namesList.append(' '.join(nameParts))
    else:
        currentName.append(nameParts[0])
        if len(currentName) >= 2:
            namesList.append(' '.join(nameParts))
        currentName=[]

print(namesList)