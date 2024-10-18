f1=open("a.txt","r")
f2=f1.readline()
y=""
n=0
m=0
s=0
for i in f2:
    y=y+i
    n=n+1
    if n%2==0:
        print("The number is ",y)
        s=s+int(y)
        m=m+1
        y=""

print("----------")
ave=s/m
print("average is ",ave)
        


