import math
pi=math.pi


def cube2(t1):
       return t1**3

def cuboid2(t1,t2,t3):
       return t1*t2*t3
    
def cylinder2(t1,t2):
       return pi*t1*t1*t2
    
def prism2(t1,t2):
       return t1*t2

def sphere2(t1):
       return (4/3)*pi*t1*t1*t1

def pyramid2(t1,t2):
       return (1/3)*t1*t2
    
def cone2(t1,t2):
       return (1/3)*pi*t1*t1*t2
    
def square2(t1,t2,t3):
       return (1/3)*t1*t2*t3

def ellipsoid2(t1,t2,t3):
       return (4/3)*pi*t1*t2*t3

def prime2(t1):     
       # iterarte upto n
       for i in range(t1):
           # adjust space
           print(' '*(t1-i), end='')
        
           # compute power of 11
           print(' '.join(map(str, str(11**i))))
       for i in range(t1 -2, -1, -1):
               # adjust space
           print(' '*(t1-i), end='')
        
           # compute power of 11
           print(' '.join(map(str, str(11**i))))
       
