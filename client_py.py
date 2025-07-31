import socket
import threading

def receive_messages(sock):
    """Continuously receive and display messages from the server"""
    while True:
        try:
            msg = sock.recv(1024).decode('utf-8')
            if msg:
                print(msg)
            else:
                break
        except:
            # Connection closed or error occurred
            print("[ERROR] Connection to server lost.")
            break

def main():
    """Main client function"""
    # Get connection details from user
    host = input("Enter server IP [127.0.0.1]: ").strip() or "127.0.0.1"
    
    try:
        port = int(input("Enter port [12345]: ").strip() or 12345)
    except ValueError:
        print("[ERROR] Invalid port number. Using default port 12345.")
        port = 12345
    
    name = input("Enter your name: ").strip()
    if not name:
        print("[ERROR] Name cannot be empty.")
        return
    
    # Create socket and connect to server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((host, port))
        print(f"Connected to the chat server at {host}:{port}")
        print("Type your messages and press Enter. Type 'exit' to quit.\n")
        
        # Start thread to receive messages
        receive_thread = threading.Thread(target=receive_messages, args=(client,))
        receive_thread.daemon = True
        receive_thread.start()
        
        # Main loop for sending messages
        while True:
            msg = input()
            
            if msg.lower() == 'exit':
                print("Disconnecting from server...")
                break
            
            if msg.strip():  # Only send non-empty messages
                try:
                    formatted_msg = f"{name}: {msg}"
                    client.send(formatted_msg.encode('utf-8'))
                except:
                    print("[ERROR] Failed to send message.")
                    break
    
    except ConnectionRefusedError:
        print(f"[ERROR] Could not connect to server at {host}:{port}")
        print("Make sure the server is running and the address is correct.")
    except Exception as e:
        print(f"[ERROR] An error occurred: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    main()