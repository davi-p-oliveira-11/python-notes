# AND operator
age = 25
has_license = True
if age >= 18 and has_license:
    print("You can drive!")

# OR operator
has_ticket = False
is_vip = True
if has_ticket or is_vip:
    print("You can enter the event!")

# NOT operator
is_raining = False
if not is_raining:
    print("Let's go for a walk!")

# Combining multiple logical operators
temperature = 22
sunny = True
if (temperature > 20 and temperature < 30) and sunny:
    print("Perfect weather!")
