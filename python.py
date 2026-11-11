import math
from turtle import*

def hearta(K):
    return 12*math.sin(K)**3
def heartb(K):
    return 12*math.cos(K)-5*\
    math.cos(2*k)-2*\
    math.cos(3*k)-\
    math.cos(4*k)
speed (0)
bgcolor("black")
for i in range(6000):
    goto(hearta(i)*20, heartb(i)*20)
    for j in range(5):
        color("red")
    goto (0,0)
done()
