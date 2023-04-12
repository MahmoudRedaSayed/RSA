import socket
import argparse
import ast
import KeyGeneration

from RSA import RSA

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bits", help="key length", type=int)
    args = parser.parse_args()
    # generate public keys at client
    rsa = RSA()
    keyGeneratorObj = KeyGeneration.KeyGeneration(int(args.bits))

    exponent = keyGeneratorObj.e
    n = keyGeneratorObj.n
    public_keys = [n, exponent]

    host = socket.gethostname()
    c = socket.socket()
    port = 82

    c.connect((host, port))

    # send keys to server
    keys = f"{str(public_keys[0])} {str(public_keys[1])}"
    c.send(keys.encode())

    msg = ''

    while msg.lower().strip() != 'bye':

        # receive from server
        data = (c.recv(1024).decode())
        data=data[1:-1]
        data=data.split(',')
        msg = rsa.decryption(data)
        print(f"Received message after decryption is: {msg}")

    c.close()
