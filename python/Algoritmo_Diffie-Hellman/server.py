import socket
import random as rnd

# Define the server's IP address and port
server_ip = '0.0.0.0'  # Change this to the IP address you want to bind to
server_port = 8000  # Choose a port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the IP address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen()  # The argument specifies the maximum number of queued connections

print(f"Server is listening on {server_ip} : {server_port}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Connection from {client_address}")
pubblic_key = None

b = rnd.randint(0, 1000)
B = None
A = None
while True:
    
    # Receive data from the client
    data = client_socket.recv(1024)
    
    if ';' in data.decode():
        pubblic_key = data.decode().split(';')
        print(pubblic_key)
    elif (len(data.decode()) == 0):
        break
    else:
        A = data.decode()
        client_socket.send(f'{int(pubblic_key[1]) ** b % int(pubblic_key[0])}'.encode())
    
    print(int(b)**int(A))
    client_socket.send(f'recived: {data}'.encode())

client_socket.close()

