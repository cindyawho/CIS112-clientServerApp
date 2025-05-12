import socket

# ~~~ SERVER SIDE STUFF ~~~ #
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(('localhost', 12345)) 
server.listen(5)
print('\nServer is Live and Listening on Port: 12345!')

client, caddress = server.accept()
print(f'~Connection from {caddress} opened...')

## sending and receiving data
received = client.recv(1024)
print(f'~Client Says: {received}')

userIn = client.recv(1024)
print(f'Userinput received: {userIn}')

# Close connection with client and the overall server
client.close()
server.close()