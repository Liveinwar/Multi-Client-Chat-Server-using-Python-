import socket
import threading

# List to keep track of connected clients
clients = []

def handle_client(conn, addr):
    """Handle messages from a connected client"""
    print(f"[NEW CONNECTION] {addr} connected.")
    
    while True:
        try:
            # Receive message from client
            msg = conn.recv(1024)
            if not msg:
                break
            
            # Broadcast the message to all other clients
            broadcast(msg, conn)
            
        except:
            # Client disconnected or error occurred
            break
    
    # Clean up when client disconnects
    print(f"[DISCONNECT] {addr} disconnected.")
    clients.remove(conn)
    conn.close()

def broadcast(message, exclude_conn):
    """Send message to all connected clients except the sender"""
    for client in clients:
        if client != exclude_conn:
            try:
                client.send(message)
            except:
                # Remove client if sending fails
                pass

def start_server(host='127.0.0.1', port=12345):
    """Start the chat server"""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((host, port))
        server.listen()
        print(f"[LISTENING] Server is running on {host}:{port}")
        print("[INFO] Waiting for clients to connect...")
        
        while True:
            # Accept new client connections
            conn, addr = server.accept()
            clients.append(conn)
            
            # Start a new thread to handle the client
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.daemon = True  # Thread will close when main program closes
            thread.start()
            
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] Server is shutting down...")
    except Exception as e:
        print(f"[ERROR] Server error: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    start_server()