import socket
import argparse
import ast
import KeyGeneration
import helper
from RSA import RSA
'''
===================
Receiver: (take para number of bits)
===================
will get the public key and send it to the sender 
and will receive the public key of the sender to chat with each other
'''
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bits", help="key length", type=int)
    args = parser.parse_args()
    rsa = RSA()
    keyGeneratorObj = KeyGeneration.KeyGeneration(int(args.bits))
    keyGeneratorObj.generateRandomKey()

    exponent = keyGeneratorObj.e
    n = keyGeneratorObj.n
    public_keys = [n, exponent,int(args.bits)]

    host = socket.gethostname()
    c = socket.socket()
    port = 82

    c.connect((host, port))

    keys = f"{str(public_keys[0])} {str(public_keys[1])} {str(public_keys[2])}"
    c.send(keys.encode())
    public_keys = c.recv(1024).decode()
    print("receiver recevie that",public_keys)
    msg = ''
    while msg.lower().strip() != 'bye':

        data = (c.recv(1024).decode())
        data=data[1:-1]
        data=data.split(',')
        ciphertext1 = helper.encryption_Decryption(data, keyGeneratorObj.d, keyGeneratorObj.n)
        msg = rsa.decryption(ciphertext1)
        print(f"Received message after decryption is: {msg}")
        text1 = input('ENTER message to send to sender:\n')
        packets=rsa.encryption(text1)
        ciphertext1 = helper.encryption_Decryption(packets, int(public_keys.split(' ')[0]), int(public_keys.split(' ')[1]))
        c.send(str(ciphertext1).encode())

    c.close()
