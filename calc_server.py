import json
import socket

SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind((SERVER_IP,SERVER_PORT))


while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)

    if not data:
        break
    
    data=data.decode()
    data=json.loads(data)
    primoNumero=data['primoNumero']
    operazione=data['operazione']
    secondoNumero=data['secondoNumero']

    risultato=0
    if operazione == '+':
        risultato=primoNumero+secondoNumero
    elif operazione == '-':
        risultato=primoNumero-secondoNumero
    elif operazione == '*':
        risultato=primoNumero*secondoNumero
    elif operazione == '/':
        if secondoNumero != 0:
            risultato=primoNumero/secondoNumero
        else:
            risultato = "Impossibile"
    elif operazione == '%':
        risultato=primoNumero%secondoNumero

    sock.sendto(str(risultato).encode(), addr)


