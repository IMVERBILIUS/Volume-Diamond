import math
pi=math.pi

def cal2(t1,t2):
       
       return(1/3)*pi*t1*t1*t2

def cube2(t1):
       return t1**3
               
def ball2(t1):
      return(4/3)*pi*t1**3
       
def beam(t1,t2,t4):
       return t1*t2*t4
       
def prime2(t1):
       for i in range(2, int(t1/2)+1):
              if t1 % i == 0:
                     return"not a prime Number"
                     break
              else:
                     return"is a prime Number"
                     break

