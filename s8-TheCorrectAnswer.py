x=input("Please enter a sentence : ")
y=["is","are","was","were"]
z=x.split()
d=""
for i in z:
    if i in y:
        d=d+"***"+" "
    else:
        d=d+i+" "
print(d)
