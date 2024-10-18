time=float(input("enter the time in hours : "))
salary=0
overtime=(time-160)

if time<= 160:
    salary=time*100000
    print("Your salary is : ",salary,"Tomaan")

elif time> 160:
    if overtime<=40:
        salary=(160*100000)+(overtime*50000)
        print("Your salary is : ",salary,"Tomaan")
    elif overtime>40:
        salary=(160*100000)+(40*50000)
        print("Your salary is : ",salary,"Tomaan")    
    

    
