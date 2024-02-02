import socket
import json
HOST = '127.0.0.1'
PORT = 22225
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))
    print(f"Connesso a: {HOST}:{PORT}...")
    print("Comandi disponibili:\n#list : per vedere i voti inseriti\n#get /nomestudente : per richiedere i voti di uno studente\n#set /nomestudente : per inserire uno studente\n#put /nomestudente/materia/voto/ore : per aggiungere i voti della materia allo studente\n#close : per chiudere la connessione")
    while True:
        comando = input("Digita comando: ")
        parametri = input("Digita parametri (lascia vuoti per #list e #close): ")
        messaggio={
            'comando':comando,
            'parametri':parametri
        }
        
        messaggio=json.dumps(messaggio)
        sock_service.send(messaggio.encode("UTF-8"))
        dati = sock_service.recv(1024)
        dati = json.loads(dati.decode())

        risposta = dati['risposta']
        valori = dati['valori']
        print(risposta)
        print(valori)
        if comando == "#close":
            sock_service.close()