import socket
IP = '127.0.0.1'
PORTA = 65432
DIM_BUFFER = 1024
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((IP, PORTA))
    sock_server.listen()
    print(f"Server in ascolto su {IP}:{PORTA}...")
    while True:
        #accetta le connessioni
        sock_service, address_client = sock_server.accept()
        with sock_service as sock_client:
        # Leggi i dati inviati dal client
            while True:
                dati = sock_client.recv(DIM_BUFFER).decode()
                if not dati:
                    break
        
                dati=dati.decode()
                primoNumero=dati['primoNumero']
                operazione=dati['operazione']
                secondoNumero=dati['secondoNumero']

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

                sock_client.sendall(str(risultato).encode())