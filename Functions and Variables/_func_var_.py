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
