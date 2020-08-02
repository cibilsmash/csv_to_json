
import csv
import json

csvFilePath = 'sample.csv'
jsonFilePath = 'students.json'

up_json_File = 'up_students.json'

# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):
    # create a dictionary
    data = {}

    data4 = []



    # Open a csv reader called DictReader
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        data1 = list(csvReader)

        data2 = json.dumps(data1)

        data3 = json.loads(data2)



        for x in range(0, len(data3)):

            key = data3[x]

            for i in key:

                if key[i] == "":
                    data[i] = "NULL"
                elif key[i].isdigit():
                    data[i] = int(key[i])
                else:
                    data[i] = key[i]

            dictionary_copy = data.copy()

            data4.append(dictionary_copy)

    data5 = json.loads(json.dumps(data4))

    with open(up_json_File, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data5, indent=4))




make_json(csvFilePath, jsonFilePath)