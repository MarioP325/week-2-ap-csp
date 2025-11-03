
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
greeting = "Hello" #string data
name = "World" #string data

# ----------------------------------------
# Basic String Operations
# ----------------------------------------

# 1. Concatenation: Combining strings using the + operator
message = greeting + " " + name
print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"

# # Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!

# # Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!
Name="MARIO PANTOJA"
print("Uppercase:", Name.upper())
# # Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False
print("name ", Name.isupper())
print("name ", Name.capitalize)
# # Find the length of the string
print("Length of phrase:", len(phrase))  # Output: 14
print
# # ----------------------------------------
# # 3. Indexing and Slicing
# # ----------------------------------------
chicago_mayor="Johnson"
print(len(chicago_mayor))
print(chicago_mayor[0])
print(chicago_mayor[4])
print(chicago_mayor[-1])
# # Indexing: Access characters by position (0-based index)
print("First character:", phrase[0])  # Output: P
print("Last character:", phrase[-1])  # Output: !
print(chicago_mayor[0:4])
# first number is inclusive
#last number is exclusive
print(chicago_mayor[:5])
# # Slicing: Get a range of characters (start inclusive, end exclusive)
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!

phrase3 = "Supercagifragilistic"
print("")
# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"

# # Printing Strings
# print(greeting1)
# print(greeting2)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

sentence = "Python is fun to learn"

# # .split(): Splits the string into a list of words
words = sentence.split()
print("Split result:", words)

# # .format(): Allows inserting values into strings using {}
# name = "Marvin"
# age = 35
# intro = "My name is {} and I am {} years old.".format(name, age)
# print(intro)

# # You can also use f-strings (Python 3.6+)
# intro_fstring = f"My name is {name} and I am {age} years old."
# print(intro_fstring)
