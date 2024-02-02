import socket
import json
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
DIM_BUFFER = 1024


studenti = {   'Antonio Barbera': [ ['Matematica', 8, 1],
                                    ['Italiano', 6, 1],
                                    ['Inglese', 9.5, 0],
                                    ['Storia', 8, 2],
                                    ['Geografia', 8, 1]],
                'Giuseppe Gullo': [ ['Matematica', 9, 0],
                                    ['Italiano', 7, 3],
                                    ['Inglese', 7.5, 4],
                                    ['Storia', 7.5, 4],
                                    ['Geografia', 5, 7]],
                'Nicola Spina': [   ['Matematica', 7.5, 2],
                                    ['Italiano', 6, 2],
                                    ['Inglese', 4, 3],
                                    ['Storia', 8.5, 2],
                                    ['Geografia', 8, 2]]}
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_ADDRESS, SERVER_PORT))
    sock_server.listen()
    print(f"Server in ascolto su {SERVER_ADDRESS}:{SERVER_PORT}...")
    while True:
        sock_service, address_client = sock_server.accept()
        with sock_service as sock_client:
            while True:
                data = sock_service.recv(DIM_BUFFER).decode()
                if not data:
                    break
                
                dati = json.loads(data)
                comando = dati['comando']
                paramentri = dati['parametri']
                
                
                if comando == "#list":
                    risposta = "Voti inseriti"
                    valori = studenti
                elif comando == "#get":
                    
                    nome =  paramentri.split("/")[1]
                    risposta = (f"Voti di {nome}")
                    valori = studenti[nome]
                elif comando == "#set":
                    nome =  paramentri.split("/")[1]
                    if nome not in studenti:
                        studenti[nome] = []
                        risposta = (f"Studente {nome} inserito con successo")
                    else:
                        risposta = (f"Lo studente {nome} è già presente")
                elif comando == "#put":
                    nome = paramentri.split("/")[1]
                    materia = paramentri.split("/")[2]
                    voto = float(paramentri.split("/")[3])
                    ore = int(paramentri.split("/")[4])
                    studenti[nome]=[materia,voto,ore]
                elif comando == "#close":
                    risposta = "Chiusura della connessione"
                    valori = ""
                    break
                else:
                    risposta = "Comando non valido"
                    valori = ""


                risp = {"risposta": risposta, 
                            "valori": valori}
                
                risp = json.dumps(risp)
                sock_service.sendall(risp.encode("UTF-8"))
    