# CIS112-clientServerApp
The task is to develop a client-server application in Python using sockets. The application consists of two parts: a server (host) application and a client application.

The server stores information about individuals in a dictionary and responds to client requests by sending information about the requested individual if available. The client prompts the user to enter the name of the individual they're interested in, sends the request to the server, receives the response, and displays it to the user.

## Part 1: Server (Host) Application (10 points)
### Requirements:
1. Implement a server application (`server.py`) that listens for incoming connections from clients.
2. Define a dictionary (`people`) containing information about individuals (you can choose what information you want to include. Have fun with it!). Each key-value pair represents the name and associated information of an individual.
3. While the server is active it should print status updates to the terminal. Specifically the following statuses:
   - "Listening on [host:port]" when the server starts listening for incoming connections.
   - "Connection established with [client_address]" when a connection is established with a client.
4. Upon receiving a client request, the server should check if the requested name exists in the dictionary:
   - If the name exists, the server should send the associated information to the client.
   - If the name does not exist, the server should send a notification to the client that the person does not exist.
5. Utilize the `pickle` module to serialize and deserialize data for communication between the client and server.

### Rubric:
- Socket Communication (2 points): Proper implementation of socket communication between the client and server.
- Dictionary Implementation (2 points): Define a dictionary (`people`) containing information about individuals.
- Status Updates (2 points): 
    - Server prints "Listening on [host:port]" when starting to listen for incoming connections.
    - Server prints "Connection established with [client_address]" when a connection is established with a client.
- Response Handling (2 points):
    - Server responds with the associated information if the requested name exists.
    - Server sends a notification if the requested name does not exist.
- Code Quality (2 points):
    - Code is well-structured, organized, and easy to understand.
    - Proper use of comments where necessary.

## Part 2: Client Application (10 points)
### Requirements:
1. Implement a client application (`client.py`) that connects to the server.
2. Upon launching, the client should prompt the user to enter the name of the individual they're interested in.
3. Send the entered name to the server for processing.
4. Receive the response from the server and display it to the user.
5. Utilize the `pickle` module to serialize and deserialize data for communication between the client and server.

### Rubric:
- User Input Handling (2 points):
    - Client prompts the user to enter the name of the individual.
- Socket Communication (3 points):
    - Proper implementation of socket communication between the client and server.
- Response Handling (3 points):
    - Client receives and properly handles the response from the server.
- Display Output (1 point):
    - Client displays the received information to the user.
- Code Quality (1 point):
    - Code is well-structured, organized, and easy to understand.
    - Proper use of comments where necessary.

Note: Adhere to Python coding conventions, provide clear comments where necessary, and thoroughly test the applications before submission.