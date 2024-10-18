n=int(input("row = "))
m=int(input("column = "))
s=0
x=[]
for i in range(n):
    y=[]
    for j in range(m):
        print(i,j)
        a=float(input("a = "))
        if i==j:
            s=s+a
        y.append(a)
    x.append(y)
print(x)
print("----------")
print("sum = ",s)
for r in x:
    print(r)
print("----------")    
print("sum = ",s)
    
