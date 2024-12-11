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

#funzione per caricare gli users dell'app
'''
def load_users(file_name = "users.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
users_loaded = load_users()
'''


#funzione per salvare i dati dell'app
def save(Account, data, file_name = "passwords.json"):
    if not Account:
        None
    else:
        confirm = input(f"\ndopo la conferma le informazioni salvate saranno:\n\n{data[Account]}\n\nvuoi confermare? premi Y per confermare\n")
    if confirm.lower() == "y":
        with open(file_name, "w") as file:
            json.dump(data, file)
        print("\nConfermato, ho salvato\n")
    else:
        print("\nok ho interrotto tutto, non è stato salvato nulla, quindi è tutto come prima.\n")

#funzione per aggiungere una password
def add_Account(Account, Email, Password, data):
    data[Account] = {"Email": Email, "Password": Password}

#funzione per cancellare una password
def del_Account(Account, data):
    if Account in data:
        del data[Account]

#funzione per modificare una password
def mod_Account(Account, Email, Password, data):
    if Account in data:
        data[Account]["Email"] = Email
        data[Account]["Password"] = Password

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

print("benvenuto\n")

#funzione per loggarsi
#def login(User)

# verifica se l'utente esiste
# def check_user(User0, User_Email0, User_Password0, User2, User_Email2, User_Password2, Users):
    


load_data()
#load_users()

x = True
while x == True:
    mode = input("\nPremi:\n1 per aggiungere una nuova password\n2 per aggiornare una password esistente\n3 per eliminare una password\n4 per navigare fra le password\n\nPREMI 5 PER FARE IL LOGOUT\n")
    if int(mode) == 1:
        Account = input("come si chiama il sito delle credenziali che devi registrare?\nes. Facebook\n")
        if Account not in data:
            Email = input("inserisci l'email da registrare.\n")
            Password = input("inserisci la password da registrare.\n")
            add_Account(Account, Email, Password, data)
            save(Account, data)
            time.sleep(2)
            print("\n\n______________________\n\n")
            continue
        else:
            print("\nl'Account esiste già, scegli un'altro nome o modifica quello esistente\n")
            time.sleep(2)
            print("\n\n______________________\n\n")
            continue
    elif int(mode) == 2:
        Account = input("\nCome si chiama il sito delle credenziali che devi modificare?\nes. Facebook\n\n")
        if Account in data:
            print(f"\nLe info che c'erano prima sono:\nEmail: {data[Account]['Email']}\nPassword: {data[Account]['Password']}\n")
            Email = input("inserisci la nuova Email.\n")
            Password = input("inserisci la nuova Password.\n")
            mod_Account(Account, Email, Password, data)
            save(Account, data)
            time.sleep(2)
            print("\n\n______________________\n\n")
        else:
            print("Non ho trovato un Account con questo nome...")
            time.sleep(2)
            print("\n\n______________________\n\n")
            continue
    elif int(mode) == 3:
        Account = input("come si chiama il sito delle credenziali che devi eliminare?\nes. Facebook\n")
        if Account in data:
            print(f"le info che contenute in {Account} sono:\nEmail: {data[Account]['Email']}\nPassword: {data[Account]['Password']}\n\n")
            del_Account(Account, data)
            save(Account, data)
            time.sleep(2)
            print("\n\n______________________\n\n")
        else:
            print("Non ho trovato un Account con questo nome...\n")
            time.sleep(2)
            print("\n\n______________________\n\n")
            continue
    elif int(mode) == 4:
        target = input("\n\ncosa vuoi vedere?\n1 per vedere gli account disponibili\n2 per vedere un'account specifico\n\n")
        if int(target) == 1:
            print_accounts(None, data)
            time.sleep(2)
            print("\n\n______________________\n\n")
        elif int(target) == 2:
            Account = input("\nQuale credenziali vuoi vedere?\n")
            print_accounts(Account, data)
            time.sleep(2)
            print("\n\n______________________\n\n")
            continue
        else:
            print("Hai inserito qualcosa che non va...")
            time.sleep(2)
            print("\n\n______________________\n\n")
            continue
    
    again = input(f"vuoi tornare alla home? y/n\n")
    if again.lower() == "n":
        x = False
              
    