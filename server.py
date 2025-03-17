import socket
import threading

def handle_client(client_socket, address):
    """Handle individual client connections"""
    print(f"New connection from {address}")
    
    while True:
        try:
            # Receive message from client (1024 is buffer size in bytes)
            message = client_socket.recv(1024).decode('utf-8')
            
            if not message:  # If connection is closed
                break
                
            print(f"Message from {address}: {message}")
            
            # Send response back to client
            response = f"Server received: {message}"
            client_socket.send(response.encode('utf-8'))
            
        except:
            break
    
    print(f"Connection from {address} closed")
    client_socket.close()

def start_server():
    """Start the server and listen for connections"""
    # Create a TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Server configuration
    HOST = '127.0.0.1'  # localhost
    PORT = 5555        # port to listen on
    
    # Bind the socket to address and port
    server.bind((HOST, PORT))
    
    # Listen for incoming connections (5 is the backlog)
    server.listen(5)
    print(f"Server listening on {HOST}:{PORT}")
    
    while True:
        # Accept incoming connections
        client_socket, address = server.accept()
        
        # Create new thread to handle client
        client_thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address)
        )
        client_thread.start()
        print(f"Active connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()