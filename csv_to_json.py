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

        for ele in result:
            if ele.isdigit():
                data4.append(int(ele))
            elif ele == "":
                data4.append("NULL")
            else:
                data4.append(ele)

        

    with open(json_File, 'w', encoding='utf-8') as json_f:
                    json_f.write(json.dumps(data4))

View_json(csv_File_path)

# initialize list
test_list = ["gfg", "1.6", "is", "6", "best",""]

# printing original list
print("The original list : " + str(test_list))

# Convert String numbers to integers in mixed List
# using list comprehension + isdigit()
#res = [int(ele) if ele.isdigit() else ele for ele in test_list]
res = []
for ele in test_list:
    if ele.isdigit():
        res.append(int(ele))
    elif ele == "":
        res.append("NULL")
    else:
        res.append(ele)

# printing result
print("List after converting string numbers to integers : " + str(res))
















