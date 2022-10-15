import socket

def client_program():
    ## Get Client Hostname
    host_name = socket.gethostname()
    print("The Client Hostname is: ", host_name)
    client_IP = socket.gethostbyname(host_name)
    print("The Client IP Address is: ", client_IP)
    ## Example Port Number in both Sid (Client and Server)
    port = 15200
    
    client_socket = socket.socket()
    ## Connect to the server
    client_socket.connect((host_name, port))

    ## Get Client input
    message = input(" -> ")
    ## The process continue till Client input "Bye"
    while message.lower().strip() != "bye":

        ## Encode, change a string to a String of Bytes, This is nessasary in Networking communications
        client_socket.send(message.encode()) 
        data = client_socket.recv(1024).decode()  # receive response
        
        print("recieved from server: " + data)
        
        message = input(" -> ") ## again take input

    client_socket.close() ## close the connection
    
if __name__ == "__main__":
    client_program()