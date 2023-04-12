import random
from helper import *
import re
from random import randint


class RSA:

    def __init__(self):
        print("new object")
    


    def encryption(self,message):
        print(len(message),message.lower())
        message=message.lower()
        packets=[]
        num=len(message)%5
        if num==0:
            pass
        else:
            for i in range(5-num):
                message+=" "
        print(len(message))
        for i in range((len(message)//5)):
                value=0
                for j in range(5):
                    print(message[i*5+j],4-j)
                    value+=alph_Mapping[message[i*5+j]]*pow(37, 4-j)
                packets.append(value)
        print(packets)
        return packets
    

    def decryption(self,data):
        plaintext=[]
        message=""
        for text in data:
            text=int(text)
            group = []
            for i in range(5):
                group.append(alph_Mapping_Decryption[text%(37)])
                text//=37
            group.reverse()
            plaintext.extend(group)
        for i in plaintext:
            message+=i
        return message


