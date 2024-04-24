vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
user_input = input("Intput: ")

output = ""
for char in user_input:
    if char not in vowels:
        output += char

print("Output: ", output)
