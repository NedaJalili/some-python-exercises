informations={}
names=[]
n=int(input("How many people are there? "))

for i in range(n):
    name=input("name : ")
    age=int(input("age : "))
    informations[name]=age
print("The dictionary of people : ",informations)



