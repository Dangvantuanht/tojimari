"""Sniff the packets that are passing through the host."""

import socket
import sys
import threading

class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.response = b"HTTP/1.1 503 OK\n\nIt's all working!!"
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def __enter__(self):
        self.sock.bind((self.host, self.port))
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.sock.close()

    def handle_client(self, conn):
        try:
            print(conn.recv(1024).decode())
            conn.sendall(self.response)
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            conn.close()

    def start(self):
        self.sock.listen()
        print(f"Server is listening on {self.host}:{self.port}")
        while True:
            try:
                conn, _ = self.sock.accept()
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
