#1 Cat
print("meow")
print("meow")
print("meow")


#2 while loop
i = 3
while i != 0:
    print("meow")
    i = i - 1


#3
i = 1
while i <= 3:
    print("meow")
    i = i + 1


#4 start from 0 instead of 1
i = 0
while i < 3:
    print("meow")
    i = i + 1


#5 i + 1 is written as += 1
i = 0
while i < 3:
    print("meow")
    i += 1


# for loop

#1
for i in [0, 1, 2]:
    print("meow")


#2 sets a range of values
# we can write _ insted of i as i is not used as a variable
for _ in range(3):
    print("meow")


#3 will show meowmeowmeow
print("meow" * 3)


#4 \n prints each meow in seperate lines
print("meow\n" * 3)


#5 removes the default end at the end
print("meow\n" * 3, end = "")


#6
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break


#7
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")