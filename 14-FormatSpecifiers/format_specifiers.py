# format_specifiers.py
# Demonstrates different ways to format output in Python

# -------------------------------
# 1. f-Strings (Recommended)
# -------------------------------

name = "David"
age = 20
height = 1.82

print("=== f-STRINGS ===")
print(f"My name is {name}, I am {age} years old and {height:.2f}m tall.")
print(f"Binary of age: {age:b}")
print(f"Hexadecimal of age: {age:X}")
print(f"Aligned right: |{name:>10}|")
print(f"Aligned left:  |{name:<10}|")
print(f"Centered:      |{name:^10}|")
print(f"With commas:   {1234567:,.2f}")
print()

# -------------------------------
# 2. .format() Method
# -------------------------------

print("=== .format() METHOD ===")
print("My name is {}, I am {} years old and {:.2f}m tall.".format(name, age, height))
print("My name is {0}, I am {1} years old and {2:.2f}m tall.".format(name, age, height))
print("My name is {n}, I am {a} years old.".format(n=name, a=age))
print("Binary of age: {0:b}".format(age))
print("Hexadecimal: {0:X}".format(age))
print("With commas: {:,}".format(1000000))
print()

# -------------------------------
# 3. Old-Style (%) Formatting
# -------------------------------

print("=== OLD-STYLE (%) FORMATTING ===")
print("My name is %s, I am %d years old and %.2fm tall." % (name, age, height))
print("Binary: %s" % bin(age))
print("Hexadecimal: %X" % age)
print("Scientific notation: %.3e" % 1234.56789)
print()

# -------------------------------
# 4. Practical examples
# -------------------------------

print("=== PRACTICAL USES ===")

# Display currency
price = 49.99
print(f"Price: ${price:.2f}")

# Percentage
progress = 0.756
print(f"Progress: {progress:.1%}")

# Table formatting
print("\nProduct\t\tPrice")
print("-" * 20)
print(f"Apples\t\t${1.25:.2f}")
print(f"Oranges\t\t${2.50:.2f}")
print(f"Bananas\t\t${0.99:.2f}")
