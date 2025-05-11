import socket

# ~~~ client server setup ~~~ #
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# ~~~ CLIENT SIDE ~~~ #
server_address = ('localhost', 12345)
client.connect(server_address)

print(f'~Connected to host at port {server_address[1]}')

# Note: run this python client.py only after running server.py


## sending and receiving data
client.send('Hello server! How is the weather today?'.encode())
received = client.recv(1024)
print(f'~~Server Responded: {received}')
client.send('Thank you! Goodbye'.encode())
client.close()