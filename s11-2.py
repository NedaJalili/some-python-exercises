# تعریف وضعیت اولیه اتاقها
rooms = {
'A': {'یک تخته': 3, 'دو تخته': 4, 'سه تخته': 2},
'B': {'یک تخته': 3, 'دو تخته': 4, 'سه تخته': 2},
'C': {'یک تخته': 3, 'دو تخته': 4, 'سه تخته': 2}
}

def reserve_room():
   class_type = input("کلاس اتاق (A, B, C): ")
   bed_type = input("نوع تخت (یک تخته, دو تخته, سه تخته): ")
   days = int(input("برای چند روز: "))

   if class_type in rooms and bed_type in rooms[class_type]:
      if rooms[class_type][bed_type] > 0:
         rooms[class_type][bed_type] -= 1
         print(f"اتاق {class_type} با {bed_type} برای {days} روز رزرو شد.")
      else:
         print("متاسفانه اتاق مورد نظر خالی نیست.")
   else:
      print("نوع اتاق یا تخت نامعتبر است.")

# اجرای تابع رزرو اتاق
reserve_room()
