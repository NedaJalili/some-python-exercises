x=("reza","mahsa",12,3,4,9,"neda")
y=(125,12,1,0,"sasan","reza")
x1=set(x)
y1=set(y)

z=x1.intersection(y1)
z1=tuple(z)

h1=x1.difference(y1)
h2=y1.difference(x1)
h3=h1.union(h2)
h4=tuple(h3)

print("x : ",x)
print("y : ",y)
print("intesection : ",z1)
print("difference : ",h4)
