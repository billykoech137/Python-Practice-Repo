import random
import sys
import pandas as pd

def digGen():
    digits = ['1','2','3','4','5','6','7','8','9','0']
    return random.choice(digits)

def lowGen():
    lower = ['a','b','c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return random.choice(lower)

def uppGen():
    upper = ['A','B','C','D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return random.choice(upper)

def signGen():
    sign = ['@','#','$','%','&','*','(',')','!','^']
    return random.choice(sign)

def passGen():
    myPass = []
    for i in range(4):
        dig = digGen()
        myPass.append(dig)

        low = lowGen()
        myPass.append(low)

        upp = uppGen()
        myPass.append(upp)

        sign = signGen()
        myPass.append(sign)
    
    random.shuffle(myPass)
    
    password = ''.join(myPass)
    
    return password


account = 'example1'
password = passGen()

PASSWORDS = {account:password}

















