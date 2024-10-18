import random
list1=[1,2,3]
print("سنگ :","3")
print("کاغذ :","2")
print("قيچي :","1")
print("بازي 5 مرتبه انجام مي شود :")
print("-----------")
sx=0
sy=0
n=5
while n>0:
    x=int(input("انتخاب شما :"))
    y=random.choice(list1)
    print("انتخاب حريف :",y)
    if x not in list1:
        print("عبارت وارد شده صحيح نمي باشد! دوباره امتحان کن=)")
        continue
    elif x==y:
        print("اوه! مقادير برابر است. دوباره امتحان کنيد=)")
        continue
    elif x==1 and y==2:
        sx+=1
    elif x==1 and y==3:
        sy+=1
    elif x==2 and y==1:
        sy+=1
    elif x==2 and y==3:
        sx+=1
    elif x==3 and y==1:
        sx+=1
    elif x==3 and y==2:
        sy+=1
    n-=1    
print("---------------")        
print("امتياز شما :",sx)
print("امتياز حريف :",sy)
print("---------------")        
if sx>sy:
    print("تو برنده شدي")
elif sy>sx:
    print("يوهاها!")
        
