from ctypes import *

def BruteForce():
    flag = c_int(-2147483648) # Casting to int-32bit
    x3=0
    while (x3 != -889275714):
        x1 = c_int((flag.value) << 3)
        x2 = 525024598
        x2 = x2 ^ (flag.value)
        n3 = x2 ^ x1.value
        flag.value+=1
    print((flag.value)-1)

BruteForce()



