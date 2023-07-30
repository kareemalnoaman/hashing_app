import socket
import hashlib
import os
# Author: Abdulkareem Alnoaman
# Date: 07/30/2023
# Course: CYBR 432 - Cryptography for Cybersecurity Practitioners
# Program: Final Project - Hashing Application [Step-5]

# Description: This is a simple server that receives a username and password
# from a client and stores them in a file.
# The server also hashes the password before storing it in the file.
# The server sends a response to the client after receiving the credentials.

host = 'localhost'
port = 8080

# creating a client's socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def start_server():
    server_socket.bind((host, port))
    server_socket.listen(5)  # Number of queued connections

    print(f"Server started. Listening on {host}:{port}")
    handle_client(server_socket)
    
def hash_password(password):
    if not password:
        print("No password was received")
    if password != password:
        print("Password is not correct")
    else:
        # Create a salt
        salt = os.urandom(32)
        # Use the hashlib.sha256 function to hash the password along with its salt
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        hex_password = hashed_password.hex()
        # Return the salt and the hashed password
        return hex_password

def handle_client(client_socket):
    # Example: Echo back messages from the client until it disconnects
    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"\nReceived user's credential [Printed to 'credentials.txt' file too]:\n\n{data.decode()}")
            # Store the username and password in variables
            username = data.decode().split('\n')[0].split(':')[1]
            password = data.decode().split('\n')[1].split(':')[1]
            # Hash the password
            hashed_password = hash_password(password)
            # Store the username and hashed password in a file
            with open('credentials.txt', 'w') as f:
                f.write(f"Username: {username}\nPassword: {hashed_password}")
            # Send a response to the client
            client_socket.sendall(f"Thank you for your credentials!".encode())
            client_socket.close()

    except Exception as e:
        print(f"Error: {e}")
        client_socket.close()

def handle_file(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)
    with open(file_path, 'r') as f:
        content = f.read()
        print(content)
    return content


def main():
    start_server()
    file_path = 'credentials.txt'
    content = 'Username: {username}\nPassword:{password}'
    
    handle_file(file_path, content)

if __name__ == "__main__":
    main()






