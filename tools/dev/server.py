"""Local server for testing."""

import socket
import sys
import threading
from datetime import datetime

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.response = b"HTTP/1.1 503 OK\n\nIt's all working!!"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __enter__(self):
        try:
            self.sock.bind((self.host, self.port))
            self.sock.listen()
            print(f"Server is listening on {self.host}:{self.port}")
        except Exception as e:
            print(f"Failed to bind server on {self.host}:{self.port}: {e}")
            sys.exit(1)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.sock.close()

    def handle_client(self, conn):
        try:
            peername = conn.getpeername()
            print(f"Received connection from {peername}")
            request = conn.recv(1024).decode()
            print(f"Received request from {peername}:\n{request}")
            self.log_request(peername, request)
            conn.sendall(self.response)
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            conn.close()

    def log_request(self, peername, request):
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("request_log.txt", "a") as log_file:
                log_file.write(f"[{timestamp}] {peername} - Request:\n{request}\n")
        except Exception as e:
            print(f"Error logging request: {e}")

    def start(self):
        while True:
            try:
                conn, addr = self.sock.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(conn,))
                client_thread.start()
            except KeyboardInterrupt:
                print("Server is shutting down.")
                break
            except Exception as e:
                print(f"Server error: {e}")
                sys.exit(1)

def main():
    HOST, PORT = "192.168.1.2", 9999
    with Server(HOST, PORT) as server:
        server.start()

if __name__ == "__main__":
    main()
