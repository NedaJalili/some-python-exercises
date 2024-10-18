violations={"A1":20,"A2":32,"A3":53,"A4":17,"A5":8,
           "A6":40,"A7":64,"A8":23,"A9":71,"A10":50}

print(violations)
n=int(input("Please input number of all types of violation that done : "))
s=0
m=0
for i in range(n):
    name=input("name of violation : ")
    num=int(input("number of violation : "))
    m=violations[name]*num
    s+=m

print("sum of paid : ",s)
    
