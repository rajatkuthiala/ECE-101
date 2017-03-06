from Myro import *
import random

def Prob1():
    L=[0,1]
    for i in range (30):
        a=random.choice(L)
        
        if a == 0:
            forward(1,1)
        if a == 1:
            backward(1,1)
    stop()
Prob1()