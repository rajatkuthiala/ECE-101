from Myro import *

def Prob4():
    for a in range(100):
        b=getLight(1)
        if b in range(3000,65000):
            setLED("front", "on")
            setLED("left", "on")
            setLED("right", "on")
            print(getLight(1))
            
        if b in range(0,3000):
            setLED("front", "off")
            setLED("left", "off")
            setLED("right", "off")
            print(getLight(1))
    
    setLED("front", "off")
    setLED("left", "off")
    setLED("right", "off")        
    
    
    stop()
Prob4()
    