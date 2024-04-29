def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    for char in s:
        if (
            char.isupper()
            and 2 <= len(s) <= 6
            and s[:2].isalpha()
            and s.isalpha() or s.isalnum()
            and all(char.isalpha() for char in s[2:-2])
            and not s.isdigit()
            and s[-1].isdigit()
            and s[-2] != "0"
        ):
            return True


main()
