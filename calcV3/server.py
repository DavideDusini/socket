import socket, json
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

def ricevi_comandi(sock_service,addr_client):
    print("avviato")
    while True:
        data=sock_service.recv(1024)
        if not data: 
            break
        data=data.decode
        data=json.loads(data)
        primoNumero=data['primoNumero']
        operazione=data['operazione']
        secondoNumero=data['secondoNumero']
        risultato=""
        if operazione =="+":
            risultato=primoNumero +secondoNumero
        elif operazione=="-":
            risultato=primoNumero-secondoNumero
        elif operazione=="*":
            risultato=primoNumero*secondoNumero
        elif operazione =="/":
            if secondoNumero==0:
                risultato="non puoi dividere per 0"
            else:
                risultato=primoNumero/secondoNumero
        elif operazione=="%":
            risultato=primoNumero%secondoNumero
        else:
            risultato="Operazione non riconosciuta"
        risultato=str(risultato)
        sock_service.sendall(risultato.encode("UTF-8"))
        sock_service.close(0)

def ricevi_connessioni(sock_listen):
    while True:
        sock_service, addr_client = sock_listen.accept()
        print("\nConnessione ricevuta da %s" % str(addr_client))
        print("Creo un thread per servire le richieste")
        try:
            Thread(target=ricevi_comandi, args=(sock_service, addr_client)).start()
        except:
            print("Il thread non si avvia")
            sock_listen.close()

def avvia_server(indirizzo, porta):
    sock_listen = socket.socket()
    sock_listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_listen.bind((indirizzo, porta))
    sock_listen.listen(5)
    print("Server in ascolto su %s" %str((indirizzo, porta)))
    ricevi_connessioni(sock_listen)

if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)
print("Termina")