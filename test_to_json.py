import csv
import json

csv_name = "dummy.csv"
json_name = "output.json"
#json_name2 = "output2.json"
#json_name3 = "output3.json"

with open(csv_name, 'r', encoding="utf-8") as f:
    d_reader = csv.DictReader(f)
    d_list = [row for row in d_reader]

with open(json_name, 'w') as f:
    json.dump(d_list, f, ensure_ascii=False, indent=2)

#with open(json_name2, 'w') as f:
#    json.dump(d_list[10:25], f, ensure_ascii=False, indent=2)

#with open(json_name3, 'w') as f:
#    json.dump(d_list[0:20], f, ensure_ascii=False, indent=2)

# python3 test_to_json.py
