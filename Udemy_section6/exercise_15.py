# Please read the instructions carefully and write your script here:
# You need to:
# - read data from csv_file.txt
# - process data and convert them into a single JSON object
# - store the JSON object into json_file.txt
# Your code starts here:
import json
jsonList = []
file = open('csv_file.txt', 'r')
club = [line.strip() for line in file.readlines()]
file.close()

for index in club:
    valueClub, valueCity, valueCountry = index.split(',')
    dictionary = dict(club = valueClub, country = valueCountry, city = valueCity)
    jsonList.append(dictionary)

file = open('json_file.txt', 'w')
json.dump(jsonList, file)
file.close()
