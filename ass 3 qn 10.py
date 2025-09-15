#server client-server with sockets
#server listens and sends a greeting;client connects and receives.
#run server first in one process/terminal;then client
 #server.py

import socket

def start_server():
    host = "127.0.0.1"  # localhost
    port = 65432        # non-privileged port

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print("Server is listening...")
        conn, addr = s.accept()
        with conn:
            print("Connected by", addr)
            conn.sendall(b"Hello from server!")

if __name__ == "__main__":
    start_server()

 #client.py

import socket

def start_client():
    host = "127.0.0.1"
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((host, port))
            data = s.recv(1024)
            print("Received:", data.decode())
        except ConnectionError:
            print("Error: Could not connect to server.")

if __name__ == "__main__":
    start_client()

