import json


'''
def show(Account, data):
    if Account in data:
        conferma = input(f"le info che c'erano prima sono:\n{data[Account]['email']}\n{data[Account]['password']}\n\nVuoi sostituire le info")
    else:
        return ("non ho trovato il file")

data = {
    "utente1": {"password": "segreta123", "email": "utente1@example.com"},
    "Facebook": {"password": "sicura456", "email": "utente2@example.com"}
}

x = True
while x == True:
    show("Facebook", data)
    print(f"\nemail:{data[utente1][email]}\n\npassword:\n{data[utente1][password]}")
    
'''

#testando print_accounts()
'''
data = {
    "utente1": {"password": "segreta123", "email": "utente1@example.com"},
    "Facebook": {"password": "sicura456", "email": "utente2@example.com"}
}

def print_accounts(data):
    print("nomi degli accounts:\n")
    for Account in data.keys():
        print(Account)
'''

#

def print_accounts(Account, data):
    print("gli accounts attualmente registrati sono:\n")
    with open ("passwords.json", "r") as file:
        data = json.load(file)
    print(json.dumps(data, indent=4))
    if Account == {}:
        for account in data.keys():
            print(account)
    else:
        for account in data.keys():
            print(account)
            for value in data.keys():
                print(value)
