import socket

server_ip = '127.0.0.1'
server_address = (server_ip, 8000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connectionToServer():
    client_socket.connect(server_address)
    print(f"Connected to {server_address[0]}:{server_address[1]}")

def body():
    connectionToServer()
    
    while True:
        data = client_socket.recv(1024)
        print(f"server: {data.decode()}")

        message = input('comando:')
        client_socket.send(message.encode())

        if message.lower() == 'exit':
            break

        

    client_socket.close()

def main():
    body()


if __name__ == '__main__':
    main()
