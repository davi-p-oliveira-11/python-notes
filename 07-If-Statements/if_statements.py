# 🧠 Syntax:
# if condition:
    # code executes if condition is True
# elif another_condition:
    # code executes if the first condition is False but this is True
# else:
    # code executes if all above conditions are False

# Example 1: Basic if
age = 20
if age >= 18:
    print("You are an adult.")

# Example 2: If-else
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example 3: If-elif-else
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print("Grade:", grade)

# Example 4: Nested if
x = 10
if x > 0:
    if x % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
