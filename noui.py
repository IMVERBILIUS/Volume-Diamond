from func2 import w2
from func2 import w3


def garis():
    print("====================================")
while True :
            
    print(" Formula of every shape ")
    print(" -----------------------------------------------------------")
    print ("| shapes        |   Volume                               | ")
    print(" -----------------------------------------------------------")
    print ("|  Cube         | V = a3                                 | ")
    print ("|  Cuboid       | V = l × w × h                        | ")
    print ("|  Cylinder     | V = πr2h                              | ")
    print ("|  Prism        | V = B × h                             | ")
    print ("|  Sphere       | V = (4⁄3)πr3                          | ")
    print ("|  Pyramid      | V = (1⁄3) × B × h                    | ")
    print ("|  Cone         | V = (1⁄3)πr2h                         | ")
    print ("|  Square       | V = (1⁄3) × l × w × h               | ")
    print ("|  Ellipsoid    | V = (4⁄3) × π × a × b × c         | ")
    print ("|  Diamond      | Loop                                   | ")
    print("--------------------------------------------------------------")

    print ("Shape          ")
    print ("1. cube        ")
    print ("2. Cuboid      ")
    print ("3. Cylinder    ")
    print ("4. Prism       ")
    print ("5. Sphere      ")
    print ("6. Pyramid     ")
    print ("7. Cone        ")
    print ("8. Square      ")
    print ("9. Ellipsoid   ")
    print ("10. Diamond    ")
  


    Shapes = input("select type of shapes : ")


    if Shapes == "1":
            t1= int(input("a:"))
            result=w2.cube2(t1)

    elif Shapes == "2":
           t1= int(input("l:"))
           t2= int(input("w:"))
           t3= int(input("h:"))
           result=w2.cuboid2(t1,t2,t3)

    elif Shapes == "3":
           t1= int(input("r:"))
           t2= int(input("h:"))
           result=w2.cylinder2(t1,t2)

    elif Shapes == "4":
           t1= int(input("b:"))
           t2= int(input("h:"))
           result=w2.prism2(t1,t2)

    elif Shapes == "5":
           t1= int(input("r:"))
           result=w2.sphere2(t1)

    elif Shapes == "6":
           t1= int(input("B:"))
           t2= int(input("h:"))
           result=w2.pyramid2(t1,t2)

    elif Shapes == "7":
           t1= int(input("r:"))
           t2= int(input("h:"))
           result=w2.cone2(t1,t2)

    elif Shapes == "8":
           t1= int(input("l:"))
           t2= int(input("w:"))
           t3= int(input("h:"))
           result=w2.square2(t1,t2,t3)

    elif Shapes == "9":
           t1= int(input("a:"))
           t2= int(input("b:"))
           t3= int(input("c:"))
           result=w2.ellipsoid2(t1,t2,t3)
    elif Shapes == "10":
           t1= int(input("a:"))
           result=w2.prime2(t1)           
    else:
           result=w3.out()
           
           





    garis()
    print("Shapes that you choose : ",(Shapes))
    print("Result : ",(result))

    if input('Want a repeat again? ') != 'y':
        break
