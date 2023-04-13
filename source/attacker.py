import math
import helper
import KeyGeneration
from RSA import RSA
import time
'''
    =========================
    the idea of the attacker 
    =========================
    to try to factorize n into 2 prime factor p, q 
    and then will calculate the private key d
    and will use d to decrypte the pair of the texts
    and then will compare the result to see if success to get the private key or not
'''
if __name__ == '__main__':
    rsa = RSA()
    times = []
    for i in range(5, 20):
        keyGeneratorObj = KeyGeneration.KeyGeneration(i)
        keyGeneratorObj.generateRandomKey()

        testPlaintext1 = "text for test"
        testPlaintext2 = "this is a new secret"
        preprocessedInput1 = rsa.encryption(testPlaintext1)
        preprocessedInput2 =rsa.encryption(testPlaintext2)
        ciphertext1 = helper.encryption_Decryption(preprocessedInput1, keyGeneratorObj.e, keyGeneratorObj.n)
        ciphertext2 = helper.encryption_Decryption(preprocessedInput2, keyGeneratorObj.e, keyGeneratorObj.n)

        prev = time.time()

        p, q = helper.factorize(keyGeneratorObj.n)
        phiNGen = (p - 1) * (q - 1)
        dGen, _, _ = helper.extendedEuclideanAlgorithm(keyGeneratorObj.e, phiNGen) 
        dGen = dGen % phiNGen

        decryptedCiphertext1 = helper.encryption_Decryption(ciphertext1, dGen, keyGeneratorObj.n)
        decryptedCiphertext2 = helper.encryption_Decryption(ciphertext2, dGen, keyGeneratorObj.n)
        decodedPlaintext1 = rsa.decryption(decryptedCiphertext1)
        decodedPlaintext2 = rsa.decryption(decryptedCiphertext2)
        success1 = decodedPlaintext1 == testPlaintext1.lower()
        success2 = decodedPlaintext2 == testPlaintext2.lower()
        delay = time.time() - prev
        times.append(delay)
        print("Delay (", i, "): ", delay)
        print("text1", " (", i, ") ", decodedPlaintext1)
        print("text2", " (", i, ") ", decodedPlaintext2)
        if success1:
            print("(#", i, ") ", "Succeeded on first !")
        else:
            print("(#", i, ") ", "Failed on first :(")
        if success2:
            print("(#", i, ") ", "Succeeded on second !")
        else:
            print("(#", i, ") ", "Failed on second  :(")
        if success1 and success2:
            print("(#", i, ") ", "Private key (d): \n", dGen)
        else:
            print("(#", i, ") ", "Failed to find private key :(")

    print("Delays", times)

    