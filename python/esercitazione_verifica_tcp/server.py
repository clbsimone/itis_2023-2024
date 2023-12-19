import socket
from threading import Thread
import sqlite3
import time

# Definisci l'indirizzo del server (host, porta)
server_address = ('0.0.0.0', 8000)

# Crea un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa il socket all'indirizzo del server
server_socket.bind(server_address)

# Metti in ascolto per connessioni in entrata
server_socket.listen()

# Classe per gestire ciascun client
class ThreadForClient(Thread):
    def __init__(self, id,  client_socket, client_address):
        super().__init__()
        self.id = id
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):

        while True:
            data = self.client_socket.recv(1024)
            if not data:
                break  # Connection closed by the client

            message = data.decode()
            print(f"{message} from {self.client_address}")

            if message.lower() == 'exit':
                break  # Terminate the connection
            elif message.lower() == 'op':
                self.sendOperation('5+6*(454483+3447)')
            elif message.lower() == 'getop':
                for row in data_db:
                    if self.id == row[1]:
                        
                        self.sendOperation(row[-1])
            

        # Chiudi la connessione
        self.client_socket.close()
        print(f"Connection with {self.client_address} closed")

    def sendOperation(self, op):
        self.client_socket.send(op.encode())

file_db = 'operations.db'
data_db = None

def letturaDB():
    global data_db
    conn_db = sqlite3.connect(file_db)
    cursor_db = conn_db.cursor()
    data_db = cursor_db.execute('SELECT * FROM operations').fetchall()

def main():
    letturaDB()
    id_client = 0
    while True:
        # Aspetta una connessione
        client_socket, client_address = server_socket.accept()
        id_client += 1
        # Crea un nuovo thread per gestire il client
        client_handler = ThreadForClient(id_client, client_socket, client_address)
        client_handler.start()


if __name__ =='__main__':
    main()