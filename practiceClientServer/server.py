import socket

# ~~~ SERVER SIDE STUFF ~~~ #
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP, capital bc it's constant

# instead of localhost can also do the ip address
# takes single input as a tuple
server.bind(('localhost', 12345)) 

server.listen(5)

print('Server is Live and Listening on Port: 12345!')

client, caddress = server.accept()
print(f'~Connection from {caddress} opened...')

# RUN THIS CODE FIRST on terminal: 
# python server.py 
# then run client.py

# Sending and receiving data with server
## sending and receiving data
received = client.recv(1024)
print(f'~~Client Responded: {received}')
client.send('Hello Client. Thanks for joining us. The weather today is delightful'.encode())

received = client.recv(1024)
print(f'~~~Client Responded: {received}')

# Close connection with client and the overall server
client.close()
server.close()