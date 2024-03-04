import socket

def echo_server(host, port):
    # Create a socket object
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        # Bind the socket to the host and port
        server_socket.bind((host, port))
        # Listen for incoming connections
        server_socket.listen(1)
        print(f"Echo server is listening on {host}:{port}...")
        
        while True:
            # Accept a client connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection established with {client_address}")
            
            with client_socket:
                while True:
                    # Receive data from the client
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode().strip()}")
                    
                    # Echo the received data back to the client
                    client_socket.sendall(data)
                    print("Sent back to client.")
                    
            print(f"Connection with {client_address} closed.")

if __name__ == "__main__":
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 8080    # Port to listen on (non-privileged ports are > 1023)
    echo_server(HOST, PORT)
