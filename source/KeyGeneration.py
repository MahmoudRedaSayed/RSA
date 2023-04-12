import helper
import math

'''
===================
calculate the key according to the num of the bits 
===================
will get a random prime numbers p and q 
and then will calculate n 
and then will calculate phin
and then will calculate d
'''

class KeyGeneration:
    def __init__(self, bitsNum):
        self.e = 0
        self.d = 0
        self.n = 0
        self.bitsNum = bitsNum

    def generateRandomKey(self):
        p_num = helper.getPrime(self.bitsNum)
        q_num = helper.getPrime(self.bitsNum)
        n_num = p_num * q_num
        phi_n = (p_num - 1) * (q_num - 1)
        e_num = helper.getPrime(self.bitsNum)
        while math.gcd(e_num, phi_n) != 1:
            e_num = helper.getPrime(self.bitsNum)
        d_num, _, _ = helper.extendedEuclideanAlgorithm(e_num, phi_n)  
        d_num = d_num % phi_n
        self.e = e_num
        self.d = d_num
        self.n = n_num