
# 1 just prints a text
print("hello, world")


# 2 takes input
print("What's your name?")
input()
print("hello, world")


# 3
input("What's your name?")
print("hello, world")


# 4
input("What's your name?")
print("hello, Spondon")


# 5 define a variable to store the input
# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print("hello,")
print(name)


# 6 prints the input name
# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print("hello, " + name)


# 7 removes the new line integreted with print
# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print("hello, ", end="")
print(name)


# 8 seperate hello and name input by anything. ex: ???
# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print("hello,", name, sep="???")


# 9 prints quoted text
# Say hello to user
print('hello, "friend"')


# 10
# Say hello to user
print("hello, \"friend\"")


# 11 using {} to print the input value or str
# Ask user for their name
name = input("What's your name? ")

# Say hello to user
print(f"hello, {name}")


# 12
# Ask user for their name
name = input("What's your name? ")

# removes whitespace from str
name = name.strip()

# Say hello to user
print(f"hello, {name}")


# 13
# Ask user for their name
name = input("What's your name? ")

# removes whitespace from str
name = name.strip()

# capitalizes each string
name = name.title()

# Say hello to user
print(f"hello, {name}")


# 14
# Ask user for their name
name = input("What's your name? ")

# removes whitespace from str and capitalizes each str
name = name.strip().title()

# Say hello to user
print(f"hello, {name}")


# 15
# Ask user for their name and also removes whitespace and capitalizes the str
name = input("What's your name? ").strip().title()

# Say hello to user
print(f"hello, {name}")


# 16
# Ask user for their name and also removes whitespace and capitalizes the str
name = input("What's your name? ").strip().title()

# Split Users name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")


# 17
# Ask user for their name and also removes whitespace and capitalizes the str
name = input("What's your name? ").strip().title()

# Split Users name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"hello, {first}")



# CALCULATIONS

# #1
x = 1
y = 2
z = x + y
print(z)


#2
x = input("What's x? ")
y = input("What's y? ")
z = x + y
print(z)


#3 'int' defines a value as integer
x = input("What's x? ")
y = input("What's y? ")
z = int(x) + int(y)
print(z)


#4
x = int(input("What's x? "))
y = int(input("What's y? "))
print(x + y)


#5 compact
print(int(input("What's x? ")) + int(input("What's y? ")))


#6 float
x = float(input("What's x? "))
y = float(input("What's y? "))
print(x + y)


#7 rounds up a float to the nearest integer
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(z)


#8 formats the number by using ","
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x + y)
print(f"{z:,}")


#9 rounds up a float
x = float(input("What's x? "))
y = float(input("What's y? "))
z = round(x / y, 2)
print(z)


#10 rounds up a float using f string
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x / y
print(f"{z:.2f}")