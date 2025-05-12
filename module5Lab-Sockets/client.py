import socket


# ~~~ client server setup ~~~ #
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# ~~~ CLIENT SIDE ~~~ #
server_address = ('localhost', 12345)
client.connect(server_address)
print(f'\nConnected to host at port {server_address[1]} ~~~')


## sending and receiving data
client.send('Please hold for user input.'.encode())

userIn = input("\nUser, please enter a name: ")
client.send(userIn.encode())

client.close()