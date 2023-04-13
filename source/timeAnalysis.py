import KeyGeneration
from RSA import RSA
import time
import helper
'''
===================
time analysis :
===================
will make encryption with different size of keys
and calculate the time to each step
the range from 14 to 800 with step 20 
'''
if __name__ == '__main__':
    RSA_Obj=RSA()
    testPlaintext1 = "this is secret"
    encodedPlaintext1 = RSA_Obj.encryption(testPlaintext1)
    print(encodedPlaintext1)
    times = []
    for i in range(14, 800, 20):
        keyGeneratorObj = KeyGeneration.KeyGeneration(i)
        keyGeneratorObj.generateRandomKey()
        prev = time.time()
        ciphertext1 = helper.encryption_Decryption(encodedPlaintext1, keyGeneratorObj.e, keyGeneratorObj.n)
        times.append(time.time() - prev)

    print("Delays: ", times)

'''
Delays: [0.0, 0.0, 0.0, 0.0, 0.001001596450805664, 0.0, 0.0009992122650146484, 0.0, 0.0010001659393310547, 0.0009984970092773438, 0.0019996166229248047, 0.0020003318786621094, 0.0009980201721191406, 0.0029981136322021484, 0.0019989013671875, 0.0029969215393066406, 0.0040051937103271484, 0.0029976367950439453, 0.00500035285949707, 0.006001710891723633, 0.006993293762207031, 0.007995367050170898, 0.005995750427246094, 0.005022764205932617, 0.005000591278076172, 0.006999015808105469, 0.007999420166015625, 0.00800013542175293, 0.007997751235961914, 0.010001897811889648, 0.01099848747253418, 0.011018753051757812, 0.011997699737548828, 0.01600337028503418, 
0.013998985290527344, 0.016000032424926758, 0.015065431594848633, 0.018979549407958984, 0.01999974250793457, 0.01997542381286621]

'''