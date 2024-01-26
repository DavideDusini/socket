import socket

SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 22225
DIM_BUFFER = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock_server:
    sock_server.bind((SERVER_ADDRESS, SERVER_PORT))
    sock_server.listen()
    print(f"Server in ascolto su: {SERVER_ADDRESS}:{SERVER_PORT}")
    