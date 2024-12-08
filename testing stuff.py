import json

#funzione per caricare i dati dell'app
def load_data(file_name = "passwords.json"):
    try:    
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
data = load_data()

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


def print_accounts(Account, data):
    print("gli accounts attualmente registrati sono:\n")
    with open ("passwords.json", "r") as file:
        data_show = json.load(file)
    if not Account:
        for account in data_show.keys():
            print(json.dumps(data, indent=4))
    else:
        for account in data_show.keys():
            if Account in data.show.keys():
                print(Account.keys())
            else:
                print(f"non ho trovato {Account}\n")

x= True
while x == True:
    mode = input("\nPremi:\n1 per aggiungere una nuova password\n2 per aggiornare una password esistente\n3 per eliminare una password\n4 per navigare fra le password\n\nPREMI 5 PER FARE IL LOGOUT\n")
    if int(mode) == 1:
        target = input("\n\ncosa vuoi vedere?\n1 per vedere gli account disponibili\n2 per vedere un'account specifico\n")
        if int(target) == 1:
            print_accounts(data)
        elif int(target) == 2:
            Account = input("Quale credenziali vuoi vedere?\n\n")
            print_accounts(Account, data)
            continue
        else:
            print("niente")
    else:
        print("niente")