'''
Method	             Description	                            Example
len(s)	             Returns length of string	             len("Hello") → 5
s.upper()	         Converts to uppercase	                "Hello".upper() → "HELLO"
s.lower()	         Converts to lowercase	                "Hello".lower() → "hello"
s.strip()	         Removes leading/trailing whitespace	" Hi ".strip() → "Hi"
s.replace(old, new)	 Replaces substring	"                    abc".replace("a","x") → "xbc"
s.find(sub)	         Returns first index of substring (-1 if not found)	"Hello".find("l") → 2
s.rfind(sub)	     Returns last index of substring	"Hello".rfind("l") → 3
s.startswith(prefix)	Checks if string starts with prefix	"Hi".startswith("H") → True
s.endswith(suffix)	   Checks if string ends with suffix	"Hi".endswith("i") → True
s.isdigit()	           Checks if all characters are digits	"123".isdigit() → True
s.isalpha()	           Checks if all characters are letters	"abc".isalpha() → True
s.isspace()	           Checks if all characters are whitespace	" ".isspace() → True
s.split(sep)	       Splits string into list	"a,b,c".split(",") → ["a","b","c"]
s.join(list)	       Joins list into string	".".join(["a","b","c"]) → "a.b.c"
s.count(sub)	       Counts occurrences of substring	"Hello".count("l") → 2
s.capitalize()	       Capitalizes first character	"hello".capitalize() → "Hello"
s.title()	           Capitalizes first character of each word	"hello world".title() → "Hello World"
s.lower() == s.lower()	Case-insensitive comparison	"Hello".lower() == "hello".lower() → True

'''

text = "  Hello World  "

# Length
print(len(text))  # 15

# Case conversion
print(text.upper())  # "  HELLO WORLD  "
print(text.lower())  # "  hello world  "

# Strip whitespace
print(text.strip())  # "Hello World"

# Replace
print(text.replace("World", "Python"))  # "  Hello Python  "

# Find / rfind
print(text.find("l"))  # 2
print(text.rfind("l")) # 9

# Startswith / endswith
print(text.startswith("  He"))  # True
print(text.endswith("ld  "))    # True

# Check type of content
print("123".isdigit())  # True
print("abc".isalpha())  # True
print("   ".isspace())  # True

# Split / join
words = text.strip().split()  # ["Hello","World"]
print(words)
print("-".join(words))        # "Hello-World"

# Count occurrences
print(text.count("l"))  # 3

# Capitalize / title
print("hello world".capitalize())  # "Hello world"
print("hello world".title())       # "Hello World"

# Case-insensitive comparison
print("Hello".lower() == "hello".lower())  # True
