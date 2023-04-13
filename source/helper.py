import sympy
alph_Mapping={
    "0":0,"1":1,"2":2,"3":3,"4":4,
    "5":5,"6":6,"7":7,"8":8,"9":9,
    "a":10,"b":11,"c":12,"d":13,"e":14,
    "f":15,"g":16,"h":17,"i":18,"j":19,
    "k":20,"l":21,"m":22,"n":23,"o":24,
    "p":25,"q":26,"r":27,"s":28,"t":29,
    "u":30,"v":31,"w":32,"x":33,"y":34,
    "z":35," ":36
}

alph_Mapping_Decryption=[
    "0","1","2","3","4",
    "5","6","7","8","9",
    "a","b","c","d","e",
    "f","g","h","i","j",
    "k","l","m","n","o",
    "p","q","r","s","t",
    "u","v","w","x","y",
    "z"," "
]
def extendedEuclideanAlgorithm(a: int, b: int) -> tuple:
    if b == 0:
        return (1, 0, a)
    else:
        x, y, gcd = extendedEuclideanAlgorithm(b, a % b)
        return (y, x - (a // b) * y, gcd)

def isPrime(n):
    if (n <= 1):
        return False
    if (n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6
    return True


def getPrime(bitsNum):
    p = sympy.randprime(2 ** (bitsNum - 1), 2 ** bitsNum - 1)
    return p




def encryption_Decryption(encodedPlaintext, e, n):
    ciphertext = []
    for i in range(len(encodedPlaintext)):
        ciphertext.append(pow(int(encodedPlaintext[i]), e, n))
    return ciphertext

def factorize(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            factor1 = i
            factor2 = n // i
            if isPrime(factor1) and isPrime(factor2):
                return factor1, factor2
    return None
