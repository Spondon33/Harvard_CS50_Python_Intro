"""
the debugger can help to see what is
happening in each line of code
line by line,
step by step,
which is very useful for finding a bug in the code.
"""

def main():
    height = int(input("Height: "))
    pyramid(height)


def pyramid(n):
    for i in range(n):
        print("#" * (i + 1))


if __name__ == '__main__':
    main()