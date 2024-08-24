# 1
name = input("Whats your name? ")
print(f"Hello, {name}")


# 2
names = []

for _ in range(3):
    name = input("Whats your name? ")
    names.append(name)

print(f"Hello, {names}")


# 3
names = []

for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f'Hello, {name}')
