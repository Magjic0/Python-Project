import socket

HOST = '0.0.0.0'
PORT = 8888

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Serveur prêt sur {HOST}:{PORT}... En attente de connexion...")

    conn, addr = s.accept()
    with conn:
        print(f"Connexion de : {addr}")
        message = (
            "Bienvenue agent.\n"
            "Transmission sécurisée :\n"
            "Dernier Indice : ECHO-X\n"
        )
        conn.sendall(message.encode('utf-8'))
