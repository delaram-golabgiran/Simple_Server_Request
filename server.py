import socket

def server_program():
    # Get Server Hostname
    srv_host_name = socket.gethostname()
    print("The Server Hostname is: ", srv_host_name)
    srv_IP = socket.gethostbyname(srv_host_name)
    print("The Server IP Address is: ", srv_IP)
    # Recommended to user port address above 1024
    port = 15200
    
    server_socket = socket.socket()
    server_socket.bind((srv_host_name, port)) # bind host address and port together
    
    # Configure how many client the server can listen simultaneously
    server_socket.listen(2)
    # Accept new connection
    conn, address = server_socket.accept()
    print("connection from: " + str(address))
    
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input(" -> ")
        conn.send(data.encode()) # send data to the client
    conn.close()
    
if __name__ == "__main__":
    server_program()
    
    
    