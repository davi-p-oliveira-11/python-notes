# Example 1: Basic ternary
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

# Example 2: With math
number = 7
parity = "Even" if number % 2 == 0 else "Odd"
print(parity)  # Output: Odd

# Example 3: Nested ternary
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print("Grade:", grade)  # Output: Grade: B

# Example 4: Using with function calls
print("Positive" if number > 0 else "Negative or zero")
