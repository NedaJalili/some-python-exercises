
# Define initial room status
rooms = {
'A': {'single': 3, 'double': 4, 'triple': 2},
'B': {'single': 3, 'double': 4, 'triple': 2},
'C': {'single': 3, 'double': 4, 'triple': 2}
}

def reserve_room():
   class_type = input("Room class (A, B, C): ")
   bed_type = input("Bed type (single, double, triple): ")
   days = int(input("Number of days: "))

   if class_type in rooms and bed_type in rooms[class_type]:
      if rooms[class_type][bed_type] > 0:
         rooms[class_type][bed_type] -= 1
         print(f"Room {class_type} with {bed_type} bed reserved for {days} days.")
      else:
         print("Unfortunately, the requested room is not available.")
   else:
      print("Invalid room class or bed type.")

# Execute the room reservation function

reserve_room()
