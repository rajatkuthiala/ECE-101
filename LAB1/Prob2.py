#Leap Year Calculator By Rajat Kuthiala


def Prob2(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    else:
        return False
