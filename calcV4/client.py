import socket, sys, random, os, time, threading, multiprocessing, json

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22224
NUM_WORKERS = 15

def genera_richieste(address, port):
    start_time_thread = time.time()
    try:
        s=socket.socket()
        s.connect((address,port))
        print(f"\n{threading.current_thread().name} Connessione al server: {address}:{port}")
    except:
        print(f"\n{threading.current_thread().name} Errore, sto uscendo...")
        sys.exit()

    comandi=['+','-','*','%','/']
    primoNumero=random.randint(1,100)
    operazione=comandi[random.randint(0,4)]
    secondoNumero=random.randint(1,100)

    messaggio={
        'primoNumero':primoNumero,
        'operazione':operazione,
        'secondoNumero':secondoNumero
    }
    messaggio = json.dumps(messaggio)
    s.sendall(messaggio.enconde('UTF-8'))
    data=s.recv(1024)
    if not data:
        print(f"{threading.current_thread().name}: Server non rispode")
    else:
        print(f"{threading.current_thread().name}: Risultato: {data.decode()}")
    s.close()
    end_time_thread = time.time()
    print(f"{threading.current_thread().name} tempo di eseguzione =", end_time_thread - start_time_thread)

if __name__ == '__main__':
    start_time = time.time()
    threads = [threading.Thread(target=genera_richieste,args=(SERVER_ADDRESS, SERVER_PORT)) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]
    end_time = time.time()

    print("Tempo totale = ", end_time - start_time)

