# variable = A container for a value (string, integer, float, boolean)
#            A variable behaves  as if it was the value it contains

#Strings
first_name = "john"
food = "pizza"
email = "john123@gmail.com"

print(f"Hello {first_name}")
print(f"You like {food}")

# Integers
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity}")
print(f"Your class has {num_of_students} students")

# Float

price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gps is: ${gpa}")
print(f"You ran {distance}km")

# Boolean

is_student = False
for_sale = True
is_online = True

if is_student:
    print("You are a student")
else:
    print("You are NOT A student")

if for_sale:
    print("That item is for sale")
else:
    print("THat item is NOT avaiable")

if is_online:
    print("You are online")
else:
    print("You are offline")