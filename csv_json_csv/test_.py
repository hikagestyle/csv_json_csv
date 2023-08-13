import json

with open('output.json', 'r') as f:
    data = json.load(f)

with open('data.json', 'w') as f:
    json.dump(data[10:25], f, indent=2, ensure_ascii=False)

# python3 test_.py
