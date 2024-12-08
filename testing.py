import json

with open ("passwords.json", "r") as file:
    data = json.load(file)
print(json.dumps(data, indent=4))