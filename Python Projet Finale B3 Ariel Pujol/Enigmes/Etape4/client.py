import socket

HOST = input("Adresse reçu")
PORT = input("Port reçu")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print("Connexion établie. Réception en cours...\n")
        data = s.recv(1024)
        print(data.decode('utf-8'))
    except Exception as e:
        print(f"Erreur de connexion : {e}")
