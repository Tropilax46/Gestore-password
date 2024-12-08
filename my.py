import json

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
    confirm = input(f"dopo la conferma le informazioni salvate saranno:\n\n{data[Account]}\n\nvuoi confermare? premi Y per confermare\n")
    if confirm.lower() == "y":
        with open(file_name, "w") as file:
            json.dump(data, file)
        print("Confermato, ho salvato\n")
    else:
        print("ok ho interrotto tutto, non è stato salvato nulla, quindi è tutto come prima.\n")

#funzione per aggiungere una password
def add_password(Account, Email, Password, data):
    data[Account] = {"Email": Email, "Password": Password}

#funzione per cancellare una password
def del_password(Account, data):
    if Account in data:
        del data[Account]

#funzione per modificare una password
def mod_password(Account, Email, Password, data):
    if Account in data:
        data[Account]["Password"] = Password

def print_accounts(Account, data):
    print("gli accounts attualmente registrati sono:\n")
    if not Account:
        for account in data.keys():
            print(account)
    else:
        for account in data.keys():
            print(account)
            for value in data.keys():
                print(value)

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
            add_password(Account, Email, Password, data)
            save(Account, data)
            continue
        else:
            print("l'Account esiste già, scegli un'altro nome o modifica quello esistente")
    elif int(mode) == 2:
        Account = input("come si chiama il sito delle credenziali che devi modificare?\nes. Facebook\n")
        if Account in data:
            print(f"le info che c'erano prima sono:\nEmail: {data[Account]['Email']}\nPassword: {data[Account]['Password']}\n\n")
            Email = input("inserisci la nuova email.\n")
            Password = input("inserisci la nuova password.\n")
            mod_password(Account, Email, Password, data)
            save(Account, data)
            continue
        else:
            print("Non ho trovato un Account con questo nome...")
            continue
    elif int(mode) == 3:
        Account = input("come si chiama il sito delle credenziali che devi modificare?\nes. Facebook\n")
        if Account in data:
            print(f"le info che c'erano prima sono:\nEmail: {data[Account]['email']}\nPassword: {data[Account]['password']}\n\n")
            del_password(Account, data)
            save(Account, data)
            continue
        else:
            print("Non ho trovato un Account con questo nome...\n")
    elif int(mode) == 4:
        target = input("\n\ncosa vuoi vedere?\n1 per vedere gli account disponibili\n2 per vedere un'account specifico\n")
        if int(target) == 1:
            print_accounts(None,data)
        elif int(target) == 2:
            Account = input("Quale credenziali vuoi vedere?\n\n")
            print_accounts(Account, data)
        continue
    
    again = input(f"premi vuoi ritornare alla home? y/n\n")
    if again.lower() == "y":
        print("")
    else:
        x = False
              
    