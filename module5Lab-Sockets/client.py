import socket

# ~~~ client server setup ~~~ #
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# ~~~ CLIENT SIDE ~~~ #
server_address = ('localhost', 12345)
client.connect(server_address)
print(f'\nConnected to {server_address[0]} at port {server_address[1]}\n')

## sending and receiving data
client.send('Please hold for user input.'.encode())

userIn = input("\nUser, please enter a name: ")
client.send(userIn.encode())

# Server Response to user input
received = client.recv(1024).decode('UTF-8')
print(f'\n{received}\n')
# Check if found or not
found = client.recv(1024).decode()
if found == "false":
    userIn = input("Would you like to add your character to our database? Y/N: ")
    client.send(userIn.lower().encode())
    if userIn.lower() == "y":
        newCharacter = input("Please enter their name: ")
        newInfo = input("Please enter a description: ")
        newRelated = input("Please enter any Related Characters separated by periods. If none, leave blank and press enter: ")
        client.send(newCharacter.encode())
        client.send(newInfo.encode())
        client.send(newRelated.encode())

client.close()