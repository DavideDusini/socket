import socket
import json
HOST = '127.0.0.1'
PORT = 65432 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_service:
    sock_service.connect((HOST, PORT))
    while True:
        primoNumero=float(input("Inserisci primo numero: "))
        operazione=input("Inserisci l'operazione (+,-,/,*,%): ")
        secondoNumero=float(input("Inserisci il secondo numero: "))

        messaggio={
            'primoNumero':primoNumero,
            'operazione':operazione,
            'secondoNumero':secondoNumero
        }
        messaggio=json.dumps(messaggio)
        sock_service.sendto(messaggio.encode("UTF-8"), (HOST, PORT))
        data = sock_service.recv(1024)
        print('Risultato: '+ data.decode())