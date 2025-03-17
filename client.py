import socket

def start_client():
    """Start the client and connect to server"""
    # Create a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Server configuration (must match server's HOST and PORT)
    HOST = '127.0.0.1'
    PORT = 5555
    
    try:
        # Connect to server
        client.connect((HOST, PORT))
        print(f"Connected to server at {HOST}:{PORT}")
        
        while True:
            # Get message from user
            message = input("Enter message (or 'quit' to exit): ")
            
            if message.lower() == 'quit':
                break
                
            # Send message to server
            client.send(message.encode('utf-8'))
            
            # Receive response from server
            response = client.recv(1024).decode('utf-8')
            print(f"Server response: {response}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()
        print("Connection closed")

if __name__ == "__main__":
    start_client()