import socket
from RSA import RSA
import KeyGeneration
import helper
'''
===================
sender: 
===================
will get the public key and send it to the receiver 
and will receive the public key of the receiver to chat with each other
'''
host = socket.gethostname()
s = socket.socket()
port = 82
s.bind((host, port))
print("socket binded to %s" % (port))

s.listen(1)
print("server socket is listening, waiting for connectors")

userB, addr_acc = s.accept()
print('Got connection from', addr_acc)

public_keys = 0 
public_keys = userB.recv(1024).decode()
n = int(public_keys.split(' ')[0])
e = int(public_keys.split(' ')[1])
bit_num = int(public_keys.split(' ')[2])
print("num of bits",bit_num)
keyGeneratorObj = KeyGeneration.KeyGeneration(bit_num)
keyGeneratorObj.generateRandomKey()
print(keyGeneratorObj.n,n)
key=[keyGeneratorObj.e,keyGeneratorObj.n]
keys = f"{str(key[0])} {str(key[1])}"
userB.send(keys.encode())
rsa = RSA()
text1 = ''
while text1.lower().strip() != 'bye':
    text1 = input('ENTER message to send to receiver:\n')
    packets=rsa.encryption(text1)
    ciphertext1 = helper.encryption_Decryption(packets, e, n)
    userB.send(str(ciphertext1).encode())
    data = (userB.recv(1024).decode())
    data=data[1:-1]
    data=data.split(',')
    ciphertext1 = helper.encryption_Decryption(data, keyGeneratorObj.d, keyGeneratorObj.n)
    msg = rsa.decryption(ciphertext1)
    print(f"Received message after decryption is: {msg}")
userB.close()
