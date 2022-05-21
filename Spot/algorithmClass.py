
class algorithm:
    
    def __init__(self):
        pass

def yuzdeHesap(deger1,deger2):
    if deger1>deger2:
        x = deger1-deger2
        y = deger2/100
        z = round(x/y,2)
        return z
    elif deger2>deger1:
        x = deger2-deger1
        y = deger1/100
        z = round(x/y,2)*-1
        return z
    return 0



