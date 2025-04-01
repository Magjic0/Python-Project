import socket

HOST = input("Entrez l'adresse IP : ")
PORT_STR = input("Entrez le port : ")
try:
    PORT = int(PORT_STR)
except ValueError:
    print("Erreur : Le port doit être un nombre entier.")
    exit()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print("Connexion établie. Réception en cours...\n")
        data = s.recv(1024)
        print(data.decode('utf-8'))
    except Exception as e:
        print(f"Erreur de connexion : {e}")
