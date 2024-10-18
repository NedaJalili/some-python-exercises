import re

name=input("name : ")
idn=input("id number : ")
phone=input("phone number : ")
pas=input("password : ")

pas1=re.search(name,pas)
idn1=re.search(idn,pas)
phone1=re.search(phone,pas)

if pas1 or idn1 or phone1:
    print("password is invalid , please try again")
else:
    print("password is OK")
