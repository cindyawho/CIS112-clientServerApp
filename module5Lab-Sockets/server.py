import socket

# Fictional Character Dictionary
people = {
    "percy jackson": "Son of Sally Jackson and Poseidon. Characters in Same Universe: Annabeth Chase. Leo Valdez.",
    "annabeth chase": "Daughter of Athena and excellent strategist. Characters in Same Universe: Percy Jackson. Leo Valdez.",
    "leo valdez": "Son of Hephaestus with a tragic backstory that makes him the most humorous. Characters in Same Universe: Annabeth Chase. Percy Jackson",
    "clara": "Overpowered companion of the Doctor. Characters in Same Universe: The Doctor. Donna.",
    "the doctor": "Timelord who travels in the TARDIS across time and space. Characters in Same Universe: Clara. Donna.",
    "donna": "The Doctor's companion with a big personality and a tragic ending worse than death. Characters in Same Universe: Clara. The Doctor.",
    "violet baudelaire": "Uniquely gifter in inventing abilities.",
    "remus lupin": "Werewolf",
    "hank hill": "One of the good republicans",
    "ender wiggin": "Super genius leader who has difficult choices to make",
}

# ~~~ SERVER SIDE STUFF ~~~ #
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.bind(('localhost', 12345)) 
server.listen(5)
print('\nListening on localhost : port 12345!')

client, caddress = server.accept()
print(f'Connection from {caddress} opened...')

## sending and receiving data
received = client.recv(1024)
print(f'Client Says: {received}')

userIn = client.recv(1024).decode('UTF-8').lower()
print(f'\nUser Input received: {userIn}\n')

# Check Dictionary for Information
if userIn in people:
    found = True
    result = people[userIn]
else: 
    found = False
    result = "We're sorry. The person you're searching for does not exist in our database."
    # Idea: prompt user to add their person to the database
client.send(result.encode())
if found:
    client.send("true".encode())
else:
    client.send("false".encode())

userIn = client.recv(1024).decode('UTF-8').lower()
if userIn == 'y':
    newChar = client.recv(1024).decode('UTF-8').lower()
    newInfo = client.recv(1024).decode('UTF-8') + " Characters in the Same Universe: " + client.recv(1024).decode('UTF-8') 
    print(f"\nNew Char: {newChar} and their info: {newInfo}\n")
    people[newChar] = newInfo

print("Current Dictionary: ")
print(people)

# Close connection with client and the overall server
client.close()
server.close()