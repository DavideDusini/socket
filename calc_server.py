import json
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((SERVER_IP,SERVER_PORT))

primoNumero=float(input("Inserisci primo numero: "))
operazione=input("Inserisci l'operazione (+,-,/,*,%): ")
secondoNumero=float(input("Inserisci il secondo numero: "))

messaggio={
    'primoNumero':primoNumero,
    'operazione':operazione,
    'secondoNumero':secondoNumero
}
messaggio=json.dumps(messaggio)

sock.sendall(messaggio.encode("UTF-8"))
data = sock.recv(BUFFER_SIZE)
print("Risultato: ", data.decode())

sock.close()
