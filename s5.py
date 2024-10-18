from math import sqrt
n=int(input("n = "))
s=0
for i in range(n):
    s=s+pow(i,2)
    ss=sqrt(s)
    
print("s = ",s,"ss = ",ss)
