import csv
import json

json_name = "data.json"
csv_name = "dummy-data.csv"

with open(json_name, 'r') as f:
    json_dict = json.load(f)

with open(csv_name, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=json_dict[0].keys(),
        doublequote=True,
        quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(json_dict)

# python3 test_to_csv.py
