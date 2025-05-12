import socket

# People Dictionary
people = {
    "percy jackson": "Son of Sally Jackson and Poseidon"
}

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

userIn = client.recv(1024).decode('UTF-8').lower()
print(f'Userinput received: {userIn}\n')

# Check Dictionary for Information
if userIn in people:
    result = people[userIn]
else: 
    result = "We're sorry. The person you're searching for does not exist in our database."
    # Idea: prompt user to add their person to the database
client.send(result.encode())

# Close connection with client and the overall server
client.close()
server.close()