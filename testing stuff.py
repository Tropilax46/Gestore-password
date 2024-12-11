import json
import time

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
    with open ("passwords.json", "r") as file:
        data_show = json.load(file)
    if not Account:
        print("\n\ngli accounts attualmente registrati sono:\n")
        for account in data_show.keys():
            print(account)
    else:
        if Account in data_show.keys():
            print(f"l'Email: {data[Account]['Email']}\nla Password:{data[Account]['Password']}\n")
        else:
            print(f"non ho trovato un'account chiamato \"{Account}\"\n")
    time.sleep(2)
    print("\n\n______________________\n\n")

x= True
while x == True:
    mode = input("\nPremi:\n1 per aggiungere una nuova password\n2 per aggiornare una password esistente\n3 per eliminare una password\n4 per navigare fra le password\n\nPREMI 5 PER FARE IL LOGOUT\n")
    if int(mode) == 1:
        target = input("\n\ncosa vuoi vedere?\n1 per vedere gli account disponibili\n2 per vedere un'account specifico\n\n")
        if int(target) == 1:
            print_accounts(None, data)
        elif int(target) == 2:
            Account = input("\nQuale credenziali vuoi vedere?\n")
            print_accounts(Account, data)
            continue
        else:
            print("niente")
    else:
        print("niente")