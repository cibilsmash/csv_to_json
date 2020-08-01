import csv

import json


csv_File = 'sample.csv'
json_File = 'students.json'

def make_json(csv_File, json_File):

    data = {}
    with open(csv_File, encoding='utf-8') as csv_f:
        csv_data = csv.DictReader(csv_f)



        for rows in csv_data:

            key = rows['Name']

            if type(rows) is int:


                data[key] = int(rows)

            else:

                data[key] = rows




    with open(json_File, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(data, indent=4))


make_json(csv_File, json_File)





csv_file = 'sample.csv'


merge = []

def view_sample(csv_file):

    with open(csv_file, encoding='utf-8') as csv_f:

        csv_data = csv.reader(csv_f)

        dict_list = list(csv_data)

        print(dict_list)

















