def multiple_7_2(x):
    if x%7==0 and x%2==0:
       print(x,"is a multiple of 2 and 7")
    elif x%7!=0 and x%2==0:
       print(x,"is not a multiple of 7 but it ia a multipule of 2")
    elif x%7==0 and x%2!=0:
       print(x,"is not a multiple of 2 but it ia a multipule of 7")

a=int(input("enter a number : "))
multiple_7_2(a)
       
