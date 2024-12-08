import json

# Funzione per salvare i dati su un file
def salva_dati(dati, nome_file='user.json'):
    with open(nome_file, 'w') as file:
        json.dump(dati, file)

# Funzione per caricare i dati da un file
def carica_dati(nome_file='user.json'):
    try:
        with open(nome_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


dati = {
    "user1": {"password": "segreta123", "email": "utente1@example.com"},
    "user2": {"password": "sicura456", "email": "utente2@example.com"}
}

# Salva i dati
salva_dati(dati)

# Carica i dati
dati_caricati = carica_dati()
print(dati_caricati)

def aggiungi_password(username, password, email, dati):
    dati[username] = {"password": password, "email": email}
    salva_dati(dati)

# Funzione per rimuovere una password
def rimuovi_password(username, dati):
    if username in dati:
        del dati[username]
        salva_dati(dati)

# Funzione per aggiornare una password esistente
def aggiorna_password(username, nuova_password, dati):
    if username in dati:
        dati[username]['password'] = nuova_password
        salva_dati(dati)

aggiungi_password("user3", "babba123", "info@mama.os", dati)

print(dati_caricati)