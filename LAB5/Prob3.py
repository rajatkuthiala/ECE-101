from Myro import *


def Prob3():
    for a in range (1000):
        b=getObstacle(1)
        if b<6400:
            forward(1,1)
            print(b)
        if b==6400:
            turnRight(1,.6)
            print(b)
    
    stop()
    
Prob3()