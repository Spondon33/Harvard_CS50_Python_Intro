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


# else
# if there are no error then else will be executed.

try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")


# Reprompting and break
# will loop until the user gives a valid input according to try.
# when the input meets the requirement as int,
# else will break the loop and print the desired output.
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")


# break can also be written as follows :
# if the input meets the requirement as int,
# we will break out of the loop and print the output.

while True:
    try:
        x = int(input("What's x? "))
        break
    except ValueError:
        print("x is not an integer")

print(f"x is {x}")


# get_int


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()


# modifying get_int
# return does not only break the loop but also returns the value.
# so break is not needed as return does the job.


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x? "))
            return x
        except ValueError:
            print("x is not an integer")


main()

# we can directly return the input.


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")


main()


# pass


# instead of saying "x is not an integer" to the user,
# pass will just accept that there is an error
# and it'll just rerun the loop without saying anything.


def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass


main()
