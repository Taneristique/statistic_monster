import math 

def std(x):
    "x is an array or list!"
    m=0
    sd=0
    for i in range(len(x)):
        m+=x[i]
    m/=len(x)
    for j in range(len(x)):
        sd+=((x[j]-m))**2/len(x)
    return math.sqrt(sd)

