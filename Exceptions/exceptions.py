# Syntax Error:

# syntax error: problem in the written code.
# unterminated: did not stop or finished the code.
# literal: that is typed in.
# syntax error has to be solved by self.

print("Hello, world)

# Correct:
print("Hello, world")


# Value Error:

# will show value error if input is string
# int() only accepts numbers, not string.

x = int(input("What's x?"))
print(f"x is {x}")

# Correct:

# try and except

# try: tells the code to try and run the program.
# except: if there are any exceptions such as value Error,
# except will run.

try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")


# NameError:

# the input showed an error before it could save the value in the variable x.

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")



