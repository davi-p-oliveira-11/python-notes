# for_loops.py
# Demonstrates different types of for loops and use cases in Python

print("=== EXAMPLE 1: BASIC FOR LOOP ===")
for i in range(5):
    print("Iteration:", i)
print()


print("=== EXAMPLE 2: RANGE WITH START AND STEP ===")
for i in range(1, 11, 2):  # start=1, stop=11, step=2
    print(i)
print()


print("=== EXAMPLE 3: LOOPING THROUGH A STRING ===")
word = "Python"
for letter in word:
    print(letter)
print()


print("=== EXAMPLE 4: LOOPING THROUGH A LIST ===")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)
print()


print("=== EXAMPLE 5: LOOPING WITH INDEX (using enumerate) ===")
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"Index {index} -> {name}")
print()


print("=== EXAMPLE 6: NESTED FOR LOOPS ===")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
print()


print("=== EXAMPLE 7: USING break AND continue ===")
for i in range(10):
    if i == 5:
        continue  # skip 5
    if i == 8:
        break     # stop loop when i == 8
    print(i)
print("Loop ended (break encountered).\n")


print("=== EXAMPLE 8: FOR LOOP WITH ELSE ===")
for i in range(3):
    print(i)
else:
    print("Loop finished normally (no break used).")
print()


print("=== EXAMPLE 9: LOOPING THROUGH A DICTIONARY ===")
person = {"name": "Alice", "age": 25, "city": "London"}
for key, value in person.items():
    print(f"{key}: {value}")
print()


print("=== EXAMPLE 10: LIST COMPREHENSION ===")
# Compact way to create lists using for loops
squares = [x**2 for x in range(6)]
print("Squares:", squares)

evens = [x for x in range(10) if x % 2 == 0]
print("Even numbers:", evens)
