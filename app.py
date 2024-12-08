import json

#creo un metodo per far si di capire se l'utente conferma.
positive_words_it = {"si", "sì", "certo", "ovvio", "ènormale", "eccome", "certamente", "affermativo", "palese", "sicuro", "yes", "yep", "yeah"}
def positive(word):
    return word.lower().strip("!. ") in positive_words_it

def save_data(data, file_name = "password.json"):
    with open(file, "w") as file:
        json.dump(data, file)
        
def load_data(file_name = "password.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def check_login(Users, Username0, Password0, file_name = "User.json"):
    try:
        with open(file_name, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


    
signed0 = input("Sei già registrato?\n")
signed1 = positive(signed0)



Username0 = input("inserisci l'Username:\n")
Password0 = input("inserisci Password:\n")

if signed1 == True:
    print (x)

if Username1 and Password1 == True:
    x = True
else:
    print (x)

while x:
    print(x)
