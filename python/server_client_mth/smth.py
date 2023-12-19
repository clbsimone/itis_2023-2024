import socket
from threading import Thread

# Definisci l'indirizzo del server (host, porta)
server_address = ('0.0.0.0', 8000)

# Crea un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa il socket all'indirizzo del server
server_socket.bind(server_address)

# Metti in ascolto per connessioni in entrata
server_socket.listen()
print(f"Server is listening on {server_address[0]}:{server_address[1]}")

# Classe per gestire ciascun client
class ThreadForClient(Thread):
    def __init__(self, id,  client_socket, client_address):
        super().__init__()
        self.id = id
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        print(f"Connection from {self.client_address}")

        while True:
            # Ricevi dati dal client
            data = self.client_socket.recv(1024)
            if not data:
                break  # Connection closed by the client
                
            message = data.decode()
            print(f"Received from {self.client_address}: {message}")

            if message.lower() == 'exit':
                break  # Terminate the connection
            elif message.lower() == 'info':
                infoClient(self.id, self.client_socket, self.client_address)
            
            # Invia una risposta al client
            response = f"{self.id} I received: {message}"
            self.client_socket.send(response.encode())

        # Chiudi la connessione
        self.client_socket.close()
        print(f"Connection with {self.client_address} closed")

def infoClient(id,  client_socket, client_address):
    print(f'Client {id}: {client_address}')

def main():
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