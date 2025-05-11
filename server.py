import socket

# ~~~ SERVER SIDE STUFF ~~~ #
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP, capital bc it's constant

# instead of localhost can also do the ip address
# takes single input as a tuple
server.bind(('localhost', 12345)) 

server.listen() # no argument means no queue specified

print('Server is Live and Listening on Port: 12345!')

client, caddress = server.accept()
print(f'Connection from {caddress} opened...')

# RUN THIS CODE FIRST on terminal: 
# python server.py 
# then run client.py