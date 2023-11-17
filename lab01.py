from math import floor
from math import cos
from math import sin
from math import exp

def Euler(t,h,y0,t0):
    n=floor((t-t0)/h)
    y=y0
    for i in range(n):
        y=y+h*f(t0+h*i,y)
    return y

def RK(t,h,y0,t0):
    n=floor((t-t0)/h)
    y=y0
    for i in range(n):
        t=t0+h*i
        y=y + (h/2)*(f(t,y) + f(t+h,y+h*f(t,y)))
    return y

def f(t,y):

   
    value_f=1/(1+t**2)-2*y**2
   
    return value_f

def Eulersys(t,h,y10,y20,t0):
    n=floor((t-t0)/h)
    y1=y10
    y2=y20
    for i in range(n):
        newy1=y1+h*f1(t0+h*i,y1,y2)
        newy2=y2+h*f2(t0+h*i,y1,y2)
        y1=newy1
        y2=newy2
    return [y1,y2]


def f1(t,y1,y2):
    value_f1=y2
    return value_f1

def f2(t,y1,y2):
    value_f2=-4*y2-13*y1+40*cos(t)
    return value_f2