def main():
    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    output = ""
    for char in word:
        if char not in vowels:
            output += char
    return output


if __name__ == "__main__":
    main()
