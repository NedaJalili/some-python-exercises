from math import sqrt,pow
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
delta=pow(b,2)-(4*a*c)
print("delta = ",delta)
if delta>0:
   x1=(-b+sqrt(delta))/(2*a)
   x2=(-b-sqrt(delta))/(2*a)
   print("the answers : ",x1,x2)
elif delta==0:
   x3=(-b)/2*a
   print("the avswer : ",x3)
else:
   print("there is no answer!")
   

