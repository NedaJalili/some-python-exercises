from math import sqrt,pow
def d(x1,y1,x2,y2):
    d1=(sqrt(pow((x2-x1),2)+pow((y2-y1),2)))
    print("Distance between (x1,y1) and (x2,y2) is : ",d1)


x1=float(input("x1 : "))
y1=float(input("y1 : "))
x2=float(input("x2 : "))
y2=float(input("y2 : "))

d(x1,y1,x2,y2)
    
