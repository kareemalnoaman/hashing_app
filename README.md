# Metropolitan State University
## CYBR 432 - Cryptography 
## Summer 2023
### Author: Abdulkareem Alnoaman
### Date completed: 07/30/2023

### Final Project - Hash Application {#hash_app-001}

### Description {#description-002}

This is a simple application that can be used to generate hashes for a given string. 
The application can also be used to verify a given hash against a given string.
The application can be used to generate hashes for the following algorithms:
- sha256 [default]
- sha512
- sha3_256
- sha3_512

The main purpose of this application is to demonstrate the use of the hashlib library in python.
The application can store the user's username and password in a file. The password is stored as a hash.
The application can also verify the user's password against the stored hash.

### Usage {#usage-003}
The application can be used in two modes: generate and verify. The default mode is to generates hash for a user's password.
To use the application in generate mode, the following command can be used:
```
python3 hashing_app.py -m generate -a sha256 -s "Hello World"
```
The above command will generate a sha256 hash for the string "Hello World". The output will be as follows:
```
Hash:  2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e730
```
To use the application in verify mode, the following command can be used:
```
python3 hashing_app.py -m verify -a sha256 -s "Hello World" -H 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e730
```
The above command will verify that the hash 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e730 is indeed the hash for the string "Hello World". The output will be as follows:
```
Hash:  2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e730
Verified:  True
```
### References {#references-004}
- https://docs.python.org/3/library/hashlib.html