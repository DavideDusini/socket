import socket, json
from threading import Thread

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224

def ricevi_comandi(sock_service, addr_client):
    
    sock_service.close()

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
    try:
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
            sock_server.bind((SERVER_ADDRESS, SERVER_PORT))
            sock_server.listen()

    except socket.error as errore:
        print(errore)

    ricevi_connessioni(sock_server)

if __name__ == '__main__':
    avvia_server(SERVER_ADDRESS,SERVER_PORT)
print("Termina")