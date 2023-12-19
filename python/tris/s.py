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

tabella = [[0,1,2],
           [3,4,5],
           [6,7,8]]
pos = [0,1,2,3,4,5,6,7,8]

# Classe per gestire ciascun client
class ThreadForClient(Thread):
    def __init__(self, id,  client_socket, client_address):
        super().__init__()
        self.id = id
        self.client_socket = client_socket
        self.client_address = client_address

    def run(self):
        global tabella
        print(f"Connection from {self.client_address}")
        while True:
            response = f"inserisci comando"
            self.client_socket.send(response.encode())
            
            # Ricevi dati dal client
            data = self.client_socket.recv(1024)
            if not data:
                break  # Connection closed by the client
                
            command = data.decode()
            print(command)
            
            if int(command) in pos:
                command = int(command)
                for row in tabella:
                    if command in row:
                        row[row.index(int(command))] = f'P{self.id}'

                print(tabella)
                if controlloWin(tabella):
                    self.client_socket.send('Hai Vinto'.encode())
                    tabella = [[0,1,2],
                               [3,4,5],
                               [6,7,8]]
                    print(tabella)

            if data.lower() == 'exit':
                break

        # Chiudi la connessione
        self.client_socket.close()
        print(f"Connection with {self.client_address} closed")

def controlloWin(tab):
    for i in range(len(tab)):
        if tab[i][0] == tab[i][1] and tab[i][1] == tab[i][2]:
            return True
        if tab[0][i] == tab[1][i] and tab[1][i] == tab[2][i]:
            return True
        if i == 0:
            if tab[0][i] == tab[1][i+1] and tab[1][i+1] == tab[2][i+2]:
                return True
        
    return False

def sono_tutti_uguali(lista):
    # Verifica se tutti gli elementi sono uguali al primo elemento
    return all(elemento == lista[0] for elemento in lista)

def main():
    id_client = 0
    print(tabella)
    while True:
        # Aspetta una connessione
        client_socket, client_address = server_socket.accept()
        id_client += 1
        # Crea un nuovo thread per gestire il client
        client_handler = ThreadForClient(id_client, client_socket, client_address)
        client_handler.start()


if __name__ =='__main__':
    main()