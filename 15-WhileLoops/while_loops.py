# while_loops.py
# Demonstrates different while loop structures and practical uses in Python

print("=== EXAMPLE 1: BASIC WHILE LOOP ===")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1
print()


print("=== EXAMPLE 2: COUNTDOWN ===")
num = 5
while num > 0:
    print(num)
    num -= 1
print("Lift off!\n")


print("=== EXAMPLE 3: SENTINEL-CONTROLLED LOOP ===")
# Uncomment to test manually
# password = ""
# while password != "python123":
#     password = input("Enter password: ")
# print("Access granted!\n")


print("=== EXAMPLE 4: INFINITE LOOP (with break) ===")
# Demonstrates how to prevent infinite loops
counter = 0
while True:
    print("Loop iteration:", counter)
    counter += 1
    if counter == 3:
        print("Stopping loop with break.\n")
        break


print("=== EXAMPLE 5: USING break AND continue ===")
x = 0
while x < 10:
    x += 1
    if x == 5:
        continue  # skip number 5
    if x == 8:
        break     # stop loop at 8
    print(x)
print("Loop finished (break encountered).\n")


print("=== EXAMPLE 6: WHILE LOOP WITH else ===")
n = 3
while n > 0:
    print(n)
    n -= 1
else:
    print("Loop finished normally (no break used).")
