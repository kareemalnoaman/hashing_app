import socket
# Author: Abdulkareem Alnoaman
# Date: 07/30/2023
# Course: CYBR 432 - Cryptography for Cybersecurity Practitioners
# Program: Final Project - Hashing Application [Step-5]

# Description: This is a simple client that sends a username and password
# to a server.

def send_credentials(host, port, username, password):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    try:
        credentials = f"Username: {username}\nPassword: {password}".encode()
        client_socket.sendall(credentials)

        response = client_socket.recv(1024)
        print(f"\nReceived ...\n{response.decode()}")
    except Exception as e:
        print(f"Error: {e}")
        client_socket.close()
    finally:
        print("\nDone!")
        

def main():
    HOST = "127.0.0.1"  # Replace this with your server's IP address or use "localhost"
    PORT = 8080       # Use the same port as your server
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    send_credentials(HOST, PORT, username, password)
if __name__ == "__main__":
    main()


