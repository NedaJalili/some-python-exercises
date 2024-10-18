t=("sasan","reza","neda","omid","reza","ali","zahra","mahan","ashkan","reza")
l=list(t)
n=l.count("reza")
for i in range(n):
    l.remove("reza")
t2=tuple(l)    
print(t2)    
