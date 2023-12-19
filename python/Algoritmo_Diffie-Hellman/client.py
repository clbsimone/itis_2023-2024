import socket
import random as rnd

# Define the server's IP address and port
server_ip = '127.0.0.1'  # Change this to the IP of your server
server_port = 8000  # Change this to the port your server is listening on

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

pubblic_key = None
A = None
N, g = 929, rnd.randint(1, 929)
a = None
B = None

def reciveServer():
    data = client_socket.recv(1024)
    print("Received from server:", data.decode())

def pubblicKey():
    pubblic_key = f'{N};{g}'
    client_socket.send(pubblic_key.encode())
    reciveServer()

def alice():
    global A, a
    a = rnd.randint(0, 1000)
    A = (g ** a)% N

def body():
    global B
    client_socket.send(f'{A}'.encode())
    B = client_socket.recv(1024)



def main():
    pubblicKey()
    alice()
    body()
    print(int(a) ** int(B.decode()))
    client_socket.close()
    
if __name__ == '__main__':
    main()



