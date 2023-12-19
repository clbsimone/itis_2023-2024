import socket

server_ip = '127.0.0.1'
server_address = (server_ip, 8000)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connectionToServer():
    client_socket.connect(server_address)
    print(f"Connected to {server_address[0]}:{server_address[1]}")

def operation(data):
    result = f'{data} = {eval(data)}'
    print(result)
    client_socket.send(result.encode())

def body():
    connectionToServer()
    
    message = input('mex: ')
    client_socket.send(message.encode())

    while True:
        

        if message.lower() == 'exit':
            break
        elif message.lower() == 'op' or message.lower() == 'getop':
            data = client_socket.recv(1024).decode()
            operation(data)
        else:
            data = client_socket.recv(1024)
            print(f"Received from server: {data.decode()}")

    client_socket.close()

def main():
    body()

if __name__ == '__main__':
    main()
    
