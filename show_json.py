import json

x = True
while x == True:
    restart = input("\npremi un pulsante per vedere i dati\n")
    print("\n\n\n")
    with open ("passwords.json", "r") as file:
        data = json.load(file)
    print(json.dumps(data, indent=4))
    print("\n\n\n")