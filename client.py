import socket

# ~~~ client server setup ~~~ #
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# ~~~ CLIENT SIDE ~~~ #
server_address = ('localhost', 12345)
client.connect(server_address)

print(f'Connected to host at port 12345')

# run this python client.py only after running server.py