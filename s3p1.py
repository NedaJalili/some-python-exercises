grade=float(input("input the grade : "))

if 0<=grade<10:
   print("fail",grade)
elif 10<=grade<15:
   print("good",grade)
elif 15<=grade<18:
   print("very good",grade)   
elif 18<=grade<=20:
   print("excellent",grade)
else:
   print("invalid grad")
   
