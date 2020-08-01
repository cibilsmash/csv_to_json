import csv

import json

json_File = 'students.json'

csv_File_path = 'sample.csv'


def View_json(csv_File_path):


    data4 = []
    with open(csv_File_path, encoding='utf-8') as csv_fi:
        csv_data1 = csv.reader(csv_fi)

        data1 = list(csv_data1)

        result = sum(data1, [])

        for i in result:
            if i == "":
                data4.append("NULL")
            else:
                data4.append(i)

    with open(json_File, 'w', encoding='utf-8') as json_f:
                    json_f.write(json.dumps(data4))

View_json(csv_File_path)






















